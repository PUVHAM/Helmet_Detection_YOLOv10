import cv2
import numpy as np
import os
from ultralytics import YOLOv10
from pytube import YouTube


# Initialize YOLOv10 model with pretrained weights
MODEL_PATH = './best.pt'  # Ensure this path is correct and points to your best.pt file
model = YOLOv10(MODEL_PATH)

def process_image(file_bytes):
    # Read image using OpenCV
    image = cv2.imdecode(np.asarray(bytearray(file_bytes), dtype=np.uint8), 1)
    
    # Convert image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Perform prediction on the image
    results = model(source=image_rgb)[0]

    # Get annotated image and return
    annotated_image = results.plot()  # Using plot to get image with bounding boxes and confidence scores
    return annotated_image

def process_video(youtube_url=None, uploaded_video=None):
    if youtube_url:
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_path = stream.download(filename='youtube_video.mp4')
    elif uploaded_video:
        video_path = uploaded_video.name

        with open(video_path, "wb") as f:
            f.write(uploaded_video.getbuffer())

    results = model(source=video_path, show=False, save=False, stream=True)

    # Get the current directory path of the Python script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_video_path = os.path.join(current_directory, 'output_video.mp4')

    # Initialize video writer variables
    video_writer = None
    frame_rate = 30  # Frame rate of the output video

    for result in results:
        annotated_image = result.plot()
        
        # If video_writer is not initialized, initialize it with the frame dimensions
        if video_writer is None:
            height, width, _ = annotated_image.shape
            video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

        video_writer.write(annotated_image)

    if video_writer:
        video_writer.release()

    return output_video_path