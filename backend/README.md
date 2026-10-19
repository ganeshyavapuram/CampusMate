# CampusMate back end

FastAPI app, laid out as described in [docs/folder-structure.md](../docs/folder-structure.md) (ADR-030).

## First-time setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
```

## Run

```bash
uvicorn app.main:app --reload --port 8001
```

- Health check: <http://127.0.0.1:8001/api/v1/health>
- Interactive API docs: <http://127.0.0.1:8001/docs>

Port 8001 is used because 8000 is often taken by Docker. If you change it, also change `apiBaseUrl` in `frontend/campusmate-web/src/environments/environment.development.ts`.

## Tests

```bash
python -m pytest
```

Tests use a temporary SQLite database, never `campusmate.db`.

## Changing the database

Edit a model in `db/models/`, then:

```bash
alembic revision --autogenerate -m "describe the change"
alembic upgrade head
```

Commit the new file in `migrations/versions/` (ADR-017).
