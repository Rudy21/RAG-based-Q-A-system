from app.vector_store import VectorStore

model = None
vector_store = VectorStore(dim=384)

def get_model():
    global model
    if model is None:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

def ingest_document(text: str):
    model = get_model()
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)
    vector_store.add(embeddings, chunks)

def retrieve_context(query: str, k=3):
    if len(vector_store.texts) == 0:
        return []
    model = get_model()
    query_embedding = model.encode(query)
    return vector_store.search(query_embedding, k)
