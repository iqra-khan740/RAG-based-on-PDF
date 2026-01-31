# streamlit_app.py
import streamlit as st
from rag_engine import RAGEngineW
import numpy as np

# -------------------------
# Load RAG Engine
# -------------------------
@st.cache_resource
def load_rag():
    return RAGEngineW()

rag = load_rag()

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="📄 RAG Q&A",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Custom CSS for styling
# -------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #FF4E50, #FC913A, #9D50BB);
    font-family: 'Segoe UI', sans-serif;
    color: white;
}
h1, h2 {
    font-weight: bold;
}
h1 {
    text-align: center;
    font-size: 42px;
    margin-bottom: 10px;
}
h2 {
    font-size: 24px;
}
.stButton>button {
    background: linear-gradient(to right, #FF4E50, #FC913A, #9D50BB);
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 10px 25px;
    border-radius: 10px;
    border: none;
    transition: transform 0.2s;
}
.stButton>button:hover {
    transform: scale(1.05);
}
.stTextInput>div>div>input {
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
}
.stSpinner>div {
    color: white;
}
.stCheckbox>div>label {
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Title & Description
# -------------------------
st.title("📄 RAG Document Q&A")
st.subheader("Ask questions and get answers directly from your documents!")

# -------------------------
# Sidebar Info (Scraping notice)
# -------------------------
with st.sidebar:
    st.header("ℹ️ Info")
    st.write("This RAG pipeline is built on a **single scraped page** from:")
    st.markdown("[Getting Started - VS Code Docs](https://code.visualstudio.com/docs/getstarted/getting-started)")

# -------------------------
# Question Input
# -------------------------
st.markdown("### ❓ Ask a Question")
question = st.text_input("Type your question here:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question!")
    else:
        with st.spinner("Fetching answer... 🧠"):
            # For single page, you can fix top_k = 2 or any number
            answer = rag.ask(question, top_k=3)
        st.markdown("### ✅ Answer")
        st.success(answer)

        # Optional: show retrieved context
        show_context = st.checkbox("Show retrieved context")
        if show_context:
            st.markdown("### 📚 Retrieved Context")
            query_vector = np.array(rag.embedding_model.embed_query(question), dtype="float32").reshape(1, -1)
            context = "\n\n".join(
                rag.docstore[rag.mapping[i]] for i in rag.index.search(query_vector, top_k=3)[1][0] if i != -1
            )
            st.info(context)
