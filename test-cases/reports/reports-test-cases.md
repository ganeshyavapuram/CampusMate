# Reports — test cases

- **Feature folder:** `reports`
- **Automated tests:** back end `not decided yet`; front end `not decided yet`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-039 — View weekly productivity report](../../docs/specs/what/user-stories/US-039-view-weekly-productivity-report.md)
- [US-040 — View attendance report](../../docs/specs/what/user-stories/US-040-view-attendance-report.md)
- [US-041 — View assignment status report](../../docs/specs/what/user-stories/US-041-view-assignment-status-report.md)
- [US-042 — View notes summary log](../../docs/specs/what/user-stories/US-042-view-notes-summary-log.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-REP-01 | US-039 | System | The student can pick a week (Monday to Sunday); the current week is the default. | | Not run |
| TC-REP-02 | US-039 | System | The report shows, per subject, total minutes of completed sessions and the number of sessions completed out of planned. | | Not run |
| TC-REP-03 | US-039 | System | The report shows how many assignments were due that week and what percentage were completed. | | Not run |
| TC-REP-04 | US-039 | System | The figures match the underlying records exactly (checked against a test data set). | | Not run |
| TC-REP-05 | US-039 | System | The report can be downloaded as CSV and printed from the browser. | | Not run |
| TC-REP-06 | US-040 | System | The report shows, per subject, classes held, classes attended, percentage, and status (OK, At risk or Below 75%). | | Not run |
| TC-REP-07 | US-040 | System | The figures match the attendance screen exactly. | | Not run |
| TC-REP-08 | US-040 | System | The report can be downloaded as CSV and printed from the browser. | | Not run |
| TC-REP-09 | US-041 | System | The report shows, per subject, counts of pending, completed and overdue assignments. | | Not run |
| TC-REP-10 | US-041 | System | The report can be filtered to one subject. | | Not run |
| TC-REP-11 | US-041 | System | The report can be downloaded as CSV and printed from the browser. | | Not run |
| TC-REP-12 | US-042 | System | The log lists every note with subject, title, upload date, the first 200 characters of its summary, and its best quiz score. | | Not run |
| TC-REP-13 | US-042 | System | The log can be filtered by subject. | | Not run |
| TC-REP-14 | US-042 | System | The log can be downloaded as CSV and printed from the browser. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
