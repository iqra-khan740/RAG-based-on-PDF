from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_core import get_book_answer   # import your function from model_core.py

# =====================================
# FASTAPI APP SETUP
# =====================================
app = FastAPI(
    title="Book Brain RAG API",
    description="RAG-based LLM API for 'The Forty Rules of Love'",
    version="1.0"
)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local dev, use "*" or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Schema for the incoming query
class QueryRequest(BaseModel):
    query: str

# =====================================
# Root endpoint
# =====================================
@app.get("/")
def home():
    return {"message": "Welcome to Book Brain RAG API. Use POST /ask to get answers."}

# =====================================
# Ask endpoint
# =====================================
@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        query = request.query.strip()
        if not query:
            raise HTTPException(status_code=400, detail="Query cannot be empty.")
        
        # Call your model logic
        answer = get_book_answer(query)
        return {"query": query, "answer": answer}

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# =====================================
# Run the API
# =====================================
# Command to start: uvicorn main:app --reload
