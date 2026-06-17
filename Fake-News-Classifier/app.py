import streamlit as st
import joblib
import os

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

# Title
st.title("Fake News Classifier")

# Input box
news = st.text_area("Enter news article here:")

# Prediction
if st.button("Predict"):

    prediction = model.predict([news])

    if prediction[0] == "fake":
        st.error("🚨 Fake News")
    else:
        st.success("✅ Real News")