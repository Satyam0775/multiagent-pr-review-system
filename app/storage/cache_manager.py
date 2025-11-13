import os
import json
import hashlib
from loguru import logger
from app.config import settings


class CacheManager:
    """
    Simple file-based cache.
    Each diff is hashed using SHA256 and stored as JSON.
    """

    def __init__(self):
        self.cache_dir = settings.CACHE_DIR
        os.makedirs(self.cache_dir, exist_ok=True)

    def _hash(self, text: str) -> str:
        """Create SHA256 hash from input text."""
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def _path(self, diff_hash: str) -> str:
        """Return file path for a given hash."""
        return os.path.join(self.cache_dir, f"{diff_hash}.json")

    def exists(self, diff_text: str) -> bool:
        """Check if cache entry exists."""
        diff_hash = self._hash(diff_text)
        return os.path.exists(self._path(diff_hash))

    def load(self, diff_text: str):
        """Load cached json if exists."""
        diff_hash = self._hash(diff_text)
        path = self._path(diff_hash)

        try:
            with open(path, "r") as f:
                logger.info("Loaded cached PR review")
                return json.load(f)
        except Exception:
            return None

    def save(self, diff_text: str, review_output: dict):
        """Save review output."""
        diff_hash = self._hash(diff_text)
        path = self._path(diff_hash)

        with open(path, "w") as f:
            json.dump(review_output, f, indent=2)

        logger.info("Saved PR review to cache")


# THIS is the correct exported instance
cache_manager = CacheManager()
