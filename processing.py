import cv2
import numpy as np
from ultralytics import YOLOv10

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
