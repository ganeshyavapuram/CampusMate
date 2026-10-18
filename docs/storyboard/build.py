"""Build the review storyboard from the user-story and ADR files.

    python3 docs/storyboard/build.py              # writes docs/storyboard.html (opens in any browser)
    python3 docs/storyboard/build.py --artifact X # also writes the page body to X, for publishing to claude.ai
"""
import html
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import specs  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SCENES = json.loads((HERE / "scenes.json").read_text())
RECS = json.loads((HERE / "recommendations.json").read_text())
ARTIFACT_URL = "https://claude.ai/artifact/NAoWWJqtPiReaBegkAiCfw"
e = html.escape

US_STATUS = {"draft": "Draft", "approved": "Approved", "needs-changes": "Needs changes", "rejected": "Rejected"}
ADR_STATUS = {"proposed": "Proposed", "accepted": "Accepted", "rejected": "Rejected"}


def ref_links(ids):
    return " ".join(f'<a class="ref" href="#{r}">{r}</a>' for r in ids) or "None"


def review_bar(item_id, rec_state):
    return f'''<div class="review" data-id="{item_id}">
  <div class="choices" role="group" aria-label="Decision for {item_id}">
    <button type="button" data-d="approved">Approve</button>
    <button type="button" data-d="changes">Needs changes</button>
    <button type="button" data-d="rejected">Reject</button>
  </div>
  <label class="note-label" for="note-{item_id}">Note (optional)</label>
  <textarea id="note-{item_id}" rows="2" placeholder="What should change, or why?"></textarea>
  <p class="saved" aria-live="polite"></p>
</div>'''


def rec_block(item_id, rec, open_q):
    applied = open_q.startswith("Resolved")
    changes = []
    for c in rec.get("add_criteria", []):
        changes.append(f"<li>Adds the check: {e(c)}</li>")
    for old, new in rec.get("replace_criteria", []):
        changes.append(f"<li>Changes the check to: {e(new)}</li>")
    changes.append(f"<li>Closes the question as: {e(rec['resolution'])}</li>")
    if applied:
        action = '<p class="applied">Accepted and applied to the story file.</p>'
    else:
        action = f'<button type="button" class="accept" data-accept="{item_id}" aria-pressed="false">Accept recommendation</button>'
    return f'''<div class="question{' resolved' if applied else ''}" data-rec="{item_id}" data-rec-applied="{int(applied)}">
  <span class="kicker">{'Question resolved' if applied else 'Open question'}</span>
  <p>{e(open_q)}</p>
  <div class="rec"><span class="kicker">Our recommendation</span><p>{e(rec['recommendation'])}</p><p class="rec-why">{e(rec['why'])}</p>
  <p class="rec-if">If you accept, the story file changes like this:</p><ul>{''.join(changes)}</ul>{action}</div>
</div>'''


def story_card(path):
    text = path.read_text()
    f = specs.front(text)
    s = specs.sections(text)
    sid, title, status = f["id"], f["title"], f["status"]
    scene = SCENES["stories"][sid]
    story = " ".join(l.strip() for l in s["Story"].splitlines())
    acs = "".join(f"<li>{e(c)}</li>" for c in specs.criteria(text))
    open_q = s["Open questions"]
    has_q = open_q != "None."
    if sid in RECS and has_q:
        q = rec_block(sid, RECS[sid], open_q)
    elif has_q:
        q = f'<div class="question"><span class="kicker">Open question</span><p>{e(open_q)}</p></div>'
    else:
        q = ""
    pending_q = int(has_q and not open_q.startswith("Resolved"))
    return f'''<article class="card" id="{sid}" data-kind="story" data-q="{pending_q}" data-repo="{e(status)}">
<header class="card-head"><span class="id">{sid}</span><h3>{e(title)}</h3><span class="pill repo {e(status)}">In repo: {US_STATUS.get(status, e(status))}</span><span class="state" data-state-for="{sid}">Not reviewed</span></header>
<div class="scene"><span class="kicker">Priya's moment</span><p>{e(scene['moment'])}</p></div>
<div class="pair">
  <div class="analogy"><span class="kicker">Think of it like</span><p>{e(scene['analogy'])}</p></div>
  <div class="why"><span class="kicker">Why it's needed</span><p>{e(s['Why this matters'])}</p></div>
</div>
<p class="formal">{e(story)}</p>
<details><summary>How we'll know it works ({len(specs.criteria(text))} checks)</summary><ul class="checks">{acs}</ul>
<p class="oos"><strong>Not included:</strong> {e(s['Out of scope'])}</p></details>
{q}
<p class="related">Related decisions: {ref_links(specs.related(text))}</p>
{review_bar(sid, None)}
</article>'''


