import gradio as gr
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

IMG_SIZE = 224

model = load_model("deepfake_model_phase1.h5")

def predict_image(img):

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img_array = img / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0][0]

    if pred > 0.5:
        label = "Real"
        confidence = float(pred) * 100
    else:
        label = "Fake"
        confidence = (1 - float(pred)) * 100

    return f"{label} ({confidence:.2f}%)"

interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="Deepfake AI Detection",
    description="Upload an image to detect whether it is Real or Fake."
)

interface.launch()
