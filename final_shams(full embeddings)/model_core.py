import subprocess, time, socket, faiss, pickle, numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

def ensure_ollama_running():
    try:
        with socket.create_connection(("127.0.0.1", 11434), timeout=2):
            return
    except OSError:
        print("🚀 Starting Ollama server...")
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

faiss_index_layer1 = faiss.read_index("faiss_layer1/index.faiss")
docstore1, index_to_uuid1 = pickle.load(open("faiss_layer1/index.pkl", "rb"))

faiss_index_layer2 = faiss.read_index("faiss_layer2/index.faiss")
docstore2, index_to_uuid2 = pickle.load(open("faiss_layer2/index.pkl", "rb"))

def get_book_answer(query: str):
    ensure_ollama_running()
    query_vector = np.array([embedding_model.embed_query(query)], dtype="float32")

    D1, I1 = faiss_index_layer1.search(query_vector, k=3)
    D2, I2 = faiss_index_layer2.search(query_vector, k=3)

    context_parts = []
    for idx in I1[0]:
        try:
            uuid = index_to_uuid1[idx]
            doc = docstore1.search(uuid)
            text = doc.page_content if hasattr(doc, "page_content") else str(doc)
            context_parts.append(text)
        except Exception:
            pass
    for idx in I2[0]:
        try:
            uuid = index_to_uuid2[idx]
            doc = docstore2.search(uuid)
            text = doc.page_content if hasattr(doc, "page_content") else str(doc)
            context_parts.append(text)
        except Exception:
            pass

    combined_context = "\n\n".join(context_parts)
    llm = Ollama(model="gemma3:4b")

    prompt = f"""
    You are an expert literary assistant.
    Use the following context from *The Forty Rules of Love* to answer truthfully.

    Context: {combined_context}

    Question: {query}
    """

    try:
        response = llm.invoke(prompt)
        return response
    except Exception as e:
        print("LLM invoke error:", e)
        raise e


