# CampusMate — Folder Structure

Decided in [ADR-030](specs/how/adr/ADR-030-feature-sliced-back-end-with-route-controller-service-layers.md) (back end) and [ADR-031](specs/how/adr/ADR-031-feature-sliced-front-end-with-core-shared-and-features.md) (front end).

The idea in one line: **one folder per feature, with the same feature name on the back end, the front end and the test cases.**

## Repository root

```
campusmate/
├── backend/
├── frontend/
│   └── campusmate-web/
├── test-cases/                # written test cases, one folder per feature (for the project report)
├── docs/                      # this folder
├── .gitignore                 # node_modules, .venv, .env, uploads, *.db, service-account key
└── README.md                  # how to run the project
```

## Back end

```
backend/
├── app/                                  # wiring only, no business logic
│   ├── main.py                           # creates the app, CORS, startup, error handlers
│   └── router/
│       └── api_router.py                 # MAIN router: includes every feature route under /api
│
├── api/                                  # all features, one folder each
│   ├── auth/
│   │   ├── auth_route.py                 # URLs
│   │   ├── auth_controller.py            # handles the request, maps errors to HTTP codes
│   │   ├── auth_service.py               # business logic + database work
│   │   ├── auth_schemas.py               # Pydantic request/response models
│   │   └── auth_dependency.py            # get_current_user (used by every feature)
│   ├── subjects/                         # route, controller, service, schemas
│   ├── assignments/                      # route, controller, service, schemas
│   ├── attendance/
│   │   ├── (route, controller, service, schemas)
│   │   └── attendance_calculations.py    # the 75% maths, pure functions
│   ├── planner/
│   │   ├── (route, controller, service, schemas)
│   │   ├── planner_prompts.py            # AI prompt text
│   │   └── planner_validation.py         # checks the AI timetable against the rules
│   ├── notes/
│   │   ├── (route, controller, service, schemas)
│   │   └── notes_prompts.py
│   ├── dashboard/                        # route, controller, service, schemas
│   └── gamification/
│       ├── (route, controller, service, schemas)
│       └── gamification_rules.py         # XP amounts, streak and badge logic
│
├── core/
│   ├── config.py                         # reads .env
│   ├── security.py                       # verifies the Firebase token
│   └── exceptions.py                     # NotFoundError, AIUnavailableError, ...
│
├── db/
│   ├── database.py                       # engine, session, Base
│   └── models/                           # one file per table
│       ├── user.py
│       ├── subject.py
│       ├── assignment.py
│       ├── study_session.py
│       ├── note.py
│       ├── attendance.py
│       └── gamification_record.py
│
├── utils/                                # small helpers, no business rules
│   ├── ai_client.py                      # ask_ai(): the only file that calls OpenRouter
│   ├── text_extract.py
│   ├── file_validation.py
│   └── dates.py
│
├── tests/
│   ├── conftest.py
│   ├── fixtures/                         # saved AI replies (good and bad)
│   └── api/                              # one folder per feature, mirrors api/
│       ├── auth/test_auth.py
│       ├── subjects/test_subjects.py
│       ├── assignments/test_assignments.py
│       ├── attendance/
│       │   ├── test_attendance.py
│       │   └── test_attendance_calculations.py
│       ├── planner/
│       │   ├── test_planner.py
│       │   └── test_planner_validation.py
│       ├── notes/test_notes.py
│       ├── dashboard/test_dashboard.py
│       ├── gamification/test_gamification_rules.py
│       └── common/test_data_isolation.py # rules that cover every feature
│
├── uploads/                              # gitignored
├── .env  .env.example
├── requirements.txt
└── README.md
```

### What each file type does

| File | Job | Rule |
|---|---|---|
| `*_route.py` | URL, HTTP method, `response_model`, login check | No logic. |
| `*_controller.py` | Calls the service, turns errors into HTTP responses (404, 409, 503) | The only layer that raises `HTTPException`. |
| `*_service.py` | Business rules and database queries | Knows nothing about HTTP. |
| `*_schemas.py` | Shape of data going in and out | Pydantic only. |
| `*_calculations.py`, `*_rules.py`, `*_validation.py` | Pure rules, easy to unit test | No database, no HTTP. |
| `*_prompts.py` | Text sent to the AI model | No code that calls the AI. |

A request flows downward only:

