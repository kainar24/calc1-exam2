"""Helpers for writing problem sources in data/src/*.py.

Every problem is a dict made by P(...). `check` is a zero-argument callable that
returns True when SymPy confirms the answer (run by tools/make_problems.py).
"""
import sympy as sp

x, t, u, y, k, n, w, theta = sp.symbols('x t u y k n w theta', real=True)

PROBLEMS = []
PAPERS = []

IN_SCOPE = {"4.1", "4.2", "4.4", "4.5", "4.6", "4.8", "5.1", "5.2", "5.3", "5.4", "5.5",
            "5.6", "5.7", "5.8", "5.9", "5.10", "7.2", "7.3"}


def paper(id, title, short, kind, year, term, files, has_solutions, instructor=None,
          duration_min=None, notes=None, split=True):
    PAPERS.append(dict(id=id, title=title, short=short, kind=kind, year=year, term=term,
                       files=[{"path": f[0], "label": f[1]} for f in files],
                       has_solutions=has_solutions, instructor=instructor,
                       duration_min=duration_min, notes=notes, split=split, problems=[]))


def P(id, paper, number, section, topic, statement, answer=None, steps=(), check=None,
      diff="exam", src="official", points=None, note=None, mc=False, figure=None,
      page=None, tags=(), unverified=None, solution_note=None):
    oos = section not in IN_SCOPE
    d = dict(id=id, origin="past", paper=paper, number=str(number), section=section,
             topic=topic, difficulty=diff, statement=statement.strip(), answer=answer,
             steps=list(steps), solution_source=src if (answer or steps) else None,
             out_of_scope=oos, points=points, tags=list(tags) + (["originally multiple choice"] if mc else []),
             figure=figure, source_image=page, note=note, solution_note=solution_note,
             unverified_note=unverified)
    d["_check"] = check
    PROBLEMS.append(d)
    for pa in PAPERS:
        if pa["id"] == paper:
            pa["problems"].append(id)
    return d


def G(id, section, topic, statement, answer, steps, check, diff="exam", figure=None, tags=(),
      family=None):
    """Generated problem (must pass `check`, otherwise it is dropped)."""
    d = dict(id=id, origin="generated", paper=None, number=None, section=section, topic=topic,
             difficulty=diff, statement=statement.strip(), answer=answer, steps=list(steps),
             solution_source="own", out_of_scope=False, points=None, tags=list(tags),
             figure=figure, source_image=None, family=family)
    d["_check"] = check
    PROBLEMS.append(d)
    return d


# ---------------- SymPy check helpers ----------------
def same(a, b, tol=1e-9):
    a, b = sp.sympify(a), sp.sympify(b)
    try:
        if sp.simplify(a - b) == 0:
            return True
    except Exception:
        pass
    try:
        return abs(complex(sp.N(a - b, 30))) < tol
    except Exception:
        return False


def antideriv(F, f, var=x, pts=(0.3, 0.7, 1.1, 1.9, 2.6)):
    """F' == f (symbolically or at sample points)."""
    dF = sp.diff(F, var)
    try:
        if sp.simplify(dF - f) == 0:
            return True
    except Exception:
        pass
    for p in pts:
        try:
            if abs(complex(sp.N((dF - f).subs(var, p), 30))) > 1e-8:
                return False
        except Exception:
            return False
    return True


def defint(f, a, b, value, var=x):
    """Exact integral equals value, and a numeric quadrature agrees."""
    exact = sp.integrate(f, (var, a, b))
    num = sp.Integral(f, (var, a, b)).evalf(30)
    return same(exact, value) and abs(complex(num - sp.N(value, 30))) < 1e-8


def numint(f, a, b, value, var=x):
    """High-precision quadrature (mpmath), split at the kinks of any |g(x)| inside (a, b)."""
    import mpmath
    mpmath.mp.dps = 30
    fa, fb = float(sp.N(a)), float(sp.N(b))
    lo, hi = min(fa, fb), max(fa, fb)
    cuts = set()
    for ab in f.atoms(sp.Abs):
        try:
            for r in sp.solve(ab.args[0], var):
                if r.is_real and lo < float(r) < hi:
                    cuts.add(float(r))
        except Exception:
            pass
    pts = [lo] + sorted(cuts) + [hi]
    g = sp.lambdify(var, f, "mpmath")
    num = mpmath.quad(g, pts)
    if fa > fb:
        num = -num
    return abs(complex(num) - complex(sp.N(value, 30))) < 1e-8


def crit(f, var=x):
    return sorted(sp.solve(sp.diff(f, var), var), key=lambda r: float(r))


def all_true(*xs):
    return all(bool(v) for v in xs)
