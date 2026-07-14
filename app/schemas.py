from typing import Literal
from pydantic import BaseModel, Field

class Source(BaseModel):
    document: str
    chunk_id: str
    excerpt: str
    relevance_score: float
class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=2000)
class IngestRequest(BaseModel):
    reset: bool = False
class AskResponse(BaseModel):
    answer: str
    sources: list[Source] = Field(default_factory=list)
    confidence: Literal["high","medium","low"]
    confidence_reason: str
    route: Literal["rag","appointment_tool","safety"]
    grounded: bool
    response_time_ms: float
    tool: dict | None = None
class IngestResponse(BaseModel):
    status: str; documents_processed: int; chunks_created: int; collection_name: str; message: str
