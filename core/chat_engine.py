import httpx
from groq import Groq
import config
from core.embeddings import query_chunks

_client = Groq(api_key=config.GROQ_API_KEY, http_client=httpx.Client(verify=False))

SYSTEM_PROMPT = (
    "You are a helpful assistant. Answer the user's question using ONLY "
    "the context provided below. If the answer is not in the context, say "
    "'I don't have enough information in the uploaded documents to answer that.'"
)


def answer(question: str) -> dict:
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
