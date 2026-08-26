"""
upload.py — POST /api/upload — Accepts a document, parses and stores in ChromaDB.
"""
import uuid
from fastapi import APIRouter, File, UploadFile, HTTPException
from core.document_loader import load_document
from core.embeddings import store_chunks

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        chunks = load_document(file_bytes, file.filename)
        if not chunks:
            raise HTTPException(status_code=400, detail="No text could be extracted from the document.")

        doc_id = str(uuid.uuid4())
        count = store_chunks(chunks, doc_id)

        return {
            "message": f"Document '{file.filename}' uploaded and stored successfully.",
            "doc_id": doc_id,
            "chunks_stored": count,
        }
    except ValueError as exc:
        raise HTTPException(status_code=415, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Upload failed: {exc}")