`main.py` → `api_router.py` → route → controller → service → `db/models`

### Import rules

1. Imports go downward only. A service never imports a route or controller.
2. Services raise errors from `core/exceptions.py`; controllers convert them to HTTP responses.
3. Features do not import each other, with two exceptions: everyone may use `get_current_user` from `api/auth`, and the assignments and planner services may call `gamification_service`.
4. Only `utils/ai_client.py` calls the AI provider.
5. Database models live in `db/`, never inside a feature.

### Naming rules

- Feature files start with the feature name: `assignments_route.py`, not `route.py`.
- Folders and Python files use `snake_case`; classes use `PascalCase`.
- A new feature is added by creating its folder and adding one line to `api_router.py`.

## Front end

```
frontend/campusmate-web/src/app/
├── app.component.ts
├── app.config.ts                         # providers: router, HttpClient, interceptors, Firebase
│
├── routes/
│   └── app.routes.ts                     # top-level routes; each feature is lazy-loaded
│
├── core/                                 # app-wide singletons, loaded once
│   ├── auth/
│   │   ├── auth.service.ts               # Google sign-in, sign-out, current user
│   │   ├── auth.guard.ts                 # blocks pages when signed out
│   │   └── auth.interceptor.ts           # adds the Bearer token to requests
│   ├── http/
│   │   ├── api.service.ts                # base URL and shared helpers
│   │   └── error.interceptor.ts          # friendly error messages
│   └── layout/
│       └── shell/                        # toolbar + router outlet
│
├── shared/                               # reusable, knows nothing about any feature
│   ├── components/                       # loading-spinner, empty-state, confirm-dialog
│   ├── models/                           # TypeScript interfaces used by several features
│   └── utils/
│
└── features/                             # one folder per feature
    ├── auth/login/                       # login page
    ├── dashboard/
    ├── subjects/
    ├── assignments/
    │   ├── pages/                        # assignments-list.page.ts, ...
    │   ├── components/                   # assignment-form, assignment-row
    │   ├── services/assignments.service.ts
    │   ├── models/assignment.model.ts
    │   └── assignments.routes.ts         # this feature's own routes
    ├── attendance/
    ├── planner/
    ├── notes/
    └── profile/                          # XP, streak, badges
```

Every feature follows the `assignments/` layout. Front-end unit tests are `*.spec.ts` files placed next to the file they test, so they are already grouped by feature (for example `features/assignments/services/assignments.service.spec.ts`).

### Import rules

1. Features do not import other features.
2. `core/` and `shared/` never import from `features/`.
3. If two features need the same thing, move it to `shared/`.

## Test cases

Written test cases live outside the code, one folder per feature, with the same feature names as the back end. They are the test-case designs and outcome records the BCSP-064 Project Report requires, and each case comes from an acceptance criterion in a user story.

```
test-cases/
├── README.md                             # ID format, test levels, status values, how to record a run
├── auth/auth-test-cases.md
├── subjects/subjects-test-cases.md
├── assignments/assignments-test-cases.md
├── attendance/attendance-test-cases.md
├── planner/planner-test-cases.md
├── notes/notes-test-cases.md
├── dashboard/dashboard-test-cases.md
├── gamification/gamification-test-cases.md
├── reports/reports-test-cases.md         # reports have no back-end or front-end folder yet
└── common/common-test-cases.md           # rules for every feature: data isolation, phone layout
```

### Test case rules

1. One file per feature: `test-cases/<feature>/<feature>-test-cases.md`.
2. IDs are `TC-<CODE>-NN`, using the same codes as the Notion tasks: `AUTH`, `SUBJ`, `ASGN`, `ATT`, `PLAN`, `NOTE`, `DASH`, `GAME`, `REP`, `COM`.
3. Every case names the user story it proves and its level: Unit, Integration or System.
4. When a case is automated, its file lives in the same feature folder under `backend/tests/api/<feature>/` or next to the code in `frontend/.../features/<feature>/`.

## Same names on both sides

