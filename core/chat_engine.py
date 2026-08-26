"""
chat_engine.py — RAG: retrieves relevant chunks and calls OpenAI to answer.
"""
from openai import OpenAI

import config
from core.embeddings import query_chunks

_client = OpenAI(api_key=config.OPENAI_API_KEY)

SYSTEM_PROMPT = (
    "You are a helpful assistant. Answer the user's question using ONLY "
    "the context provided below. If the answer is not in the context, say "
    "'I don't have enough information in the uploaded documents to answer that.'"
)


def answer(question: str) -> dict:
    """Retrieve relevant chunks and generate an answer using OpenAI."""
    chunks = query_chunks(question)
    if not chunks:
        return {"answer": "No documents found. Please upload a document first.", "sources": []}

    context = "\n\n".join(chunks)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
    ]

    response = _client.chat.completions.create(
        model=config.MODEL,
        messages=messages,
        temperature=0.2,
    )

    return {
        "answer": response.choices[0].message.content,
        "model": config.MODEL,
        "sources": chunks,
    }
