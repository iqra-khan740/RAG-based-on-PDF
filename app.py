from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import RAGEngine

app = FastAPI(title="API OF RAG(Documentation)")

# Load RAG once (important for speed)
rag = RAGEngine()

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

@app.get("/")
def health():
    return {"status": "RAG API running"}

@app.post("/ask")
def ask_rag(request: QueryRequest):
    answer = rag.ask(
        question=request.question,
        top_k=request.top_k
    )
    return {
        "question": request.question,
        "answer": answer
    }
