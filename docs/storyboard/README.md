# Review storyboard

The storyboard tells every user story and architecture decision through one student's week, so the team can review and approve them. The live, shared copy is on claude.ai: <https://claude.ai/artifact/NAoWWJqtPiReaBegkAiCfw>. Decisions made there are saved with the page; [../storyboard.html](../storyboard.html) is a read-only copy for opening locally.

The story and decision files in `docs/specs/` are the source of truth. The storyboard is generated from them, and review decisions flow back into them.

## Files

| File | What it holds |
|---|---|
| `scenes.json` | Priya's moment and the analogy for each story, the plain-words text for each decision, and how cards are grouped |
| `recommendations.json` | Our recommended answer to each open question, and how the story changes if it's accepted |
| `template.html` | Page layout, styles and the review script |
| `specs.py` | Reads and edits the markdown files |
| `build.py` | Builds the storyboard from the markdown files |
| `apply_reviews.py` | Writes review decisions into the story, decision and test-case files |

## Syncing decisions into the repository

Ask Claude to **sync the storyboard**. Claude then:

1. Exports the page's `reviews` collection to a folder (one JSON file per reviewed item).
2. Runs `python3 docs/storyboard/apply_reviews.py <folder>`, which:
   - sets each story's status to `approved`, `needs-changes` or `rejected`, and each decision's status to `accepted`, `proposed` or `rejected`;
   - for an accepted recommendation, adds or changes the acceptance criteria, marks the open question resolved, and adds or updates the matching rows in `test-cases/`;
   - records notes and status changes in each file's Discussion section.
3. Runs `python3 docs/storyboard/build.py --artifact <file>` and republishes the page, so its "In repo" labels match the files.
4. Commits the changes.

Running the sync twice with the same decisions changes nothing the second time. Clearing a decision on the page doesn't change a file that was already synced; change its status by hand if needed.

## Adding a story or decision

Write the markdown file in `docs/specs/`, add its text and area to `scenes.json` (the build stops and names any file that's missing), then rebuild.