| Feature | Back end | Front end | Test cases |
|---|---|---|---|
| Sign-in | `api/auth/` | `core/auth/` and `features/auth/login/` | `test-cases/auth/` |
| Subjects | `api/subjects/` | `features/subjects/` | `test-cases/subjects/` |
| Assignments | `api/assignments/` | `features/assignments/` | `test-cases/assignments/` |
| Attendance | `api/attendance/` | `features/attendance/` | `test-cases/attendance/` |
| Planner | `api/planner/` | `features/planner/` | `test-cases/planner/` |
| AI Notes | `api/notes/` | `features/notes/` | `test-cases/notes/` |
| Dashboard | `api/dashboard/` | `features/dashboard/` | `test-cases/dashboard/` |
| Rewards | `api/gamification/` | `features/profile/` | `test-cases/gamification/` |
| Reports | not decided yet | not decided yet | `test-cases/reports/` |
| Every feature | `tests/api/common/` | — | `test-cases/common/` |

## Where to look when something breaks

| Symptom | Look in |
|---|---|
| Wrong URL or 404 on a route | `*_route.py`, then `api_router.py` |
| Wrong status code or error message | `*_controller.py` |
| Wrong number or wrong data saved | `*_service.py`, then `db/models/` |
| Bad data accepted | `*_schemas.py` |
| AI gives odd output | `*_prompts.py`, then `*_validation.py` |
| Signed-in user refused | `core/security.py`, `api/auth/`, `auth.interceptor.ts` |
| Page blank or wrong in the browser | the feature's `pages/` and its `services/` file |
| Request never reaches the server | `core/http/api.service.ts`, CORS in `app/main.py` |
| A test case fails | the feature's file in `test-cases/`, then its automated test in `backend/tests/api/<feature>/` |

## Where the Notion task paths now point

The Notion tasks were written before this layout was chosen. Use these paths instead of the ones in the task text.

| Task | New location |
|---|---|
| SET-05 | `backend/app/main.py` |
| SET-06 | `backend/core/config.py` |
| DB-01 | `backend/db/database.py`, `backend/db/models/user.py`, `gamification_record.py` |
| DB-02 | `backend/db/models/` (one file per table) |
| AUTH-06 | `backend/core/security.py`, `backend/api/auth/auth_dependency.py` |
| AUTH-07 | `backend/api/auth/auth_service.py` |
| AUTH-08 | `backend/tests/api/auth/test_auth.py` |
| SUBJ-01 | `backend/api/subjects/` |
| ASGN-01, ASGN-02 | `backend/api/assignments/` |
| ATT-01 | `backend/api/attendance/attendance_calculations.py` |
| ATT-02 | `backend/tests/api/attendance/test_attendance_calculations.py` |
| ATT-03 | `backend/api/attendance/` |
| DASH-02, AI-05 | `backend/api/dashboard/` |
| GAME-01, GAME-02 | `backend/api/gamification/gamification_rules.py` and `gamification_service.py` |
| GAME-03 | `assignments_service.py` and `planner_service.py` call `gamification_service` |
| PLAN-02, PLAN-04, PLAN-05 | `backend/api/planner/` |
| AI-01 | `backend/core/config.py` (`OPENROUTER_API_KEY`, `AI_MODEL`) |
| AI-02 | `backend/utils/ai_client.py` |
| AI-03 | `backend/api/planner/planner_prompts.py` and `planner_service.py` |
| AI-04 | `backend/api/planner/planner_validation.py` |
| NOTE-01 | `backend/api/notes/`, `backend/utils/file_validation.py` |
| NOTE-02 | `backend/utils/text_extract.py` |
| NOTE-04, NOTE-06 | `backend/api/notes/notes_service.py`, `notes_prompts.py` |
| TEST-01 | `backend/tests/api/common/test_data_isolation.py` |
| API-01 | `frontend/.../core/http/api.service.ts` |
| AUTH-02 | `frontend/.../features/auth/login/` |
| AUTH-03, AUTH-04, AUTH-05 | `frontend/.../core/auth/` (service, guard, interceptor) |
| DASH-01 | `frontend/.../core/layout/shell/` and `features/dashboard/` |
| SUBJ-02 | `frontend/.../features/subjects/` |
| ASGN-03, ASGN-04, ASGN-05 | `frontend/.../features/assignments/` |
| ATT-04 | `frontend/.../features/attendance/` |
| PLAN-01, PLAN-03, PLAN-06 | `frontend/.../features/planner/` |
| NOTE-03, NOTE-05, NOTE-07 | `frontend/.../features/notes/` |
| GAME-04 | `frontend/.../features/profile/` |
| TEST-02 | `frontend/.../core/http/error.interceptor.ts` |
