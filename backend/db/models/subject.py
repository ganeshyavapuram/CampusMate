from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from db.models.base import UUIDPrimaryKey


class Subject(UUIDPrimaryKey, Base):
    __tablename__ = "subjects"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(100))
    is_weak_subject: Mapped[bool] = mapped_column(Boolean, default=False, server_default="0")
    exam_date: Mapped[date | None] = mapped_column(Date)
