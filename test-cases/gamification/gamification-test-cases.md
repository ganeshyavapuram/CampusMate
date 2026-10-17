# Rewards: XP, streaks, levels and badges — test cases

- **Feature folder:** `gamification`
- **Automated tests:** back end `backend/tests/api/gamification/`; front end `frontend/campusmate-web/src/app/features/profile/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-034 — Earn XP for study activity](../../docs/specs/what/user-stories/US-034-earn-xp-for-study-activity.md)
- [US-035 — Keep a daily study streak](../../docs/specs/what/user-stories/US-035-keep-a-daily-study-streak.md)
- [US-036 — Unlock badges](../../docs/specs/what/user-stories/US-036-unlock-badges.md)
- [US-037 — See my level](../../docs/specs/what/user-stories/US-037-see-my-level.md)
- [US-038 — View profile and rewards](../../docs/specs/what/user-stories/US-038-view-profile-and-rewards.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-GAME-01 | US-034 | System | Completing an assignment awards 20 XP and completing a study session awards 10 XP. | | Not run |
| TC-GAME-02 | US-034 | System | The XP total on the dashboard and profile updates straight after the action. | | Not run |
| TC-GAME-03 | US-034 | System | Each assignment or session awards XP at most once, even if reopened and completed again. | | Not run |
| TC-GAME-04 | US-034 | System | Reopening a completed item doesn't remove XP. | | Not run |
| TC-GAME-05 | US-035 | System | Completing an assignment or a study session counts as activity for that day in the student's time zone. | | Not run |
| TC-GAME-06 | US-035 | System | The first activity on a day after an active previous day increases the streak by 1; more activity on the same day doesn't increase it again. | | Not run |
| TC-GAME-07 | US-035 | System | If a whole day passes without activity, the streak shows 0 until the next activity starts a new streak at 1. | | Not run |
| TC-GAME-08 | US-035 | System | The current streak appears on the dashboard and profile. | | Not run |
| TC-GAME-09 | US-036 | System | Reaching a 7-day streak unlocks the "7-Day Streak" badge. | | Not run |
| TC-GAME-10 | US-036 | System | Each badge is earned at most once per student and stores the date it was earned. | | Not run |
| TC-GAME-11 | US-036 | System | When a badge unlocks, a short on-screen message names it. | | Not run |
| TC-GAME-12 | US-036 | System | The full badge list and the conditions for each are defined before this story is built. | | Not run |
| TC-GAME-13 | US-037 | Unit | Level = floor(XP / 100) + 1, so 0–99 XP is level 1 and 100–199 XP is level 2. | | Not run |
| TC-GAME-14 | US-037 | System | The profile and dashboard show the current level. | | Not run |
| TC-GAME-15 | US-037 | System | Progress towards the next level is shown, for example "40 / 100 XP". | | Not run |
| TC-GAME-16 | US-038 | System | The profile shows display name, email, XP total, level, current streak, and earned badges with the date each was earned. | | Not run |
| TC-GAME-17 | US-038 | System | Badges not yet earned appear greyed out with the condition for unlocking them. | | Not run |
| TC-GAME-18 | US-038 | System | The profile shows only the signed-in student's information. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
