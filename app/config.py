from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Healthcare AI Assistant"
    app_version: str = "1.0.0"
    app_env: str = "development"
    host: str = "0.0.0.0"
    port: int = 8000
    data_dir: str = "data"
    vector_store_dir: str = "vector_store"
    chroma_collection: str = "healthcare_knowledge"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2:3b"
    llm_temperature: float = 0.1
    llm_timeout_seconds: int = 120
    chunk_size: int = 800
    chunk_overlap: int = 120
    top_k: int = 4
    min_relevance_score: float = 0.45
    max_question_length: int = 2000
    log_level: str = "INFO"
    log_file: str = "logs/healthcare_ai.log"
    api_base_url: str = "http://localhost:8000"
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, extra="ignore")

@lru_cache
def get_settings(): return Settings()
