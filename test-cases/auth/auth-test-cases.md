# Sign-in and account — test cases

- **Feature folder:** `auth`
- **Automated tests:** back end `backend/tests/api/auth/`; front end `frontend/campusmate-web/src/app/core/auth/ and features/auth/login/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-001 — Sign in with Google](../../docs/specs/what/user-stories/US-001-sign-in-with-google.md)
- [US-002 — Sign out](../../docs/specs/what/user-stories/US-002-sign-out.md)
- [US-003 — Edit profile and delete account](../../docs/specs/what/user-stories/US-003-edit-profile-and-delete-account.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-AUTH-01 | US-001 | System | The login screen shows a "Sign in with Google" button and a one-paragraph introduction to CampusMate. | | Not run |
| TC-AUTH-02 | US-001 | System | After a successful Google sign-in the student is taken to the dashboard (or to first-time setup, US-004, if they have no subjects). | | Not run |
| TC-AUTH-03 | US-001 | System | On a student's first sign-in exactly one User record and one GamificationRecord are created; signing in again creates no new records. | | Not run |
| TC-AUTH-04 | US-001 | Integration | A request to any protected API endpoint without a valid Firebase ID token returns HTTP 401 and no data (TC-01). | | Not run |
| TC-AUTH-05 | US-001 | System | If the student closes the Google pop-up without signing in, they remain on the login screen and no error page is shown. | | Not run |
| TC-AUTH-06 | US-002 | System | A "Sign out" control is reachable from every screen after sign-in (header or profile menu). | | Not run |
| TC-AUTH-07 | US-002 | System | Selecting it returns the student to the login screen. | | Not run |
| TC-AUTH-08 | US-002 | System | After signing out, pressing the browser Back button does not display any previously loaded student data. | | Not run |
| TC-AUTH-09 | US-002 | Integration | After signing out, the front end holds no Firebase ID token, and the next API call from that browser is rejected with HTTP 401 until the student signs in again. | | Not run |
| TC-AUTH-10 | US-003 | System | The profile screen lets the student change their display name; names of 1 to 100 characters are saved, and an empty name is rejected with a message. | | Not run |
| TC-AUTH-11 | US-003 | System | "Delete account" opens a confirmation dialog stating that all subjects, assignments, study sessions, notes, quiz attempts, attendance and rewards will be permanently removed. | | Not run |
| TC-AUTH-12 | US-003 | System | After confirmation, no rows belonging to that user remain in any table, any stored note files are removed, and the student is signed out. | | Not run |
| TC-AUTH-13 | US-003 | System | Signing in again with the same Google account afterwards starts as a brand-new user with no data. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
