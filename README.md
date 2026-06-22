# RAG Document Q&A API

A production-ready REST API that lets users upload any PDF and ask questions about it using AI. Built with RAG (Retrieval-Augmented Generation).

## What it does

Upload a PDF → the system extracts the text, breaks it into chunks, converts them to embeddings, and stores them in a vector database. When you ask a question, it finds the most relevant chunks and sends them to an LLM to generate a precise, document-grounded answer.

## Tech Stack

- **FastAPI** — REST API framework
- **PyMuPDF** — PDF text extraction
- **sentence-transformers** — local embeddings (no GPU needed)
- **ChromaDB** — local vector database
- **Groq (LLaMA 3.3)** — LLM for answer generation
- **Streamlit** — browser UI
- **Webhooks** — async notifications when processing completes

## Features

- Upload any PDF via REST API or browser UI
- Ask natural language questions about the document
- AI answers grounded in document content only
- API key authentication
- Webhook notifications on document processing
- Auto-generated interactive API docs at `/docs`

## Installation

```bash
git clone https://github.com/dotglev/RAG-document-qa-api.git
cd RAG-document-qa-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root folder:


OUR_API_KEY=your-api-key-here

GROQ_API_KEY=your-groq-api-key-here


Get a free Groq API key at https://console.groq.com

## Running the API

```bash
uvicorn main:app --reload
```

API runs at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

## Running the UI

```bash
streamlit run ui/streamlit_app.py
```

UI runs at `http://localhost:8501`

## API Usage

**Upload a PDF:**
```bash
curl -X POST "http://localhost:8000/upload" \
  -H "X-API-Key: your-api-key" \
  -F "file=@document.pdf"
```

**Ask a question:**
```bash
curl -X POST "http://localhost:8000/query" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"document_id": "your-document-id", "question": "What is this document about?"}'
```

## Project Structure

RAG-document-qa-api/

├── main.py              # FastAPI app entry point

├── config.py            # Environment variable loader

├── requirements.txt     # Dependencies

├── routers/

│   ├── auth.py          # API key authentication

│   ├── upload.py        # PDF upload endpoint

│   └── query.py         # Question answering endpoint

├── services/

│   ├── pdf_processor.py # PDF text extraction

│   ├── chunker.py       # Text chunking

│   ├── embedder.py      # Embedding generation

│   ├── vector_store.py  # ChromaDB operations

│   ├── llm.py           # Groq LLM integration

│   └── webhook.py       # Webhook notifications

└── ui/

└── streamlit_app.py # Browser interface