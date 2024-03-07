# Youtube Video Transcriber
Web app link : https://youtubevideotranscriberapp-ysmkqnbyhwnnqvz8lre9qu.streamlit.app/

This project is a Youtube video transcript generator and summarizer application powered by Generative AI. It extracts the transcript of a provided Youtube video and generates a detailed summary of the video content in a concise and meaningful format.

## Features
- **Youtube Video Transcript Extraction:** Utilizes the YouTube Transcript API to extract the transcript text from a specified Youtube video URL.
- **Summarization using Generative AI:** Leverages Google's Generative AI model, Gemini Pro, to generate a detailed summary of the video transcript.
- **Streamlit Web Application:** Developed as a Streamlit web application, providing a user-friendly interface for inputting Youtube video URLs and obtaining the transcript and summary.

## Technical Details
- **Libraries Used:**
  - `streamlit`: For building the web application interface.
  - `dotenv`: For loading environment variables.
  - `google.generativeai`: For accessing the Generative AI model.
  - `youtube_transcript_api`: For fetching the Youtube video transcript.
- **Google API Key:** Requires a valid Google API key to access the Generative AI model. Ensure to set up the API key in the environment variables.
- **Generative AI Model:** Utilizes Google's Gemini Pro model for content generation, configured through the `GenerativeModel` class.
- **Transcript Extraction:** The `extract_transcript_details` function extracts the transcript text from the provided Youtube video URL using the YouTube Transcript API.
- **Summarization:** The `generate_gemini_content` function generates a detailed summary of the video transcript using the provided transcript text and a predefined prompt.
- **Streamlit Application:** The Streamlit web application allows users to input a Youtube video URL, fetch the original transcript, and obtain a detailed summary of the video content with the click of a button.

## Usage
1. Provide the URL of the desired Youtube video in the input field.
2. Click on the "Get Youtube Video Original Transcript" button to fetch the original transcript of the video.
3. Click on the "Get Detailed Summary of the Video" button to generate a detailed summary of the video content.

## Deployment
- **Local Deployment:** Clone the repository, install the required dependencies listed in the `requirements.txt` file, set up the Google API key in the environment variables, and run the Streamlit application locally using `streamlit run app.py`.
- **Online Deployment:** Deploy the application to platforms like Heroku or Streamlit Sharing for online access.

## Credits
- This project utilizes the YouTube Transcript API for transcript extraction.
- Powered by Google's Generative AI model, Gemini Pro, for content summarization.
