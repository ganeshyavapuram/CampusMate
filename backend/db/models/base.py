"""Shared column helpers for every table."""
import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


def new_id() -> str:
    return str(uuid.uuid4())


class UUIDPrimaryKey:
    """Application-generated UUID primary key, stored as text (ADR-007)."""

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
