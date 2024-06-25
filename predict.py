import streamlit as st 
import time
from processing import process_image
from PIL import Image

def predict_uploaded_image(uploaded_file):
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

