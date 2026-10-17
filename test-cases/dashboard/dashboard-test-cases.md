# Dashboard and reminders — test cases

- **Feature folder:** `dashboard`
- **Automated tests:** back end `backend/tests/api/dashboard/`; front end `frontend/campusmate-web/src/app/features/dashboard/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-008 — View daily dashboard](../../docs/specs/what/user-stories/US-008-view-daily-dashboard.md)
- [US-009 — Get a daily AI study suggestion](../../docs/specs/what/user-stories/US-009-get-a-daily-ai-study-suggestion.md)
- [US-029 — See in-app deadline reminders](../../docs/specs/what/user-stories/US-029-see-in-app-deadline-reminders.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-DASH-01 | US-008 | System | The dashboard shows five sections: today's classes, pending assignments sorted by due date, upcoming exams, attendance percentage per subject, and XP with current streak. | | Not run |
| TC-DASH-02 | US-008 | System | Pending assignments due today or tomorrow are visually highlighted (US-027). | | Not run |
| TC-DASH-03 | US-008 | System | Subjects below or at risk of falling below the attendance threshold show a warning label (US-033). | | Not run |
| TC-DASH-04 | US-008 | System | A section with no data shows a short explanation and a link to the screen where that data is added. | | Not run |
| TC-DASH-05 | US-008 | System | The dashboard shows only the signed-in student's data. | | Not run |
| TC-DASH-06 | US-009 | System | The dashboard shows a one-sentence suggestion that names at least one of the student's subjects or assignments. | | Not run |
| TC-DASH-07 | US-009 | Integration | Reloading the dashboard on the same day (in the student's time zone) shows the same suggestion and makes no new AI request. | | Not run |
| TC-DASH-08 | US-009 | System | The first dashboard load on the next day shows a newly generated suggestion. | | Not run |
| TC-DASH-09 | US-009 | System | If the AI service fails, a fixed fallback message is shown instead, no error page appears, and generation is retried on the next load. | | Not run |
| TC-DASH-10 | US-029 | System | A notification indicator in the header shows the number of pending assignments that are due soon or overdue. | | Not run |
| TC-DASH-11 | US-029 | System | Opening it lists those assignments, each linking to its detail. | | Not run |
| TC-DASH-12 | US-029 | System | The count updates as soon as an assignment is completed. | | Not run |
| TC-DASH-13 | US-029 | System | No emails or push notifications are sent. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
