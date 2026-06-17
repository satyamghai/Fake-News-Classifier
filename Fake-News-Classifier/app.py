import streamlit as st
import joblib
import os
st.write("Current Folder:", os.getcwd())
st.write("Files:", os.listdir())

model=joblib.load('model.pkl')

st.title("Fake News Classifier")

news=st.text_area("Enter news article here:")

if(st.button("Predict")):

    prediction=model.predict([news])

    if(prediction[0]=="fake"):
        st.error("Fake News")
    else:
        st.success("Real News")


