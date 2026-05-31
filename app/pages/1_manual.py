import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

# data for sidebar
filepath_csv = r"C:\Users\jfung\Documents\Stats418_FinalProject\data\processed\processed.csv"
df = pd.read_csv(filepath_csv)


st.title("Manual Color Analysis")
st.markdown("""
This allows you to input your contrast, eye color, hair color, and skin tone to predict your color season.
Enter your details below to get your color analysis prediction. 
           """)

# load random forest model
@st.cache_resource
def load_model():
    model = joblib.load("models/rf.pkl")
    return model

bundle = load_model()
pipeline = bundle['pipeline']
label_encoder = bundle['label_encoder']

# Sidebar for inputs
st.sidebar.header("Your features")

# Input features
contrast = st.sidebar.radio(
    "Choose your contrast level",
    df['contrast_level'].value_counts().index.to_list()
)

eye_color = st.sidebar.selectbox(
    "Choose your eye color",
    df['eye_cat'].value_counts().index.to_list()
)

hair_color = st.sidebar.selectbox(
    "Choose your hair color",
    df['hair_cat'].value_counts().index.to_list()
)

skin_tone = st.sidebar.radio(
    "Choose your skin tone",
    df['skin_tone'].value_counts().index.to_list()
)

# Predict button
predict_button = st.sidebar.button("Predict Season", type = "primary")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Your details")
    # Input summary
    details_df = pd.DataFrame({
        'Feature': ['Contrast', 'Eye Color', 'Hair Color', 'Skin Tone'],
        'Value': [contrast, eye_color, hair_color, skin_tone]
    })
    st.table(details_df)

with col2:
    st.subheader("Color Season")
    if predict_button:
        # Prep features
        features = pd.DataFrame([{
            "contrast_level": contrast,
            "eye_cat": eye_color,
            "hair_cat": hair_color,
            "skin_tone": skin_tone
        }])

        # Make prediction
        with st.spinner("Predicting..."):
            encoded_prediction = pipeline.predict(features)[0]
            prediction = label_encoder.inverse_transform([encoded_prediction])[0]

        # display prediction
        st.metric(
            label = "Color Analysis",
            value = f"{prediction}",
            delta = None
        )
    
with st.expander("About the Model"):
    st.write("""
    Model Type: Random Forest Regressor
             
    Features: 
             
             - Contrast level
             - Eye color
             - Hair color
             - Skin tone

    Model Performance:
             
             - F1 Score: 0.3217
             - Accuracy: 0.4583
             - Training Data: 224 people
             """)
    
with st.expander("High, Medium, or Low contrast"):
    st.write("""
    If you do not know your contrast level:
             
    Convert a natural light photo of yourself to black and white.
             
    1) High: light and dark differentials are clear      
    2) Medium: balance between light and dark elements
    3) Low: subtle mixes and smooth fades between light and dark

    From https://color-analysis.app/blog/what-is-your-contrast-level-high-and-low-contrast-coloring-guide
             """)

with st.expander("Warm or Cool"):
    st.write("""
    If you do not know if you are cool toned or warm toned:
             
    Hold a piece of white paper up next to your skin.
             
    1) Cool: your skin looks pink or blue next to the paper.
             
    2) Warm: your skin looks yellowish next to the paper.
             
    From https://www.wikihow.com/Determine-Skin-Tone
             """)