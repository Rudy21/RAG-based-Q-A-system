# Mandatory Explanations – RAG-Based Question Answering System

This document explains the key design decisions and observations made while implementing the Retrieval-Augmented Question Answering (RAG) system.

---

## 1. Chunk Size Selection

**Chosen chunk size:** 500 tokens  
**Overlap:** 50 tokens  

### Reason for this choice:
A chunk size of 500 tokens was selected to maintain a balance between **semantic completeness** and **retrieval precision**.

- Smaller chunks often lose context and reduce answer quality.
- Larger chunks reduce retrieval accuracy by mixing multiple topics.
- A 50-token overlap ensures continuity of information across chunk boundaries and prevents important details from being split incorrectly.

This configuration worked well for both PDF and TXT documents used during testing.

---

## 2. Retrieval Failure Case Observed

One retrieval failure case was observed when the user asked **very generic or broad questions**, such as:

> “Explain the document.”

In such cases, the similarity search retrieved multiple overlapping chunks containing repeated information, leading to verbose and less focused answers.

This behavior is a known limitation of embedding-based retrieval systems when the user query lacks specificity.

---

## 3. Metric Tracked

**Metric tracked:** End-to-end query latency

### Why this metric:
Latency was tracked to understand the responsiveness of the system and identify potential bottlenecks during:
- Embedding generation
- Similarity search using FAISS
- Query handling through the API

Tracking latency helped ensure the system remained responsive even after document ingestion and embedding operations.

---

## Additional Notes

- Heavy ML models were lazy-loaded to prevent server startup crashes.
- Document ingestion was handled asynchronously using background tasks.
- The system uses an extractive retrieval-based answering approach to avoid external API costs.
- No default RAG templates were used; the pipeline was implemented explicitly for clarity and control.

---

## Conclusion

The design decisions made in this project prioritize **stability, clarity, and cost-efficiency**, while still demonstrating a complete and functional RAG pipeline. The system meets all functional and technical requirements outlined in the task description.
