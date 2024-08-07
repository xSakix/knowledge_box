import os.path
import sys

from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, Transcript
from youtube_transcript_api.formatters import TextFormatter
import argparse
from pytube import Playlist, YouTube
from urllib.parse import urlparse,parse_qs
import requests
import sys
from rouge_score import rouge_scorer
import tiktoken
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from langchain.text_splitter import TokenTextSplitter,SentenceTransformersTokenTextSplitter
from bert_score import score
import nltk
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize

MAIN_VIDEOS_DIR = "videos"
MAX_TOKENS = 8192
N_PREDICT=8192
# N_PREDICT = -1
TEMPERATURE = 0.7
OVERLAP = 0
DEFAULT_TEMPLATE=f"templates/instruct.txt"


def get_template(video, template_type="instruct", isedit = False):
    
    # print(f"Using template type:{template_type}", file=sys.stderr)

    if isedit:
        filename = f"templates/edit/"+template_type+".txt"
    else:
        filename = f"templates/"+template_type+".txt"
    if os.path.exists(filename):
        template=open(filename,"r").read()
    else:
        template=open(DEFAULT_TEMPLATE,"r").read()

    if "name" in video.keys():
        result = template.format(title=video["title"],context=video["transcript"], description=video["description"],name=video["name"])
    else:
        result = template.format(title=video["title"],context=video["transcript"], description=video["description"])
    # print(result, file=sys.stderr)
    return result



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

def count_tokens(text):
    # Load the desired encoding, e.g., "cl100k_base" for second-generation embedding models
    encoding = tiktoken.get_encoding("cl100k_base")
    # Convert the text into tokens
    tokens = encoding.encode(text)
    # Count the number of tokens
    num_tokens = len(tokens)
    return num_tokens

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


def parseargs():
    parser = argparse.ArgumentParser(description="d/l transcript of y video")
    parser.add_argument("-v", "--video-id", required=False, help="youtube video id for summarization")
    parser.add_argument("-l", "--playlist", required=False, help="youtube playlist")
    parser.add_argument("-s", "--stats", action="store_true", required=False,help="print rouge score")
    parser.add_argument("-t", "--template-type", default="instruct", required=False, help="Model type. One of instruct, llama, chatml, neuralchat, carbon, alpaca")    
    parser.add_argument("-c", "--context-size", default=8192, required=False, help="Context size, default is 8192(for mistral/monarch/etc)")
    parser.add_argument("-r", "--randomness", default=0.7, required=False, help="Temperature or randomness of the output. Default is 0.7")
    parser.add_argument("-n","--name",default="video conference", required=False,help="Name of the list")

    args = parser.parse_args()

    if args.video_id is None and args.playlist is None:
        parser.print_help()
        exit(1)
    return args


def get_one_video_transcript(video_id):

    file_path = MAIN_VIDEOS_DIR + "/" + str(video_id) + ".txt"

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


def edit_summary(context,template_type="instruct"):
    data = {"prompt": get_template(context,template_type,isedit=True), "n_predict": 1024, "temperature": TEMPERATURE}

    response = requests.post("http://localhost:8080/completion", json=data)

    if response.status_code == 200:
        return response.json()['content']

    return "error..."

def summarize_whole(video,params):
    data = {
        "prompt": get_template(video,params['template_type']), 
        "n_predict": N_PREDICT, 
        "temperature": params['temperature'], 
        "stop":['<|end_of_turn|>','<|im_end|>', '</s>','<|endoftext|>'], 
        "keep":-1}

    response = requests.post("http://localhost:8080/completion", json=data)

    if response.status_code == 200:
        return response.json()['content']

    return "error..."


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

