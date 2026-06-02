import streamlit as st


# Page configuration
st.set_page_config(
    page_title = "Color Analysis Classifier",
    layout = "wide"
)

# Title and description
st.title("Color Analysis Prediction App")
st.markdown("""
            This app predicts a person's color analysis as one of 12 categories:
            - Winter: clear, cool, deep
            - Spring: clear, light, warm
            - Summer: cool, light, soft
            - Autumn: deep, soft, warm.
            """)
st.subheader("You can get your color analysis two ways:")
st.markdown("""
            1) Manually input your characteristics such as eye and hair color and get results

            OR

            2) Input a picture and get your color analysis.
            
            Use the sidebar to navigate between the two options.
""")

