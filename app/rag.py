import re
import time

from app.confidence import confidence
from app.config import get_settings
from app.exceptions import EmptyKnowledgeBaseError
from app.prompts import FALLBACK, SYSTEM_PROMPT
from app.utils import excerpt


class RAGPipeline:
    def __init__(self, embeddings, store, llm):
        self.embeddings = embeddings
        self.store = store
        self.llm = llm

    async def answer(self, question):
        start = time.perf_counter()
        settings = get_settings()

        if not self.store.count():
            raise EmptyKnowledgeBaseError()

        query_embedding = self.embeddings.embed_query(question)

        results = self.store.search(
            query_embedding,
            settings.top_k,
        )

        relevant = [
            result
            for result in results
            if result["relevance_score"]
            >= settings.min_relevance_score
        ]

        level, reason = confidence(relevant)

        if not relevant or level == "low":
            return {
                "answer": FALLBACK,
                "sources": [],
                "confidence": "low",
                "confidence_reason": (
                    "No sufficiently relevant evidence was found."
                ),
                "route": "rag",
                "grounded": False,
                "response_time_ms": round(
                    (time.perf_counter() - start) * 1000,
                    2,
                ),
                "tool": None,
            }

        context = "\n\n".join(
            (
                f'[SOURCE {index + 1}: '
                f'{result["metadata"]["document"]}]\n'
                f'{result["text"]}'
            )
            for index, result in enumerate(relevant)
        )

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=question,
        )

        answer = await self.llm.generate(prompt)

        # Remove source labels copied by the LLM.
        # Verified citations are generated separately from vector metadata.
        answer = re.sub(
            r"\s*\((?:source)\s*\d*\s*:\s*[^)]+\)",
            "",
            answer,
            flags=re.IGNORECASE,
        ).strip()

        if FALLBACK.lower() in answer.lower():
            return {
                "answer": FALLBACK,
                "sources": [],
                "confidence": "low",
                "confidence_reason": (
                    "The supplied evidence was insufficient."
                ),
                "route": "rag",
                "grounded": False,
                "response_time_ms": round(
                    (time.perf_counter() - start) * 1000,
                    2,
                ),
                "tool": None,
            }

        sources = [
            {
                "document": result["metadata"]["document"],
                "chunk_id": result["metadata"]["chunk_id"],
                "excerpt": excerpt(result["text"]),
                "relevance_score": round(
                    result["relevance_score"],
                    4,
                ),
            }
            for result in relevant
        ]

        return {
            "answer": answer,
            "sources": sources,
            "confidence": level,
            "confidence_reason": reason,
            "route": "rag",
            "grounded": True,
            "response_time_ms": round(
                (time.perf_counter() - start) * 1000,
                2,
            ),
            "tool": None,
        }