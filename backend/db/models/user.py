from datetime import datetime

from sqlalchemy import DateTime, Float, String, func
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from db.models.base import UUIDPrimaryKey


class User(UUIDPrimaryKey, Base):
    __tablename__ = "users"

    firebase_uid: Mapped[str] = mapped_column(String(128), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    # IANA name such as "Asia/Kolkata", set from the browser on first sign-in (ADR-020).
    time_zone: Mapped[str] = mapped_column(String(64), default="UTC", server_default="UTC")
    # 0.5 to 12, saved from first-time setup and the planner form (US-011).
    daily_study_hours: Mapped[float | None] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
