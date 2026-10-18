# Subjects and timetable — test cases

- **Feature folder:** `subjects`
- **Automated tests:** back end `backend/tests/api/subjects/`; front end `frontend/campusmate-web/src/app/features/subjects/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-004 — Complete first-time setup](../../docs/specs/what/user-stories/US-004-complete-first-time-setup.md)
- [US-005 — Manage subjects](../../docs/specs/what/user-stories/US-005-manage-subjects.md)
- [US-006 — Set exam dates and weak subjects](../../docs/specs/what/user-stories/US-006-set-exam-dates-and-weak-subjects.md)
- [US-007 — Enter weekly class timetable](../../docs/specs/what/user-stories/US-007-enter-weekly-class-timetable.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-SUBJ-01 | US-004 | System | A signed-in student with zero subjects is shown the setup screen instead of the dashboard. | | Not run |
| TC-SUBJ-02 | US-004 | System | Setup collects at least one subject name, an optional exam date and weak-subject flag per subject, and daily study hours. | | Not run |
| TC-SUBJ-03 | US-004 | System | The student's time zone is detected from the browser and saved without asking. | | Not run |
| TC-SUBJ-04 | US-004 | System | The "Finish" button stays disabled until at least one subject has a name. | | Not run |
| TC-SUBJ-05 | US-004 | System | After finishing, the dashboard lists the subjects entered, and setup is not shown again while the student has at least one subject. | | Not run |
| TC-SUBJ-06 | US-005 | System | The student can add a subject with a name of 1 to 100 characters. | | Not run |
| TC-SUBJ-07 | US-005 | System | Adding a second subject with the same name (ignoring case) is rejected with a message. | | Not run |
| TC-SUBJ-08 | US-005 | System | The student can rename a subject, and the new name appears everywhere it is used. | | Not run |
| TC-SUBJ-09 | US-005 | System | Deleting a subject shows a confirmation that states how many assignments, notes, study sessions and attendance records will also be removed. | | Not run |
| TC-SUBJ-10 | US-005 | System | After confirming, the subject and all those records are gone, and none of them appear on any screen or report. | | Not run |
| TC-SUBJ-11 | US-006 | System | The student can set, change and clear an exam date for each subject. | | Not run |
| TC-SUBJ-12 | US-006 | System | An exam date before today is rejected with a message. | | Not run |
| TC-SUBJ-13 | US-006 | System | The student can toggle a subject's weak flag, and weak subjects show a visible "Weak" label in the subject list and planner form. | | Not run |
| TC-SUBJ-14 | US-006 | System | The dashboard's "Upcoming exams" section lists subjects with an exam in the next 30 days, soonest first, with the number of days remaining. | | Not run |
| TC-SUBJ-15 | US-007 | System | The student can add a class slot with a subject, weekday, start time and end time. | | Not run |
| TC-SUBJ-16 | US-007 | System | A slot whose end time is not after its start time is rejected with a message. | | Not run |
| TC-SUBJ-17 | US-007 | System | A slot overlapping another slot on the same weekday is rejected with a message naming the conflicting class. | | Not run |
| TC-SUBJ-18 | US-007 | System | The student can edit and delete slots. | | Not run |
| TC-SUBJ-19 | US-007 | System | The dashboard's "Today's classes" section lists today's slots in start-time order, using the student's time zone. | | Not run |
| TC-SUBJ-20 | US-007 | System | Attendance percentages and warnings use only logged attendance records, never classes predicted from the timetable. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
