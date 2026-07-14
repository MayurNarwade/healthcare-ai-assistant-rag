from pathlib import Path
import hashlib, logging
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import get_settings
from app.utils import normalize_text
log=logging.getLogger(__name__)
SUPPORTED={".txt",".md",".pdf"}
def _read(path):
    if path.suffix.lower()==".pdf":
        return "\n".join((p.extract_text() or "") for p in PdfReader(str(path)).pages)
    return path.read_text(encoding="utf-8",errors="replace")
def load_documents(data_dir=None):
    base=Path(data_dir or get_settings().data_dir)
    if not base.exists(): raise FileNotFoundError(f"Data directory not found: {base}")
    out=[]
    for p in sorted(base.iterdir()):
        if not p.is_file(): continue
        if p.suffix.lower() not in SUPPORTED:
            log.warning("Skipping unsupported file=%s",p.name); continue
        text=normalize_text(_read(p))
        if not text: log.warning("Skipping empty document=%s",p.name); continue
        out.append({"document":p.name,"source_path":str(p.as_posix()),"text":text})
    return out
def chunk_documents(documents):
    s=get_settings()
    splitter=RecursiveCharacterTextSplitter(chunk_size=s.chunk_size,chunk_overlap=s.chunk_overlap,
        separators=["\n\n","\n",". "," ",""])
    chunks=[]
    for doc in documents:
        for i,text in enumerate(splitter.split_text(doc["text"])):
            digest=hashlib.sha256(f'{doc["document"]}:{i}:{text}'.encode()).hexdigest()[:16]
            cid=f'{Path(doc["document"]).stem}_chunk_{i:03d}_{digest}'
            chunks.append({"id":cid,"text":text,"metadata":{"document":doc["document"],
              "chunk_id":cid,"source_path":doc["source_path"],"document_type":Path(doc["document"]).stem}})
    return chunks
