from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import your RAGEngine class
from rag_engine import RAGEngineW  # make sure rag_engine.py is in the same folder

# -----------------------
# FastAPI app
# -----------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Request model
# -----------------------
class QuestionPayload(BaseModel):
    question: str

# -----------------------
# Initialize RAG
# -----------------------
rag = RAGEngineW()

# -----------------------
# Endpoint
# -----------------------
@app.post("/ask")
async def ask_question(payload: QuestionPayload):
    question = payload.question

    # Call RAG engine
    answer = rag.ask(question)

    return {"answer": answer}
