"""Read and edit the user-story and ADR markdown files in docs/specs."""
import pathlib
import re

DOCS = pathlib.Path(__file__).resolve().parent.parent
US_DIR = DOCS / "specs" / "what" / "user-stories"
ADR_DIR = DOCS / "specs" / "how" / "adr"
TEST_CASES = DOCS.parent / "test-cases"


def find(item_id):
    folder = US_DIR if item_id.startswith("US-") else ADR_DIR
    matches = sorted(folder.glob(f"{item_id}-*.md"))
    if not matches:
        raise FileNotFoundError(item_id)
    return matches[0]


def all_files(prefix):
    folder = US_DIR if prefix == "US" else ADR_DIR
    return sorted(folder.glob(f"{prefix}-[0-9][0-9][0-9]-*.md"))


def front(text):
    block = text.split("---", 2)[1]
    out = {}
    for line in block.strip().splitlines():
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip()
    return out


def related(text):
    return [r.strip() for r in front(text)["related"].strip("[]").split(",") if r.strip()]


def sections(text):
    """Map of '## Heading' -> section text (without the heading line)."""
    body = text.split("---", 2)[2]
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts), 2)}


def bullets(block, prefix="- "):
    return [l[len(prefix):].strip() for l in block.splitlines() if l.startswith(prefix)]


def criteria(text):
    return [re.sub(r"^\[[ x]\]\s*", "", c) for c in bullets(sections(text)["Acceptance criteria"])]


def set_front(text, key, value):
    head, sep, rest = text.partition("\n---\n")
    head = re.sub(rf"^{key}:.*$", f"{key}: {value}", head, flags=re.M)
    return head + sep + rest


def set_section(text, heading, new_body):
    pattern = rf"(^## {re.escape(heading)}\n\n)(.*?)(?=\n\n## |\Z)"
    new, n = re.subn(pattern, lambda m: m.group(1) + new_body, text, count=1, flags=re.M | re.S)
    if n != 1:
        raise ValueError(f"section {heading!r} not found")
    return new


def get_section(text, heading):
    return sections(text)[heading]
