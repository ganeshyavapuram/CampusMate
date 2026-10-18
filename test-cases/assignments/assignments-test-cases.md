# Assignments — test cases

- **Feature folder:** `assignments`
- **Automated tests:** back end `backend/tests/api/assignments/`; front end `frontend/campusmate-web/src/app/features/assignments/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-024 — Add an assignment](../../docs/specs/what/user-stories/US-024-add-an-assignment.md)
- [US-025 — Edit and delete assignments](../../docs/specs/what/user-stories/US-025-edit-and-delete-assignments.md)
- [US-026 — Mark an assignment completed](../../docs/specs/what/user-stories/US-026-mark-an-assignment-completed.md)
- [US-027 — Highlight assignments due soon](../../docs/specs/what/user-stories/US-027-highlight-assignments-due-soon.md)
- [US-028 — Flag overdue assignments](../../docs/specs/what/user-stories/US-028-flag-overdue-assignments.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-ASGN-01 | US-024 | System | The student can add an assignment with a title of 1 to 150 characters, a subject and a due date. | | Not run |
| TC-ASGN-02 | US-024 | System | A due date before today is rejected with a message, and nothing is saved (TC-03). | | Not run |
| TC-ASGN-03 | US-024 | System | A new assignment has status "pending" and appears in the assignment list sorted by due date. | | Not run |
| TC-ASGN-04 | US-024 | System | It also appears in the dashboard's pending assignments. | | Not run |
| TC-ASGN-05 | US-025 | System | The student can change an assignment's title, subject and due date. | | Not run |
| TC-ASGN-06 | US-025 | System | Changing the due date to a date before today is rejected; an existing past due date doesn't block editing other fields. | | Not run |
| TC-ASGN-07 | US-025 | System | The student can delete an assignment after confirming. | | Not run |
| TC-ASGN-08 | US-025 | System | Deleting a completed assignment doesn't remove XP already earned for it. | | Not run |
| TC-ASGN-09 | US-026 | System | Marking an assignment completed sets its status to "completed" and records the completion time. | | Not run |
| TC-ASGN-10 | US-026 | System | The student is awarded assignment XP once (TC-04). | | Not run |
| TC-ASGN-11 | US-026 | System | A completed assignment can be reopened to "pending"; completing it again awards no extra XP. | | Not run |
| TC-ASGN-12 | US-026 | System | Completed assignments leave the pending lists and appear under a "Completed" filter. | | Not run |
| TC-ASGN-13 | US-027 | System | Pending assignments due today or tomorrow (in the student's time zone) show a "Due soon" label on the dashboard and the assignment list. | | Not run |
| TC-ASGN-14 | US-027 | System | Completed assignments never show the label. | | Not run |
| TC-ASGN-15 | US-027 | System | The label disappears once the due date has passed and the assignment becomes overdue (US-028). | | Not run |
| TC-ASGN-16 | US-028 | System | A pending assignment whose due date is before today shows an "Overdue" label. | | Not run |
| TC-ASGN-17 | US-028 | System | The dashboard shows the number of overdue assignments. | | Not run |
| TC-ASGN-18 | US-028 | System | Completing an overdue assignment removes the label. | | Not run |
| TC-ASGN-19 | US-028 | System | Overdue is worked out from the due date and today's date; it is never stored as a status. | | Not run |
| TC-ASGN-20 | US-024 | System | The student can add an optional description of up to 500 characters; longer text is rejected with a message. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
