"""
document_loader.py — Loads and chunks PDF, DOCX, TXT, CSV into text chunks.
"""
import csv
import io
from pathlib import Path
from typing import List

import docx
import pypdf


def load_document(file_bytes: bytes, filename: str) -> List[str]:
    """Parse uploaded file bytes into a list of text chunks by file type."""
    ext = Path(filename).suffix.lower()
    if ext == ".pdf":
        return _load_pdf(file_bytes)
    elif ext == ".docx":
        return _load_docx(file_bytes)
    elif ext == ".txt":
        return _load_txt(file_bytes)
    elif ext == ".csv":
        return _load_csv(file_bytes)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def _load_pdf(data: bytes) -> List[str]:
    reader = pypdf.PdfReader(io.BytesIO(data))
    return [page.extract_text() for page in reader.pages if page.extract_text()]


def _load_docx(data: bytes) -> List[str]:
    doc = docx.Document(io.BytesIO(data))
    return [p.text for p in doc.paragraphs if p.text.strip()]


def _load_txt(data: bytes) -> List[str]:
    return [data.decode("utf-8", errors="ignore")]


def _load_csv(data: bytes) -> List[str]:
    reader = csv.DictReader(io.StringIO(data.decode("utf-8", errors="ignore")))
    return [str(row) for row in reader]
