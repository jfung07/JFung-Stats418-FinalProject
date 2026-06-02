import streamlit as st
import pandas as pd
import requests

# data for sidebar
filepath_csv = r"data/processed/processed.csv"
df = pd.read_csv(filepath_csv)


st.title("Manual Color Analysis")
st.markdown("""
This allows you to input your contrast, eye color, hair color, and skin tone to predict your color season.
Enter your details below to get your color analysis prediction. 
           """)

# load random forest model
RF_API_URL = "https://rf-api-980738607455.us-central1.run.app/predict"


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
                # Make prediction
        with st.spinner("Predicting..."):
            payload = {
                "contrast_level": contrast,
                "eye_cat": eye_color,
                "hair_cat": hair_color,
                "skin_tone": skin_tone
            }
            response = requests.post(RF_API_URL, json=payload)
            if response.status_code == 200:
                prediction = response.json().get("season")
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
                prediction = None

        # display prediction
        st.metric(
            label = "Color Analysis",
            value = prediction
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