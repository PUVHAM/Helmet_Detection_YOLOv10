# YOLOv10 Helmet Safety Detection

This repository contains code and instructions for training and deploying a YOLOv10 model to monitor working safety by detecting helmets. The training is performed using Google Colab for free GPU access, and a Streamlit web application is provided for users to interact with the model.

## Table of Contents
- [Purpose](#purpose)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Streamlit App](#running-the-streamlit-app)
  - [Training the Model](#training-the-model)
  - [Testing Pre-trained Model](#testing-pre-trained-model)
- [Files in the Repository](#files-in-the-repository)
- [Model and Dataset](#model-and-dataset)
- [Acknowledgments](#acknowledgments)

## Purpose

The purpose of this project is to ensure working safety by monitoring the use of helmets in various environments. By using the YOLOv10 model, the system can detect whether individuals are wearing helmets, thus helping to enforce safety regulations and prevent accidents.

## Installation

To get started, clone the repository and install the required dependencies.

### Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)

### Step-by-Step Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/PUVHAM/Helmet_Detection_YOLOv10.git
    cd Helmet_Detection_YOLOv10
    ```

2. **Create and Activate Conda Environment:**

    If you don't have Miniconda or Anaconda installed, you can download it [here](https://docs.conda.io/en/latest/miniconda.html).

    ```bash
    conda create --name helmet_detection python=3.8
    conda activate helmet_detection
    ```

3. **Install Dependencies from requirements.txt:**

    Make sure you are in the root directory of the project.

    ```bash
    pip install -r requirements.txt
    ```

    This will install necessary Python packages including Streamlit, OpenCV, and other dependencies.

4. **Install Additional System Dependencies (if needed):**

    For Ubuntu or Debian-based systems, you might need to install `libGL`:

    ```bash
    sudo apt-get update
    sudo apt-get install libgl1-mesa-glx
    ```
```

## Usage 

### Running the Streamlit App

The Streamlit app allows users to upload images or provide YouTube video links for helmet detection.

1. Start the Streamlit app:

```bash
streamlit run app.py
```

2. Upload an image:

* Navigate to the web interface.
* Upload an image file (jpg, jpeg, png).
* Click on the "Predict" button to see the detection results.

### Testing Pre-trained Model
Use the provided pre_trained_model.ipynb notebook to test the pre-trained model.

1. Open `pre_trained_model.ipynb` in Google Colab.
2. Follow the instructions in the notebook to test the pre-trained model on sample images or videos.

### Training the Model
Training is done on Google Colab using the provided Jupyter notebook.

1. Open `helmet_safety_detection.ipynb` in Google Colab.
2. Follow the instructions in the notebook to train the model using the Safety Helmet Dataset.
3. The trained model will be saved as `best.pt`.
4. Download the Safety Helmet Dataset [here](https://drive.google.com/file/d/1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R/view).

## Files in the Repository
* `app.py:` Streamlit application code for helmet detection.
* `requirements.txt:` List of dependencies to be installed.
* `pre_trained_model.ipynb:` Jupyter notebook for testing the pre-trained model.
* `helmet_safety_detection.ipynb:` Jupyter notebook for training YOLOv10 on the Safety Helmet Dataset.
* `best.pt:` The YOLOv10 model trained on the Safety Helmet Dataset.
* `predict.py:` Code to handle the image prediction process in the Streamlit app.
* `processing.py:` Code for processing the image using the YOLOv10 model.

## Model and Dataset
* The model is trained on the Safety Helmet Dataset.
* The `best.pt` file is the result of the training process and is used for inference in the Streamlit app.

## Acknowledgments
* [YOLOv10 GitHub Repository](https://github.com/THU-MIG/yolov10)

Feel free to reach out if you have any questions or issues!

