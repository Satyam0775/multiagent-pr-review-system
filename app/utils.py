from loguru import logger

def clean_json_output(text: str):
    """
    Attempts to clean malformed JSON responses from LLMs.
    """
    try:
        import json
        return json.loads(text)
    except:
        logger.warning("Failed to parse JSON output.")
        return []

def truncate_text(text: str, limit: int = 8000):
    """Ensures text does not exceed model limits."""
    return text[:limit]
