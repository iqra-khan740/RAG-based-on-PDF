# 📄 RAG based on PDF — Document Question Answering System

RAG based on PDF is a **Retrieval-Augmented Generation (RAG)** application that enables users to ask questions from PDF documents and receive **fact-based, document-grounded answers**.

The system combines **FAISS vector search**, **HuggingFace sentence embeddings**, and a **local Ollama LLM**, exposed via a **FastAPI backend** for real-world and production use cases.

---

## 🚀 Key Features

- Ask natural language questions from PDF files
- Multi-layer FAISS vector indexing for efficient retrieval
- Local LLM inference using Ollama (no paid APIs)
- FastAPI backend with REST endpoints
- Windows & Linux compatible file handling
- Scalable and modular architecture

---

## 🧠 Technology Stack

- **Python**
- **FastAPI**
- **FAISS**
- **LangChain**
- **HuggingFace Sentence Transformers**
- **Ollama (Gemma 3 – 4B)**
- **Pickle**

---

## 📂 Project Structure

```

RAG based on PDF/
│
├── faiss_layer1/                # Chunk-level embeddings
│   ├── index.faiss
│   └── index.pkl
│
├── faiss_layer2/                # Summary-level embeddings
│   ├── index.faiss
│   └── index.pkl
│
├── final_shams(full embeddings)/ # Source documents
    └── BOOK (VS Code Editor Documentation).pdf
    └──embeddings.ipynb          # PDF chunking & embedding pipeline
    └──requirements.txt

└──.gitignore                
└──app.py                         # FastAPI entry point
└──rag_engine.py
└──README.md
````

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment
```bash

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
````

---

### 2️⃣ Install Dependencies

```bash

pip install -r requirements.txt
```

---

### 3️⃣ Install & Run Ollama

using link: https://ollama.com/
and then run

```bash

ollama pull gemma3:4b
ollama serve
```

---

## ▶️ Run the Application

```bash

python -m uvicorn app:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔍 Example API Request

**POST** `/ask`

```json
{
  "question": "What is the main topic discussed in this document?",
  "top_k": 3
}
```

**Response**

```json
{
  "answer": "The document mainly discusses..."
}
```

---

## 🧩 RAG Workflow Overview

1. PDF is split into semantic chunks
2. Chunks are embedded and stored in FAISS (Layer 1)
3. Chunk summaries are embedded again (Layer 2)
4. User query is embedded
5. FAISS retrieves the most relevant contexts
6. Retrieved content is passed to the LLM
7. LLM generates a factual answer

---

## 📌 Important Notes

* The system answers strictly from the PDF content
* If no relevant context is found, it avoids hallucination
* No internet or external APIs are required during inference

---

## 👩‍💻 Author

**Iqra Khan**
AI Engineer | RAG Systems | LLM Applications | FastAPI

---

## 📄 License

This project is intended for educational and demonstration purposes.

