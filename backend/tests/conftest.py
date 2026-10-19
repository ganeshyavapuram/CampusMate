"""Test setup: every test run uses a fresh temporary SQLite database, never campusmate.db."""
import os
import tempfile

_tmp_dir = tempfile.mkdtemp(prefix="campusmate-tests-")
os.environ["DATABASE_URL"] = f"sqlite:///{_tmp_dir}/test.db"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

import db.models  # noqa: E402,F401
from app.main import app  # noqa: E402
from db.database import Base, SessionLocal, engine  # noqa: E402


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture()
def db_session():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
