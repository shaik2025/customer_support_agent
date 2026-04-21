from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models import BaseChatModel
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm(model: str = "gemini-2.5-flash-lite") -> BaseChatModel:
    return ChatGoogleGenerativeAI(
        model=model,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    