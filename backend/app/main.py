"""Creates the FastAPI app: settings, CORS and the main router. No business logic here (ADR-030)."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router.api_router import api_router
from core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