def summarize_per_parts(video, num_tokens, params):

    template_tokens = count_tokens(get_template({"title":"","transcript":"","description":""},params['template_type']))

    i = 2        
    parts = split_number(num_tokens,i)
    while parts[0] > (params['context']-template_tokens-OVERLAP):
        i += 1
        parts = split_number(num_tokens,i)

    print(f"Split:{parts}", file=sys.stderr)

    summary = []

    chunk_size=parts[0]
    print(f"chunk size:{chunk_size}", file=sys.stderr)
    text_splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=OVERLAP, encoding_name="cl100k_base")

    parts = text_splitter.split_text(video["transcript"])
    sizes = [count_tokens(part) for part in parts]
    print(f"Num of parts after text splitter:{len(parts)} | {sizes}", file=sys.stderr)

    for part in parts:
        video_part = video.copy()
        video_part["transcript"]=part
        prompt = get_template(video_part, params['template_type'])
        print("part num of tokens:",count_tokens(prompt), file=sys.stderr)
        data = {"prompt": prompt, "n_predict": N_PREDICT, "temperature": params['temperature'],"stop":['<|end_of_turn|>','<|im_end|>', '</s>','<|endoftext|>'], "keep":-1}

        response = requests.post("http://localhost:8080/completion", json=data)

        if response.status_code == 200:
            summary_part = str(response.json()['content'])
            if not summary_part.endswith('\n'):
                summary_part += '\n'
            summary.append(summary_part)
        else:
            return "error..."
    summary = "".join(summary)
    # summary = edit_summary(summary, template_type=template_type)
    return summary

def summarize_video(video,params):
    
    num_tokens = count_tokens(get_template(video, params['template_type']))
    print(f'Num tokens:{num_tokens}| MAX_TOKENS={params["context"]}',file=sys.stderr)
    if num_tokens <= params['context']:
        return summarize_whole(video, params)
    return summarize_per_parts(video, num_tokens, params)


def print_stats(summary, transcript):
    scorer = rouge_scorer.RougeScorer(['rouge1','rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(transcript, summary)
    for key in scores.keys():
        print(f"{key}:{scores[key]}", file=sys.stderr)
    print(f"Number of tokens in original text:{count_tokens(transcript)}", file=sys.stderr)
    print(f"Number of tokens in summary:{count_tokens(summary)}", file=sys.stderr)

    # P, R, F1 = score([summary], [transcript], lang="en", verbose=False)
    # print(f"Precision: {P.mean().item():.4f}", file=sys.stderr)
    # print(f"Recall: {R.mean().item():.4f}", file=sys.stderr)
    # print(f"F1 Score: {F1.mean().item():.4f}", file=sys.stderr)

    # reference_tokens = word_tokenize(transcript)
    # candidate_tokens = word_tokenize(summary)

    # # Calculate BLEU score
    # # Note: Since we are comparing a summary to its original, we wrap the reference in a list
    # bleu_score = sentence_bleu([reference_tokens], candidate_tokens, weights=(0.5, 0.5))

    # print(f"BLEU score: {bleu_score:.4f}", file=sys.stderr)

def main():
    args = parseargs()

    if  args.video_id is not None and args.video_id.startswith("'"):
        args.video_id = args.video_id[1:-1]

    params = {
        "context": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "template_type": "instruct"
    }

    if args.context_size is not None:
        params["context"]=int(args.context_size)
    if args.randomness is not None:
        params["temperature"]=float(args.randomness)
    if args.template_type is not None:
        params["template_type"] = args.template_type



    print(f"Context:{params['context']}", file=sys.stderr)
    print(f"Temperature:{params['temperature']}", file=sys.stderr)

    if args.video_id is not None:
        transcript = get_one_video_transcript(args.video_id)
        transcript = clean_text(transcript)

        url = f"https://www.youtube.com/watch?v={args.video_id}"
        title,desc = get_youtube_video_title_description(url)
        video = {
            "video_id": args.video_id,
            "url": url,
            "title": title,
            "description": desc,
            "transcript":transcript
        }
        if args.name is not None:
            video["name"] = args.name

        print(f"Using template type:{args.template_type}", file=sys.stderr)
        summary = summarize_video(video, params)
        print("## " + title+"\n")
        print("URL: ["+url+"]("+url+")\n")
        print(summary)
        print("\n")
        if args.stats:
            print_stats(summary, transcript)
    elif args.playlist is not None:
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
                video["transcript"]=transcript

                if args.name is not None:
                    video["name"] = args.name
                
                summary = summarize_video(video, params)
                
                if args.stats:
                    print_stats(summary, transcript)

            except:
                summary = "Error"
            print(summary)
            print("\n")


if __name__ == "__main__":
    main()