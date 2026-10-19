from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from db.models.base import UUIDPrimaryKey


class GamificationRecord(UUIDPrimaryKey, Base):
    """One per student. Earned badges live in their own table, added in DB-04 (ADR-009)."""

    __tablename__ = "gamification_records"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    xp_total: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    current_streak: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
