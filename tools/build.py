#!/usr/bin/env python3
"""Bundle everything in data/ into assets/js/data.js.

The site must open straight from index.html (file://), where fetch() of JSON
is blocked, so all data is shipped as one JS file that sets window.DATA.
Run:  .venv/bin/python tools/build.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "assets" / "js" / "data.js"


def load(name, default):
    p = DATA / name
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def main():
    sections = load("sections.json", [])
    problems = load("problems.json", [])
    papers = load("papers.json", [])
    resources = load("resources.json", [])
    plan = load("plan.json", [])
    stats = load("stats.json", {})
    cheatsheet = (DATA / "cheatsheet.html").read_text(encoding="utf-8") if (DATA / "cheatsheet.html").exists() else ""

    notes = {}
    ndir = DATA / "notes"
    if ndir.exists():
        for f in sorted(ndir.glob("*.html")):
            notes[f.stem.replace("-", ".")] = f.read_text(encoding="utf-8")
    slides = load("slides.json", {})
    lessons = {}
    ldir = DATA / "lessons"
    if ldir.exists():
        for f in sorted(ldir.glob("*.html")):
            sec = f.stem.replace("-", ".")
            lessons[sec] = f.read_text(encoding="utf-8")

    # --- validation -------------------------------------------------------
    sec_ids = {s["id"] for s in sections}
    errors = []
    seen = set()
    for p in problems:
        if p["id"] in seen:
            errors.append(f"duplicate problem id {p['id']}")
        seen.add(p["id"])
        if p.get("section") not in sec_ids and not p.get("out_of_scope"):
            errors.append(f"{p['id']}: section {p.get('section')} not in course list")
        if p.get("origin") == "generated" and not p.get("verified"):
            errors.append(f"{p['id']}: generated problem is not verified")
    pids = {p["id"] for p in problems}
    for pa in papers:
        for q in pa.get("problems", []):
            if q not in pids:
                errors.append(f"paper {pa['id']}: unknown problem {q}")
    if errors:
        print("\n".join(errors))
        sys.exit(1)

    bundle = {
        "sections": sections,
        "problems": problems,
        "papers": papers,
        "resources": resources,
        "plan": plan,
        "stats": stats,
        "lessons": lessons,
        "notes": notes,
        "slides": slides,
        "cheatsheet": cheatsheet,
    }
    import re, time
    idx = ROOT / "index.html"
    idx.write_text(re.sub(r"\?v=\d+", "?v=%d" % int(time.time()), idx.read_text(encoding="utf-8")), encoding="utf-8")
    OUT.write_text("window.DATA = " + json.dumps(bundle, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"ok: {len(sections)} sections, {len(problems)} problems, {len(papers)} papers, "
          f"{len(lessons)} lessons, {len(resources)} resources -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
