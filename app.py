import streamlit as st
from predict import predict_uploaded_image

def main():
    st.title('YOLOv10 Helmet Detection')

    uploaded_file = st.file_uploader("Choose an image to predict", type=['jpg', 'jpeg', 'png'])
    
    if st.button('Predict') and uploaded_file is not None:
        predict_uploaded_image(uploaded_file)

if __name__ == '__main__':
    main()