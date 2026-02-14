import os
import numpy as np
import tensorflow as tf
import cv2
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from gradcam_utils import make_gradcam_heatmap

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

IMG_SIZE = 224
MODEL_PATH = "deepfake_model_converted.keras"

def build_model():
    base_model = MobileNetV2(
        input_shape=(IMG_SIZE, IMG_SIZE, 3),
        include_top=False,
        weights=None
    )
    x = layers.GlobalAveragePooling2D()(base_model.output)
    x = layers.Dense(128, activation="relu")(x)
    output = layers.Dense(1, activation="sigmoid")(x)
    model = models.Model(inputs=base_model.input, outputs=output)
    return model

model = build_model()
model.load_weights(MODEL_PATH)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def save_heatmap(original_path, heatmap):
    img = cv2.imread(original_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    heatmap = cv2.resize(heatmap, (IMG_SIZE, IMG_SIZE))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    superimposed_img = heatmap * 0.4 + img
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], "heatmap.jpg")
    cv2.imwrite(output_path, superimposed_img)

    return "static/uploads/heatmap.jpg"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    heatmap_path = None
    uploaded_image = None
    risk = None

    if request.method == "POST":
        file = request.files["file"]
        if file:
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            uploaded_image = file.filename
            img_array = preprocess_image(file_path)

            pred = model.predict(img_array)[0][0]

            if pred > 0.5:
                prediction = "Real"
                confidence = round(float(pred) * 100, 2)
                risk = "Low"
            else:
                prediction = "Fake"
                confidence = round((1 - float(pred)) * 100, 2)
                risk = "High"

            heatmap = make_gradcam_heatmap(img_array, model, "Conv_1")
            heatmap_path = save_heatmap(file_path, heatmap)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        heatmap_path=heatmap_path,
        uploaded_image=uploaded_image,
        risk=risk
    )

if __name__ == "__main__":
    app.run()
