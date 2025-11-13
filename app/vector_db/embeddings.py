from sentence_transformers import SentenceTransformer
import numpy as np
from app.config import settings
from loguru import logger

class EmbeddingGenerator:
    """
    Generates embeddings using local MiniLM model.
    This is used for FAISS vector storage.
    """

    def __init__(self):
        model_name = settings.EMBEDDING_MODEL
        logger.info(f"Loading embedding model: {model_name}")

        try:
            self.model = SentenceTransformer(model_name)
            self.dim = self.model.get_sentence_embedding_dimension()
            logger.info(f"Embedding model loaded. Dimension = {self.dim}")
        except Exception as e:
            logger.error(f"Failed to load embedding model: {e}")
            raise

    def embed(self, text: str) -> np.ndarray:
        """Return 1D numpy embedding vector."""
        if not text.strip():
            return np.zeros(self.dim)

        emb = self.model.encode(text, convert_to_numpy=True)
        return np.array(emb, dtype="float32")

