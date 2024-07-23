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
from langchain.text_splitter import TokenTextSplitter


class Transcription:
    def __init__(self):
        self.youtube_transcript_api = YouTubeTranscriptApi()
        
    def get_transcript(self, video_id):
        try:
            transcript = self.youtube_transcript_api.get_transcript(video_id)
            return transcript
        except NoTranscriptFound as ne:
            # Handle exception here
            pass

class TextCleaner:
    def __init__(self) -> None:
        self.lemmatizer = WordNetLemmatizer()
        pass

    def clean(self, text):
        # Remove HTML tags
        text = re.sub(r"<.*?>", "", text)

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Correct spelling
        # (Optional, replace with a spell checker library)

        # Remove extra spaces
        text = " ".join(text.split())

        # Remove stop words
        stop_words = set(stopwords.words("english"))
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        text = " ".join(filtered_words)

        # Lemmatize or stem words
        # (Choose lemmatize or stemming based on your preference)
        
        words = text.split()
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words]
        text = " ".join(lemmatized_words)

        return text

class Summarization:
    def __init__(self, temperature=0.1):
        # Initialize parameters here
        pass

    def summarize(self, text):
        # Implement your summarization logic here
        pass

class FactChecking:
    def __init__(self):
        pass
        
    def check(self, transcript, summary):
        # Your fact checking logic goes here
        pass
        
class YouTubeDataProcessor:
    def __init__(self, youtube_transcript_api, summarizer, fact_checker):
        self.youtube_transcript_api = youtube_transcript_api
        self.summarizer = summarizer
        self.fact_checker = fact_checker
        
    def process(self, video_id):
        transcript = self.youtube_transcript_api.get_transcript(video_id)
        summary = self.summarizer.summarize(transcript)
        mistakes = self.fact_checker.check(transcript, summary)
        # Handle and print the result here

def main():    
    pass

if __name__ == "__main__":
    main()