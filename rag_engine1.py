import os
import pickle
import faiss
import numpy as np
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

# ------------------------------------------------------------------
# Load environment variables
# ------------------------------------------------------------------
load_dotenv()

# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(r"C:/Users/LS/RAG-based-on-PDF/faiss_layer1"))

FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_layer2", "index.faiss")
FAISS_META_PATH  = os.path.join(BASE_DIR, "faiss_layer2", "index.pkl")

# ------------------------------------------------------------------
# RAG Engine
# ------------------------------------------------------------------
class RAGEngine1:
    def __init__(self):
        # Embedding model
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # OpenRouter LLM (Cloud)
        self.llm = ChatOpenAI(
            model="meta-llama/llama-3.1-8b-instruct",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            temperature=0.2,
        )

        # Load FAISS index
        self.index = faiss.read_index(FAISS_INDEX_PATH)

        # Load metadata
        with open(FAISS_META_PATH, "rb") as f:
            data = pickle.load(f)

        self.docstore = data["docstore"]
        self.mapping = data["mapping"]

    # ------------------------------------------------------------------
    # Ask Question
    # ------------------------------------------------------------------
    def ask(self, question: str, top_k: int = 3):
        # Embed query
        query_vector = self.embedding_model.embed_query(question)

        # Search FAISS
        distances, indices = self.index.search(
            np.array([query_vector]).astype("float32"),
            top_k
        )

        # Build context
        context = "\n\n".join(
            self.docstore[self.mapping[i]]
            for i in indices[0]
            if i != -1
        )

        # Prompt
        prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the context below.
If the answer is not present, say "Not found in document".

Context:
{context}

Question:
{question}
"""

        # Call OpenRouter
        response = self.llm.invoke(prompt)
        return response.content
