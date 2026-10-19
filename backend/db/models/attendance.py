import datetime as dt

from sqlalchemy import Boolean, Date, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from db.models.base import UUIDPrimaryKey


class Attendance(UUIDPrimaryKey, Base):
    __tablename__ = "attendance"
    __table_args__ = (UniqueConstraint("subject_id", "date", name="uq_attendance_subject_id_date"),)

    subject_id: Mapped[str] = mapped_column(String(36), ForeignKey("subjects.id", ondelete="CASCADE"), index=True)
    date: Mapped[dt.date] = mapped_column(Date)
    present: Mapped[bool] = mapped_column(Boolean)
