# 📄 RAG-based-on-PDF

**RAG-based-on-PDF** is a Retrieval-Augmented Generation (RAG) system that lets users ask questions and get document-grounded answers. In this version, the system is **built on a single scraped web page** from VS Code documentation.

It uses FAISS vector search, HuggingFace embeddings, and OpenRouter LLM via a Python backend, with a Streamlit frontend for interactive usage.

---

## 🚀 Key Features

* Ask natural language questions from web-scraped documents
* Efficient retrieval using FAISS embeddings
* Context-aware answers using OpenRouter LLM
* Streamlit frontend for interactive Q&A
* Fully Python-based and modular architecture

---

## 🧠 Technology Stack

* **Python:** FAISS, LangChain, HuggingFace Transformers, Streamlit
* **OpenRouter LLM** (Cloud-based)
* **Pickle** for embeddings storage

---

## 📂 Project Structure

```
RAG-based-on-PDF/
├─ .venv/                      # Python virtual environment
├─ scraped_docs/               # Scraped text files
│   └─ getting_started.txt      # VS Code Getting Started page
├─ .env                        # Environment variables
├─ app.py                       # (Optional backend for future extensions)
├─ App_streamlit.py            # Streamlit frontend for Q&A
├─ faiss_index.index           # FAISS index
├─ faiss_index.pkl             # FAISS metadata
├─ rag_engine.py               # RAG engine implementation
├─ web_scraping.py             # Script to scrape VS Code page
├─ README.md
├─ requirements.txt
└─ other project files
```

---

## ⚙️ Setup Instructions

### 1️⃣ Environment Setup

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

Add your OpenRouter API key to `.env`:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---

### 2️⃣ Run Streamlit Frontend

```bash
streamlit run App_streamlit.py
```

Open in browser: `http://localhost:8501`

---

## ▶️ Usage

1. Open the Streamlit app in your browser
2. Type a question in the input box
3. The system retrieves relevant content from the scraped VS Code page and generates an answer using OpenRouter LLM

Optional: You can show the **retrieved context** to see which text chunks were used.

---

## 🎥 Demo
Watch the demo video here:
👉 https://drive.google.com/drive/folders/1hQ1H5QJlVAmvm9sM1MyERI-o9GXKp5-z?usp=drive_link

## 🧩 RAG Workflow Overview

1. The VS Code page is scraped and saved as text (`getting_started.txt`)
2. The text is split into smaller chunks
3. Chunks are embedded using **HuggingFace embeddings** and stored in **FAISS**
4. User question is embedded
5. FAISS retrieves the most relevant chunks
6. Retrieved chunks are passed to **OpenRouter LLM**
7. LLM generates a factual, document-grounded answer

---

## 📌 Important Notes

* Answers are strictly based on the scraped page content
* If no relevant context is found, it returns **“Not found in document”**
* No additional internet or external APIs are required during inference (except for OpenRouter LLM calls)

---

## 👩‍💻 Author

**Iqra Khan**
AI Engineer | RAG Systems | LLM Applications | Streamlit

---

## 📄 License

For **educational and demonstration purposes** only.

---
