# Rules for every feature — test cases

- **Feature folder:** `common`
- **Automated tests:** back end `backend/tests/api/common/`; front end `every feature folder`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-043 — See only my own data](../../docs/specs/what/user-stories/US-043-see-only-my-own-data.md)
- [US-044 — Use CampusMate on a phone browser](../../docs/specs/what/user-stories/US-044-use-campusmate-on-a-phone-browser.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-COM-01 | US-043 | Integration | For every API resource, requesting another student's record by its id returns HTTP 404 (automated test with two users). | | Not run |
| TC-COM-02 | US-043 | System | Every list endpoint returns only the signed-in student's records. | | Not run |
| TC-COM-03 | US-043 | System | No endpoint accepts a user id from the client; the user always comes from the verified token. | | Not run |
| TC-COM-04 | US-044 | System | Every screen is usable at 375 px wide with no horizontal page scrolling. | | Not run |
| TC-COM-05 | US-044 | System | All buttons and inputs are at least 44 by 44 px. | | Not run |
| TC-COM-06 | US-044 | System | Every user story's main flow works in current Chrome on Android and Safari on iOS. | | Not run |
| TC-COM-07 | US-044 | System | Forms stay usable while the on-screen keyboard is open. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
