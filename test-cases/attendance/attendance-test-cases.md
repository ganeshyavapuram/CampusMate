# Attendance — test cases

- **Feature folder:** `attendance`
- **Automated tests:** back end `backend/tests/api/attendance/`; front end `frontend/campusmate-web/src/app/features/attendance/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-030 — Log class attendance](../../docs/specs/what/user-stories/US-030-log-class-attendance.md)
- [US-031 — Correct an attendance entry](../../docs/specs/what/user-stories/US-031-correct-an-attendance-entry.md)
- [US-032 — See how many classes I can miss](../../docs/specs/what/user-stories/US-032-see-how-many-classes-i-can-miss.md)
- [US-033 — Get attendance warnings before it's too late](../../docs/specs/what/user-stories/US-033-get-attendance-warnings-before-it-s-too-late.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-ATT-01 | US-030 | System | The student can record present or absent for a subject on a date, defaulting to today. | | Not run |
| TC-ATT-02 | US-030 | System | A future date is rejected. | | Not run |
| TC-ATT-03 | US-030 | System | Only one record is allowed per subject per date; logging the same date again offers to edit the existing record. | | Not run |
| TC-ATT-04 | US-030 | Unit | The subject's percentage updates immediately, shown to one decimal place: 18 of 24 shows 75.0% (TC-05), and 17 of 24 shows 70.8% (TC-06). | | Not run |
| TC-ATT-05 | US-031 | System | Each subject's attendance history lists records newest first. | | Not run |
| TC-ATT-06 | US-031 | System | The student can switch a record between present and absent. | | Not run |
| TC-ATT-07 | US-031 | System | The student can delete a record. | | Not run |
| TC-ATT-08 | US-031 | System | After any change the percentage, counts and warnings are recalculated. | | Not run |
| TC-ATT-09 | US-032 | Unit | At or above 75%, the subject shows "You can miss N more classes", where N = floor((4A − 3T) / 3) for A attended out of T held. | | Not run |
| TC-ATT-10 | US-032 | Unit | Below 75%, the subject shows "Attend the next N classes", where N = 3T − 4A. | | Not run |
| TC-ATT-11 | US-032 | Unit | Examples: 20 of 24 shows "miss 2", 18 of 24 shows "miss 0", and 17 of 24 shows "attend 4". | | Not run |
| TC-ATT-12 | US-032 | System | A subject with no records shows "No classes logged yet". | | Not run |
| TC-ATT-13 | US-033 | System | A subject below 75% shows a "Below 75%" warning on the dashboard and attendance screen. | | Not run |
| TC-ATT-14 | US-033 | System | A subject at or above 75% where one more absence would drop it below shows an "At risk" warning; for example, 18 of 24 is at risk because 18 of 25 is 72%. | | Not run |
| TC-ATT-15 | US-033 | System | The two warnings look different and each has a text label. | | Not run |
| TC-ATT-16 | US-033 | System | Once a class timetable exists (US-007), an at-risk subject shows the date of its next class. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
