import string
import sys
import requests
import streamlit as st
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)
from pytube import Playlist, YouTube
import tiktoken
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import argparse

def count_tokens(text):
    # Load the desired encoding, e.g., "cl100k_base" for second-generation embedding models
    encoding = tiktoken.get_encoding("cl100k_base")
    # Convert the text into tokens
    tokens = encoding.encode(text)
    # Count the number of tokens
    num_tokens = len(tokens)
    return num_tokens

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

def call_emb(content):
    data = {"content": content}

    response = requests.post("http://localhost:8080/embedding", json=data)

    if response.status_code == 200:
        return response.json()['embedding']

    return "error..."


def call_hyde(question):
    # prompt = f"""<s>[INST] Please answer following question: {question}[/INST]"""
    prompt = f"""<s>[INST] Please read the question: {question}. Please generate 10 similar questions.Please be concise.[/INST]"""
    data = {"prompt": prompt, "n_predict": 2048, "temperature": 0.7, "stop":['</s>']}

    response = requests.post("http://localhost:8080/completion", json=data)

    if response.status_code == 200:
        return response.json()['content']

    return "error..."

def call_llama(question, context):

#     prompt = f"""<s>[INST] Here are parts of texts from a video conference:
# ```
# {context}
# ```
# Please read the text. 
# Please answer following question: {question}
# Please use only context provided. If you have no context, write 'No context'.
# Please format the output in markdown. Please format the output into paragraphs for easier readability.
# [/INST]"""
    prompt = f"""<s>[INST] Context information is below.
---------------------
{context}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:[/INST]
"""


    data = {"prompt": prompt, "n_predict": 2048, "temperature": 0.7, "stop":['</s>']}

    response = requests.post("http://localhost:8080/completion", json=data)

    if response.status_code == 200:
        return response.json()['content']

    return "error..."

def get_collection(collection_name="hello_milvus"):
    connections.connect("default", host="localhost", port="19530")    
    has = utility.has_collection(collection_name)
    if not has:
        print('Collection not found', file=sys.stderr)
        exit(-1)

    fields = [
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=4096)
    ]

    schema = CollectionSchema(fields, f"{collection_name}")

    return Collection(collection_name, schema, consistency_level="Strong")


def create_index(collection):
    try:
        collection.release()
        collection.drop_index()
    except:
        print("Unable to release and drop index", file=sys.stderr)

    index = {
        "index_type": "IVF_FLAT",
        "metric_type": "COSINE",
        "params": {"nlist": collection.num_entities},
    }

    print(f"Creating index:{index}")
    collection.create_index("embeddings", index)
    collection.load()

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

def get_candidates(collection, question):

    vectors_to_search = call_emb(question)
    search_params = {
        "metric_type": "COSINE",
        "params": {"nprobe":  collection.num_entities},
    }

    result = collection.search([vectors_to_search], "embeddings", search_params, limit=5, output_fields=["text"])
    context = []
    for hits in result:
        for hit in hits:
            print("="*30)
            foundtext = hit.entity.get('text')
            video_id = hit.id.split('-part')[0]
            # foundtext = open(f"videos/{video_id}.txt","r").read()
            url = f"https://www.youtube.com/watch?v={video_id}"
            title,_ = get_youtube_video_title_description(url)
            print(f"Found:{title}({video_id}|{hit.id})\nSimilarity score:\n{hit.distance}")
            context.append(foundtext)
    
    
    return "".join(context)

def parseargs():
    parser = argparse.ArgumentParser(description="d/l transcript of y video")
    parser.add_argument("-c", "--collection-name", required=True, help="collection name to be used for the playlist")    
    parser.add_argument("-v", "--video-id", required=False, help="youtube video id to add to the database")
    parser.add_argument("-l", "--playlist", required=False, help="youtube playlist to add to the database")

    args = parser.parse_args()

    if args.video_id is None and args.playlist is None:
        parser.print_help()
        exit(1)
    return args


st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by llama.cpp")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


if "init" not in st.session_state:
    st.session_state["init"]=True
    print("Initializing collection")
    collection = get_collection("angular")
    create_index(collection)
    st.session_state["collection"]=collection

sitebar = st.sidebar
reload = sitebar.button("Reload index")
if reload:
    print("Reloading index")
    create_index(st.session_state["collection"])
    reload = False

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)    
    print(f"======{prompt}=====")
    hyde_prompt = call_hyde(prompt)
    print(f"Hyde prompt:\n{hyde_prompt}")
    questions = hyde_prompt.split("\n")
    questions.append(prompt)
    print(questions)
    fullcontext = []
    for question in questions:
        context = get_candidates(st.session_state["collection"], question)
        #context = clean_text(context)
        if context not in fullcontext:
            fullcontext.append(context)
        else:
            print("Context already added...skipping...")
    print(f"Number of context candidates found: {len(fullcontext)}")
    fullcontext = clean_text("".join(fullcontext))
    print(f"Candidate token size:{count_tokens(fullcontext)}")
    msg = call_llama(prompt, fullcontext)
    print(f"Message received:{msg[:80]}....")
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)