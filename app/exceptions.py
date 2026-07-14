class AppError(Exception):
    def __init__(self, message: str, code="APP_ERROR", status_code=500):
        super().__init__(message); self.message=message; self.code=code; self.status_code=status_code
class EmptyKnowledgeBaseError(AppError):
    def __init__(self): super().__init__("Knowledge base is empty. Run ingestion first.","EMPTY_KNOWLEDGE_BASE",404)
class LLMUnavailableError(AppError):
    def __init__(self): super().__init__("The local LLM service is unavailable. Ensure Ollama is running and the configured model is installed.","LLM_UNAVAILABLE",503)
