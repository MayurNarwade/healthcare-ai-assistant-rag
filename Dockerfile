FROM python:3.11-slim

WORKDIR /app

RUN groupadd -r app && \
    useradd -r -g app -d /home/app -m app

ENV HOME=/home/app \
    HF_HOME=/app/.cache/huggingface \
    TRANSFORMERS_CACHE=/app/.cache/huggingface \
    SENTENCE_TRANSFORMERS_HOME=/app/.cache/sentence-transformers \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt .

RUN pip install \
    --no-cache-dir \
    --default-timeout=300 \
    --retries=10 \
    -r requirements.txt

COPY . .

RUN mkdir -p \
    /app/vector_store \
    /app/logs \
    /app/.cache/huggingface \
    /app/.cache/sentence-transformers && \
    chown -R app:app /app /home/app

USER app

EXPOSE 8000 8501

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]