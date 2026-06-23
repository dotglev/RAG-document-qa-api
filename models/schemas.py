from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    document_id: str
    question: str

class QueryResponse(BaseModel):
    question: str
    answer: str
    source_chunks: list[str]

class UploadResponse(BaseModel):
    document_id: str
    chunks_processed: int
    status: str

class WebhookPayload(BaseModel):
    event: str
    document_id: str
    status: str
    webhook_url: Optional[str] = None