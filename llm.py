from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models import BaseChatModel
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm(model) -> BaseChatModel:
    return ChatGoogleGenerativeAI(
        model=os.getenv("MODEL"),
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
