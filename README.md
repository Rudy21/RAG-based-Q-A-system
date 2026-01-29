# RAG-Based Question Answering System

A lightweight **Retrieval-Augmented Question Answering (RAG)** system built using FastAPI.  
The system allows users to upload documents and ask questions, with answers retrieved strictly from the uploaded content.

This project focuses on demonstrating **core RAG concepts** such as document ingestion, chunking, embedding generation, similarity search, and retrieval-based answering—without relying on heavy frameworks or paid APIs.

---

## 🚀 Features
- Upload PDF and TXT documents
- Background document ingestion
- Semantic search using embeddings
- FAISS-based vector storage
- Query-based retrieval of relevant content
- Cost-free extractive answering approach
- Clean and modular FastAPI design

---

## 🧠 System Overview
The system follows a Retrieval-Augmented architecture:

1. Documents are uploaded through an API
2. Text is extracted, chunked, and embedded
3. Embeddings are stored in a FAISS vector store
4. User queries are embedded at runtime
5. Relevant document chunks are retrieved using similarity search
6. Retrieved content is returned as the answer

---

## 📂 Supported File Formats
- PDF (`.pdf`)
- Text (`.txt`)

---

## ✂️ Chunking Strategy
- **Chunk size:** 500 tokens  
- **Overlap:** 50 tokens  

This configuration balances semantic context preservation with retrieval accuracy. Overlap ensures continuity across chunk boundaries.

---

## 🔍 Retrieval Strategy
- SentenceTransformer embeddings are used for both documents and queries
- FAISS performs efficient similarity search on embeddings
- Top relevant chunks are retrieved for each query

---

## 💡 Answer Generation Approach
To avoid external API costs and ensure reproducibility, this project uses an **extractive retrieval-based approach**.

Instead of generating new text using a paid LLM:
- The system returns the most relevant document chunks directly
- This still demonstrates the complete RAG pipeline

The design can be easily extended to integrate any LLM if required.

---

## ⚠️ Observed Limitation
Very generic queries (e.g., *“Explain the document”*) may retrieve multiple overlapping chunks, leading to verbose answers. This is a known limitation of embedding-based retrieval systems.

---

## 📊 Metric Tracked
- **End-to-end query latency** to monitor system responsiveness and performance bottlenecks

---

## 🛠️ Tech Stack
- **Backend:** FastAPI
- **Embeddings:** SentenceTransformers
- **Vector Store:** FAISS
- **Validation:** Pydantic
- **Language:** Python

---

## ▶️ Getting Started

## 1. Install Dependencies
 **pip install -r requirements.txt**

## 2. Run the application
**uvicorn app.main:app --reload**

## 3. Access API documentation
**http://127.0.0.1:8000/docs**

## API endpoints
**POST/upload**
**POST/query**

## Design Highlights
**Background tasks prevent API blocking during ingestion**

**Lazy-loading of ML models avoids startup crashes**

**No default RAG templates or heavy orchestration frameworks used**

**Clean separation of ingestion and query pipelines**
