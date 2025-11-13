import os
from datetime import datetime
from app.config import settings
from loguru import logger

class LocalStore:
    """
    Stores raw PR diffs and review results locally.
    Helps with debugging and offline analysis.
    """

    def __init__(self):
        self.base_dir = settings.LOCAL_STORE_DIR
        os.makedirs(self.base_dir, exist_ok=True)

    def _timestamp(self):
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def save_diff(self, diff_text: str) -> str:
        """Save raw diff text."""
        filename = f"diff_{self._timestamp()}.diff"
        path = os.path.join(self.base_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(diff_text)

        logger.info(f"Saved diff: {filename}")
        return path

    def save_review(self, review_output: dict) -> str:
        """Save final review JSON."""
        filename = f"review_{self._timestamp()}.json"
        path = os.path.join(self.base_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            import json
            json.dump(review_output, f, indent=2)

        logger.info(f"Saved review: {filename}")
        return path

local_store = LocalStore()
