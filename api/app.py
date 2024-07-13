from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server"
)
add_routes(
    app,
    ChatGroq(),
    path="/groq"
)

model = ChatGroq()

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} around 100 words.")

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)