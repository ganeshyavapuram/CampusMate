# AI notes and quizzes — test cases

- **Feature folder:** `notes`
- **Automated tests:** back end `backend/tests/api/notes/`; front end `frontend/campusmate-web/src/app/features/notes/`
- **Last updated:** 2026-10-17

Each case is one acceptance criterion from a user story. Fill in **Actual result** and **Status** each time the case is run; see [../README.md](../README.md).

## Stories covered

- [US-017 — Upload a note and get an AI summary](../../docs/specs/what/user-stories/US-017-upload-a-note-and-get-an-ai-summary.md)
- [US-018 — Generate a quiz from a note](../../docs/specs/what/user-stories/US-018-generate-a-quiz-from-a-note.md)
- [US-019 — Take a quiz and see my score](../../docs/specs/what/user-stories/US-019-take-a-quiz-and-see-my-score.md)
- [US-020 — View past quiz scores](../../docs/specs/what/user-stories/US-020-view-past-quiz-scores.md)
- [US-021 — Browse, search and delete notes](../../docs/specs/what/user-stories/US-021-browse-search-and-delete-notes.md)
- [US-022 — Regenerate a summary or quiz](../../docs/specs/what/user-stories/US-022-regenerate-a-summary-or-quiz.md)
- [US-023 — Reject invalid uploads](../../docs/specs/what/user-stories/US-023-reject-invalid-uploads.md)

## Test cases

| ID | Story | Level | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-NOTE-01 | US-017 | System | The upload screen requires choosing a subject and a file. | | Not run |
| TC-NOTE-02 | US-017 | System | The upload screen shows a one-line notice that notes are processed by an external AI service. | | Not run |
| TC-NOTE-03 | US-017 | System | PDF and plain-text files up to 10 MB are accepted. | | Not run |
| TC-NOTE-04 | US-017 | Integration | After a successful upload the AI summary is shown, and reopening the note later shows the same summary without a new AI request. | | Not run |
| TC-NOTE-05 | US-017 | System | A PDF with no extractable text is rejected with a message explaining it may be a scanned document. | | Not run |
| TC-NOTE-06 | US-018 | System | Each successfully processed note has a quiz of exactly 8 multiple-choice questions. | | Not run |
| TC-NOTE-07 | US-018 | System | Every question has exactly four options and exactly one correct answer. | | Not run |
| TC-NOTE-08 | US-018 | Integration | The quiz is saved with the note and shown again without a new AI request. | | Not run |
| TC-NOTE-09 | US-018 | System | A quiz response that doesn't meet these rules is rejected and nothing is saved (US-016). | | Not run |
| TC-NOTE-10 | US-019 | System | The student can select one option per question and submit the quiz. | | Not run |
| TC-NOTE-11 | US-019 | System | Submitting with unanswered questions asks for confirmation; unanswered questions count as wrong. | | Not run |
| TC-NOTE-12 | US-019 | System | After submitting, the score is shown as "correct / total" and each question shows the correct answer. | | Not run |
| TC-NOTE-13 | US-019 | System | Each submitted attempt is saved with its score and date. | | Not run |
| TC-NOTE-14 | US-020 | System | The note screen lists quiz attempts newest first, each with its date and score. | | Not run |
| TC-NOTE-15 | US-020 | System | The best score is shown separately. | | Not run |
| TC-NOTE-16 | US-020 | System | A note with no attempts shows "No attempts yet". | | Not run |
| TC-NOTE-17 | US-021 | System | The notes screen lists notes with title, subject and upload date, newest first. | | Not run |
| TC-NOTE-18 | US-021 | System | The list can be filtered by subject. | | Not run |
| TC-NOTE-19 | US-021 | System | Searching by title matches any part of the title, ignoring case. | | Not run |
| TC-NOTE-20 | US-021 | System | A note's title defaults to the uploaded file name and can be edited. | | Not run |
| TC-NOTE-21 | US-021 | System | Deleting a note after confirmation removes it with its summary, quiz, quiz attempts and any stored file. | | Not run |
| TC-NOTE-22 | US-022 | System | The note screen has separate "Regenerate summary" and "Regenerate quiz" actions. | | Not run |
| TC-NOTE-23 | US-022 | System | The new output replaces the old one only after it is generated and validated successfully. | | Not run |
| TC-NOTE-24 | US-022 | System | If regeneration fails, the existing summary or quiz is unchanged. | | Not run |
| TC-NOTE-25 | US-022 | Integration | Each regeneration counts towards the daily AI request limit. | | Not run |
| TC-NOTE-26 | US-022 | System | Previous quiz attempts are kept after the quiz is regenerated. | | Not run |
| TC-NOTE-27 | US-023 | System | Uploading an unsupported type (for example .exe or .docx) is rejected with a message listing the allowed types (TC-07). | | Not run |
| TC-NOTE-28 | US-023 | System | Uploading a file over the size limit is rejected with a message stating the limit. | | Not run |
| TC-NOTE-29 | US-023 | Integration | Both checks are also enforced by the API: a direct request with an invalid file returns HTTP 400 or 422. | | Not run |
| TC-NOTE-30 | US-023 | Integration | No note is created and no AI request is made for a rejected file. | | Not run |

## Run log

| Date | Build or commit | Run by | Cases run | Passed | Failed | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
