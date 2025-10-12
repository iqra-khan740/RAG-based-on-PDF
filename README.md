# 🧠 Brain — A Narrative RAG-Based LLM on *The Forty Rules of Love*

**Brain** is a Retrieval-Augmented Generation (RAG) project designed to make a Large Language Model (LLM) truly understand and respond contextually to *The Forty Rules of Love* by Elif Shafak.  
The project explores how **Narrative RAG** improves comprehension and reasoning compared to **Simple RAG**, especially when dealing with complex literature involving **dual timelines and emotional context**.

---

## 🌟 Project Overview

The novel *The Forty Rules of Love* presents two parallel timelines:
- 📜 **13th Century:** The spiritual connection between Rumi and Shams.
- 💌 **Modern Era:** Ella’s personal transformation and discovery.

This dual structure makes the narrative rich but challenging for AI models to interpret through standard RAG.  
**Brain** tackles this by enhancing RAG with **narrative-aware embeddings, timeline tagging, and contextual chunking**, resulting in deeper, contextually grounded answers.

---

## ⚙️ How It Works

### 🔹 Phase 1: Simple RAG
In the initial version:
- Text was split into small, fixed-size chunks.
- Each chunk was converted into **embeddings** (vector representations capturing meaning).
- These vectors were stored in a **vector database**.
- During a query, the system retrieved the top similar chunks and used the LLM to generate answers.

**Limitations:**
- Mixed up timelines (13th-century vs. modern-day events)
- Shallow factual answers without emotional depth
- Weak understanding of story continuity

---

### 🔹 Phase 2: Narrative RAG
The **Narrative RAG** approach enhanced the model by adding structure and context-awareness.

**Key Improvements:**
1. 🧩 **Contextual Chunking:** Passages were grouped by emotion, speaker, and storyline.
2. 🕰️ **Timeline Awareness:** Each embedding was tagged (e.g., “13th century” or “modern era”).
3. 👥 **Character Linking:** Relationships and dialogues were connected across events.
4. 📖 **Narrative Retrieval:** Retrieval considered both similarity and story progression.

**Results:**
- The model could **differentiate between timelines**.
- Answers became **emotionally aware and coherent**.
- LLM explained **cause-effect relationships** more naturally.

---

## 🧠 What Are Embeddings?

**Embeddings** are numerical vector representations of text that capture semantic meaning.  
In this project, embeddings enable the LLM to:
- Understand **contextual similarity**
- Retrieve the **right part of the novel** during queries
- Preserve **narrative and emotional depth**

Better embeddings → Better context → Smarter answers.

---

## 🛠️ Tech Stack

- **Language:** Python 🐍  
- **Framework:** FastAPI ⚡  
- **LLM:**  local model (Gemma 3:4b)  
- **Vector Database:** FAISS  
- **Embeddings Model:** Sentence Transformers   
- **Frontend :** V0  (for demo)  

---

