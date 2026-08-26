"""
embeddings.py — Embeds text chunks and stores/retrieves from ChromaDB.
"""
from typing import List

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

import config


def _get_collection():
    client = chromadb.PersistentClient(path=config.CHROMA_DIR)
    embedding_fn = OpenAIEmbeddingFunction(
        api_key=config.OPENAI_API_KEY,
        model_name=config.EMBEDDING_MODEL,
    )
    return client.get_or_create_collection(
        name=config.COLLECTION_NAME,
        embedding_function=embedding_fn,
    )


def store_chunks(chunks: List[str], doc_id: str) -> int:
    """Embed and store text chunks in ChromaDB. Returns number of chunks stored."""
    collection = _get_collection()
    ids = [f"{doc_id}_chunk_{i}" for i in range(len(chunks))]
    collection.upsert(documents=chunks, ids=ids)
    return len(chunks)


def query_chunks(query: str) -> List[str]:
    """Query ChromaDB for top-K relevant chunks for the given query."""
    collection = _get_collection()
    results = collection.query(query_texts=[query], n_results=config.TOP_K_RESULTS)
    return results["documents"][0] if results["documents"] else []
