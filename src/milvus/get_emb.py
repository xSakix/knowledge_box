import argparse
import sys
from urllib.parse import parse_qs, urlparse
import requests
import numpy as np
import os
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tiktoken
from langchain.text_splitter import TokenTextSplitter,SentenceTransformersTokenTextSplitter
from pytube import Playlist, YouTube
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, Transcript
from youtube_transcript_api.formatters import TextFormatter


def get_youtube_video_title_description(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Access the title of the video
        title = yt.title
        description = yt.description

        return title, description
    except Exception as e:
        print(f"Error: {e}")
        return None

def load_videos(playlist):

    playlist = Playlist(f"https://www.youtube.com/playlist?list={playlist}")
    if len(playlist) == 0:
        print("No videos found...", file=sys.stderr)

    videos = []
    for url in playlist:
        title, desc = get_youtube_video_title_description(url)
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        videos.append({
            "video_id": query_params.get("v")[0],
            "url": url,
            "title": title,
            "description": desc,
            "transcript":""
        })

    return videos

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra spaces
    text = " ".join(text.split())

    # Correct spelling
    # (Optional, replace with a spell checker library)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    text = " ".join(filtered_words)

    # Lemmatize or stem words
    # (Choose lemmatize or stemming based on your preference)
    lemmatizer = WordNetLemmatizer()
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    text = " ".join(lemmatized_words)

    return text

def parseargs():
    parser = argparse.ArgumentParser(description="load data into milvus")
    parser.add_argument("-c", "--collection-name", required=True, help="collection name to be used for the playlist")    
    parser.add_argument("-v", "--video-id", required=False, help="youtube video id to add to the database")
    parser.add_argument("-l", "--playlist", required=False, help="youtube playlist to add to the database")

    args = parser.parse_args()

    if args.video_id is None and args.playlist is None:
        parser.print_help()
        exit(1)
    return args

def split_number(number, n_parts):
    # Calculate the base part size and the remainder
    part_size, remainder = divmod(number, n_parts)
    
    # Initialize an empty list to store the parts
    parts = []
    
    # Distribute the base part size and the remainder
    for i in range(n_parts):
        # Add the base part size to the list
        parts.append(part_size + (1 if i < remainder else 0))
    
    return parts

def call_emb(content):
    data = {"content": content}

    response = requests.post("http://localhost:8080/embedding", json=data)

    if response.status_code == 200:
        return response.json()['embedding']

    return "error..."

def call_completion(content):
    data = {"prompt": content, "n_predict":2048}

    response = requests.post("http://localhost:8080/completion", json=data)

    if response.status_code == 200:
        return response.json()['content']

    return "error..."

def count_tokens(text):
    # Load the desired encoding, e.g., "cl100k_base" for second-generation embedding models
    encoding = tiktoken.get_encoding("cl100k_base")
    # Convert the text into tokens
    tokens = encoding.encode(text)
    # Count the number of tokens
    num_tokens = len(tokens)
    return num_tokens

def get_split_size(num_tokens, max_tokens):
    i = 2        
    parts = split_number(num_tokens,i)
    while parts[0] > max_tokens:
        i += 1
        parts = split_number(num_tokens,i)

    print(f"Splits:{parts}")

    return parts[0]

def load_file_intodb(text,id,collection):
    print(f"==========={id}=============")
    ids =[]
    texts=[]
    embeddings=[]
    num_tokens = count_tokens(text)
    print(f"Num tokens:{num_tokens}")
    
    text_splitter = TokenTextSplitter(chunk_size=get_split_size(num_tokens, 512), chunk_overlap=0, encoding_name="cl100k_base")
    splits = text_splitter.split_text(text)
    print(f"Num of splits:{len(splits)}")
    
    i = 1
    for split in splits:
        emb = call_emb(split)
        ids.append(f"{id}-part-{i}")
        texts.append(split)
        embeddings.append(emb)
        print(f"split token = {count_tokens(split)} | emb size={len(emb)}")            
        i = i + 1
    
    data = [ids, texts, embeddings]
    collection.insert(data)
    collection.flush()

def get_one_video_transcript(video_id):

    file_path = "../videos/" + str(video_id) + ".txt"

    if os.path.exists(file_path):
        print(f"{file_path} exists. Loading transcript from file...", file=sys.stderr)
        with open(file_path, "r") as fd:
            return fd.read()

    try:
        text = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        text_formatted = formatter.format_transcript(text)
        with open(file_path, "w+") as fd:
            fd.write(text_formatted)

        return text_formatted
    except:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            transcript: Transcript = transcript_list.find_generated_transcript(['en', 'nl', 'de', 'fr','en-CA','en-US','it'])
            text = transcript.fetch()
            formatter = TextFormatter()
            text_formatted = formatter.format_transcript(text)
            with open(file_path, "w+") as fd:
                fd.write(text_formatted)
            return text_formatted
        except NoTranscriptFound as ne:
            print("No transcript found:", ne, file=sys.stderr)
            # transcript = transcript_list.find_generated_transcript(ne)

    return "nothing found"

def main():
    
    args = parseargs()

    collection_name=args.collection_name

    fmt = "\n=== {:30} ===\n"
    print(fmt.format("start connecting to Milvus"))
    connections.connect("default", host="localhost", port="19530")    
    has = utility.has_collection(collection_name)
    fields = [
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=4096)
    ]

    schema = CollectionSchema(fields, f"{collection_name}")

    collection = Collection(collection_name, schema, consistency_level="Strong")

    if args.playlist is not None:
        videos = load_videos(args.playlist)
        num_videos = len(videos)
        for i in range(len(videos)):
            video = videos[i]
            print("-"*80, file=sys.stderr)
            print(f"Processing video {i+1} of {num_videos}", file=sys.stderr)
            print(f"Video title:{video['title']}",file=sys.stderr)
            print("## " + video["title"] + "\n")
            print("URL: [" + video["url"] + "](" + video["url"] + ")\n")
            try:
                transcript = get_one_video_transcript(video["video_id"])
                transcript = clean_text(transcript)
                load_file_intodb(transcript, video["video_id"],collection)
            except:
                print("Error loading file into db")
    
    
    print(f"Number of entities in Milvus: {collection.num_entities}")  # check the num_entities    
    
    
if __name__ == "__main__":
    main()