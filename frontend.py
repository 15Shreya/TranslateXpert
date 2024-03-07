import streamlit as st
import requests

st.title("Text Style Transfer")

input_text = st.text_area("Enter text to translate:", height=200)

style = st.text_area("Choose translation style:")

if st.button("Translate"):
    
    data = {
        "text": input_text,
        "style": style  
    }
    
    url = "http://localhost:5000/translate"
    response = requests.post(url, json=data)

    if response.status_code != 200:
        print(response.text)
        st.error("Request failed: " + response.text)
    else:
        translated_text = response.json()["translated_text"]
        st.write("Translated Text:")
        st.write(translated_text)
