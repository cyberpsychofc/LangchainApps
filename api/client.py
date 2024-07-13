import requests
import streamlit as st

def get_groq_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json = {'input':{'topic':input_text}})

    return response.json()['output']['content']

st.title('LangChain Bot with GroqAI')
input_text = st.text_input("Write an essay on...")

if input_text:
    st.write(get_groq_response(input_text))