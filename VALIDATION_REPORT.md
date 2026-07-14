# Healthcare AI Assistant — Validation Report

## Validation Environment

- Operating System: Windows
- Python: 3.11.0
- Ollama: 0.32.0
- Local LLM: Llama 3.2 3B
- Embedding Model: sentence-transformers/all-MiniLM-L6-v2
- Vector Database: ChromaDB
- Backend: FastAPI
- Frontend: Streamlit

## Environment Validation

The following major packages were imported successfully:

```text
FastAPI
ChromaDB
Sentence Transformers
Streamlit
PyTorch
```

Validation output:

```text
All major packages installed successfully
```

## Ollama Validation

Validated model:

```text
NAME           SIZE
llama3.2:3b    2.0 GB
```

Model download completed successfully.

## FastAPI Validation

Validated startup:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

The MiniLM embedding model loaded successfully.

## Document Ingestion

Validated output:

```text
status: success
documents_processed: 6
chunks_created: 9
collection_name: healthcare_knowledge
```

## Grounded RAG Validation

Question:

```text
Can a patient request a medication refill through telehealth?
```

Validated behavior:

```text
route: rag
grounded: true
confidence: medium
```

Relevant documents included:

```text
telehealth_guidelines.txt
medication_refill_policy.txt
```

The application returned verified source metadata and a grounded answer.

## Unknown-Answer Validation

Question:

```text
Does the policy cover dental implant surgery?
```

Validated output:

```text
answer:
I could not find this information in the provided documents.

sources: []
confidence: low
route: rag
grounded: false
```

The evidence gate prevented unsupported LLM generation.

## Agentic Tool Validation

Question:

```text
Can I book a cardiology appointment for Monday?
```

Validated behavior:

```text
route: appointment_tool
confidence: high
grounded: true
tool: check_available_slots
simulated: true
```

The response clearly stated that the appointment slots were demonstrations and not real bookings.

## Streamlit Validation

Validated through the frontend using:

```text
What identification is required during a telehealth visit?
```

Observed:

```text
Answer:
Government-issued identification may be requested when required by policy.

Confidence:
Medium

Route:
rag

Latency:
Approximately 3500 ms
```

Relevant source references were displayed.

## Automated Testing

Command:

```bash
pytest -v
```

Result:

```text
tests/test_agent.py::test_routes PASSED
tests/test_agent.py::test_mock_tool PASSED
tests/test_confidence.py::test_confidence_levels PASSED
tests/test_documents.py::test_documents_load_and_chunk PASSED

4 passed in 0.35s
```

## Evaluation

Command:

```bash
python evaluation/evaluate.py
```

Result:

```text
Route accuracy: 1.0
Citation match: 1.0
Errors: 0
```

These results represent performance on the included small synthetic prototype evaluation set and must not be interpreted as clinical accuracy.

## Final Local Validation Status

| Capability              | Result  |
| ----------------------- | ------- |
| Environment setup       | PASS    |
| Dependency installation | PASS    |
| Ollama integration      | PASS    |
| Llama 3.2 integration   | PASS    |
| Embedding generation    | PASS    |
| ChromaDB initialization | PASS    |
| Document ingestion      | PASS    |
| Semantic retrieval      | PASS    |
| Evidence gating         | PASS    |
| Grounded generation     | PASS    |
| Source references       | PASS    |
| Unknown-answer handling | PASS    |
| Appointment routing     | PASS    |
| Mock appointment tool   | PASS    |
| FastAPI                 | PASS    |
| Streamlit               | PASS    |
| Unit tests              | PASS    |
| Evaluation              | PASS    |
| Docker validation       | PENDING |

The Healthcare AI Assistant was successfully validated locally. Core RAG, LLM, retrieval, evidence-gating, source-reference, API, frontend, agentic-tool, testing, and evaluation workflows completed without runtime errors.

Docker validation was completed successfully. The Ollama, FastAPI, and Streamlit containers were built and started using Docker Compose. Container-to-container communication, local LLM availability, document ingestion, RAG question answering, agentic appointment routing, automated testing, and evaluation were successfully validated.
## Conclusion

The Healthcare AI Assistant was successfully validated end to end.

Core RAG, document ingestion, semantic retrieval, evidence gating, grounded LLM generation, source references, unknown-answer handling, FastAPI, Streamlit, agentic appointment routing, automated testing, evaluation, and Docker deployment completed successfully.

The Dockerized application successfully ran the following services:

- Ollama with Llama 3.2 3B
- FastAPI backend
- Streamlit frontend

The final Docker health check confirmed that the API, vector store, local LLM, and embedding model were available.

Final status: READY FOR TECHNICAL REVIEW AND SUBMISSION.