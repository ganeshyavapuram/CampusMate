"""Main router: every feature's routes are included here under /api/v1 (ADR-025, ADR-030)."""
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}


# Feature routers are added below, one line each, for example:
# api_router.include_router(subjects_router)
