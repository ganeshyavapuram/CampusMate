from datetime import date

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from db.models import Assignment, Attendance, GamificationRecord, Note, StudySession, Subject, User


def make_user(db, uid="firebase-1", email="priya@example.com"):
    user = User(firebase_uid=uid, name="Priya", email=email)
    db.add(user)
    db.flush()
    return user


def test_ids_are_uuids(db_session):
    user = make_user(db_session)
    assert len(user.id) == 36 and user.id.count("-") == 4


def test_attendance_is_unique_per_subject_and_date(db_session):
    user = make_user(db_session)
    subject = Subject(user_id=user.id, name="DBMS")
    db_session.add(subject)
    db_session.flush()
    db_session.add(Attendance(subject_id=subject.id, date=date(2026, 10, 19), present=True))
    db_session.flush()
    db_session.add(Attendance(subject_id=subject.id, date=date(2026, 10, 19), present=False))
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_deleting_a_subject_deletes_its_records(db_session):
    user = make_user(db_session)
    subject = Subject(user_id=user.id, name="DBMS")
    db_session.add(subject)
    db_session.flush()
    db_session.add_all([
        Assignment(subject_id=subject.id, title="ER diagram", due_date=date(2026, 11, 30)),
        StudySession(subject_id=subject.id, scheduled_date=date(2026, 10, 20), duration_minutes=45),
        Note(subject_id=subject.id, title="Normalisation notes"),
        Attendance(subject_id=subject.id, date=date(2026, 10, 19), present=True),
    ])
    db_session.commit()

    db_session.delete(subject)
    db_session.commit()

    for model in (Assignment, StudySession, Note, Attendance):
        assert db_session.scalars(select(model)).all() == []


def test_deleting_a_user_deletes_everything(db_session):
    user = make_user(db_session)
    db_session.add(GamificationRecord(user_id=user.id))
    db_session.add(Subject(user_id=user.id, name="Maths"))
    db_session.commit()

    db_session.delete(user)
    db_session.commit()

    assert db_session.scalars(select(Subject)).all() == []
    assert db_session.scalars(select(GamificationRecord)).all() == []


def test_session_duration_must_be_positive(db_session):
    user = make_user(db_session)
    subject = Subject(user_id=user.id, name="DBMS")
    db_session.add(subject)
    db_session.flush()
    db_session.add(StudySession(subject_id=subject.id, scheduled_date=date(2026, 10, 20), duration_minutes=0))
    with pytest.raises(IntegrityError):
        db_session.flush()
