import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "pr-review-agent"
    APP_ENV: str = "development"
    APP_HOST: str = "0.0.0.0"

    # GitHub Token (optional)
    GITHUB_TOKEN: str | None = None

    # Gemini LLM
    GEMINI_API_KEY: str | None = None
    GEMINI_MODEL: str = "gemini-2.0-flash"

    # Vector DB (optional, future use)
    VECTOR_DB: str = "faiss"
    FAISS_INDEX_PATH: str = "data/vector_index/index.faiss"

    # Storage
    CACHE_DIR: str = "app/storage/cache"
    LOCAL_STORE_DIR: str = "app/storage/files"

    class Config:
        env_file = ".env"


settings = Settings()
