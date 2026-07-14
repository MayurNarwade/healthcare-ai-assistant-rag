import logging
from sentence_transformers import SentenceTransformer
from app.config import get_settings
log=logging.getLogger(__name__)
class EmbeddingService:
    def __init__(self):
        self.model_name=get_settings().embedding_model
        log.info("Loading embedding model=%s",self.model_name)
        self.model=SentenceTransformer(self.model_name)
    def embed_documents(self,texts): return self.model.encode(texts,normalize_embeddings=True).tolist()
    def embed_query(self,text): return self.model.encode(text,normalize_embeddings=True).tolist()
    def available(self): return self.model is not None
