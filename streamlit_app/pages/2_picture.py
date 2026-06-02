import os
import sys
ROOT = "/app"
sys.path.append(ROOT)

import streamlit as st
import pandas as pd
import torch
from torchvision import transforms
from PIL import Image
from models.cnn import SimpleCNN



# load cnn model
@st.cache_resource
def load_model():
    model = SimpleCNN(num_classes = 12)
    weights_path = os.path.join(ROOT, "models", "cnn_weights.pth")
    state = torch.load(weights_path, map_location="cpu", weights_only=False)
    model.load_state_dict(state)
    model.eval()
    return model

model = load_model()
filepath_csv = os.path.join(ROOT, "data", "processed", "processed.csv")
df = pd.read_csv(filepath_csv)
classes = df['season'].value_counts().index.to_list()

# define transform
transform = transforms.Compose([
    transforms.Resize((192, 256)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean = [0.47972053, 0.41974678, 0.41424349],
        std = [0.27473091, 0.24852708, 0.24372503]
    )
])

st.title("Image Color Analysis")
st.markdown("""
This allows you to input your picture(as a .png) to predict your color season.
Upload your image below to get your color analysis prediction. 
           """)


# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Upload your image")
    uploaded_image = st.file_uploader("Upload a .png image of you for analysis",
                                      type = ["png"])
    if uploaded_image is not None:
        img = Image.open(uploaded_image).convert("RGB")
        st.image(img, 
                 caption = "Uploaded PNG",)
        st.success("Image uploaded successfully")

    

with col2:
    st.subheader("Color Season")
    if st.button("Predict"):
        
        tensor = transform(img).unsqueeze(0)
        with torch.no_grad():
            outputs = model(tensor)
            predicted_class = torch.argmax(outputs, dim = 1).item()
            season = classes[predicted_class]
        st.success(f"Predicted class: {season}")












