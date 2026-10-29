import os
from dotenv import load_dotenv
from src.mongodb_store import MongoDBVectorStore
from langchain_groq import ChatGroq

load_dotenv()

DEFAULT_GROQ_MODEL = "openai/gpt-oss-20b"

class RAGSearch:
    def __init__(self, embedding_model: str = "all-MiniLM-L6-v2", llm_model: str = None):
        self.vectorstore = MongoDBVectorStore(embedding_model=embedding_model)

        groq_api_key = os.getenv("GROQ_API_KEY")
        selected_model = llm_model or os.getenv("GROQ_MODEL", DEFAULT_GROQ_MODEL)
        self.llm = ChatGroq(groq_api_key=groq_api_key, model_name=selected_model)
        print(f"[INFO] Groq LLM initialized: {selected_model}")
