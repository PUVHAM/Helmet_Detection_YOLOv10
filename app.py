import streamlit as st
from predict import predict_image, predict_video

def main():
    st.title('YOLOv10 Helmet Detection')

    # Option to choose between uploading an image or predicting from a YouTube video
    option = st.selectbox("Select input source:", ("Upload Image", "YouTube Video", "Upload Video"))

    if option == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image to predict", type=['jpg', 'jpeg', 'png'])
        
        if st.button('Predict') and uploaded_file is not None:
            predict_image(uploaded_file)
    
    elif option == "YouTube Video":
        youtube_url = st.text_input("Enter YouTube video URL:", "")
        
        if st.button('Predict') and youtube_url:
            predict_video(youtube_url=youtube_url)
            
    elif option == "Upload Video":
        uploaded_video = st.file_uploader("Choose a video file to predict", type=['mp4', 'avi', 'mov'])
        
        if st.button('Predict') and uploaded_video is not None:
            predict_video(uploaded_video=uploaded_video)

if __name__ == '__main__':
    main()
