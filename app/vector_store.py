import chromadb, logging
from app.config import get_settings
log=logging.getLogger(__name__)
class VectorStore:
    def __init__(self):
        s=get_settings(); self.name=s.chroma_collection
        self.client=chromadb.PersistentClient(path=s.vector_store_dir)
        self.collection=self.client.get_or_create_collection(self.name,metadata={"hnsw:space":"cosine"})
    def upsert(self,chunks,embeddings):
        if chunks:self.collection.upsert(ids=[c["id"] for c in chunks],documents=[c["text"] for c in chunks],
          metadatas=[c["metadata"] for c in chunks],embeddings=embeddings)
    def reset(self):
        try:self.client.delete_collection(self.name)
        except Exception:pass
        self.collection=self.client.get_or_create_collection(self.name,metadata={"hnsw:space":"cosine"})
    def count(self): return self.collection.count()
    def available(self):
        try:self.count(); return True
        except Exception:return False
    def search(self,embedding,top_k):
        if not self.count(): return []
        n=min(top_k,self.count())
        r=self.collection.query(query_embeddings=[embedding],n_results=n,include=["documents","metadatas","distances"])
        out=[]
        for id_,text,meta,dist in zip(r["ids"][0],r["documents"][0],r["metadatas"][0],r["distances"][0]):
            out.append({"id":id_,"text":text,"metadata":meta,"distance":float(dist),
                        "relevance_score":max(0.0,min(1.0,1.0-float(dist)))})
        return out
