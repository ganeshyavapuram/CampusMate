# CampusMate test cases

Written test cases for every feature, kept in the same feature folders as the back end and front end. They are the test-case designs and outcome records required by the BCSP-064 Project Report (unit, integration and system testing).

## Where things are

| Folder | Feature | Back end | Front end |
|---|---|---|---|
| [`auth/`](auth/auth-test-cases.md) | Sign-in and account | `backend/tests/api/auth/` | `frontend/campusmate-web/src/app/core/auth/ and features/auth/login/` |
| [`subjects/`](subjects/subjects-test-cases.md) | Subjects and timetable | `backend/tests/api/subjects/` | `frontend/campusmate-web/src/app/features/subjects/` |
| [`dashboard/`](dashboard/dashboard-test-cases.md) | Dashboard and reminders | `backend/tests/api/dashboard/` | `frontend/campusmate-web/src/app/features/dashboard/` |
| [`planner/`](planner/planner-test-cases.md) | Smart planner | `backend/tests/api/planner/` | `frontend/campusmate-web/src/app/features/planner/` |
| [`notes/`](notes/notes-test-cases.md) | AI notes and quizzes | `backend/tests/api/notes/` | `frontend/campusmate-web/src/app/features/notes/` |
| [`assignments/`](assignments/assignments-test-cases.md) | Assignments | `backend/tests/api/assignments/` | `frontend/campusmate-web/src/app/features/assignments/` |
| [`attendance/`](attendance/attendance-test-cases.md) | Attendance | `backend/tests/api/attendance/` | `frontend/campusmate-web/src/app/features/attendance/` |
| [`gamification/`](gamification/gamification-test-cases.md) | Rewards: XP, streaks, levels and badges | `backend/tests/api/gamification/` | `frontend/campusmate-web/src/app/features/profile/` |
| [`reports/`](reports/reports-test-cases.md) | Reports | `not decided yet` | `not decided yet` |
| [`common/`](common/common-test-cases.md) | Rules for every feature | `backend/tests/api/common/` | `every feature folder` |

## How a test case is written

- **ID:** `TC-<CODE>-NN`, numbered within the feature. Codes match the Notion task codes: `AUTH`, `SUBJ`, `DASH`, `PLAN`, `NOTE`, `ASGN`, `ATT`, `GAME`, `REP`, `COM`.
- **Story:** the user story whose acceptance criterion the case proves.
- **Level:**
  - **Unit:** one function on its own, with no database or network (for example the attendance formulas).
  - **Integration:** a request through the API to the database (for example "returns HTTP 401 without a token").
  - **System:** the whole app in a browser, end to end, as a student would use it.
- **Expected result:** what must be true for the case to pass.
- **Actual result:** what happened when the case was run.
- **Status:** `Not run`, `Pass`, `Fail` or `Blocked` (cannot be run yet, with the reason in Actual result).

## Recording a run

1. Run the cases in the feature's file and fill in **Actual result** and **Status** for each.
2. Add a line to that file's **Run log** with the date, commit, who ran it and the pass/fail counts.
3. For a failed case, open a task in Notion that names the test case ID.

## Adding a case

Add a new acceptance criterion to the user story first, then add a row here with the next free number in that feature. Never reuse an ID that has been deleted.

The synopsis test cases TC-01 to TC-08 are included under their features; their original numbers appear in parentheses in the expected result.
