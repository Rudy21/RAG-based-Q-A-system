# RAG-Based Question Answering System

## Project Overview
This project implements a **Retrieval-Augmented Question Answering (RAG) system** using FastAPI.  
The system allows users to upload documents and ask questions, with answers generated strictly from the uploaded content.

The project focuses on demonstrating the **core RAG pipeline** rather than relying on paid or external Large Language Models.

---

## Objective
The objective of this project is to build an applied AI system that:
- Accepts document uploads
- Generates embeddings from document content
- Stores embeddings in a vector store
- Retrieves relevant information based on user queries
- Returns answers grounded in the uploaded documents

---

## System Workflow
1. User uploads a document (PDF or TXT)
2. Document ingestion runs in the background
3. Text is chunked and converted into embeddings
4. Embeddings are stored in a FAISS vector store
5. User submits a question
6. Relevant chunks are retrieved using similarity search
7. Retrieved content is returned as the answer

---

## Supported File Formats
- PDF (`.pdf`)
- Text (`.txt`)

---

## Chunking Strategy
- **Chunk size:** 500 tokens  
- **Overlap:** 50 tokens  

This chunk size preserves sufficient context while maintaining retrieval accuracy.  
Overlap ensures continuity of information across chunk boundaries.

---

## Retrieval Strategy
- SentenceTransformer embeddings are used for documents and queries
- FAISS performs similarity search on vector embeddings
- Top-k relevant chunks are retrieved for answering user queries

---

## Answer Generation Approach
To avoid external API costs and ensure reproducibility, this system uses a **retrieval-only (extractive) approach**.

Instead of generating new text using a paid LLM:
- The system returns the most relevant document chunks directly
- This still validates the complete RAG process

The design can be easily extended to integrate any LLM if required.

---

## Observed Retrieval Failure Case
When very generic questions such as *“Explain the document”* are asked, multiple overlapping chunks may be retrieved, leading to verbose responses.  
This is a known limitation of embedding-based retrieval for broad queries.

---

## Metric Tracked
- **End-to-end query latency** was monitored to evaluate system responsiveness and identify performance bottlenecks.

---

## Technology Stack
- FastAPI
- SentenceTransformers
- FAISS
- Pydantic
- Python

---

## API Endpoints

### Upload Document

## POST/upload

# Uploads a document and starts background ingestion.

### Query Document

## POST/query

# Accepts a question and returns relevant information from the uploaded documents.


## How to Run the Project

### 1. Install dependencies
# pip install -r requirements.txt

### 2. Run the application
# uvicorn app.main:app --reload

### 3. Open API documentation
# http://127.0.0.1:8000/docs