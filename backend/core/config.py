"""App settings, read from environment variables and backend/.env (ADR-027)."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "CampusMate"
    database_url: str = "sqlite:///./campusmate.db"
    cors_origins: list[str] = ["http://localhost:4200"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
