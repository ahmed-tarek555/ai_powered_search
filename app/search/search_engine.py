from app.config import BASE_DIR
from app.models.embedder import get_embedding
import numpy as np
import json

with open(f"{BASE_DIR}/data/documents.json", "r") as f:
    documents = json.load(f)

for doc in documents:
    if "embedding" not in doc:
        doc["embedding"] = get_embedding(doc["description"]).tolist()

with open(f"{BASE_DIR}/data/documents.json", "w") as f:
    json.dump(documents, f)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))