"""Write storyboard review decisions into the user-story, ADR and test-case files.

    python3 docs/storyboard/apply_reviews.py <reviews-dir> [--date YYYY-MM-DD]

<reviews-dir> holds one JSON file per reviewed item (US-001.json, ADR-006.json, ...),
as exported from the live storyboard's "reviews" collection. Each file has
decision (approved | changes | rejected | null), note and recAccepted.

What changes:
- Story status: approved / needs-changes / rejected. Decision status: accepted / proposed / rejected.
  A cleared decision leaves the status as it is.
- An accepted recommendation adds or changes acceptance criteria, closes the open question,
  and adds or updates the matching rows in test-cases/.
- Notes and status changes are added to the file's Discussion section.
Running it twice with the same input changes nothing the second time.
"""
import datetime
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import specs  # noqa: E402

RECS = json.loads((pathlib.Path(__file__).resolve().parent / "recommendations.json").read_text())
US_MAP = {"approved": "approved", "changes": "needs-changes", "rejected": "rejected"}
ADR_MAP = {"approved": "accepted", "changes": "proposed", "rejected": "rejected"}
WORDS = {"approved": "Approved", "changes": "Needs changes", "rejected": "Rejected"}


def load(path):
    raw = json.loads(path.read_text())
    if isinstance(raw.get("data"), dict):
        raw = raw["data"]
    return raw


def format_note(note):
    """First line inline; later lines indented under the entry, links as a sub-list."""
    lines = [l.strip() for l in note.splitlines() if l.strip()]
    if not lines:
        return ""
    rest = [f"  - <{l}>" if re.fullmatch(r"https?://\S+", l) else f"  {l}" for l in lines[1:]]
    return "\n".join([lines[0]] + rest)


def add_discussion(text, line):
    disc = specs.get_section(text, "Discussion")
    if line in disc:
        return text
    return specs.set_section(text, "Discussion", disc + "\n\n" + line)


def level(ac):
    if re.search(r"HTTP|API|request", ac):
        return "Integration"
    if re.search(r"floor\(|N = |Level = |shows 75\.0%|one decimal", ac):
        return "Unit"
    return "System"


def update_test_cases(sid, added, replaced):
    for f in sorted(specs.TEST_CASES.glob("*/*-test-cases.md")):
        t = f.read_text()
        if f"| {sid} |" not in t:
            continue
        for old, new in replaced:
            t = t.replace(f"| {old} |", f"| {new} |")
        rows = re.findall(r"^\| (TC-([A-Z]+)-(\d+)) \|.*$", t, flags=re.M)
        if added and rows:
            code = rows[-1][1]
            last_line = re.findall(r"^\| TC-[A-Z]+-\d+ \|.*$", t, flags=re.M)[-1]
            n = max(int(r[2]) for r in rows)
            new_rows = []
            for ac in added:
                if f"| {ac} |" in t:
                    continue
                n += 1
                new_rows.append(f"| TC-{code}-{n:02d} | {sid} | {level(ac)} | {ac.replace('|', chr(92) + '|')} | | Not run |")
            if new_rows:
                t = t.replace(last_line, last_line + "\n" + "\n".join(new_rows), 1)
        f.write_text(t)
        return f.relative_to(specs.DOCS.parent)
    return None


def apply(item_id, review, date):
    path = specs.find(item_id)
    text = before = path.read_text()
    log = []
    is_story = item_id.startswith("US-")
    decision = review.get("decision")
    note = format_note(review.get("note") or "")

    if decision in WORDS:
        new_status = (US_MAP if is_story else ADR_MAP)[decision]
        if specs.front(text)["status"] != new_status:
            text = specs.set_front(text, "status", new_status)
            log.append(f"status -> {new_status}")
            text = add_discussion(text, f"- **Review, {date}:** {WORDS[decision]}." + (f" {note}" if note else ""))
        elif note:
            text = add_discussion(text, f"- **Review, {date}:** {WORDS[decision]}. {note}")
    elif note:
        text = add_discussion(text, f"- **Review note, {date}:** {note}")
    if text != before and not log:
        log.append("note added")

    rec = RECS.get(item_id)
    if review.get("recAccepted") and rec and is_story:
        q = specs.get_section(text, "Open questions")
        if not q.startswith("Resolved"):
            ac = specs.get_section(text, "Acceptance criteria")
            for old, new in rec.get("replace_criteria", []):
                if old not in ac:
                    raise SystemExit(f"{item_id}: criterion to replace not found: {old}")
                ac = ac.replace(old, new)
            for c in rec.get("add_criteria", []):
                if c not in ac:
                    ac += f"\n- [ ] {c}"
            text = specs.set_section(text, "Acceptance criteria", ac)
            text = specs.set_section(text, "Open questions", f"Resolved {date}: {rec['resolution']}")
            text = add_discussion(text, f"- **Review, {date}:** Recommendation accepted. {rec['recommendation']}")
            tc = update_test_cases(item_id, rec.get("add_criteria", []), rec.get("replace_criteria", []))
            log.append("recommendation applied" + (f", test cases updated in {tc}" if tc else ""))

    if text != before:
        text = specs.set_front(text, "updated", date)
        path.write_text(text.rstrip("\n") + "\n")
    return log


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    folder = pathlib.Path(sys.argv[1])
    date = sys.argv[sys.argv.index("--date") + 1] if "--date" in sys.argv else datetime.date.today().isoformat()
    changed = 0
    for f in sorted(folder.rglob("*.json")):
        item_id = f.stem
        if not re.fullmatch(r"(US-\d{3}|ADR-\d{3})", item_id):
            continue
        log = apply(item_id, load(f), date)
        if log:
            changed += 1
            print(f"{item_id}: {'; '.join(log)}")
    print(f"{changed} file(s) changed")


if __name__ == "__main__":
    main()
