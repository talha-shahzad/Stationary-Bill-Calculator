Here's a professional and clear `README.md` for your **Stationary Object Detection using YOLOv5 and Streamlit** project:

---

# 📦 Stationary Object Detection And Bill Calculation using YOLOv5 and Streamlit

This project is a web-based application that detects stationary objects (such as pens, notebooks, staplers, etc.) using a custom-trained **YOLOv5** model. The app is built with **Streamlit** to provide a fast and interactive user interface.

---

## 🚀 Features

* 📷 Upload an image and detect stationary items in real-time
* 🎯 Uses a YOLOv5 model trained on a custom dataset annotated via Roboflow
* ⚡ Built with Streamlit for a responsive and simple UI
* 📥 Supports drag-and-drop image upload
* 💡 Displays detection confidence scores and bounding boxes

---

## 🖼️ Demo

![image](https://github.com/user-attachments/assets/8b1f2b3b-f28c-43f2-9329-c7aeb2957d6d)

---

## 🛠️ Technologies Used

* [YOLOv5](https://github.com/ultralytics/yolov5) – object detection model
* [Streamlit](https://streamlit.io/) – frontend interface
* [PyTorch](https://pytorch.org/) – model inference backend
* [Roboflow](https://roboflow.com/) – used for dataset annotation and augmentation

---

## 📁 Project Structure

```
stationary-object-detection/
├── yolov5/                  # YOLOv5 cloned repo
├── best.pt                 # Trained model weights
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stationary-object-detection.git
cd stationary-object-detection
```

### 2. Install Dependencies

We recommend creating a virtual environment:

```bash
pip install -r requirements.txt
```

Make sure you have **PyTorch** installed with CUDA support if you're using GPU.

### 3. Download YOLOv5 and Place Model

Clone YOLOv5 (if not already):

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
cd ..
```

Place your `best.pt` model weights in the root or appropriate folder.

---

### 4. Run the Streamlit App

```bash
streamlit run app.py --server.fileWatcherType none
```

---

## 📸 How to Use

1. Launch the app in your browser.
2. Upload an image using the sidebar.
3. The app will detect and display stationary objects in the image.
4. You can view confidence scores and bounding boxes in real-time.

---


## 📌 Future Improvements

* Add support for video or webcam input
* Improve UI with multiple layout modes
* Add object counting and result export
* Integrate sound or text alerts for detected objects

---

## 🧠 Acknowledgments

* [Ultralytics](https://github.com/ultralytics/yolov5) for the YOLOv5 framework
* [Roboflow](https://roboflow.com/) for dataset management and annotation

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more information.

---

Let me know if you'd like it tailored with your GitHub repo link or demo screenshots.
