"""
config.py — Central configuration. Change MODEL here to switch GPT version.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ── OpenAI ────────────────────────────────────────────────────────────────────
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

# ── Model config — change here to switch: "gpt-3.5-turbo" | "gpt-4" | "gpt-4o"
MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
EMBEDDING_MODEL: str = "text-embedding-3-small"

# ── ChromaDB ──────────────────────────────────────────────────────────────────
CHROMA_DIR: str = "chroma_store"
COLLECTION_NAME: str = "documents"

# ── RAG ───────────────────────────────────────────────────────────────────────
CHUNK_SIZE: int = 500
CHUNK_OVERLAP: int = 50
TOP_K_RESULTS: int = 5
