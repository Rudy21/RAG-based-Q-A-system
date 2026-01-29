from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from app.utils import load_pdf, load_txt
from app.rag import ingest_document, retrieve_context
from app.schemas import QueryRequest
import os

app = FastAPI()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def health():
    return {"status": "RAG API running"}

@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    if file.filename.endswith(".pdf"):
        text = load_pdf(file_path)
    elif file.filename.endswith(".txt"):
        text = load_txt(file_path)
    else:
        return {"error": "Unsupported file format"}

    background_tasks.add_task(ingest_document, text)
    return {"message": "Document uploaded and processing started"}

@app.post("/query")
async def query_document(request: QueryRequest):
    contexts = retrieve_context(request.question)

    if not contexts:
        return {"answer": "No relevant information found in the document."}

    # Extractive answer (RAG without paid LLM)
    answer = " ".join(contexts[:2])

    return {
        "answer": answer,
        "note": "Answer generated using retrieval-only (cost-free) approach"
    }
