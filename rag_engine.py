import os
import pickle
import faiss
import numpy as np
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

# -----------------------
# Load environment variables
# -----------------------
load_dotenv()

# -----------------------
# Paths
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRAPED_FILE = os.path.join(BASE_DIR, "scraped_docs", "getting_started.txt")
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index.index")
FAISS_META_PATH = os.path.join(BASE_DIR, "faiss_index.pkl")

# -----------------------
# Load & Chunk Text
# -----------------------
def chunk_text(text, chunk_size=200, overlap=50):
    """
    Splits text into smaller overlapping chunks for better embeddings
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

with open(SCRAPED_FILE, "r", encoding="utf-8") as f:
    raw_text = f.read()

chunks = chunk_text(raw_text)

# -----------------------
# Embeddings
# -----------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectors = [embedding_model.embed_query(chunk) for chunk in chunks]
vectors = np.array(vectors).astype("float32")

# Normalize vectors for cosine similarity
faiss.normalize_L2(vectors)

# -----------------------
# FAISS Index (Inner Product = Cosine Similarity)
# -----------------------
index = faiss.IndexFlatIP(vectors.shape[1])
index.add(vectors)

# Save FAISS index
faiss.write_index(index, FAISS_INDEX_PATH)

# Save metadata
meta = {
    "docstore": {i: chunks[i] for i in range(len(chunks))},
    "mapping": {i: i for i in range(len(chunks))}
}

with open(FAISS_META_PATH, "wb") as f:
    pickle.dump(meta, f)

print("FAISS index created and saved!")

# -----------------------
# RAG Engine
# -----------------------
class RAGEngineW:
    def __init__(self):
        self.embedding_model = embedding_model
        self.llm = ChatOpenAI(
            model="meta-llama/llama-3.1-8b-instruct",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            temperature=0.2
        )
        self.index = faiss.read_index(FAISS_INDEX_PATH)
        with open(FAISS_META_PATH, "rb") as f:
            data = pickle.load(f)
        self.docstore = data["docstore"]
        self.mapping = data["mapping"]



    def ask(self, question: str, top_k: int = 3):
        # Get embedding (as list) and convert to NumPy
        query_vector = np.array(self.embedding_model.embed_query(question), dtype="float32")

        # Normalize for cosine similarity
        faiss.normalize_L2(query_vector.reshape(1, -1))

        distances, indices = self.index.search(query_vector.reshape(1, -1), top_k)
        context = "\n\n".join(
            self.docstore[self.mapping[i]] for i in indices[0] if i != -1
        )

        prompt = f"""
     You are a helpful assistant.

     Answer the question using ONLY the context below.
     If the answer is not present, say "Not found in document".

     Context:
     {context}

     Question:
     {question}
     """
        response = self.llm.invoke(prompt)
        return response.content


# -----------------------
# Test RAG
# -----------------------
rag = RAGEngineW()
question = "What is this documentation all about?"
answer = rag.ask(question)
print("Question:", question)
print("Answer:", answer)
