import os
import faiss
import numpy as np
from app.vector_db.embeddings import EmbeddingGenerator
from app.config import settings
from loguru import logger

class StoreManager:
    """
    Handles FAISS index for similarity search.
    Used for advanced reasoning and reusable patterns.
    """

    def __init__(self):
        self.index_path = settings.FAISS_INDEX_PATH
        self.embedder = EmbeddingGenerator()

        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)

        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            logger.info("Loaded existing FAISS index")
        else:
            self.index = faiss.IndexFlatL2(self.embedder.dim)
            self._save()
            logger.info("Created new FAISS index")

    def _save(self):
        faiss.write_index(self.index, self.index_path)
        logger.info("FAISS index saved")

    def add_text(self, text: str):
        embedding = self.embedder.embed(text)
        self.index.add(np.array([embedding], dtype="float32"))
        self._save()
        logger.info("Added new embedding to FAISS index")

    def search(self, query: str, k: int = 5):
        vector = self.embedder.embed(query).reshape(1, -1)
        distances, indices = self.index.search(vector, k)
        return distances, indices

store_manager = StoreManager()
