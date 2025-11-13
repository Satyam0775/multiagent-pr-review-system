import os
import faiss
import numpy as np
from app.vector_db.embeddings import EmbeddingGenerator
from app.config import settings
from loguru import logger

class VectorStoreClient:
    def __init__(self):
        self.index_path = settings.FAISS_INDEX_PATH
        self.embedding_model = EmbeddingGenerator()
        self.index = None

        # Create folder if not exists
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)

        if os.path.exists(self.index_path):
            self._load_index()
        else:
            self._create_index()

    def _create_index(self):
        """Create an empty FAISS index."""
        self.index = faiss.IndexFlatL2(self.embedding_model.dim)
        self._save_index()
        logger.info("Created new FAISS index")

    def _load_index(self):
        """Load FAISS index if available."""
        self.index = faiss.read_index(self.index_path)
        logger.info("Loaded existing FAISS index")

    def _save_index(self):
        """Save FAISS index to disk."""
        faiss.write_index(self.index, self.index_path)

    def add_text(self, text: str):
        """Add text embedding to FAISS index."""
        embedding = self.embedding_model.embed(text)
        self.index.add(np.array([embedding], dtype="float32"))
        self._save_index()
        logger.info("Added new vector to FAISS index")

    def search(self, query: str, k: int = 3):
        """Search similar text."""
        embedding = self.embedding_model.embed(query).reshape(1, -1)
        distances, indices = self.index.search(embedding, k)
        return distances, indices

vector_store = VectorStoreClient()
