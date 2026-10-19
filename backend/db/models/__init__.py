"""Import every model here so Alembic sees all tables."""
from db.models.assignment import Assignment
from db.models.attendance import Attendance
from db.models.gamification_record import GamificationRecord
from db.models.note import Note
from db.models.study_session import StudySession
from db.models.subject import Subject
from db.models.user import User

__all__ = ["Assignment", "Attendance", "GamificationRecord", "Note", "StudySession", "Subject", "User"]
