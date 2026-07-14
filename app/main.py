from contextlib import asynccontextmanager
from datetime import datetime,timezone
import logging
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.config import get_settings
from app.logging_config import configure_logging
from app.schemas import AskRequest,IngestRequest,AskResponse,IngestResponse
from app.exceptions import AppError
from app.embeddings import EmbeddingService
from app.vector_store import VectorStore
from app.llm import OllamaClient
from app.rag import RAGPipeline
from app.agent import route_intent,safety_response,appointment_response
from app.document_loader import load_documents,chunk_documents
from app.metrics import metrics
configure_logging(); log=logging.getLogger(__name__); services={}
@asynccontextmanager
async def lifespan(app):
    services["embeddings"]=EmbeddingService(); services["store"]=VectorStore(); services["llm"]=OllamaClient()
    services["rag"]=RAGPipeline(services["embeddings"],services["store"],services["llm"]); yield; services.clear()
s=get_settings(); app=FastAPI(title=s.app_name,version=s.app_version,lifespan=lifespan)
@app.exception_handler(AppError)
async def app_error(request:Request,exc:AppError):
    metrics.error(); return JSONResponse(status_code=exc.status_code,content={"detail":{"code":exc.code,"message":exc.message}})
@app.exception_handler(Exception)
async def unexpected(request:Request,exc:Exception):
    log.exception("Unhandled error"); metrics.error(); return JSONResponse(status_code=500,content={"detail":{"code":"INTERNAL_ERROR","message":"An unexpected error occurred."}})
@app.get("/")
async def root(): return {"name":s.app_name,"version":s.app_version,"status":"running","documentation":"/docs"}
@app.get("/health")
async def health():
    vs=services["store"].available(); emb=services["embeddings"].available(); llm=await services["llm"].available()
    return {"status":"healthy" if vs and emb and llm else "degraded","api":"available","vector_store":"available" if vs else "unavailable","llm":"available" if llm else "unavailable","embedding_model":"available" if emb else "unavailable","timestamp":datetime.now(timezone.utc).isoformat()}
@app.post("/ingest",response_model=IngestResponse)
async def ingest(req:IngestRequest):
    if req.reset:services["store"].reset()
    docs=load_documents(); chunks=chunk_documents(docs); embeddings=services["embeddings"].embed_documents([c["text"] for c in chunks])
    services["store"].upsert(chunks,embeddings); metrics.ingestion()
    return {"status":"success","documents_processed":len(docs),"chunks_created":len(chunks),"collection_name":s.chroma_collection,"message":"Healthcare documents were ingested successfully."}
@app.post("/ask",response_model=AskResponse)
async def ask(req:AskRequest):
    q=" ".join(req.question.split()); route=route_intent(q)
    result=safety_response() if route=="safety" else appointment_response(q) if route=="appointment_tool" else await services["rag"].answer(q)
    metrics.question(result); return result
@app.get("/metrics")
async def get_metrics():return metrics.snapshot()
