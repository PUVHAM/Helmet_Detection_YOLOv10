import streamlit as st 
import time
import os
from processing import process_image, process_video
from PIL import Image
from pytube import YouTube

def predict_image(uploaded_file):
    with st.spinner('Uploading image...'):
        time.sleep(3)
    st.success('Image uploaded successfully!')
    
    # Process image using image_processing module
    annotated_image = process_image(uploaded_file.read())
    
    # Display original image
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_column_width=True)
    
    st.text("Processing image...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    
    # Display annotated image
    st.image(annotated_image, caption='Predicted Image', use_column_width=True)
    st.balloons()

def predict_video(youtube_url=None, uploaded_video=None):
    with st.spinner('Downloading video and performing prediction...'):
        st.info("Processing video... This may take a while.")
        output_video_path = process_video(youtube_url=youtube_url, uploaded_video=uploaded_video)
    st.success('Video has been successfully processed!')

    # Check if the video file exists
    if os.path.exists(output_video_path):
        # Read the video file content
        with open(output_video_path, "rb") as file:
            video_bytes = file.read()
        
        # Create a download button
        st.download_button(
            label="Download video",
            data=video_bytes,
            file_name="output_video.mp4",  # The filename when downloading
            mime="video/mp4"  # The MIME type of the video
        )
    else:
        st.error(f"The video file {output_video_path} does not exist.")
