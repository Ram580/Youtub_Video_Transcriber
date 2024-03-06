import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt  = """You are a Amazing Youtube video summarizer, Your objective is to take the provided transcript text
and summerize the entire video transcript into to consise and meaningful summary in points within 250 points, The summary should cover all the
important points.
The transcript text is :
"""

## Getting the transcript data from the videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        
        transcript = ""
        for i in transcript_text:
            transcript += " "+i["text"]
        return transcript
    
    except Exception as e:
        raise e

## getting the esummary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text


## Streamlit APP

st.set_page_config(page_title="ATS Resume Expert")
st.header("Youtube Video Transcriber")
st.title("Youtube Transcript to detailed notes converter")

youtube_link = st.text_input("Enter Youtube Video Link: ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    #print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    

if st.button("Get Youtube Video Original Transcript"):
    original_transcript = extract_transcript_details(youtube_link)
    st.subheader('The Original Transcript is ')
    st.write(original_transcript)
    
if st.button("Get Detailed Summary of the Video"):
    transcript_text = extract_transcript_details(youtube_link)
    
    if transcript_text:
        summary = generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)