# 🚀 Deepfake AI Detection System

An AI-powered Deepfake Detection Web Application built using **TensorFlow, MobileNetV2, Flask, and Grad-CAM Explainability**.

This project demonstrates real-world AI deployment using transfer learning and explainable AI techniques.

---

## 📌 Project Overview

Deepfake content is becoming increasingly sophisticated.  
This system detects whether an uploaded face image is:

- ✅ Real  
- ❌ Fake  

The model uses **Transfer Learning (MobileNetV2)** and provides **Grad-CAM heatmaps** to explain predictions visually.

The application is deployed as a full-stack web application using Flask.

---

## 🧠 AI Model Details

- Architecture: **MobileNetV2 (Pretrained on ImageNet)**
- Transfer Learning Approach
- Binary Classification (Real vs Fake)
- Image Size: 224x224
- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Explainability: Grad-CAM Visualization

---

## 🌐 Web Application Features

- Modern cinematic UI (Orange + Dark Theme)
- Custom animated cursor
- Scroll animations (GSAP + AOS)
- Orange planet dynamic background
- Image upload interface
- Confidence score display
- Risk level classification
- Grad-CAM heatmap visualization
- Responsive design

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- TensorFlow
- NumPy
- OpenCV

### Frontend
- HTML5
- CSS3
- JavaScript
- GSAP Animations
- AOS Scroll Animations

---

## 📂 Project Structure

deepfake-ai-detection/
│
├── app.py
├── train_model.py
├── gradcam_utils.py
├── face_utils.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ ├── css/
│ ├── js/
│ └── uploads/


---

## ▶️ How to Run Locally

1. Clone the repository:

git clone https://github.com/o1dsport/deepfake-ai-detection.git

cd deepfake-ai-detection


2. Install dependencies:

pip install -r requirements.txt


3. Add your trained `.h5` model file in the root directory.


4. Run the application:

python app.py


5. Open in browser:
http://127.0.0.1:5000/


## 🔬 Training the Model

To train the model:

python train_model.py

csharp
Copy code

Make sure dataset is structured as:

dataset/
├── real/
└── fake/

yaml
Copy code

---

## 📈 Future Improvements

- Deploy to cloud (Render / Railway / AWS)
- Add face detection preprocessing
- Support video deepfake detection
- Improve dataset scale
- Implement CNN fine-tuning phase
- Add API endpoint support

---

## 👨‍💻 Author

**Ashish Kumar**  
B.Tech Student | AI & Machine Learning Enthusiast  

Focused on building real-world AI systems with production-level deployment.

---

## ⭐ If You Like This Project

Give it a star ⭐ on GitHub.