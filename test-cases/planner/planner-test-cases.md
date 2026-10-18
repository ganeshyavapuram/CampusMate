# Smart planner — test cases

- **Feature folder:** `planner`
- **Automated tests:** back end `backend/tests/api/planner/`; front end `frontend/campusmate-web/src/app/features/planner/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-010 — Generate an AI study timetable](../../docs/specs/what/user-stories/US-010-generate-an-ai-study-timetable.md)
- [US-011 — Save daily study hours](../../docs/specs/what/user-stories/US-011-save-daily-study-hours.md)
- [US-012 — View weekly study timetable](../../docs/specs/what/user-stories/US-012-view-weekly-study-timetable.md)
- [US-013 — Mark a study session completed](../../docs/specs/what/user-stories/US-013-mark-a-study-session-completed.md)
- [US-014 — Mark a session missed and reschedule](../../docs/specs/what/user-stories/US-014-mark-a-session-missed-and-reschedule.md)
- [US-015 — Regenerate the study plan](../../docs/specs/what/user-stories/US-015-regenerate-the-study-plan.md)
- [US-016 — See a clear error when AI is unavailable](../../docs/specs/what/user-stories/US-016-see-a-clear-error-when-ai-is-unavailable.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-PLAN-01 | US-010 | System | The planner form is pre-filled with the student's subjects, weak flags, exam dates and saved daily study hours. | | Not run |
| TC-PLAN-02 | US-010 | System | Generating a plan creates study sessions with status "planned" from today up to the latest exam date. | | Not run |
| TC-PLAN-03 | US-010 | System | No day's planned sessions add up to more than the student's daily study hours. | | Not run |
| TC-PLAN-04 | US-010 | System | No session for a subject is scheduled after that subject's exam date. | | Not run |
| TC-PLAN-05 | US-010 | System | Every subject with a future exam date has at least one session. | | Not run |
| TC-PLAN-06 | US-010 | System | If the AI response breaks any of these rules or the AI is unavailable, a clear error is shown and no sessions are saved (TC-08). | | Not run |
| TC-PLAN-07 | US-011 | System | The student can set daily study hours between 0.5 and 12, in steps of 0.5. | | Not run |
| TC-PLAN-08 | US-011 | System | Values outside that range are rejected with a message. | | Not run |
| TC-PLAN-09 | US-011 | System | The saved value pre-fills the planner form on later visits, including after signing out and back in. | | Not run |
| TC-PLAN-10 | US-011 | System | Changing the value does not alter the existing plan until the student regenerates it (US-015). | | Not run |
| TC-PLAN-11 | US-012 | System | The timetable shows Monday to Sunday of the current week, with each session's subject and duration under its day. | | Not run |
| TC-PLAN-12 | US-012 | System | The student can move to the previous and next week. | | Not run |
| TC-PLAN-13 | US-012 | System | Planned, completed and missed sessions are distinguishable by both colour and a text label. | | Not run |
| TC-PLAN-14 | US-012 | System | Today's column is highlighted. | | Not run |
| TC-PLAN-15 | US-012 | System | At a screen width of 375 px the week is readable without horizontal page scrolling. | | Not run |
| TC-PLAN-16 | US-013 | System | A planned session dated today or earlier can be marked completed; a future-dated session cannot. | | Not run |
| TC-PLAN-17 | US-013 | System | The session's status changes to "completed" on the timetable and in the weekly report. | | Not run |
| TC-PLAN-18 | US-013 | System | The student is awarded session XP once; marking it again or reopening and re-completing it awards nothing more. | | Not run |
| TC-PLAN-19 | US-013 | System | Completing a session counts as activity for today's streak. | | Not run |
| TC-PLAN-20 | US-014 | System | Marking a session missed sets its status to "missed". | | Not run |
| TC-PLAN-21 | US-014 | System | The remaining planned sessions dated today or later are replaced by a newly generated plan that meets the rules in US-010. | | Not run |
| TC-PLAN-22 | US-014 | System | Completed and missed sessions are not changed. | | Not run |
| TC-PLAN-23 | US-014 | System | The missed session's subject appears at least once in the new plan before its exam date. | | Not run |
| TC-PLAN-24 | US-014 | System | If rescheduling fails, the session stays marked missed, the previous planned sessions are unchanged, and a "Try again" action is shown. | | Not run |
| TC-PLAN-25 | US-015 | System | A "Regenerate plan" action is available on the timetable screen. | | Not run |
| TC-PLAN-26 | US-015 | System | Before regenerating, a confirmation states how many planned sessions will be replaced. | | Not run |
| TC-PLAN-27 | US-015 | System | Only planned sessions dated today or later are replaced; completed and missed sessions stay. | | Not run |
| TC-PLAN-28 | US-015 | System | The new plan uses the current subjects, exam dates, weak flags and daily hours. | | Not run |
| TC-PLAN-29 | US-015 | System | If generation fails, the existing plan is left exactly as it was. | | Not run |
| TC-PLAN-30 | US-016 | Integration | When an AI request fails or times out, the student sees a message saying the AI service is unavailable and to try again later, within 70 seconds of starting the action. | | Not run |
| TC-PLAN-31 | US-016 | System | No study sessions, summaries, quizzes or suggestions are partially saved after a failure. | | Not run |
| TC-PLAN-32 | US-016 | System | The failed action can be retried from the same screen. | | Not run |
| TC-PLAN-33 | US-016 | Integration | When the student has reached the daily AI request limit, a different message says so and states when the limit resets. | | Not run |
| TC-PLAN-34 | US-010 | System | Each weak subject's total planned minutes are at least 1.5 times those of every non-weak subject whose exam date is the same or later. | | Not run |
| TC-PLAN-35 | US-013 | System | A planned session dated before today shows a "Not marked" label, and the dashboard lists it with buttons to mark it completed or missed. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
