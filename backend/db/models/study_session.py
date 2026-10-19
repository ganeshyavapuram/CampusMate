from datetime import date

from sqlalchemy import CheckConstraint, Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from db.models.base import UUIDPrimaryKey


class StudySession(UUIDPrimaryKey, Base):
    __tablename__ = "study_sessions"
    __table_args__ = (
        CheckConstraint("duration_minutes > 0", name="duration"),
        CheckConstraint("status IN ('planned', 'completed', 'missed')", name="status"),
    )

    subject_id: Mapped[str] = mapped_column(String(36), ForeignKey("subjects.id", ondelete="CASCADE"), index=True)
    scheduled_date: Mapped[date] = mapped_column(Date)
    duration_minutes: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(10), default="planned", server_default="planned")
