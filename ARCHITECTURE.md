# Architecture
The API owns orchestration; modules isolate loading, embeddings, storage, generation, routing, tools, confidence, metrics, and schemas. Ingestion creates deterministic content-derived chunk IDs and uses Chroma upsert, making repeated ingestion idempotent. Query flow is safety routing → appointment routing → RAG. RAG embeds the query, retrieves cosine-nearest chunks, applies evidence gating, prompts Ollama, and attaches metadata-derived citations.

FastAPI was selected for typed async APIs and OpenAPI. Ollama enables local model serving. MiniLM is compact and CPU-friendly. ChromaDB provides simple persistent local vector search. Deterministic routing is predictable and testable.

Failure behavior: Ollama absence degrades health and returns 503 only for generation; mock tools remain usable. Unknown evidence returns a fixed fallback without calling the LLM. Production scaling would separate ingestion workers, use durable observability, access-control filters, a scalable vector service, model serving, and document versioning.
