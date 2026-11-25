#!/usr/bin/env python3
"""Run every problem source in data/src/, verify answers with SymPy, write
data/problems.json, data/papers.json and data/stats.json.

    .venv/bin/python tools/make_problems.py
"""
import importlib.util
import json
import pathlib
import signal
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import pkit  # noqa: E402

# Same problem in several papers: duplicate -> canonical
DUPS = {
    "f20f-5a": "f17f-5b",
    "rev-5-2": "f25t3a-8",
    "rev-5-4a": "f25t3a-4",
}
TYPES = {
    "Increase/decrease & concavity": ["Reading f′ graph", "Concavity", "Increase/decrease", "Inflection points", "Curve analysis", "Increase/decrease, concavity, inflection"],
    "Relative extrema & curve sketching": ["First derivative test", "Curve sketching", "Second derivative test"],
    "Absolute extrema": ["Absolute extrema"],
    "Optimization": ["Optimization"],
    "Rectilinear motion (derivatives)": ["Rectilinear motion"],
    "Mean Value Theorem / Rolle": ["Mean Value Theorem", "MVT hypotheses", "Rolle"],
    "MVT inequality proofs": ["MVT inequality"],
    "Antiderivatives & IVPs": ["Antiderivatives", "Initial value problem"],
    "u-substitution (indefinite)": ["u-substitution"],
    "Riemann sums & sigma notation": ["Limit of a Riemann sum", "Riemann sum", "Area as a limit", "Definite integral as a limit", "Sigma"],
    "Definite integral: properties & geometry": ["Properties of definite integrals", "Integrals with absolute value", "Piecewise definite integral", "Integral as area"],
    "FTC: evaluating definite integrals": ["Area under a curve (FTC)", "FTC: evaluate"],
    "FTC: derivative of an integral": ["FTC: derivative", "FTC: both limits", "FTC: find f"],
    "Motion via integrals": ["Position from acceleration", "Displacement vs distance", "Constant acceleration", "Average velocity", "Motion via integrals"],
    "Average value": ["Average value"],
    "Definite u-substitution": ["Definite u-substitution", "Definite integrals (substitution", "Substitution (recognize", "Substitution in definite"],
    "Functions defined by integrals": ["Functions defined by integrals", "ln as an integral"],
    "Integration by parts": ["Integration by parts", "Substitution + integration by parts"],
    "Trig integrals": ["Trig integrals"],
}


def canon_topic(t):
    if t in TYPES:
        return t
    for name, prefixes in TYPES.items():
        if any(t.startswith(pf) for pf in prefixes):
            return name
    return None


ACHENEF = {"f25-t2a", "f25-t2b", "f25-t3a", "f25-t3b", "rev-f26"}


class Timeout(Exception):
    pass


def _alarm(*_):
    raise Timeout()


def run_check(fn, secs=60):
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(secs)
    try:
        return bool(fn()), None
    except Timeout:
        return False, "timeout"
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"
    finally:
        signal.alarm(0)


def main():
    only = set(sys.argv[1:])
    for f in sorted((ROOT / "data" / "src").glob("*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

    probs, papers = pkit.PROBLEMS, pkit.PAPERS
    by_id = {p["id"]: p for p in probs}
    for p in probs:
        if not p["out_of_scope"]:
            c = canon_topic(p["topic"])
            if c is None:
                print("WARNING: no type for topic", repr(p["topic"]), p["id"])
            elif c != p["topic"]:
                p["subtopic"], p["topic"] = p["topic"], c
    fails, dropped = [], []
    out = []
    for p in probs:
        fn = p.pop("_check")
        if fn is None:
            p["verified"] = None
        elif only and p["id"] not in only and p["origin"] == "past":
            p["verified"] = None
        else:
            ok, err = run_check(fn)
            p["verified"] = ok
            if not ok:
                fails.append((p["id"], err))
        if p["origin"] == "generated" and not p["verified"]:
            dropped.append(p["id"])
            continue
        out.append(p)

    for dup, canon in DUPS.items():
        if dup in by_id and canon in by_id:
            by_id[dup]["duplicate_of"] = canon
            by_id[canon].setdefault("also_in", []).append(by_id[dup]["paper"])

    # ---------------- stats over in-scope past problems (duplicates merged)
    sec_c, top_c, sec_ach, top_sec = Counter(), Counter(), Counter(), defaultdict(set)
    for p in out:
        if p["origin"] != "past" or p["out_of_scope"] or p.get("duplicate_of") or p["paper"] == "deck-nu":
            continue
        occ = 1 + len(p.get("also_in", []))
        sec_c[p["section"]] += occ
        top_c[p["topic"]] += occ
        top_sec[p["topic"]].add(p["section"])
        if p["paper"] in ACHENEF or any(a in ACHENEF for a in p.get("also_in", [])):
            sec_ach[p["section"]] += occ
    oos = Counter(p["section"] for p in out if p["origin"] == "past" and p["out_of_scope"] and p["paper"] != "deck-nu")
    stats = dict(by_section=dict(sec_c.most_common()), by_topic=dict(top_c.most_common()),
                 by_section_achenef=dict(sec_ach.most_common()),
                 topic_sections={k: sorted(v) for k, v in top_sec.items()},
                 out_of_scope_by_section=dict(oos.most_common()))

    order = ["rev-f26", "deck-nu", "f25-t3a", "f25-t3b", "f25-t2a", "f25-t2b", "f22-e3", "f24-m3", "f24-m2", "f20-m3"]
    papers.sort(key=lambda pa: (not pa.get("split", True), pa.get("kind") == "homework", order.index(pa["id"]) if pa["id"] in order else 99, -pa["year"]))
    (ROOT / "data" / "problems.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    (ROOT / "data" / "papers.json").write_text(json.dumps(papers, ensure_ascii=False, indent=1))
    (ROOT / "data" / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1))

    past = [p for p in out if p["origin"] == "past"]
    print(f"papers: {len(papers)}  past problems: {len(past)} (in scope {sum(not p['out_of_scope'] for p in past)})  "
          f"generated: {sum(p['origin'] == 'generated' for p in out)}")
    print(f"verified: {sum(p['verified'] is True for p in out)}  failed: {len(fails)}  no check: {sum(p['verified'] is None for p in out)}")
    for pid, err in fails:
        print("  FAIL", pid, err or "")
    if dropped:
        print("dropped generated (failed check):", ", ".join(dropped))


if __name__ == "__main__":
    main()