def adr_card(path):
    text = path.read_text()
    f = specs.front(text)
    s = specs.sections(text)
    aid, title, status = f["id"], f["title"], f["status"]
    scene = SCENES["adrs"][aid]
    opts = re.findall(r"^\*\*[A-D] — (.+?)\*\*( \(chosen\))?", s["Options considered"], flags=re.M)
    chosen = next((n for n, c in opts if c), opts[0][0])
    others = "".join(f"<li>{e(n)}</li>" for n, c in opts if n != chosen)
    cons = s["Consequences"]
    good = "".join(f"<li>{e(x)}</li>" for x in specs.bullets(cons.split("**Neutral**")[0]))
    bad = "".join(f"<li>{e(x)}</li>" for x in specs.bullets(cons.split("**Bad / accepted limitations**")[1]))
    rel = specs.related(text)
    if status == "proposed":
        label, rec = "Needs your decision", "Approve. Option A is the best fit for a one-student, zero-cost project; what you give up is listed under “You accept”."
    elif status == "accepted":
        label, rec = "Decided", "Approve, unless you want to change a choice the team has already made."
    else:
        label, rec = "Rejected", "Leave rejected unless the reason for rejecting it has changed."
    return f'''<article class="card adr" id="{aid}" data-kind="adr" data-status="{e(status)}" data-repo="{e(status)}">
<header class="card-head"><span class="id">{aid}</span><h3>{e(title)}</h3><span class="pill repo {e(status)}">In repo: {ADR_STATUS.get(status, e(status))}</span><span class="state" data-state-for="{aid}">Not reviewed</span></header>
<div class="scene"><span class="kicker">In plain words</span><p>{e(scene['plain'])}</p></div>
<div class="pair">
  <div class="analogy"><span class="kicker">Think of it like</span><p>{e(scene['analogy'])}</p></div>
  <div class="why"><span class="kicker">If you approve</span><p>{e(scene['means'])}</p></div>
</div>
<div class="tradeoff">
  <div><span class="kicker good">You gain</span><ul>{good}</ul></div>
  <div><span class="kicker bad">You accept</span><ul>{bad}</ul></div>
</div>
<p class="adr-rec"><span class="kicker">Our recommendation ({label})</span>{e(rec)}</p>
<details><summary>Full reasoning</summary>
<p><strong>Why decide now:</strong> {e(s['Context'])}</p>
<p><strong>Chosen:</strong> {e(chosen)}. <strong>Also considered:</strong></p><ul>{others}</ul>
<p><strong>Why not the others:</strong> {e(s['Rejected alternatives'])}</p>
<p><strong>When to rethink:</strong> {e(s['Revisit triggers'])}</p>
<p><strong>How we keep to it:</strong> {e(s['How this is enforced'])}</p></details>
<p class="related">Stories it supports: {ref_links([r for r in rel if r.startswith('US')])} · Related decisions: {ref_links([r for r in rel if r.startswith('ADR')])}</p>
{review_bar(aid, None)}
</article>'''


def summary(n_q, n_prop):
    q = f"{n_q} {'story still has' if n_q == 1 else 'stories still have'} an open question"
    p = f"{n_prop} {'decision is' if n_prop == 1 else 'decisions are'} still proposed"
    return f"{q} and {p}. Those need the most attention." if n_q or n_prop else "Every story and decision has been reviewed and has no open questions."


def build():
    us_files = {p.name[:6]: p for p in specs.all_files("US")}
    adr_files = {p.name[:7]: p for p in specs.all_files("ADR")}
    placed = set()

    def area(a, card_fn, files, scene_no=None):
        ids = [i for i in a["ids"] if i in files]
        placed.update(ids)
        cards = "\n".join(card_fn(files[i]) for i in ids)
        num = f'<span class="scene-no">Scene {scene_no}</span>' if scene_no else ""
        return f'<section class="area" id="area-{a["key"]}"><div class="area-head">{num}<h2>{e(a["name"])}</h2><p>{e(a["intro"])}</p></div>{cards}</section>'

    us_html = "".join(area(a, story_card, us_files, n + 1) for n, a in enumerate(SCENES["story_areas"]))
    adr_html = "".join(area(a, adr_card, adr_files) for a in SCENES["adr_areas"])
    missing = sorted((set(us_files) | set(adr_files)) - placed)
    if missing:
        raise SystemExit(f"Add these to scenes.json first: {', '.join(missing)}")

    texts = [p.read_text() for p in us_files.values()]
    n_q = sum(1 for t in texts if specs.sections(t)["Open questions"] not in ("None.",) and not specs.sections(t)["Open questions"].startswith("Resolved"))
    n_prop = sum(1 for p in adr_files.values() if specs.front(p.read_text())["status"] == "proposed")
    nav = lambda areas: "".join(f'<li><a href="#area-{a["key"]}">{e(a["name"])}</a></li>' for a in areas)
    page = (HERE / "template.html").read_text()
    for k, v in {
        "{{NAV_US}}": nav(SCENES["story_areas"]), "{{NAV_ADR}}": nav(SCENES["adr_areas"]),
        "{{US_SECTIONS}}": us_html, "{{ADR_SECTIONS}}": adr_html,
        "{{N_US}}": str(len(us_files)), "{{N_ADR}}": str(len(adr_files)),
        "{{SUMMARY}}": summary(n_q, n_prop), "{{N_ALL}}": str(len(us_files) + len(adr_files)),
    }.items():
        page = page.replace(k, v)
    return page


def main():
    page = build()
    standalone = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
                  "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
                  f"<!-- Generated by docs/storyboard/build.py. Live review copy: {ARTIFACT_URL} . Opened locally, the page is read-only. -->\n"
                  "</head>\n<body>\n" + page + "\n</body>\n</html>\n")
    (specs.DOCS / "storyboard.html").write_text(standalone)
    if "--artifact" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--artifact") + 1]).write_text(page)
    print("storyboard built")


if __name__ == "__main__":
    main()
