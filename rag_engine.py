import pickle
import faiss
import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

import os

BASE_DIR = os.path.dirname(os.path.abspath(r"C:/Users/LS/RAG based on PDF/faiss_layer1"))

FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_layer2", "index.faiss")
FAISS_META_PATH  = os.path.join(BASE_DIR, "faiss_layer2", "index.pkl")


class RAGEngine:
    def __init__(self):
        # Load embedding model
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Load LLM
        self.llm = Ollama(model="gemma3:4b")

        # Load FAISS index
        self.index = faiss.read_index(FAISS_INDEX_PATH)

        with open(FAISS_META_PATH, "rb") as f:
            data = pickle.load(f)

        self.docstore = data["docstore"]
        self.mapping = data["mapping"]

    def ask(self, question: str, top_k: int = 3):
        query_vector = self.embedding_model.embed_query(question)

        distances, indices = self.index.search(
            np.array([query_vector]).astype("float32"),
            top_k
        )

        context = "\n\n".join(
            self.docstore[self.mapping[i]]
            for i in indices[0]
        )

        prompt = f"""
Answer the question using ONLY the context below.
If the answer is not present, say "Not found in document".

Context:
{context}

Question:
{question}
"""

        return self.llm.invoke(prompt)
