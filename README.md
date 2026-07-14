# 🏥 Healthcare AI Assistant Using RAG and Local LLMs

> A privacy-conscious, healthcare-focused Retrieval-Augmented Generation (RAG) assistant that generates grounded answers from an approved document knowledge base using semantic retrieval, evidence gating, ChromaDB, FastAPI, Streamlit, Ollama, and Llama 3.2.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![Llama](https://img.shields.io/badge/LLM-Llama%203.2%203B-purple)
![ChromaDB](https://img.shields.io/badge/Vector%20Database-ChromaDB-orange)
![Docker](https://img.shields.io/badge/Docker-Validated-2496ED)
![Tests](https://img.shields.io/badge/Tests-4%2F4%20Passed-brightgreen)
![Evaluation](https://img.shields.io/badge/Evaluation-Passed-success)
![License](https://img.shields.io/badge/License-Project%20Use-lightgrey)

---

## ⚠️ Healthcare Safety Disclaimer

This application is an **engineering prototype** designed to demonstrate Retrieval-Augmented Generation, local LLM integration, semantic search, API development, agentic routing, testing, evaluation, and containerized deployment.

The system provides information only from the included synthetic healthcare policy documents.

It does **not** provide:

- Medical diagnosis
- Treatment recommendations
- Medication prescriptions
- Dosage recommendations
- Personalized medical advice
- Clinical decision support
- Emergency medical assistance
- Real appointment booking

The included healthcare documents are synthetic and contain:

- No real patient information
- No Protected Health Information (PHI)
- No confidential healthcare records
- No personally identifiable patient information

This application must not be used as a replacement for qualified healthcare professionals or validated clinical systems.

---

# 📌 Table of Contents

1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Objectives](#-objectives)
4. [Key Features](#-key-features)
5. [Project Status](#-project-status)
6. [System Architecture](#-system-architecture)
7. [Architecture Components](#-architecture-components)
8. [Technology Stack](#-technology-stack)
9. [Project Structure](#-project-structure)
10. [Healthcare Knowledge Base](#-healthcare-knowledge-base)
11. [RAG Pipeline](#-rag-pipeline)
12. [Document Ingestion Pipeline](#-document-ingestion-pipeline)
13. [Retrieval Pipeline](#-retrieval-pipeline)
14. [Evidence-Gating Strategy](#-evidence-gating-strategy)
15. [Grounded Answer Generation](#-grounded-answer-generation)
16. [Prompt-Engineering Strategy](#-prompt-engineering-strategy)
17. [Hallucination-Reduction Strategy](#-hallucination-reduction-strategy)
18. [Agentic Tool Workflow](#-agentic-tool-workflow)
19. [Confidence Scoring](#-confidence-scoring)
20. [Source References](#-source-references)
21. [API Documentation](#-api-documentation)
22. [Local Installation](#-local-installation)
23. [Docker Deployment](#-docker-deployment)
24. [Using the Streamlit Interface](#-using-the-streamlit-interface)
25. [API Usage Examples](#-api-usage-examples)
26. [Testing](#-testing)
27. [Evaluation](#-evaluation)
28. [Validated Functional Scenarios](#-validated-functional-scenarios)
29. [Logging and Error Handling](#-logging-and-error-handling)
30. [Configuration](#-configuration)
31. [Security and Privacy](#-security-and-privacy)
32. [Design Decisions and Trade-offs](#-design-decisions-and-trade-offs)
33. [Performance Considerations](#-performance-considerations)
34. [Limitations](#-limitations)
35. [Future Improvements](#-future-improvements)
36. [Troubleshooting](#-troubleshooting)
37. [Validation Summary](#-validation-summary)
38. [Responsible Use](#-responsible-use)
39. [Conclusion](#-conclusion)

---

# 🔎 Project Overview

The **Healthcare AI Assistant** is a document-grounded question-answering application developed using Retrieval-Augmented Generation.

The assistant answers healthcare operational and policy-related questions using only an approved local knowledge base. It retrieves relevant evidence from ChromaDB and sends the retrieved context to a local Llama 3.2 3B model through Ollama.

Unlike a general-purpose chatbot, the system is designed to reduce unsupported generation by applying an evidence gate before invoking the LLM.

The complete system includes:

- Healthcare document ingestion
- Text normalization
- Overlapping document chunking
- Semantic embedding generation
- Persistent vector storage
- Semantic similarity retrieval
- Relevance-based evidence gating
- Local LLM generation
- Context-grounded answers
- Application-generated source references
- Unknown-answer fallback behavior
- Healthcare safety controls
- Deterministic intent routing
- Mock appointment scheduling tool
- Confidence scoring
- FastAPI backend
- Streamlit frontend
- Environment-based configuration
- Logging and error handling
- Automated tests
- Evaluation framework
- Docker and Docker Compose deployment

---

# 🎯 Problem Statement

Healthcare organizations maintain large collections of internal documents, including:

- Patient discharge instructions
- Appointment scheduling policies
- Insurance eligibility guidelines
- Privacy and information-handling policies
- Medication refill procedures
- Telehealth consultation guidelines

Finding accurate information across these documents can be time-consuming.

A general-purpose LLM may generate fluent answers, but it can also:

- Use unsupported external knowledge
- Generate information absent from organizational documents
- Hallucinate policy details
- Produce answers without traceable evidence
- Ignore organization-specific rules
- Provide unsafe or inappropriate medical guidance

This project addresses these limitations through Retrieval-Augmented Generation.

Instead of asking the LLM to answer directly, the application first searches an approved healthcare knowledge base. The LLM receives only relevant retrieved evidence and is instructed to generate an answer using that evidence.

If sufficient evidence is unavailable, the system returns:

```text
I could not find this information in the provided documents.
```

---

# 🎯 Objectives

The primary objectives of this project are to:

1. Ingest healthcare policy documents from a local directory.
2. Clean and divide documents into manageable overlapping chunks.
3. Generate semantic embeddings for document chunks.
4. Store embeddings and metadata in a persistent vector database.
5. Convert user questions into semantic embeddings.
6. Retrieve relevant evidence using vector similarity search.
7. Reject weak or insufficient evidence.
8. Generate grounded answers using a local LLM.
9. Return verifiable document references.
10. Avoid unsupported answers when information is unavailable.
11. Apply healthcare-specific safety controls.
12. Route appointment-related requests to a mock tool.
13. Expose functionality through a REST API.
14. Provide an interactive frontend.
15. Support local and Docker-based execution.
16. Include automated tests and a prototype evaluation framework.

---

# ✨ Key Features

## Retrieval-Augmented Generation

The system retrieves relevant healthcare policy evidence before generating an answer.

## Local LLM Execution

Llama 3.2 3B runs locally through Ollama.

Benefits include:

- No paid LLM API required
- Local inference
- Reduced external data transfer
- Better suitability for privacy-conscious prototypes
- Reproducible development environment

## Semantic Search

The application uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

to generate dense vector representations of healthcare documents and user questions.

## Persistent Vector Database

ChromaDB stores:

- Document embeddings
- Document names
- Chunk identifiers
- Text content
- Retrieval metadata

The vector store persists between application restarts.

## Evidence Gating

The LLM is not automatically called for every question.

Retrieved evidence must satisfy the configured relevance threshold before generation is allowed.

## Grounded Answers

The LLM receives:

- A healthcare safety prompt
- Retrieved document evidence
- The user question

It is instructed to answer only from the supplied context.

## Unknown-Answer Handling

When sufficient evidence is unavailable, the application returns:

```text
I could not find this information in the provided documents.
```

## Source References

Source references are generated from vector-store metadata rather than invented by the LLM.

## Agentic Appointment Workflow

Appointment-related requests are routed to a deterministic mock scheduling tool.

## Healthcare Safety Controls

The assistant avoids:

- Diagnosis
- Prescribing
- Dosage recommendations
- Individualized treatment advice
- Unsupported medical claims

## Interactive Streamlit Interface

The frontend displays:

- Generated answer
- Confidence level
- Selected route
- Response latency
- Supporting evidence
- Source document names
- Relevance scores

## REST API

FastAPI provides:

- Automatic request validation
- Interactive Swagger documentation
- Structured JSON responses
- Health monitoring
- Metrics
- Document ingestion
- Question-answering functionality

## Docker Deployment

The complete application runs using Docker Compose with:

- Ollama service
- FastAPI service
- Streamlit service
- Persistent model storage
- Persistent vector storage
- Internal service networking

---

# ✅ Project Status

| Component | Status |
|---|---|
| FastAPI backend | ✅ Validated |
| Healthcare document ingestion | ✅ Validated |
| Text normalization | ✅ Validated |
| Overlapping text chunking | ✅ Validated |
| MiniLM embedding generation | ✅ Validated |
| Persistent ChromaDB storage | ✅ Validated |
| Semantic document retrieval | ✅ Validated |
| Evidence relevance gating | ✅ Validated |
| Ollama integration | ✅ Validated |
| Llama 3.2 3B integration | ✅ Validated |
| Context-grounded generation | ✅ Validated |
| Source references | ✅ Validated |
| Unknown-answer fallback | ✅ Validated |
| Healthcare safety controls | ✅ Implemented |
| Appointment intent routing | ✅ Validated |
| Mock appointment tool | ✅ Validated |
| Confidence scoring | ✅ Validated |
| Response latency measurement | ✅ Validated |
| Streamlit frontend | ✅ Validated |
| Application logging | ✅ Implemented |
| Error handling | ✅ Implemented |
| Environment configuration | ✅ Validated |
| Automated tests | ✅ 4/4 passed |
| Evaluation framework | ✅ Validated |
| Docker image build | ✅ Validated |
| Docker Compose deployment | ✅ Validated |
| Docker service networking | ✅ Validated |
| Docker API health | ✅ Validated |

---

# 🏗 System Architecture

```text
                         OFFLINE INGESTION PIPELINE

                    Synthetic Healthcare Documents
                                  │
                                  ▼
                         Document Loader
                                  │
                                  ▼
                      Text Cleaning and Normalization
                                  │
                                  ▼
                    Recursive Overlapping Chunking
                                  │
                                  ▼
                all-MiniLM-L6-v2 Embedding Model
                                  │
                                  ▼
                  Persistent ChromaDB Vector Store


                    ONLINE QUESTION-ANSWERING PIPELINE

                              User Question
                                    │
                                    ▼
                            Streamlit Frontend
                                    │
                                    ▼
                         FastAPI POST /ask
                                    │
                                    ▼
                    Request Validation and Routing
                                    │
              ┌─────────────────────┼────────────────────┐
              │                     │                    │
              ▼                     ▼                    ▼
      Healthcare Safety      Appointment Intent       RAG Route
             Route                  Route                  │
              │                     │                     ▼
              │                     ▼             Question Embedding
              │          check_available_slots()          │
              │                     │                     ▼
              │                     │             ChromaDB Retrieval
              │                     │                     │
              │                     │                     ▼
              │                     │              Evidence Gating
              │                     │              ┌──────┴──────┐
              │                     │              │             │
              │                     │         Evidence Found   Missing
              │                     │              │             │
              │                     │              ▼             ▼
              │                     │         Ollama LLM      Safe Fallback
              │                     │              │
              │                     │              ▼
              │                     │      Grounded Generation
              │                     │              │
              └─────────────────────┴──────────────┘
                                    │
                                    ▼
                       Structured API Response
                                    │
                                    ▼
       Answer + Sources + Confidence + Route + Grounded + Latency
```

---

# 🧩 Architecture Components

## 1. Document Loader

Responsibilities:

- Reads healthcare documents from the configured data directory
- Supports local text-based knowledge sources
- Extracts document content
- Preserves document metadata
- Rejects empty or invalid documents

## 2. Text Chunking

Large documents are divided into smaller overlapping chunks.

Configured values:

```env
CHUNK_SIZE=800
CHUNK_OVERLAP=120
```

Chunk overlap preserves semantic continuity across chunk boundaries.

## 3. Embedding Service

Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Responsibilities:

- Converts document chunks into dense vectors
- Converts user questions into vectors
- Supports semantic comparison

## 4. ChromaDB Vector Store

Responsibilities:

- Stores embeddings
- Stores document metadata
- Performs similarity search
- Persists indexed knowledge locally

## 5. Evidence Gate

Responsibilities:

- Evaluates retrieved relevance scores
- Rejects weak evidence
- Prevents unnecessary LLM generation
- Triggers the unknown-answer fallback when evidence is insufficient

## 6. Ollama LLM Service

Model:

```text
llama3.2:3b
```

Responsibilities:

- Receives retrieved context
- Follows the grounding prompt
- Generates clear document-based answers
- Runs locally

## 7. Intent Router

Responsibilities:

- Detects appointment-related requests
- Routes document questions to RAG
- Routes appointment requests to the mock scheduling tool
- Supports healthcare safety behavior

## 8. FastAPI Backend

Responsibilities:

- Validates requests
- Exposes API endpoints
- Coordinates ingestion
- Executes RAG
- Executes tool routing
- Returns structured responses
- Provides health information and metrics

## 9. Streamlit Frontend

Responsibilities:

- Accepts user questions
- Sends requests to FastAPI
- Displays answers and metadata
- Displays source references
- Displays confidence and latency

---

# 🛠 Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Programming language | Python 3.11 | Application development |
| Backend framework | FastAPI | REST API development |
| API server | Uvicorn | ASGI application server |
| Local LLM runtime | Ollama | Local model management and inference |
| Generative model | Llama 3.2 3B | Grounded response generation |
| Embedding model | all-MiniLM-L6-v2 | Semantic embeddings |
| Vector database | ChromaDB | Persistent vector storage and retrieval |
| Text splitting | LangChain Text Splitters | Overlapping document chunks |
| Frontend | Streamlit | Interactive demonstration interface |
| Validation | Pydantic | Request and response validation |
| HTTP client | HTTPX | Service communication |
| Testing | Pytest | Automated unit tests |
| Configuration | Environment variables | Runtime configuration |
| Containerization | Docker | Application packaging |
| Multi-service deployment | Docker Compose | Container orchestration |
| Version control | Git | Source-code management |

---

# 📁 Project Structure

```text
healthcare-ai-assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── rag.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── document_loader.py
│   ├── llm.py
│   ├── agent.py
│   ├── tools.py
│   ├── prompts.py
│   ├── confidence.py
│   ├── schemas.py
│   ├── config.py
│   ├── exceptions.py
│   └── utils.py
│
├── data/
│   ├── appointment_policy.txt
│   ├── discharge_instructions.txt
│   ├── hipaa_privacy_guidelines.txt
│   ├── insurance_eligibility_faq.txt
│   ├── medication_refill_policy.txt
│   └── telehealth_guidelines.txt
│
├── evaluation/
│   ├── evaluate.py
│   ├── evaluation_dataset.json
│   ├── evaluation_results.json
│   └── README.md
│
├── frontend/
│   └── streamlit_app.py
│
├── logs/
│   └── healthcare_ai.log
│
├── scripts/
│   └── ingest_documents.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_confidence.py
│   └── test_documents.py
│
├── vector_store/
│   ├── chroma.sqlite3
│   └── vector-index files
│
├── .dockerignore
├── .env
├── .env.example
├── .gitignore
├── ARCHITECTURE.md
├── Big_README.md
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── LIMITATIONS.md
├── Makefile
├── pytest.ini
├── README.md
├── requirements.txt
└── VALIDATION_REPORT.md
```

---

# 📚 Healthcare Knowledge Base

The application uses six synthetic healthcare policy documents.

| Document | Purpose |
|---|---|
| `appointment_policy.txt` | Appointment requests, scheduling, cancellation, and attendance |
| `discharge_instructions.txt` | General discharge and follow-up guidance |
| `hipaa_privacy_guidelines.txt` | Privacy, records, and healthcare information handling |
| `insurance_eligibility_faq.txt` | Insurance eligibility and verification guidance |
| `medication_refill_policy.txt` | Refill requests, review, processing, and restrictions |
| `telehealth_guidelines.txt` | Telehealth eligibility, privacy, identification, and limitations |

Dataset characteristics:

| Attribute | Description |
|---|---|
| Data type | Unstructured text |
| Source | Project-created synthetic documents |
| Real patient data | No |
| PHI | No |
| PII | No patient PII |
| Clinical validation | No |
| Intended purpose | RAG engineering demonstration |
| Production healthcare use | Not permitted |

The knowledge base is intentionally small so that the complete RAG workflow can be inspected, tested, and evaluated.

---

# 🔄 RAG Pipeline

Retrieval-Augmented Generation combines information retrieval with generative AI.

The system follows this process:

```text
User Question
      │
      ▼
Question Validation
      │
      ▼
Intent Classification
      │
      ▼
Question Embedding
      │
      ▼
Semantic Vector Search
      │
      ▼
Relevant Document Chunks
      │
      ▼
Evidence Relevance Gate
      │
      ├──────── Insufficient Evidence
      │                    │
      │                    ▼
      │            Exact Safe Fallback
      │
      ▼
Context Construction
      │
      ▼
Grounding and Safety Prompt
      │
      ▼
Local Llama 3.2 Generation
      │
      ▼
Answer Validation
      │
      ▼
Application-Generated Sources
      │
      ▼
Structured API Response
```

---

# 📥 Document Ingestion Pipeline

The ingestion pipeline converts healthcare documents into searchable vector representations.

## Processing Stages

```text
Healthcare Documents
          │
          ▼
Read File Content
          │
          ▼
Normalize Text
          │
          ▼
Split into Overlapping Chunks
          │
          ▼
Generate MiniLM Embeddings
          │
          ▼
Attach Source Metadata
          │
          ▼
Store in Persistent ChromaDB
```

## Validated Ingestion Result

Request:

```http
POST /ingest
```

Request body:

```json
{
  "reset": false
}
```

Validated response:

```json
{
  "status": "success",
  "documents_processed": 6,
  "chunks_created": 9,
  "collection_name": "healthcare_knowledge",
  "message": "Healthcare documents were ingested successfully."
}
```

---

# 🔍 Retrieval Pipeline

For every RAG question:

1. The question is validated.
2. The embedding model converts the question into a dense vector.
3. ChromaDB compares the question vector with stored document vectors.
4. The most semantically relevant chunks are returned.
5. Similarity values are converted into application relevance scores.
6. Retrieved evidence is filtered using the configured minimum threshold.
7. Accepted evidence is passed to the LLM.
8. Rejected evidence triggers the fallback response.

Configured retrieval values:

```env
TOP_K=4
MIN_RELEVANCE_SCORE=0.45
```

---

# 🚧 Evidence-Gating Strategy

Evidence gating is a key hallucination-reduction mechanism.

The system does not assume that every retrieved chunk is useful.

Retrieved evidence must satisfy the configured relevance threshold:

```env
MIN_RELEVANCE_SCORE=0.45
```

If no sufficiently relevant evidence is available:

- The LLM is not trusted to answer from general knowledge.
- Unsupported generation is avoided.
- Source references are returned as an empty list.
- Confidence is marked as low.
- Grounded status is false.
- The application returns the exact fallback message.

```text
I could not find this information in the provided documents.
```

This behavior is especially important in healthcare-related systems because fluent but unsupported information may be misleading.

---

# 🧠 Grounded Answer Generation

When sufficient evidence is found:

1. Relevant document chunks are combined into a controlled context.
2. The system prompt defines grounding and healthcare safety rules.
3. The user question is included.
4. The prompt is sent to Llama 3.2 3B through Ollama.
5. The generated answer is processed.
6. Source references are attached separately from vector-store metadata.

The LLM is not responsible for generating trusted citations.

This separation reduces the possibility of fabricated source names.

---

# ✍️ Prompt-Engineering Strategy

The prompt is designed around five principles.

## 1. Context-Only Generation

The model must answer only from retrieved evidence.

## 2. Explicit Uncertainty Handling

The model must not guess when information is missing.

## 3. Healthcare Safety

The model must avoid:

- Diagnosis
- Prescribing
- Dosage recommendations
- Individualized treatment decisions
- Unsupported clinical guidance

## 4. Professional Communication

Responses should be:

- Clear
- Concise
- Neutral
- Professional
- Easy to understand

## 5. Citation Separation

The LLM should not invent source labels.

Verified source metadata is attached by application logic.

Conceptual prompt structure:

```text
SYSTEM ROLE

You are a healthcare policy information assistant.

GROUNDING RULE

Answer only from the supplied context.
Do not use unsupported outside information.

UNKNOWN INFORMATION RULE

If the context does not contain enough information, return:
"I could not find this information in the provided documents."

HEALTHCARE SAFETY RULE

Do not provide diagnosis, prescriptions, dosage recommendations,
individualized treatment advice, or emergency medical guidance.

SOURCE RULE

Do not invent document names or citations.
Verified sources are attached separately by the application.

STYLE RULE

Keep the answer clear, professional, and directly relevant.

RETRIEVED CONTEXT

{context}

USER QUESTION

{question}
```

---

# 🛡 Hallucination-Reduction Strategy

The project uses defense in depth rather than relying on one prompt.

| Layer | Control |
|---|---|
| Knowledge source | Approved synthetic local documents |
| Retrieval | Semantic search |
| Retrieval filtering | Minimum relevance threshold |
| Generation control | Evidence gate |
| Prompt control | Context-only instruction |
| Missing information | Exact fallback response |
| Citation control | Application-generated source metadata |
| Safety control | Healthcare-specific restrictions |
| Routing control | Deterministic appointment workflow |
| Data control | No real patient data or PHI |

These controls reduce unsupported generation but do not guarantee complete factual correctness.

---

# 🤖 Agentic Tool Workflow

The application includes a basic tool-based workflow.

Appointment-related questions are routed to:

```python
check_available_slots(department, requested_date)
```

Example question:

```text
Can I book a cardiology appointment for Monday?
```

Example response:

```text
I checked the simulated appointment schedule. Cardiology has mock
availability for Monday at 10:00 AM, 1:30 PM, and 4:00 PM.

These are demonstration slots only and are not real bookings.
```

Expected metadata:

```json
{
  "route": "appointment_tool",
  "confidence": "high",
  "grounded": true,
  "tool": {
    "name": "check_available_slots",
    "simulated": true
  }
}
```

The tool is:

- Deterministic
- Local
- Transparent
- Easy to test
- Clearly marked as simulated

It does not:

- Access a hospital system
- Reserve appointments
- Store patient details
- Connect to a real scheduling API

---

# 📊 Confidence Scoring

Confidence is an application-level heuristic.

It is not:

- A clinical confidence score
- A probability that the answer is medically correct
- A calibrated uncertainty estimate

General interpretation:

| Confidence | Meaning |
|---|---|
| High | Deterministic tool result or strong supporting evidence |
| Medium | Relevant document evidence was retrieved |
| Low | Evidence was insufficient or unavailable |

Confidence values should be interpreted only as prototype pipeline indicators.

---

# 📑 Source References

Sources are derived from ChromaDB metadata.

Each source may contain:

```json
{
  "document": "medication_refill_policy.txt",
  "chunk_id": "medication_refill_policy_0",
  "relevance_score": 0.79,
  "excerpt": "Relevant evidence text..."
}
```

The application may display:

- Document name
- Chunk identifier
- Evidence excerpt
- Relevance score

The LLM does not generate trusted source names.

---

# 🌐 API Documentation

FastAPI provides automatic interactive documentation.

After starting the application:

```text
Swagger UI:
http://localhost:8000/docs
```

```text
OpenAPI specification:
http://localhost:8000/openapi.json
```

## Available Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | Application information |
| `GET` | `/health` | Service health and dependency status |
| `POST` | `/ingest` | Process and index healthcare documents |
| `POST` | `/ask` | Ask a healthcare policy question |
| `GET` | `/metrics` | View basic application metrics |

---

# 💻 Local Installation

## Prerequisites

Install:

- Python 3.11
- Git
- Ollama

Recommended resources:

- At least 8 GB RAM
- Approximately 4–6 GB available storage
- Stable internet connection for the initial model download

CPU inference is supported but may be slower than GPU inference.

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd healthcare-ai-assistant
```

## 2. Create a Virtual Environment

### Windows PowerShell

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
py -3.11 -m venv venv
venv\Scripts\activate
```

### Linux or macOS

```bash
python3.11 -m venv venv
source venv/bin/activate
```

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Create the Environment File

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

### Windows Command Prompt

```cmd
copy .env.example .env
```

### Linux or macOS

```bash
cp .env.example .env
```

## 6. Install the Local LLM

```bash
ollama pull llama3.2:3b
```

Verify:

```bash
ollama list
```

Expected model:

```text
NAME           SIZE
llama3.2:3b    approximately 2.0 GB
```

## 7. Start Ollama

If Ollama is not already running:

```bash
ollama serve
```

## 8. Start FastAPI

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

## 9. Ingest Documents

Using the script:

```bash
python scripts/ingest_documents.py
```

Or use Swagger:

```text
POST /ingest
```

Request:

```json
{
  "reset": false
}
```

## 10. Start Streamlit

Open another terminal and run:

```bash
streamlit run frontend/streamlit_app.py
```

Frontend:

```text
http://localhost:8501
```

---

# 🐳 Docker Deployment

The complete Docker deployment has been successfully validated.

Docker Compose runs three services:

| Service | Internal Address | Host Port | Purpose |
|---|---|---:|---|
| Ollama | `http://ollama:11434` | `11434` | Local LLM inference |
| FastAPI | `http://api:8000` | `8000` | Backend API |
| Streamlit | `http://streamlit:8501` | `8501` | Interactive frontend |

## Docker Architecture

```text
Browser
   │
   ▼
localhost:8501
   │
   ▼
Streamlit Container
   │
   │ API_BASE_URL=http://api:8000
   ▼
FastAPI Container
   │
   │ OLLAMA_BASE_URL=http://ollama:11434
   ▼
Ollama Container
   │
   ▼
Llama 3.2 3B


Host data/
    │
    ▼
/app/data

Host vector_store/
    │
    ▼
/app/vector_store

Host logs/
    │
    ▼
/app/logs

Docker Volume
ollama_data
    │
    ▼
/root/.ollama
```

## 1. Open the Project Directory

PowerShell:

```powershell
cd "C:\Users\Dipika\Desktop\MEDS\healthcare-ai-assistant"
```

> `cd /d` is a Command Prompt command. Do not use `cd /d` in PowerShell.

## 2. Validate Docker Compose

```powershell
docker compose config
```

The command should print the normalized Compose configuration without errors.

## 3. Stop Previous Containers

```powershell
docker compose down
```

## 4. Build the Images

First clean build:

```powershell
docker compose build --no-cache
```

The first build may take several minutes because Python, PyTorch, Transformers, Sentence Transformers, ChromaDB, and other dependencies must be downloaded.

Validated result:

```text
Image healthcare-ai-assistant-api Built
Image healthcare-ai-assistant-streamlit Built
```

Future builds can use:

```powershell
docker compose build
```

## 5. Start All Services

```powershell
docker compose up -d
```

Validated result:

```text
Network healthcare-ai-assistant_default Created
Container healthcare-ai-assistant-ollama-1 Started
Container healthcare-ai-assistant-api-1 Started
Container healthcare-ai-assistant-streamlit-1 Started
```

## 6. Verify Container Status

```powershell
docker compose ps
```

Expected:

```text
healthcare-ai-assistant-api-1         Up
healthcare-ai-assistant-ollama-1      Up
healthcare-ai-assistant-streamlit-1   Up
```

## 7. Download Llama Inside the Ollama Container

```powershell
docker exec -it healthcare-ai-assistant-ollama-1 ollama pull llama3.2:3b
```

Verify:

```powershell
docker exec -it healthcare-ai-assistant-ollama-1 ollama list
```

Validated result:

```text
NAME           ID              SIZE
llama3.2:3b    a80c4f17acd5    2.0 GB
```

The model is stored in the persistent `ollama_data` Docker volume.

## 8. Restart API and Streamlit

```powershell
docker compose restart api streamlit
```

## 9. Verify API Health

```powershell
curl.exe http://localhost:8000/health
```

Validated response:

```json
{
  "status": "healthy",
  "api": "available",
  "vector_store": "available",
  "llm": "available",
  "embedding_model": "available"
}
```

## 10. Ingest Documents

Open:

```text
http://localhost:8000/docs
```

Select:

```text
POST /ingest
```

Use:

```json
{
  "reset": false
}
```

Validated response:

```json
{
  "status": "success",
  "documents_processed": 6,
  "chunks_created": 9,
  "collection_name": "healthcare_knowledge",
  "message": "Healthcare documents were ingested successfully."
}
```

## 11. Open the Application

Streamlit:

```text
http://localhost:8501
```

FastAPI:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

Ollama:

```text
http://localhost:11434
```

## 12. Stop the Application

```powershell
docker compose down
```

The persistent Ollama model volume remains available.

To remove containers and the model volume:

```powershell
docker compose down -v
```

> Warning: `-v` removes the Ollama model volume. The model may need to be downloaded again.

---

# 🖥 Using the Streamlit Interface

Open:

```text
http://localhost:8501
```

The interface displays:

- Project title
- Healthcare safety disclaimer
- Example questions
- Question input
- Generated answer
- Confidence level
- Selected route
- Response latency
- Retrieval status
- Relevant source documents
- Relevance scores

Recommended test questions:

```text
What is the medication refill policy?
```

```text
Can a patient request a medication refill through telehealth?
```

```text
What identification is required during a telehealth visit?
```

```text
Can I book a cardiology appointment for Monday?
```

```text
What is the recommended treatment for pneumonia?
```

---

# 📡 API Usage Examples

## Health Check

Request:

```bash
curl http://localhost:8000/health
```

Example response:

```json
{
  "status": "healthy",
  "api": "available",
  "vector_store": "available",
  "llm": "available",
  "embedding_model": "available"
}
```

## Ingest Documents

Request:

```bash
curl -X POST "http://localhost:8000/ingest" \
-H "Content-Type: application/json" \
-d "{\"reset\":false}"
```

Example response:

```json
{
  "status": "success",
  "documents_processed": 6,
  "chunks_created": 9,
  "collection_name": "healthcare_knowledge"
}
```

## Ask a RAG Question

Request:

```bash
curl -X POST "http://localhost:8000/ask" \
-H "Content-Type: application/json" \
-d "{\"question\":\"What is the medication refill policy?\"}"
```

Example response:

```json
{
  "answer": "Refill requests for previously prescribed maintenance medicines may be submitted through the patient portal or the prescribing office. Patients should allow 48–72 business hours for routine processing.",
  "sources": [
    {
      "document": "medication_refill_policy.txt",
      "relevance_score": 0.79
    }
  ],
  "confidence": "medium",
  "route": "rag",
  "grounded": true
}
```

## Ask an Appointment Question

Request:

```bash
curl -X POST "http://localhost:8000/ask" \
-H "Content-Type: application/json" \
-d "{\"question\":\"Can I book a cardiology appointment for Monday?\"}"
```

Expected behavior:

```json
{
  "route": "appointment_tool",
  "confidence": "high",
  "grounded": true
}
```

## Ask an Unsupported Question

Request:

```bash
curl -X POST "http://localhost:8000/ask" \
-H "Content-Type: application/json" \
-d "{\"question\":\"What is the recommended treatment for pneumonia?\"}"
```

Expected answer:

```text
I could not find this information in the provided documents.
```

Expected metadata:

```json
{
  "sources": [],
  "confidence": "low",
  "route": "rag",
  "grounded": false
}
```

---

# 🧪 Testing

The project includes automated unit tests.

Validated areas:

- Intent routing
- Mock appointment tool
- Confidence scoring
- Document loading
- Document chunking

## Run Tests Locally

```bash
pytest -v
```

## Run Tests in Docker

```powershell
docker compose exec api pytest -v
```

Validated result:

```text
tests/test_agent.py::test_routes PASSED
tests/test_agent.py::test_mock_tool PASSED
tests/test_confidence.py::test_confidence_levels PASSED
tests/test_documents.py::test_documents_load_and_chunk PASSED

4 passed in 1.97s
```

Final test result:

```text
4 passed
```

---

# 📈 Evaluation

The project includes:

```text
evaluation/
├── evaluate.py
├── evaluation_dataset.json
├── evaluation_results.json
└── README.md
```

## Run Evaluation Locally

```bash
python evaluation/evaluate.py
```

## Run Evaluation in Docker

```powershell
docker compose exec api python evaluation/evaluate.py
```

Validated result:

```text
Route accuracy: 1.0
Citation match: 1.0
Errors: 0
```

Interpretation:

| Metric | Result | Meaning |
|---|---:|---|
| Route accuracy | 1.0 | All included evaluation questions used the expected route |
| Citation match | 1.0 | Expected source documents matched on the included evaluation set |
| Runtime errors | 0 | No evaluation requests failed |

These values apply only to the included small synthetic prototype dataset.

They do not represent:

- Clinical accuracy
- Medical correctness
- Production reliability
- Performance on unseen healthcare data
- Regulatory validation

---

# ✅ Validated Functional Scenarios

## Scenario 1: Grounded Medication Policy Answer

Question:

```text
What is the medication refill policy?
```

Observed behavior:

```text
Confidence: Medium
Route: rag
Relevant evidence: Retrieved
```

Relevant documents:

```text
medication_refill_policy.txt
telehealth_guidelines.txt
```

Result:

- Relevant evidence retrieved
- Local LLM generated the response
- Source references displayed
- Answer remained grounded in the policy documents

## Scenario 2: Telehealth Refill Question

Question:

```text
Can a patient request a medication refill through telehealth?
```

Observed behavior:

```text
Route: rag
Grounded: true
Confidence: medium
```

Relevant documents:

```text
telehealth_guidelines.txt
medication_refill_policy.txt
```

## Scenario 3: Unknown Medical Information

Question:

```text
What is the recommended treatment for pneumonia?
```

Response:

```text
I could not find this information in the provided documents.
```

Observed behavior:

```text
Confidence: Low
Route: rag
Grounded: false
Sources: []
```

The evidence gate prevented unsupported medical generation.

## Scenario 4: Appointment Tool

Question:

```text
Can I book a cardiology appointment for Monday?
```

Response:

```text
I checked the simulated appointment schedule. Cardiology has mock
availability for Monday at 10:00 AM, 1:30 PM, and 4:00 PM.

These are demonstration slots only and are not real bookings.
```

Observed behavior:

```text
Confidence: High
Route: appointment_tool
Latency: approximately 0 ms
```

---

# 📝 Logging and Error Handling

The application records important events such as:

- Application startup
- Document ingestion
- Number of documents processed
- Number of chunks generated
- Embedding initialization
- Vector-store initialization
- Retrieval execution
- LLM requests
- Routing decisions
- Tool execution
- Errors and exceptions

Configured log file:

```env
LOG_FILE=logs/healthcare_ai.log
```

Configured log level:

```env
LOG_LEVEL=INFO
```

Error handling covers:

- Missing documents
- Empty documents
- Invalid requests
- Unavailable vector store
- Unavailable embedding model
- Unavailable Ollama service
- Missing Ollama model
- LLM timeout
- Retrieval failures
- Tool-routing failures

---

# ⚙️ Configuration

Configuration is managed using environment variables.

Example:

```env
APP_NAME=Healthcare AI Assistant
APP_VERSION=1.0.0

DATA_DIR=data
VECTOR_STORE_DIR=vector_store
CHROMA_COLLECTION=healthcare_knowledge

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
LLM_TEMPERATURE=0.1
LLM_TIMEOUT_SECONDS=120

CHUNK_SIZE=800
CHUNK_OVERLAP=120

TOP_K=4
MIN_RELEVANCE_SCORE=0.45

MAX_QUESTION_LENGTH=2000

LOG_LEVEL=INFO
LOG_FILE=logs/healthcare_ai.log

API_BASE_URL=http://localhost:8000
```

Docker overrides internal service addresses:

```yaml
OLLAMA_BASE_URL: http://ollama:11434
```

```yaml
API_BASE_URL: http://api:8000
```

This is required because Docker containers communicate using Compose service names rather than host `localhost`.

---

# 🔐 Security and Privacy

Current safeguards:

- No real patient data
- No PHI
- No patient records
- No hardcoded API secrets
- Local LLM execution
- Environment-based configuration
- Document-grounded generation
- Evidence threshold
- Unknown-answer fallback
- Healthcare safety prompt
- Simulated appointment data
- Application-generated source metadata

For production use, additional controls would be required:

- Authentication
- Authorization
- Role-based access control
- Encryption in transit
- Encryption at rest
- Secret management
- Audit logging
- Tenant isolation
- Document-level permissions
- Rate limiting
- Prompt-injection defenses
- Data-retention controls
- Security testing
- Clinical governance
- Legal and regulatory review

---

# ⚖️ Design Decisions and Trade-offs

| Component | Selection | Reason | Trade-off |
|---|---|---|---|
| LLM | Llama 3.2 3B | Local, lightweight, privacy-conscious | Lower reasoning capability than larger models |
| Runtime | Ollama | Simple local model management | Requires local resources and model download |
| Embeddings | all-MiniLM-L6-v2 | Lightweight and effective | Less domain-specific than biomedical embeddings |
| Vector database | ChromaDB | Simple local persistence | Not designed here for enterprise-scale distribution |
| Backend | FastAPI | Validation and automatic API documentation | Requires separate frontend |
| Frontend | Streamlit | Rapid interactive development | Limited customization for large production applications |
| Router | Deterministic custom logic | Transparent and testable | Less flexible than advanced agent frameworks |
| Retrieval | Dense semantic retrieval | Understands semantic similarity | May miss exact keyword relationships |
| Confidence | Heuristic | Simple and interpretable | Not statistically calibrated |
| Dataset | Synthetic text | Safe and reproducible | Limited real-world complexity |

---

# ⚡ Performance Considerations

Observed behavior:

- Appointment-tool responses are nearly immediate.
- Unknown-answer responses can be fast because LLM generation may be skipped.
- Grounded RAG responses require retrieval and local model generation.
- CPU-based Llama inference can take several seconds or longer.
- Initial model loading may increase the first-response latency.

Performance depends on:

- CPU
- Available RAM
- GPU availability
- Model size
- Prompt size
- Retrieved context size
- Number of chunks
- Docker resource allocation

Potential optimizations:

- Use GPU acceleration
- Keep the model loaded
- Reduce unnecessary context
- Add response caching
- Use a smaller model for low-resource systems
- Add reranking before generation
- Separate API and frontend dependency images
- Add asynchronous request processing

---

# ⚠️ Limitations

Current limitations include:

- Small synthetic healthcare knowledge base
- Only six source documents
- Nine chunks in the validated dataset
- No real clinical data
- No clinical validation
- No real appointment system
- No EHR integration
- No FHIR integration
- No insurance-provider integration
- No authentication
- No role-based access control
- No document-level permissions
- No production-grade audit system
- No calibrated confidence model
- Dense retrieval only
- No keyword retrieval
- No reranking model
- No multilingual support
- CPU inference may be slow
- Retrieval quality depends on document quality
- Retrieval quality depends on chunking settings
- Retrieval quality depends on the relevance threshold
- LLM output may still require review

---

# 🚀 Future Improvements

## Retrieval

- Add BM25 keyword search
- Add hybrid semantic and keyword retrieval
- Add cross-encoder reranking
- Add query expansion
- Add metadata filtering
- Add document-level permissions

## Models

- Evaluate biomedical embedding models
- Compare Llama, Mistral, Phi, and Gemma
- Add model fallback support
- Add GPU inference

## Evaluation

- Expand the evaluation dataset
- Add answer-groundedness metrics
- Add faithfulness evaluation
- Add retrieval recall
- Add retrieval precision
- Add answer-relevance evaluation
- Add regression testing

## Healthcare Integration

- Add synthetic FHIR resources
- Add mock EHR workflows
- Add terminology normalization
- Add policy-version tracking

## Security

- Add authentication
- Add role-based access control
- Add audit logs
- Add rate limiting
- Add prompt-injection detection
- Add secret management
- Add encrypted storage

## Deployment

- Add CI/CD
- Add Docker image optimization
- Add production reverse proxy
- Add Kubernetes manifests
- Add structured observability
- Add centralized logging
- Add distributed tracing

## User Experience

- Add conversation history
- Add source preview
- Add document upload
- Add administrator dashboard
- Add user feedback
- Add exportable reports

---

# 🛠 Troubleshooting

## Docker Compose Error

Error:

```text
services.build must be a mapping
```

Cause:

Incorrect YAML indentation or service placement.

Validate:

```powershell
docker compose config
```

## Ollama Model Is Missing

Check:

```powershell
docker exec -it healthcare-ai-assistant-ollama-1 ollama list
```

If empty:

```powershell
docker exec -it healthcare-ai-assistant-ollama-1 ollama pull llama3.2:3b
```

Restart:

```powershell
docker compose restart api streamlit
```

## Local LLM Service Is Unavailable

Verify:

```powershell
curl.exe http://localhost:8000/health
```

Expected:

```json
{
  "llm": "available"
}
```

Check Ollama logs:

```powershell
docker compose logs ollama
```

## API Container Stops

Inspect:

```powershell
docker compose logs api
```

Run:

```powershell
docker compose ps
```

## Streamlit Cannot Reach FastAPI

Inside Docker, use:

```yaml
API_BASE_URL: http://api:8000
```

Do not use:

```yaml
API_BASE_URL: http://localhost:8000
```

because `localhost` inside the Streamlit container refers to the Streamlit container itself.

## FastAPI Cannot Reach Ollama

Inside Docker, use:

```yaml
OLLAMA_BASE_URL: http://ollama:11434
```

Do not use:

```yaml
OLLAMA_BASE_URL: http://localhost:11434
```

inside the API container.

## No Relevant Information Is Found

Run ingestion:

```text
POST /ingest
```

Use:

```json
{
  "reset": false
}
```

Check:

```powershell
Get-ChildItem .\data -Recurse
```

Check:

```powershell
Get-ChildItem .\vector_store -Recurse
```

## Slow First Response

Possible reasons:

- Llama model loading
- CPU-only inference
- Docker resource limits
- Initial embedding-model loading

The first response may be slower than later responses.

---

# 🏁 Validation Summary

## Environment

| Capability | Result |
|---|---|
| Python 3.11 | PASS |
| Required dependencies | PASS |
| FastAPI | PASS |
| Streamlit | PASS |
| ChromaDB | PASS |
| Sentence Transformers | PASS |
| Ollama | PASS |
| Llama 3.2 3B | PASS |

## RAG

| Capability | Result |
|---|---|
| Document loading | PASS |
| Text normalization | PASS |
| Chunk generation | PASS |
| Embedding generation | PASS |
| Persistent vector storage | PASS |
| Semantic retrieval | PASS |
| Evidence gating | PASS |
| Context-grounded generation | PASS |
| Source references | PASS |
| Unknown-answer handling | PASS |

## Agentic Workflow

| Capability | Result |
|---|---|
| Intent routing | PASS |
| Appointment route | PASS |
| Mock appointment tool | PASS |
| Simulated-result disclosure | PASS |

## Application

| Capability | Result |
|---|---|
| FastAPI backend | PASS |
| API validation | PASS |
| Swagger documentation | PASS |
| Streamlit frontend | PASS |
| Logging | PASS |
| Error handling | PASS |
| Configuration | PASS |

## Docker

| Capability | Result |
|---|---|
| Dockerfile | PASS |
| Docker image build | PASS |
| Docker Compose configuration | PASS |
| Docker network | PASS |
| Ollama container | PASS |
| Llama model in Docker | PASS |
| FastAPI container | PASS |
| Streamlit container | PASS |
| Container communication | PASS |
| API health endpoint | PASS |
| Docker document ingestion | PASS |
| Docker RAG workflow | PASS |
| Docker appointment workflow | PASS |

## Testing and Evaluation

| Capability | Result |
|---|---|
| Automated tests | 4/4 PASSED |
| Route accuracy | 1.0 |
| Citation match | 1.0 |
| Evaluation runtime errors | 0 |

---

# 🧭 Responsible Use

This application is intended only for:

- AI engineering demonstrations
- RAG experimentation
- Local LLM experimentation
- Semantic retrieval demonstrations
- Healthcare-policy document question answering
- Educational and technical evaluation

It must not be used as:

- A diagnostic system
- A treatment recommendation system
- A medication prescribing system
- A dosage recommendation system
- A clinical decision-support system
- An emergency response system
- A replacement for healthcare professionals

---

# 🏆 Conclusion

The Healthcare AI Assistant demonstrates a complete end-to-end healthcare-focused Retrieval-Augmented Generation workflow using local generative AI.

The validated implementation includes:

- Synthetic healthcare document ingestion
- Text normalization
- Overlapping document chunking
- MiniLM semantic embeddings
- Persistent ChromaDB vector storage
- Semantic evidence retrieval
- Relevance-based evidence gating
- Local Llama 3.2 3B inference through Ollama
- Context-grounded answer generation
- Application-generated source references
- Unknown-answer handling
- Healthcare safety controls
- Deterministic intent routing
- Mock appointment availability tool
- Confidence scoring
- FastAPI REST API
- Swagger documentation
- Streamlit frontend
- Environment-based configuration
- Application logging
- Error handling
- Automated testing
- Prototype evaluation
- Docker image creation
- Docker Compose orchestration
- Persistent Ollama model storage
- Container-to-container networking
- End-to-end Docker validation

All three Docker services—Ollama, FastAPI, and Streamlit—were successfully built, started, connected, and validated.

The Dockerized health endpoint confirmed that:

```text
API: available
Vector store: available
Local LLM: available
Embedding model: available
```

The automated test suite completed successfully:

```text
4 passed
```

The included prototype evaluation produced:

```text
Route accuracy: 1.0
Citation match: 1.0
Errors: 0
```

These results apply only to the included small synthetic healthcare-policy evaluation dataset. They must not be interpreted as clinical accuracy, medical validation, regulatory approval, or production readiness.

The application is a complete engineering prototype demonstrating practical knowledge of:

- Retrieval-Augmented Generation
- Local LLM integration
- Prompt engineering
- Semantic embeddings
- Vector databases
- Evidence-grounded generation
- Hallucination reduction
- Agentic tool routing
- REST API development
- Interactive AI application development
- Automated testing
- RAG evaluation
- Docker-based deployment

---

## Final Project Status

```text
RAG PIPELINE:          COMPLETE ✅
DOCUMENT INGESTION:    COMPLETE ✅
SEMANTIC RETRIEVAL:    COMPLETE ✅
LOCAL LLM:             COMPLETE ✅
GROUNDING CONTROLS:    COMPLETE ✅
SOURCE REFERENCES:     COMPLETE ✅
AGENTIC WORKFLOW:      COMPLETE ✅
FASTAPI BACKEND:       COMPLETE ✅
STREAMLIT FRONTEND:    COMPLETE ✅
AUTOMATED TESTING:     COMPLETE ✅
EVALUATION:            COMPLETE ✅
DOCKER DEPLOYMENT:     COMPLETE ✅
DOCUMENTATION:         COMPLETE ✅

PROJECT STATUS: READY FOR TECHNICAL REVIEW AND SUBMISSION ✅
```

---

## Author

**Mayur Narwade**

AI Engineer Candidate  
Generative AI • Machine Learning • Retrieval-Augmented Generation • Local LLMs

---

## License

This project is provided for educational, technical-assessment, demonstration, and portfolio purposes.

The included healthcare documents are synthetic and must not be interpreted as official clinical guidance.