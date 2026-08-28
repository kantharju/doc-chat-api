import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
MODEL: str = os.getenv("GROQ_MODEL", "llama3-8b-8192")

CHROMA_DIR: str = "chroma_store"
COLLECTION_NAME: str = "documents"

CHUNK_SIZE: int = 500
CHUNK_OVERLAP: int = 50
TOP_K_RESULTS: int = 5
