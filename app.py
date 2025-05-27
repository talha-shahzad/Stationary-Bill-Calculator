import torch
import streamlit as st
from PIL import Image
import numpy as np
import pathlib

# To Run the application
# streamlit run app.py --server.fileWatcherType none

# Patch to avoid PosixPath error on Windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:\\Applied ML\\best.pt', force_reload=True)

st.title("Stationary Item Bill Calculator")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Inference
    results = model(image)
    results.render()

    # Display result
    st.image(Image.fromarray(results.ims[0]), caption="Detected Image", use_column_width=True)

    # Extract labels and count
    labels = results.pandas().xyxy[0]['name']
    st.write("Detected items:")
    st.write(labels.value_counts())

    # Simple billing (example)
    price_list = {
    'Eraser': 5,
    'Pencil': 10,
    'Ruler': 15,
    'Sharpner': 7,
    'Unknown': 0  # Unknown items are not charged
}
    total = sum(price_list.get(label, 0) for label in labels)
    st.write(f"**Total Price:** Rs. {total}")
