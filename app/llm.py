import httpx
from app.config import get_settings
from app.exceptions import LLMUnavailableError
class OllamaClient:
    async def available(self):
        s=get_settings()
        try:
            async with httpx.AsyncClient(timeout=5) as c:
                r=await c.get(f"{s.ollama_base_url}/api/tags"); return r.is_success
        except httpx.HTTPError:return False
    async def generate(self,prompt):
        s=get_settings()
        try:
            async with httpx.AsyncClient(timeout=s.llm_timeout_seconds) as c:
                r=await c.post(f"{s.ollama_base_url}/api/generate",json={"model":s.ollama_model,
                    "prompt":prompt,"stream":False,"options":{"temperature":s.llm_temperature}})
                r.raise_for_status(); answer=r.json().get("response","").strip()
                if not answer: raise LLMUnavailableError()
                return answer
        except httpx.HTTPError as e: raise LLMUnavailableError() from e
