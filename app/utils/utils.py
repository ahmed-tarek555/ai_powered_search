import numpy as np
from app.models.embedder import get_embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query: str, documents: list):
    query_embedding = get_embedding(query)

    results = []

    for doc in documents:
        sim = cosine_similarity(query_embedding, doc["embedding"])

        results.append({
            "name": doc["name"],
            "description": doc["description"],
            "similarity": float(sim)
        })

    results = sorted(results, key=lambda x: x["similarity"], reverse=True)

    return results[:10]