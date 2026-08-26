"""
chat.py — POST /api/chat — Accepts a question and returns an AI answer from stored docs.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.chat_engine import answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    try:
        return answer(request.question)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Chat failed: {exc}")
