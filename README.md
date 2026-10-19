# CampusMate

AI-powered student management system: one place for a student's subjects, timetable, assignments, attendance, AI study plans, note summaries and quizzes.

- **Front end:** Angular 21 with Angular Material, in [frontend/campusmate-web](frontend/campusmate-web)
- **Back end:** Python FastAPI with SQLAlchemy and Alembic, in [backend](backend)
- **Database:** SQLite for development (PostgreSQL when deployed)

## 1. Install the tools

| Tool | Version | Check with |
|---|---|---|
| Git | any recent | `git --version` |
| Node.js | 20.19+, 22.12+ or 24+ | `node --version` |
| Python | 3.11 or newer | `python3 --version` |

On Windows, use `python` instead of `python3` in the commands below.

## 2. Get the code

```bash
git clone https://github.com/ganeshyavapuram/CampusMate.git
cd CampusMate
git switch dev
```

Work happens on `dev` and on feature branches made from it; `main` only gets tested releases.

## 3. Set up the back end

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # Windows: copy .env.example .env
alembic upgrade head               # creates campusmate.db with all tables
```

## 4. Set up the front end

Open a second terminal in the project folder:

```bash
cd frontend/campusmate-web
npm install
```

## 5. Run the app

You need both servers running at the same time, one per terminal.

**Terminal 1, back end:**

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --port 8001
```

**Terminal 2, front end:**

```bash
cd frontend/campusmate-web
npx ng serve
```

Open <http://localhost:4200>. The page should say **Back end status: ok**.

| What | Address |
|---|---|
| App | <http://localhost:4200> |
| API health check | <http://127.0.0.1:8001/api/v1/health> |
| Interactive API docs | <http://127.0.0.1:8001/docs> |

## 6. Run the tests

```bash
cd backend && python -m pytest                          # back end
cd frontend/campusmate-web && npx ng test --watch=false # front end
```

## Troubleshooting

| Problem | Fix |
|---|---|
| Page says **Back end status: unreachable** | The back end isn't running, or it's on a different port. Start it on 8001, or change `apiBaseUrl` in `frontend/campusmate-web/src/environments/environment.development.ts` to match. |
| `Address already in use` when starting the back end | Another program (often Docker) is using that port. Pick a free one, such as `--port 8002`, and update `apiBaseUrl` to match. |
| `ModuleNotFoundError` in the back end | The virtual environment isn't active. Run `source .venv/bin/activate` in that terminal. |
| `The Angular CLI requires a minimum Node.js version` | Update Node.js to a version in the table above. |
| `no such table` errors | Run `alembic upgrade head` in `backend`. |
| Changed a database model | Run `alembic revision --autogenerate -m "what changed"`, then `alembic upgrade head`, and commit the new migration file. |

Never commit `backend/.env` or `campusmate.db`; both are in `.gitignore`.

## Project documents

| Document | What it covers |
|---|---|
| [docs/folder-structure.md](docs/folder-structure.md) | Where every file goes, feature by feature |
| [docs/specs/what/user-stories](docs/specs/what/user-stories/README.md) | The 44 approved user stories |
| [docs/specs/how/adr](docs/specs/how/adr/README.md) | The 31 architecture decisions |
| [test-cases](test-cases/README.md) | Written test cases for each feature |
| [docs/storyboard.html](docs/storyboard.html) | Plain-language storyboard of every story and decision |
| [backend/README.md](backend/README.md) | Back-end details: migrations and tests |
| [frontend/campusmate-web/README.md](frontend/campusmate-web/README.md) | Front-end details: API address, folder layout and tests |
