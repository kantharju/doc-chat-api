# Doc Chat API

A RAG-based chatbot that lets you upload documents and ask questions about them.

## Stack
- **FastAPI** — REST API
- **ChromaDB** — Vector store (persisted locally)
- **OpenAI** — Embeddings (`text-embedding-3-small`) + Chat (`gpt-3.5-turbo`)
- **Simple HTML/JS** — Frontend UI

## Supported Document Types
PDF, DOCX, TXT, CSV

## Setup

```bash
git clone https://github.com/<your-username>/doc-chat-api.git
cd doc-chat-api
pip install -r requirements.txt
cp .env.example .env        # Add your OpenAI API key
```

## Run

```bash
uvicorn api.main:app --reload
```

Open http://localhost:8000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/upload` | Upload a document |
| POST | `/api/chat` | Ask a question |

## Switch GPT Model

In `.env`:
```
OPENAI_MODEL=gpt-4
```
Or options: `gpt-3.5-turbo` | `gpt-4` | `gpt-4o`

## Project Structure

```
doc-chat-api/
├── api/
│   ├── main.py              # FastAPI app
│   └── routes/
│       ├── upload.py        # Upload endpoint
│       └── chat.py          # Chat endpoint
├── core/
│   ├── document_loader.py   # Parse PDF, DOCX, TXT, CSV
│   ├── embeddings.py        # ChromaDB store/query
│   └── chat_engine.py       # RAG + OpenAI
├── frontend/
│   └── index.html           # UI
├── config.py                # Central config
├── .env.example
└── requirements.txt
```
