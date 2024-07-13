from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
##Langsmith Tracking
os.environ["LANGCHAIN_TRACING"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an assistant. Please respond to the user query."),
        ("user","Question:{question}")
    ]
)

##Interface
st.title('Langchain Demo w/ GROQ AI')
input_text = st.text_input("Enter your Question...")

llm = ChatGroq(model="llama3-8b-8192")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))