from typing import List
import chromadb
from sentence_transformers import SentenceTransformer
import config

_model = SentenceTransformer("all-MiniLM-L6-v2")


class _LocalEmbeddingFn:
    def __call__(self, input: List[str]) -> List[List[float]]:
        return _model.encode(input).tolist()


def _get_collection():
    client = chromadb.PersistentClient(path=config.CHROMA_DIR)
    return client.get_or_create_collection(
        name=config.COLLECTION_NAME,
        embedding_function=_LocalEmbeddingFn(),
    )


def store_chunks(chunks: List[str], doc_id: str) -> int:
    collection = _get_collection()
    ids = [f"{doc_id}_chunk_{i}" for i in range(len(chunks))]
    collection.upsert(documents=chunks, ids=ids)
    return len(chunks)


def query_chunks(query: str) -> List[str]:
    collection = _get_collection()
    results = collection.query(query_texts=[query], n_results=config.TOP_K_RESULTS)
    return results["documents"][0] if results["documents"] else []
