# "MATH161 Chapters 4, 5, 7 — Typical MATH 161 Midterm Preparation Problems" (@math161nu, Telegram).
# 101 slides, ~100 problems as pictures, no solutions. Every problem is transcribed here in slide order.
# Problems that already exist on the site (copied from past papers) reuse that problem's verified
# statement/answer/steps/check; the rest are solved here and checked with SymPy.
from pkit import *

DECK = "materials/telegram/MATH161_All_Sections/MATH161 Chapters 4,5,7.pptx"
paper("deck-nu", "Prep deck “Chapters 4, 5, 7” · @math161nu (101 slides)", "Prep deck", "deck", 2026, "Fall",
      [(DECK, "PowerPoint (101 slides, no solutions)")], False, None, None,
      "The student channel's midterm prep deck, all ~100 problems in slide order. About 60 of them are copied from past papers "
      "(marked “also in …”, same solution as there); the other ~40 are new and solved here. Slides with Ch. 6 areas and "
      "§4.3 rational-function sketching are marked out of scope but still solved.")
S = "deck-nu"
img = lambda n: f"assets/deck/s{n:03d}.png"
_by_id = {p["id"]: p for p in PROBLEMS}
_short = {pa["id"]: pa["short"] for pa in PAPERS}


def DUP(slide, canon, part="", note=None, **over):
    """Deck problem that already exists on the site: copy the verified version."""
    c = _by_id[canon]
    kw = dict(answer=c["answer"], steps=c["steps"], check=c["_check"], diff=c["difficulty"],
              src=c["solution_source"] or "own", figure=c["figure"], tags=[t for t in c["tags"]])
    kw.update(over)
    statement = over.pop("statement", None) or c["statement"]
    kw.pop("statement", None)
    lab = f"{_short.get(c['paper'], c['paper'])} #{c['number']}"
    d = P(f"deck-{slide}{part}", S, f"{slide}{part}", over.get("section", c["section"]), over.get("topic", c["topic"]),
          statement, page=img(slide), note=(note + " " if note else "") + f"Also in {lab}.",
          **{k: v for k, v in kw.items() if k not in ("section", "topic")})
    d["same_as"] = canon
    return d


def N(slide, section, topic, statement, answer, steps=(), check=None, part="", **kw):
    return P(f"deck-{slide}{part}", S, f"{slide}{part}", section, topic, statement, answer, steps,
             check=check, page=img(slide), src="own", **kw)


# =====================================================================  Function analysis (4.1, 4.2)
N(4, "4.3", "Asymptotes", r"Find the vertical, horizontal and oblique asymptotes of the function $2y(x+1)^2=x^3$.",
  r"Vertical $x=-1$; no horizontal; oblique $y=\dfrac x2-1$",
  [r"Solve for $y$: $y=\dfrac{x^3}{2(x+1)^2}$.",
   r"Vertical: the denominator is $0$ at $x=-1$ and the numerator is $-1\ne0$ there, so $x=-1$ is a vertical asymptote.",
   r"Horizontal: degree of numerator (3) > degree of denominator (2), so $y\to\pm\infty$: no horizontal asymptote.",
   r"Oblique: divide $x^3$ by $2(x^2+2x+1)$: $x^3=(x-2)(x^2+2x+1)+(3x+2)$, so $y=\dfrac{x-2}2+\dfrac{3x+2}{2(x+1)^2}$.",
   r"The last fraction $\to0$ as $x\to\pm\infty$, so the oblique asymptote is $y=\dfrac x2-1$."],
  check=lambda: (lambda f: all_true(same(sp.limit(f - (x/2 - 1), x, sp.oo), 0), sp.limit(f, x, -1, '+') == -sp.oo))(x**3/(2*(x+1)**2)), points=14)
N(5, "4.2", "First derivative test (critical points)", r"Find all critical points of the function $f(x)=|x^3-3x|$.",
  r"$x=-\sqrt3,\,-1,\,0,\,1,\,\sqrt3$",
  [r"Critical points = where $f'(x)=0$ <b>or</b> $f'$ does not exist (inside the domain).",
   r"Let $g(x)=x^3-3x=x(x^2-3)$. Where $g\ne0$, $f=\pm g$, so $f'=\pm g'=\pm(3x^2-3)$, which is $0$ at $x=\pm1$ (and $g(\pm1)=\mp2\ne0$).",
   r"Where $g=0$: $x=0,\pm\sqrt3$. There $g'\ne0$ ($g'(0)=-3$, $g'(\pm\sqrt3)=6$), so the graph of $|g|$ has a corner: $f'$ does not exist.",
   r"Critical points: $x=-\sqrt3,\,-1,\,0,\,1,\,\sqrt3$."],
  check=lambda: all_true(sorted(sp.solve(3*x**2 - 3, x)) == [-1, 1], sorted(sp.solve(x**3 - 3*x, x), key=float) == [-sp.sqrt(3), 0, sp.sqrt(3)]))
N(6, "4.2", "Second derivative test (find a, b)", r"What values of $a$ and $b$ make $f(x)=x^3+ax^2+bx$ have a local maximum at $x=-1$ and a local minimum at $x=3$?",
  r"$a=-3,\ b=-9$",
  [r"$f'(x)=3x^2+2ax+b$. Local extrema of a polynomial need $f'=0$: $f'(-1)=3-2a+b=0$ and $f'(3)=27+6a+b=0$.",
   r"Subtract: $24+8a=0\Rightarrow a=-3$; then $b=2a-3=-9$.",
   r"Check with the second derivative: $f''(x)=6x-6$; $f''(-1)=-12<0$ (max ✓), $f''(3)=12>0$ (min ✓)."],
  check=lambda: (lambda f: all_true(sp.diff(f, x).subs(x, -1) == 0, sp.diff(f, x).subs(x, 3) == 0, sp.diff(f, x, 2).subs(x, -1) < 0, sp.diff(f, x, 2).subs(x, 3) > 0))(x**3 - 3*x**2 - 9*x),
  points=16)
DUP(7, "f24m2-6", statement=r"If $f(x)=\dfrac{\ln x}{x}$ for all $x>0$, which is true? (a) $f$ increasing for all $x>0$; (b) increasing for all $x>1$; (c) decreasing for all $0<x<1$; (d) decreasing for all $1<x<e$; (e) decreasing for all $x>e$.",
    answer=r"(e): increasing on $(0,e]$, decreasing on $[e,\infty)$", mc=True, diff="easy")
N(8, "4.1", "Inflection points", r"Find the inflection points and the intervals of concave up and concave down of $y=e^{\sin x}$, $-\tfrac\pi2\le x\le\tfrac\pi2$.",
  r"Let $x_0=\arcsin\dfrac{\sqrt5-1}2\approx0.666$. Concave up on $\left(-\tfrac\pi2,x_0\right)$, concave down on $\left(x_0,\tfrac\pi2\right)$; inflection point $\left(x_0,\ e^{(\sqrt5-1)/2}\right)\approx(0.666,\,1.855)$",
  [r"$y'=\cos x\,e^{\sin x}$.",
   r"$y''=-\sin x\,e^{\sin x}+\cos^2x\,e^{\sin x}=e^{\sin x}\left(1-\sin^2x-\sin x\right)$.",
   r"$e^{\sin x}>0$, so the sign of $y''$ is the sign of $1-s-s^2$ with $s=\sin x\in[-1,1]$.",
   r"$s^2+s-1=0\Rightarrow s=\dfrac{-1+\sqrt5}2\approx0.618$ (the other root $<-1$). So $1-s-s^2>0$ for $s<0.618$ and $<0$ for $s>0.618$.",
   r"$\sin x$ is increasing on $[-\pi/2,\pi/2]$: $y''>0$ for $x<x_0$, $y''<0$ for $x>x_0$, with $x_0=\arcsin\frac{\sqrt5-1}2$.",
   r"Concave up on $(-\pi/2,x_0)$, concave down on $(x_0,\pi/2)$; inflection point at $x_0$, $y=e^{\sin x_0}=e^{(\sqrt5-1)/2}$."],
  check=lambda: (lambda f, x0: all_true(abs(sp.N(sp.diff(f, x, 2).subs(x, x0))) < 1e-12, sp.diff(f, x, 2).subs(x, 0.3) > 0, sp.diff(f, x, 2).subs(x, 1.0) < 0))(sp.exp(sp.sin(x)), sp.asin((sp.sqrt(5)-1)/2)),
  points=14)
DUP(9, "f24m2-1", answer=r"(b) $\left(-\infty,\tfrac43\right)$", mc=True)
DUP(10, "f24m2-7", answer=r"(a) $2$ (at $x=\pm\frac\pi2$)", mc=True)
N(11, "4.1", "Increase/decrease, concavity, inflection", r"""Which statements are true about $f(x)=\tfrac13x^3+\tfrac12x^2-2x$?
I. $f$ is increasing on $(-2,1)$. II. $f$ is concave up on $\left(-\tfrac12,\infty\right)$. III. $f$ has one inflection point.
(A) II and III only (B) I only (C) I, II, III (D) II only (E) I and II only""",
  r"(A) II and III only",
  [r"$f'(x)=x^2+x-2=(x+2)(x-1)$: negative on $(-2,1)$, so $f$ is <b>decreasing</b> there. I is false.",
   r"$f''(x)=2x+1>0\iff x>-\tfrac12$: concave up on $(-\tfrac12,\infty)$. II is true.",
   r"$f''$ changes sign only at $x=-\tfrac12$: exactly one inflection point. III is true. Answer (A)."],
  check=lambda: (lambda f: all_true(sp.solve_univariate_inequality(sp.diff(f, x) < 0, x, relational=False) == sp.Interval.open(-2, 1),
                                    sp.solve(sp.diff(f, x, 2), x) == [sp.Rational(-1, 2)]))(x**3/3 + x**2/2 - 2*x),
  mc=True, diff="easy")
N(12, "4.1", "Inflection points", r"Suppose $f''(x)=e^{-x}(x^2-4x+3)$ and $f'(1)=0$. At $x=1$, $f$ has (A) a relative maximum (B) a relative minimum (C) an inflection point (D) none of these (E) impossible.",
  r"(C) an inflection point",
  [r"$f''(x)=e^{-x}(x-1)(x-3)$, so $f''(1)=0$ and the second derivative test gives no answer.",
   r"Sign of $f''$ near $1$: positive for $x<1$ (both factors negative), negative for $1<x<3$. Concavity changes at $x=1$ ⇒ inflection point.",
   r"Is it also an extremum? $f''>0$ before $1$ means $f'$ increases up to $f'(1)=0$, so $f'<0$ just left of 1; $f''<0$ after $1$ means $f'$ decreases from $0$, so $f'<0$ just right of 1. $f'$ does not change sign ⇒ no extremum.",
   r"Answer (C): an inflection point (with a horizontal tangent)."],
  check=lambda: (lambda g: all_true(g.subs(x, 1) == 0, g.subs(x, sp.Rational(1, 2)) > 0, g.subs(x, 2) < 0))(sp.exp(-x)*(x**2 - 4*x + 3)),
  mc=True)
DUP(13, "f25t2a-5", part="a", answer=r"(A) $[-2,\infty)$", mc=True)
DUP(13, "f25t2a-6", part="b", answer=r"(B) $(-1,1)$", mc=True)

# =====================================================================  Absolute extrema (4.4)
DUP(14, "f17m2-4a")
DUP(15, "f17f-4b")
DUP(16, "f22e3-1b")
N(17, "4.4", "Absolute extrema", r"Find the absolute maxima and minima of $f(x)=\dfrac{\ln(2x)}{x}$ on $[1,e]$.",
  r"Max $f\!\left(\tfrac e2\right)=\dfrac2e\approx0.736$; min $f(e)=\dfrac{1+\ln2}e\approx0.623$",
  [r"$f'(x)=\dfrac{\frac1x\cdot x-\ln(2x)}{x^2}=\dfrac{1-\ln(2x)}{x^2}$.",
   r"$f'=0\iff\ln(2x)=1\iff x=\dfrac e2\approx1.36\in[1,e]$. No points where $f'$ fails to exist in $[1,e]$.",
   r"Values: $f(1)=\ln2\approx0.693$; $f(e/2)=\dfrac{\ln e}{e/2}=\dfrac2e\approx0.736$; $f(e)=\dfrac{\ln(2e)}e=\dfrac{1+\ln2}e\approx0.623$.",
   r"Absolute max $\dfrac2e$ at $x=\dfrac e2$; absolute min $\dfrac{1+\ln2}e$ at $x=e$."],
  check=lambda: (lambda f: all_true(crit(f) == [sp.E/2], same(f.subs(x, sp.E/2), 2/sp.E), sp.N(f.subs(x, sp.E)) < sp.N(f.subs(x, 1)) < sp.N(f.subs(x, sp.E/2))))(sp.log(2*x)/x),
  points=14)
N(18, "4.4", "Absolute extrema", r"Suppose $f(x)=\sqrt3\sin x+\cos x$. If $M$ is the absolute maximum of $f$ on $[0,\pi]$ and $m$ the absolute minimum, find $M+m$. (A) 2 (B) 3 (C) 0 (D) $\sqrt3-1$ (E) 1",
  r"(E) $1$  ($M=2$ at $x=\frac\pi3$, $m=-1$ at $x=\pi$)",
  [r"$f'(x)=\sqrt3\cos x-\sin x=0\iff\tan x=\sqrt3\iff x=\dfrac\pi3$ in $[0,\pi]$.",
   r"Values: $f(0)=1$; $f(\pi/3)=\sqrt3\cdot\frac{\sqrt3}2+\frac12=2$; $f(\pi)=0-1=-1$.",
   r"$M=2$, $m=-1$, so $M+m=1$. (Shortcut: $f=2\sin(x+\pi/6)$.)"],
  check=lambda: (lambda f: all_true(same(f.subs(x, sp.pi/3), 2), same(f.subs(x, sp.pi), -1), crit(f) and same(sp.tan(sp.pi/3), sp.sqrt(3))))(sp.sqrt(3)*sp.sin(x) + sp.cos(x)),
  mc=True, diff="easy")
N(19, "4.4", "Absolute extrema (theory)", r"""Consider $f(x)=\begin{cases}x^2,&0\le x<1\\0,&1\le x\le2\end{cases}$. Which is true?
(a) $f$ attains an absolute maximum value of 1 (b) $f$ attains an absolute minimum value of 0 (c) $f$ attains an absolute maximum value of 1 somewhere on $[0,2]$ (d) $f$ does not attain an absolute minimum (e) both (a) and (c)""",
  r"(b)",
  [r"$f$ is <b>not continuous</b> at $x=1$ (it jumps from values near 1 down to 0), so the Extreme Value Theorem does not apply.",
   r"Values of $f$: $x^2\in[0,1)$ on $[0,1)$ and $0$ on $[1,2]$. The values get as close to 1 as we like, but $1$ is never reached ⇒ no absolute max. So (a), (c), (e) are false.",
   r"The smallest value $0$ is attained (at $x=0$ and on $[1,2]$) ⇒ absolute min $0$. Answer (b)."],
  mc=True, diff="easy")
N(20, "4.4", "Absolute extrema (theory)", r"""Which statements are true?
I. A function on a closed bounded interval must achieve an absolute min and max.
II. Every absolute extremum is also a relative extremum.
III. Endpoints of closed bounded intervals could be the location of absolute extrema.
(a) I (b) II (c) III (d) II and III (e) I, II and III""",
  r"(c) III only",
  [r"I is false: the Extreme Value Theorem needs $f$ to be <b>continuous</b> on $[a,b]$ (see the jump function of slide 19).",
   r"II is false: an absolute extremum at an endpoint is not a relative extremum (Anton defines relative extrema on open intervals around the point). Example: $f(x)=x$ on $[0,1]$.",
   r"III is true: e.g. $f(x)=x$ on $[0,1]$ has its max and min at the endpoints. Answer (c)."],
  mc=True, diff="easy")

# =====================================================================  Optimization (4.5)
DUP(21, "f18m2-3")
DUP(22, "f18f-4b")
DUP(23, "f20m3-1")
N(24, "4.5", "Optimization", r"The boundary of a field is a right triangle with a straight stream along its hypotenuse and fences along its other two sides. Find the dimensions of the field with maximum area that can be enclosed using 1000 ft of fence.",
  r"Both legs $500$ ft (hypotenuse $500\sqrt2$ ft), maximal area $125\,000$ ft²",
  [r"Legs $x$ and $y$ (the fenced sides): $x+y=1000\Rightarrow y=1000-x$, $0<x<1000$.",
   r"Area $A(x)=\tfrac12x(1000-x)=500x-\tfrac12x^2$.",
   r"$A'(x)=500-x=0\Rightarrow x=500$; $A''=-1<0$ ⇒ maximum (the only critical point, and $A\to0$ at both ends ⇒ absolute).",
   r"Legs $500$ ft and $500$ ft, hypotenuse $500\sqrt2\approx707$ ft along the stream, area $\tfrac12\cdot500^2=125000$ ft²."],
  check=lambda: (lambda A: all_true(crit(A) == [500], same(A.subs(x, 500), 125000)))(x*(1000 - x)/2), points=10, tags=["bonus"])
DUP(25, "f25t2a-10")

# =====================================================================  Rolle / MVT (4.8)
N(26, "4.8", "Rolle's theorem", r"Find the value $c$ such that the conclusion of Rolle's Theorem is satisfied for $f(x)=2x^2-8$ on $[-2,2]$.",
  r"$c=0$",
  [r"Hypotheses: $f$ is a polynomial (continuous on $[-2,2]$, differentiable on $(-2,2)$) and $f(-2)=0=f(2)$ ✓.",
   r"$f'(c)=4c=0\Rightarrow c=0\in(-2,2)$."],
  check=lambda: all_true((2*x**2 - 8).subs(x, -2) == (2*x**2 - 8).subs(x, 2), sp.solve(4*x, x) == [0]), diff="easy")
N(27, "5.8", "Average value (MVT for integrals)", r"Find all values of $x^*$ in $[0,4]$ that satisfy the Mean-Value Theorem for Integrals, where $f(x)=x-4$.",
  r"$x^*=2$",
  [r"MVT for integrals: $f(x^*)=f_{\text{ave}}=\dfrac1{b-a}\displaystyle\int_a^bf(x)\,dx$.",
   r"$\displaystyle\int_0^4(x-4)\,dx=\left[\frac{x^2}2-4x\right]_0^4=8-16=-8$, so $f_{\text{ave}}=\dfrac{-8}4=-2$.",
   r"$x^*-4=-2\Rightarrow x^*=2\in[0,4]$."],
  check=lambda: same(sp.solve(sp.Eq(x - 4, sp.integrate(x - 4, (x, 0, 4))/4), x)[0], 2), diff="easy")
DUP(28, "f25t2a-3", answer=r"(A) $c=1$", mc=True)
DUP(29, "f24m2-2", answer=r"(b) $f$ is not differentiable on $(1,4)$ (corner at $x=3$)", mc=True)
DUP(30, "f24m2-10")
N(31, "4.8", "Mean Value Theorem", r"""If $f$ is differentiable on $(-\infty,\infty)$, $f(2)=4$, $f(6)=8$, which statements must be true?
I. $\exists c\in(2,6)$ with $f(c)=6$. II. $\exists c\in(2,6)$ with $f'(c)=6$. III. $\exists c\in(2,6)$ with $f'(c)=1$.
(A) Only I and II (B) Only I and III (C) Only II and III (D) Only II (E) Only I""",
  r"(B) Only I and III",
  [r"Differentiable ⇒ continuous. I: $6$ lies between $f(2)=4$ and $f(6)=8$, so by the Intermediate Value Theorem some $c\in(2,6)$ has $f(c)=6$. True.",
   r"III: by the MVT some $c\in(2,6)$ has $f'(c)=\dfrac{f(6)-f(2)}{6-2}=\dfrac44=1$. True.",
   r"II: nothing forces a slope of 6 (e.g. $f(x)=x+2$ has $f'\equiv1$). Not necessarily true. Answer (B)."],
  check=lambda: same(sp.Rational(8 - 4, 6 - 2), 1), mc=True, diff="easy")
DUP(32, "f17m2-5")
DUP(33, "f20m3-3")

# =====================================================================  Graph sketching (4.2 / 4.3)
DUP(34, "f17m2-4b", answer=r"$f(x)=x^2-2x-\dfrac8{x+2}$: VA $x=-2$, curvilinear asymptote $y=x^2-2x$; rel min $(-3,23)$; stationary inflection point $(0,-4)$; CU on $(-\infty,-2)$ and $(0,\infty)$, CD on $(-2,0)$",
    steps=[r"Divide: $x^3-4x-8=(x+2)(x^2-2x)-8$, so $f(x)=x^2-2x-\dfrac8{x+2}$, $x\ne-2$.",
           r"Asymptotes: at $x=-2$ the numerator is $-8\ne0$ ⇒ vertical asymptote $x=-2$ ($f\to+\infty$ as $x\to-2^-$, $-\infty$ as $x\to-2^+$). As $x\to\pm\infty$, $\frac8{x+2}\to0$ ⇒ the graph approaches the parabola $y=x^2-2x$ (curvilinear asymptote).",
           r"$f'(x)=2x-2+\dfrac8{(x+2)^2}=\dfrac{2(x-1)(x+2)^2+8}{(x+2)^2}=\dfrac{2x^2(x+3)}{(x+2)^2}$.",
           r"$f'=0$ at $x=-3$ and $x=0$. $f'<0$ for $x<-3$, $f'>0$ on $(-3,-2)$ and $(-2,\infty)$ (zero at $0$ without sign change). Rel min $f(-3)=\dfrac{-27+12-8}{-1}=23$; $x=0$ is not an extremum.",
           r"$f''(x)=2-\dfrac{16}{(x+2)^3}$. $f''=0\iff(x+2)^3=8\iff x=0$. $f''>0$ for $x<-2$ and $x>0$, $f''<0$ on $(-2,0)$ ⇒ inflection point $(0,f(0))=(0,-4)$.",
           r"Intercepts: $y$-intercept $-4$; one $x$-intercept (root of $x^3-4x-8$) at $x\approx2.65$. Sketch: parabola-like on the far left and right, plunging along $x=-2$."],
    check=lambda: (lambda f: all_true(sp.simplify(sp.diff(f, x) - 2*x**2*(x+3)/(x+2)**2) == 0, f.subs(x, -3) == 23, f.subs(x, 0) == -4,
                                      sp.solve(sp.diff(f, x, 2), x) == [0] or 0 in sp.solve(sp.diff(f, x, 2), x)))((x**3 - 4*x - 8)/(x + 2)))
DUP(35, "f17f-4a")
DUP(36, "f18m2-4", answer=r"$f(x)=\dfrac x2+1+\dfrac2x$: VA $x=0$, oblique $y=\dfrac x2+1$; rel max $(-2,-1)$, rel min $(2,3)$; CD on $(-\infty,0)$, CU on $(0,\infty)$; no inflection points, no $x$-intercepts",
    steps=[r"$f(x)=\dfrac{x^2+2x+4}{2x}=\dfrac x2+1+\dfrac2x$, domain $x\ne0$.",
           r"Asymptotes: vertical $x=0$; as $x\to\pm\infty$, $\frac2x\to0$ ⇒ oblique asymptote $y=\frac x2+1$.",
           r"$f'(x)=\dfrac12-\dfrac2{x^2}=\dfrac{x^2-4}{2x^2}$: zero at $x=\pm2$. Increasing on $(-\infty,-2)$ and $(2,\infty)$, decreasing on $(-2,0)$ and $(0,2)$.",
           r"Rel max $f(-2)=-1+1-1=-1$; rel min $f(2)=1+1+1=3$.",
           r"$f''(x)=\dfrac4{x^3}$: CD for $x<0$, CU for $x>0$; the sign changes only across the asymptote ⇒ no inflection point.",
           r"No $x$-intercepts ($x^2+2x+4$ has discriminant $-12<0$), no $y$-intercept."],
    check=lambda: (lambda f: all_true(crit(f) == [-2, 2], f.subs(x, -2) == -1, f.subs(x, 2) == 3, same(sp.limit(f - x/2 - 1, x, sp.oo), 0)))((x**2 + 2*x + 4)/(2*x)))
DUP(37, "f18f-4a")
DUP(38, "f20m2-5", answer=r"$f'=\dfrac{5-3x}{3(1+x)^{1/3}(3-x)^{2/3}}$: rel min $(-1,0)$ (cusp), rel max $\left(\tfrac53,\tfrac43\sqrt[3]4\right)\approx(1.67,2.12)$; ↘ on $(-\infty,-1]$, ↗ on $[-1,\tfrac53]$, ↘ on $[\tfrac53,\infty)$; CD on $(-\infty,-1)$, $(-1,3)$, CU on $(3,\infty)$; inflection point $(3,0)$ (vertical tangent); oblique asymptote $y=-x+\tfrac13$",
    steps=[r"Product rule: $f'(x)=\tfrac23(1+x)^{-1/3}(3-x)^{1/3}-\tfrac13(1+x)^{2/3}(3-x)^{-2/3}=\dfrac{2(3-x)-(1+x)}{3(1+x)^{1/3}(3-x)^{2/3}}=\dfrac{5-3x}{3(1+x)^{1/3}(3-x)^{2/3}}$.",
           r"Critical points: $f'=0$ at $x=\frac53$; $f'$ undefined at $x=-1$ (cusp) and $x=3$ (vertical tangent).",
           r"Signs ($(3-x)^{2/3}\ge0$ always): $x<-1$: numerator $+$, $(1+x)^{1/3}<0$ ⇒ $f'<0$; $-1<x<\frac53$: $f'>0$; $x>\frac53$: $f'<0$ (also past 3).",
           r"Rel min $f(-1)=0$; rel max $f(\tfrac53)=(\tfrac83)^{2/3}(\tfrac43)^{1/3}=\tfrac43\sqrt[3]4\approx2.12$. At $x=3$ $f'$ keeps its sign ⇒ no extremum.",
           r"$f''(x)=-\dfrac{32}{9(1+x)^{4/3}(3-x)^{5/3}}$: $(1+x)^{4/3}>0$; $(3-x)^{5/3}>0$ for $x<3$ ⇒ CD on $(-\infty,-1)$ and $(-1,3)$; for $x>3$ it is negative ⇒ CU. Inflection point $(3,0)$.",
           r"For large $|x|$: $f(x)=-x\,(1+\tfrac1x)^{2/3}(1-\tfrac3x)^{1/3}\approx-x\left(1+\tfrac2{3x}-\tfrac1x\right)=-x+\tfrac13$ ⇒ oblique asymptote $y=-x+\tfrac13$. No vertical/horizontal asymptotes.",
           r"Intercepts: $x=-1$, $x=3$; $y$-intercept $f(0)=\sqrt[3]3\approx1.44$."],
    check=lambda: (lambda f: all_true(abs(sp.N(sp.diff(f, x).subs(x, sp.Rational(5, 3)))) < 1e-12,
                                      same(f.subs(x, sp.Rational(5, 3)), sp.Rational(4, 3)*sp.cbrt(4)),
                                      abs(sp.N(((1 + 10**6)**2)**sp.Rational(1, 3)*(-(10**6 - 3)**sp.Rational(1, 3)) + 10**6 - sp.Rational(1, 3))) < 1e-4))((1 + x)**sp.Rational(2, 3)*(3 - x)**sp.Rational(1, 3)))
DUP(39, "f20f-4", answer=r"$f=\dfrac{x^2+x-7}{3x^2+x-1}$ for $x\ne\frac12$ (hole at $(\frac12,-25)$); VA $x=\frac{-1\pm\sqrt{13}}6$; HA $y=\frac13$; rel min at $x=10-\sqrt{103}\approx-0.149$ ($y\approx6.70$), rel max at $x=10+\sqrt{103}\approx20.15$ ($y\approx0.3349$)",
    steps=[r"$x=\frac12$ is a root of the numerator: $2x^3+x^2-15x+7=(2x-1)(x^2+x-7)$. Cancel: $f(x)=\dfrac{x^2+x-7}{3x^2+x-1}$, $x\ne\frac12$.",
           r"No vertical asymptote at $x=\frac12$: the factor cancels, $\lim_{x\to1/2}f=\dfrac{\frac14+\frac12-7}{\frac34+\frac12-1}=-25$ is finite ⇒ a hole at $(\frac12,-25)$.",
           r"Vertical asymptotes: $3x^2+x-1=0\Rightarrow x=\dfrac{-1\pm\sqrt{13}}6\approx0.434,\ -0.768$. Horizontal: ratio of leading coefficients $y=\frac13$.",
           r"$f'(x)=\dfrac{(2x+1)(3x^2+x-1)-(x^2+x-7)(6x+1)}{(3x^2+x-1)^2}=\dfrac{-2x^2+40x+6}{(3x^2+x-1)^2}=\dfrac{-2(x^2-20x-3)}{(3x^2+x-1)^2}$.",
           r"$f'=0\iff x=10\pm\sqrt{103}$. $f'>0$ between them, $f'<0$ outside (skipping the asymptotes and the hole).",
           r"Decreasing on $(-\infty,-0.768)$ and $(-0.768,\,10-\sqrt{103})$; increasing on $(10-\sqrt{103},\,0.434)$, $(0.434,\frac12)$, $(\frac12,\,10+\sqrt{103})$; decreasing after $10+\sqrt{103}$.",
           r"Rel min at $x=10-\sqrt{103}\approx-0.149$, $f\approx6.70$; rel max at $x=10+\sqrt{103}\approx20.15$, $f\approx0.3349$ (just above the asymptote $y=\frac13$)."],
    check=lambda: (lambda f: all_true(sp.simplify(f - (x**2 + x - 7)/(3*x**2 + x - 1)) == 0,
                                      sp.simplify(sp.numer(sp.together(sp.diff((x**2 + x - 7)/(3*x**2 + x - 1), x))) + 2*(x**2 - 20*x - 3)) == 0,
                                      same(sp.limit(f, x, sp.Rational(1, 2)), -25)))((2*x**3 + x**2 - 15*x + 7)/((2*x - 1)*(3*x**2 + x - 1))))
N(40, "4.3", "Curve sketching", r"""Given $y=\dfrac{x^3+x-2}{x-x^2}$: (a) identify the symmetries and the intercepts; (b) relative extrema; (c) concavity, inflection points;
(d) asymptotes (vertical, horizontal and oblique); (e) sketch the graph.""",
  r"$y=-x-1-\dfrac2x$ ($x\ne0,1$; hole at $(1,-4)$). (a) no symmetry, no intercepts; (b) rel max $(\sqrt2,-1-2\sqrt2)$, rel min $(-\sqrt2,2\sqrt2-1)$; (c) CU on $(-\infty,0)$, CD on $(0,\infty)$, no inflection points; (d) VA $x=0$, oblique $y=-x-1$, no horizontal",
  [r"Factor: $x^3+x-2=(x-1)(x^2+x+2)$ and $x-x^2=-x(x-1)$. For $x\ne1$: $y=-\dfrac{x^2+x+2}x=-x-1-\dfrac2x$. At $x=1$ there is a hole: $y\to-4$.",
   r"(a) $y(-x)\ne\pm y(x)$ (the $-1$ term) ⇒ no symmetry. $x=0$ is not in the domain ⇒ no $y$-intercept; $x^2+x+2=0$ has no real roots ⇒ no $x$-intercepts.",
   r"(b) $y'=-1+\dfrac2{x^2}=0\iff x=\pm\sqrt2$. $y''=-\dfrac4{x^3}$: $y''(\sqrt2)<0$ ⇒ rel max $y(\sqrt2)=-1-2\sqrt2\approx-3.83$; $y''(-\sqrt2)>0$ ⇒ rel min $y(-\sqrt2)=2\sqrt2-1\approx1.83$.",
   r"(c) $y''=-4/x^3>0$ for $x<0$ (CU), $<0$ for $x>0$ (CD). The sign changes only across $x=0$, which is not in the domain ⇒ no inflection points.",
   r"(d) $x=0$: $y\to\mp\infty$ ⇒ vertical asymptote ($x=1$ is only a hole). $y-(-x-1)=-\frac2x\to0$ ⇒ oblique asymptote $y=-x-1$; no horizontal asymptote.",
   r"(e) Two branches: left branch above the line $y=-x-1$ with low point $(-\sqrt2,1.83)$; right branch below it with high point $(\sqrt2,-3.83)$ and an open circle at $(1,-4)$."],
  check=lambda: (lambda f: all_true(sp.simplify(f - (-x - 1 - 2/x)) == 0, same(sp.limit(f, x, 1), -4), crit(-x - 1 - 2/x) == [-sp.sqrt(2), sp.sqrt(2)],
                                    same((-x - 1 - 2/x).subs(x, sp.sqrt(2)), -1 - 2*sp.sqrt(2))))((x**3 + x - 2)/(x - x**2)),
  points=26)
N(41, "4.3", "Curve sketching", r"""Given $y=\dfrac{x^3}{3-x^2}$: (a) identify symmetries and intercepts; (b) relative extrema; (c) concavity and inflection points;
(d) asymptotes (vertical, horizontal, oblique); (e) sketch the graph.""",
  r"(a) odd (symmetric about the origin), only intercept $(0,0)$; (b) rel min $(-3,\tfrac92)$, rel max $(3,-\tfrac92)$; (c) CU on $(-\infty,-\sqrt3)$, $(0,\sqrt3)$; CD on $(-\sqrt3,0)$, $(\sqrt3,\infty)$; inflection point $(0,0)$; (d) VA $x=\pm\sqrt3$, oblique $y=-x$",
  [r"(a) $y(-x)=-y(x)$ ⇒ odd, symmetric about the origin. $y=0\iff x=0$: the only intercept is $(0,0)$.",
   r"(b) $y'=\dfrac{3x^2(3-x^2)+2x\cdot x^3}{(3-x^2)^2}=\dfrac{x^2(9-x^2)}{(3-x^2)^2}$. Zeros $x=0,\pm3$. $y'<0$ for $|x|>3$, $y'\ge0$ for $|x|<3$ ($x\ne\pm\sqrt3$).",
   r"So $x=-3$: ↘ then ↗ ⇒ rel min $y(-3)=\frac{-27}{-6}=\frac92$; $x=3$: rel max $y(3)=-\frac92$; $x=0$: no sign change ⇒ not an extremum.",
   r"(c) $y''=\dfrac{6x(x^2+9)}{(3-x^2)^3}$. Signs: $x<-\sqrt3$: $+$ (CU); $-\sqrt3<x<0$: $-$ (CD); $0<x<\sqrt3$: $+$ (CU); $x>\sqrt3$: $-$ (CD). Inflection point at $(0,0)$ only.",
   r"(d) $3-x^2=0\Rightarrow$ vertical asymptotes $x=\pm\sqrt3$. Division: $\dfrac{x^3}{3-x^2}=-x+\dfrac{3x}{3-x^2}$ ⇒ oblique asymptote $y=-x$; no horizontal asymptote.",
   r"(e) Three branches. Left ($x<-\sqrt3$): comes down along $y=-x$, low point $(-3,4.5)$, then up to $+\infty$ as $x\to-\sqrt3^-$. Middle: rises from $-\infty$ (at $x\to-\sqrt3^+$) through the inflection point $(0,0)$ (flat there, $y'(0)=0$) to $+\infty$ (at $x\to\sqrt3^-$). Right: the mirror image of the left branch through the origin, high point $(3,-4.5)$."],
  check=lambda: (lambda f: all_true(sp.simplify(sp.diff(f, x) - x**2*(9 - x**2)/(3 - x**2)**2) == 0,
                                    sp.simplify(sp.diff(f, x, 2) - 6*x*(x**2 + 9)/(3 - x**2)**3) == 0,
                                    f.subs(x, -3) == sp.Rational(9, 2), same(sp.limit(f + x, x, sp.oo), 0)))(x**3/(3 - x**2)),
  points=26)

# =====================================================================  Sigma notation & Riemann sums (5.4, 5.5)
DUP(42, "f24m3-5", answer=r"(E) $\displaystyle\int_1^3(x^2+1)\,dx$", mc=True)
DUP(43, "f25t3b-3", answer=r"(B) $\dfrac12$", mc=True)
N(44, "5.5", "Limit of a Riemann sum", r"""Which gives the exact area under $f(x)=\ln x$ on $[1,7]$ (right endpoints)?
(A) $\lim\sum_{i=1}^n\frac6n\ln\left(\frac6ni\right)$ (B) $\lim\sum\frac7n\ln\left(1+\frac6ni\right)$ (C) $\lim\sum\frac7n\ln\left(\frac7ni\right)$ (D) $\lim\sum\frac7n\ln\left(\frac6ni\right)$ (E) $\lim\sum\frac6n\ln\left(1+\frac6ni\right)$""",
  r"(E) $\displaystyle\lim_{n\to\infty}\sum_{i=1}^n\frac6n\ln\left(1+\frac6ni\right)$",
  [r"$\Delta x=\dfrac{7-1}n=\dfrac6n$ (not $\frac7n$!).",
   r"Right endpoints: $x_i=a+i\Delta x=1+\dfrac{6i}n$.",
   r"Area $=\displaystyle\lim_{n\to\infty}\sum_{i=1}^nf(x_i)\Delta x=\lim_{n\to\infty}\sum_{i=1}^n\frac6n\ln\left(1+\frac{6i}n\right)$ ⇒ (E). (Value: $\int_1^7\ln x\,dx=7\ln7-6$.)"],
  check=lambda: abs(sp.N(sum(sp.Rational(6, 2000)*sp.log(1 + sp.Rational(6*i, 2000)) for i in range(1, 2001)) - (7*sp.log(7) - 6))) < 0.01,
  mc=True, diff="easy")
DUP(45, "f24m3-4", answer=r"(E) $\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac2n\sqrt{1+\frac{2k}n}$", mc=True)
N(46, "5.4", "Riemann sum (numeric)", r"Find the value of the left endpoint Riemann sum for $y=x^2$ on $[0,2]$ partitioned into 4 pieces. (A) $\frac72$ (B) $\frac{11}2$ (C) $\frac{13}4$ (D) $\frac74$ (E) $\frac54$",
  r"(D) $\dfrac74$",
  [r"$\Delta x=\dfrac{2-0}4=\dfrac12$. Left endpoints: $0,\ \tfrac12,\ 1,\ \tfrac32$.",
   r"$L_4=\tfrac12\left(0^2+\left(\tfrac12\right)^2+1^2+\left(\tfrac32\right)^2\right)=\tfrac12\left(0+\tfrac14+1+\tfrac94\right)=\tfrac12\cdot\tfrac72=\tfrac74$."],
  check=lambda: same(sum(sp.Rational(1, 2)*(sp.Rational(i, 2))**2 for i in range(4)), sp.Rational(7, 4)), mc=True, diff="easy")
N(47, "5.4", "Riemann sum (numeric)", r"Use a Riemann sum with two rectangles and right endpoints to estimate the area under $f(x)=3^x$ from $x=0$ to $x=2$. (A) 4 (B) 6 (C) 8 (D) 10 (E) 12",
  r"(E) $12$",
  [r"$\Delta x=\dfrac{2-0}2=1$; right endpoints $x=1,\,2$.",
   r"$R_2=1\cdot(3^1+3^2)=3+9=12$."],
  check=lambda: 3**1 + 3**2 == 12, mc=True, diff="easy")
DUP(48, "f20m3-5")

# =====================================================================  FTC (5.6)
N(49, "5.6", "FTC: evaluate", r"Use the Fundamental Theorem of Calculus to compute $\displaystyle\int_{\ln6}^47e^x\,dx$.", r"$7e^4-42$",
  [r"An antiderivative of $7e^x$ is $7e^x$.", r"$\displaystyle\int_{\ln6}^47e^x\,dx=7e^4-7e^{\ln6}=7e^4-42\approx340.2$."],
  check=lambda: defint(7*sp.exp(x), sp.log(6), 4, 7*sp.exp(4) - 42), part="a", diff="easy")
N(49, "5.6", "FTC: both limits", r"Use the Fundamental Theorem of Calculus to compute $\dfrac{d}{dx}\displaystyle\int_x^{x^2}3e^t\,dt$.", r"$6xe^{x^2}-3e^x$",
  [r"$\dfrac{d}{dx}\displaystyle\int_{g(x)}^{h(x)}f(t)\,dt=f(h(x))h'(x)-f(g(x))g'(x)$.",
   r"$=3e^{x^2}\cdot2x-3e^x\cdot1=6xe^{x^2}-3e^x$."],
  check=lambda: same(sp.diff(sp.integrate(3*sp.exp(t), (t, x, x**2)), x), 6*x*sp.exp(x**2) - 3*sp.exp(x)), part="b", diff="easy")
DUP(50, "f24m3-12", answer=r"(E) $6$", mc=True)
DUP(51, "f25t3b-5", answer=r"(B) $\cos x\sqrt{1+\sin^2x}$", mc=True)
DUP(52, "f20f-5b")
DUP(53, "f18f-5d")
DUP(54, "f17f-5d")
N(55, "5.6", "FTC: derivative", r"""Find $\dfrac{d}{dt}\displaystyle\int_0^{\sin t}\frac{du}{25-u^2}$. (A) $\frac1{25-\sin^2t}$ (B) $\frac{\cos t}{25-\sin^2t}$ (C) $\frac1{\cos t(25-\sin^2t)}$ (D) $\frac{-\cos t}{25-\sin^2t}$ (E) $\frac{\sin t}{25-\cos^2t}$""",
  r"(B) $\dfrac{\cos t}{25-\sin^2t}$",
  [r"FTC part 2 + chain rule: $\dfrac{d}{dt}\displaystyle\int_0^{g(t)}f(u)\,du=f(g(t))\,g'(t)$.",
   r"$f(u)=\dfrac1{25-u^2}$, $g(t)=\sin t$, $g'(t)=\cos t$ ⇒ $\dfrac{\cos t}{25-\sin^2t}$."],
  check=lambda: same(sp.diff(sp.Integral(1/(25 - u**2), (u, 0, sp.sin(t))).doit(), t), sp.cos(t)/(25 - sp.sin(t)**2)), mc=True, diff="easy",
  note="The slide shows only the integral and the choices; the question is the derivative with respect to $t$.")
N(56, "5.6", "FTC: derivative (graph)", r"""Below is the graph of $f(t)$ (see the slide: $f(0)=4$, the curve crosses the axis at $t=2$). Let $g(x)=\displaystyle\int_0^xf(t)\,dt$. Determine $g(0)$, $g'(0)$ and $g'(2)$.
(A) $1,0,1$ (B) $0,0,1$ (C) $0,0,0$ (D) $0,4,0$ (E) $1,4,1$""",
  r"(D) $g(0)=0$, $g'(0)=4$, $g'(2)=0$",
  [r"$g(0)=\displaystyle\int_0^0f(t)\,dt=0$ (equal limits).",
   r"FTC: $g'(x)=f(x)$. From the graph $f(0)=4$ and $f(2)=0$.",
   r"So $g'(0)=4$, $g'(2)=0$ ⇒ (D)."], mc=True, diff="easy")

# =====================================================================  Properties of the definite integral (5.5)
N(57, "5.5", "Properties of definite integrals", r"Given $\int_5^1f(x)\,dx=3$, $\int_1^3g(x)\,dx=1$ and $\int_3^5g(x)\,dx=2$, find $\displaystyle\int_5^1\big(f(x)-g(x)\big)\,dx$.",
  r"$6$",
  [r"$\int_5^1(f-g)=\int_5^1f-\int_5^1g$.",
   r"$\int_1^5g=\int_1^3g+\int_3^5g=1+2=3$, so $\int_5^1g=-3$.",
   r"$\int_5^1(f-g)=3-(-3)=6$. (Watch the order of the limits: $\int_5^1f$ is given directly, while the $g$-integrals go from 1 to 5 and must be flipped.)"],
  check=lambda: 3 - (-(1 + 2)) == 6, diff="easy")
DUP(58, "f24m3-1", answer=r"(D) $20$", mc=True)
N(59, "5.5", "Properties of definite integrals", r"Suppose $g$ is continuous, $\int_4^7g(x)\,dx=10$ and $\int_4^{10}g(x)\,dx=13$. Find $\int_7^{10}g(x)\,dx$. (A) 23 (B) $-23$ (C) 3 (D) $-3$ (E) cannot be determined",
  r"(C) $3$",
  [r"Additivity: $\int_4^{10}g=\int_4^7g+\int_7^{10}g$.", r"$13=10+\int_7^{10}g\Rightarrow\int_7^{10}g=3$."],
  check=lambda: 13 - 10 == 3, mc=True, diff="easy")
DUP(60, "f25t3b-1", answer=r"(A) $0$", mc=True)
N(61, "5.5", "Integral as area", r"The value of $\int_{-4}^4\sqrt{16-x^2}\,dx$ is $8\pi$ (area of a half-circle of radius 4). Use this to compute $\displaystyle\int_{-4}^4\left(-\pi+3\sqrt{16-x^2}\right)dx$. (A) 0 (B) $24\pi-8$ (C) $8-24\pi$ (D) $8\pi$ (E) $16\pi$",
  r"(E) $16\pi$",
  [r"Linearity: $\displaystyle\int_{-4}^4(-\pi)\,dx+3\int_{-4}^4\sqrt{16-x^2}\,dx$.",
   r"$\int_{-4}^4(-\pi)\,dx=-\pi\cdot8=-8\pi$; $\ 3\cdot8\pi=24\pi$.", r"Total: $-8\pi+24\pi=16\pi$."],
  check=lambda: defint(-sp.pi + 3*sp.sqrt(16 - x**2), -4, 4, 16*sp.pi), mc=True, diff="easy")
DUP(62, "f24m3-18", answer=r"(B) $f(2a-x)=f(x)$", mc=True)
DUP(63, "f17f-5a")
N(64, "5.5", "Integrals with absolute value", r"Evaluate $\displaystyle\int_{-1}^1\left(|x|+2\right)dx$.", r"$5$",
  [r"$\displaystyle\int_{-1}^1|x|\,dx=2\int_0^1x\,dx=1$ (two triangles of area $\tfrac12$).",
   r"$\displaystyle\int_{-1}^12\,dx=4$.", r"Total $1+4=5$."],
  check=lambda: numint(sp.Abs(x) + 2, -1, 1, 5), diff="easy")
DUP(65, "f24m3-2")

# =====================================================================  Antiderivatives & substitution (5.2, 5.3, 5.9)
DUP(66, "f24m3-10", answer=r"(A) $2\csc(2x)+c$  $\left(=\tan x+\cot x+c\right)$", mc=True)
DUP(67, "f25t3b-6", answer=r"(D) $\sec x+x+C$", mc=True)
DUP(68, "f18f-5a")
N(69, "5.2", "Antiderivatives", r"Evaluate $\displaystyle\int\frac{1+2x^2}{x^2(1+x^2)}\,dx$.", r"$-\dfrac1x+\arctan x+C$",
  [r"Split the numerator: $1+2x^2=(1+x^2)+x^2$.",
   r"$\dfrac{(1+x^2)+x^2}{x^2(1+x^2)}=\dfrac1{x^2}+\dfrac1{1+x^2}$.",
   r"$\displaystyle\int\left(x^{-2}+\frac1{1+x^2}\right)dx=-\frac1x+\arctan x+C$."],
  check=lambda: antideriv(-1/x + sp.atan(x), (1 + 2*x**2)/(x**2*(1 + x**2))), part="a", points=8)
DUP(69, "f24m2-15b", part="b")
DUP(70, "f22e3-3a", part="a")
N(70, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_0^{\pi/4}\sin(2x)\sqrt{1-\cos^2(2x)}\,dx$.", r"$\dfrac\pi8$",
  [r"$u=\cos2x$, $du=-2\sin2x\,dx$ ⇒ $\sin2x\,dx=-\tfrac12du$. Limits: $x=0\to u=1$; $x=\pi/4\to u=\cos\frac\pi2=0$.",
   r"$\displaystyle\int_1^0\sqrt{1-u^2}\left(-\tfrac12\right)du=\frac12\int_0^1\sqrt{1-u^2}\,du$.",
   r"$\int_0^1\sqrt{1-u^2}\,du$ is a quarter of the unit disk: $\dfrac\pi4$. Answer $\dfrac12\cdot\dfrac\pi4=\dfrac\pi8$.",
   r"(Alternative: $\sqrt{1-\cos^22x}=|\sin2x|=\sin2x$ on $[0,\pi/4]$, and $\int_0^{\pi/4}\sin^22x\,dx=\frac\pi8$.)"],
  check=lambda: numint(sp.sin(2*x)*sp.sqrt(1 - sp.cos(2*x)**2), 0, sp.pi/4, sp.pi/8), part="b")
DUP(71, "f25t3b-4", answer=r"(E) $\dfrac13\arctan\left(\dfrac{x^4}3\right)+C$", mc=True)
N(72, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_1^e\frac{(\ln x)^3}{x}\,dx$. (A) $\frac13$ (B) $\frac e4$ (C) $e$ (D) $e^2$ (E) $\frac14$",
  r"(E) $\dfrac14$",
  [r"$u=\ln x$, $du=\dfrac{dx}x$; $x=1\to u=0$, $x=e\to u=1$.", r"$\displaystyle\int_0^1u^3\,du=\left[\frac{u^4}4\right]_0^1=\frac14$."],
  check=lambda: defint(sp.log(x)**3/x, 1, sp.E, sp.Rational(1, 4)), mc=True, diff="easy")
N(73, "5.3", "u-substitution", r"Compute $\displaystyle\int\left(\sin^2x+\sin x+1\right)\cos x\,dx$.",
  r"(B) $\dfrac{\sin^3x}3+\dfrac{\sin^2x}2+\sin x+C$",
  [r"$u=\sin x$, $du=\cos x\,dx$.", r"$\displaystyle\int(u^2+u+1)\,du=\frac{u^3}3+\frac{u^2}2+u+C=\frac{\sin^3x}3+\frac{\sin^2x}2+\sin x+C$."],
  check=lambda: antideriv(sp.sin(x)**3/3 + sp.sin(x)**2/2 + sp.sin(x), (sp.sin(x)**2 + sp.sin(x) + 1)*sp.cos(x)), mc=True, diff="easy")
DUP(74, "f24m3-17", answer=r"(B) $\displaystyle\int_{-1}^1\frac{d\theta}{\sqrt{1-\theta^2}}$ $(=\pi)$", mc=True)
DUP(75, "f24m3-15", answer=r"(D) $\dfrac{e-1}{2(3-e)}$", mc=True)
DUP(76, "f17f-5c")
DUP(77, "f18f-5c")
DUP(78, "f20m3-4")

# =====================================================================  Integration by parts & trig integrals (7.2, 7.3)
DUP(79, "f24m3-16", answer=r"(C) $\dfrac{e^{x^2}}2\left(x^4-2x^2+2\right)+c$", mc=True)
DUP(80, "f24m3-8", answer=r"(A) $\dfrac\pi4-\dfrac12$", mc=True)
DUP(81, "f24m3-7", answer=r"(B) $-2\pi$", mc=True)
DUP(82, "f24m3-9")
N(83, "7.3", "Trig integrals (odd power of sin)", r"$\displaystyle\int\cos^6x\sin x\,dx=$ ? (A) $\frac{\cos^7x}7+C$ (B) $-\frac{\cos^6x}6+C$ (C) $-\frac{\sin^7x}7+C$ (D) $-\frac{\tan^7x}7+C$ (E) $-\frac{\cos^7x}7+C$",
  r"(E) $-\dfrac{\cos^7x}7+C$",
  [r"$u=\cos x$, $du=-\sin x\,dx$.", r"$\displaystyle\int u^6(-du)=-\frac{u^7}7+C=-\frac{\cos^7x}7+C$."],
  check=lambda: antideriv(-sp.cos(x)**7/7, sp.cos(x)**6*sp.sin(x)), mc=True, diff="easy")

# =====================================================================  Average value (5.8)
DUP(84, "f24m3-3", answer=r"(A) $\dfrac{e^{12}-1}{12}$", mc=True)
N(85, "5.8", "Average value", r"Determine the average value of $f(x)=x^2+x+1$ on $[0,3]$. (A) 11 (B) $\frac{33}2$ (C) $\frac{22}3$ (D) $\frac{11}2$ (E) 22",
  r"(D) $\dfrac{11}2$",
  [r"$f_{\text{ave}}=\dfrac1{3-0}\displaystyle\int_0^3(x^2+x+1)\,dx$.",
   r"$\displaystyle\int_0^3(x^2+x+1)\,dx=\left[\frac{x^3}3+\frac{x^2}2+x\right]_0^3=9+\frac92+3=\frac{33}2$.",
   r"$f_{\text{ave}}=\dfrac13\cdot\dfrac{33}2=\dfrac{11}2$."],
  check=lambda: same(sp.integrate(x**2 + x + 1, (x, 0, 3))/3, sp.Rational(11, 2)), mc=True, diff="easy")
DUP(86, "f25t3b-7", points=12)

# =====================================================================  Areas (Ch. 6 — not on Exam 2) and net area (5.5, 5.6)
DUP(87, "f17f-6", steps=[
    r"The region between $y=x^2$ and $y=9$ is $-3\le x\le3$; its area is $2\displaystyle\int_0^3(9-x^2)\,dx=2(27-9)=36$.",
    r"The part below the line $y=k$ ($0<k<9$): $2\displaystyle\int_0^{\sqrt k}(k-x^2)\,dx=2\left(k\sqrt k-\frac{k\sqrt k}3\right)=\frac43k^{3/2}$.",
    r"Half of the area: $\dfrac43k^{3/2}=18\Rightarrow k^{3/2}=\dfrac{27}2\Rightarrow k=\left(\dfrac{27}2\right)^{2/3}=\dfrac9{\sqrt[3]4}\approx5.67$."],
    check=lambda: same(sp.Rational(4, 3)*(9/sp.cbrt(4))**sp.Rational(3, 2), 18))
DUP(88, "f18f-6", steps=[
    r"Both curves are even, so find the area for $x\ge0$ and double it. Intersection: $\dfrac2{1+x^2}=x\Rightarrow x^3+x-2=0\Rightarrow(x-1)(x^2+x+2)=0\Rightarrow x=1$.",
    r"On $[0,1]$ the top curve is $\dfrac2{1+x^2}$ (at $x=0$: $2>0$).",
    r"$A=2\displaystyle\int_0^1\left(\frac2{1+x^2}-x\right)dx=2\left[2\arctan x-\frac{x^2}2\right]_0^1=2\left(\frac\pi2-\frac12\right)=\pi-1$."],
    check=lambda: defint(2/(1 + x**2) - x, 0, 1, (sp.pi - 1)/2))
N(89, "6.1", "Area between curves", r"Find the area of the region bounded by $y=x$ and $y=x^2$.", r"$\dfrac16$",
  [r"Intersections: $x=x^2\Rightarrow x=0,1$. On $(0,1)$, $x>x^2$.", r"$A=\displaystyle\int_0^1(x-x^2)\,dx=\frac12-\frac13=\frac16$."],
  check=lambda: defint(x - x**2, 0, 1, sp.Rational(1, 6)), diff="easy")
N(90, "6.1", "Area between curves", r"Find the area of the region enclosed by $y=4x-x^2$ and $y=3$.", r"$\dfrac43$",
  [r"Intersections: $4x-x^2=3\Rightarrow x^2-4x+3=0\Rightarrow x=1,3$. Between them the parabola is on top (at $x=2$: $4>3$).",
   r"$A=\displaystyle\int_1^3(4x-x^2-3)\,dx=\left[2x^2-\frac{x^3}3-3x\right]_1^3=0-\left(-\frac43\right)=\frac43$."],
  check=lambda: defint(4*x - x**2 - 3, 1, 3, sp.Rational(4, 3)), diff="easy")
DUP(91, "f24m3-6", answer=r"(C) $\dfrac{e^4}2-\dfrac12$", mc=True)
N(92, "5.5", "Integral as area", r"Below is the graph of $f(x)$ (see the slide): the region between $a$ and $b$ lies above the $x$-axis with area $24$, the region between $b$ and $c$ lies below it with area $7$. Evaluate $\int_a^cf(x)\,dx$. (A) 31 (B) 24 (C) $-7$ (D) 15 (E) 17",
  r"(E) $17$",
  [r"The definite integral is the <b>net signed area</b>: area above the axis counts $+$, below counts $-$.",
   r"$\int_a^cf=\int_a^bf+\int_b^cf=24+(-7)=17$. (31 would be the total area, not the integral.)"],
  check=lambda: 24 - 7 == 17, mc=True, diff="easy")
DUP(93, "f25t3b-9", steps=[
    r"Sketch: $y=\sqrt x$ starts at the origin; the line $y=x-2$ crosses the $x$-axis at $x=2$. They meet where $\sqrt x=x-2$ ⇒ $x=(x-2)^2$, $x^2-5x+4=0$, $x=4$ ($x=1$ fails: $1\ne-1$). Point $(4,2)$.",
    r"Easiest with $y$ as the variable: for $0\le y\le2$ the region runs from $x=y^2$ (left, the root curve) to $x=y+2$ (right, the line).",
    r"$A=\displaystyle\int_0^2\left(y+2-y^2\right)dy=\left[\frac{y^2}2+2y-\frac{y^3}3\right]_0^2=2+4-\frac83=\frac{10}3$.",
    r"Check with $x$: $\int_0^4\sqrt x\,dx-\int_2^4(x-2)\,dx=\frac{16}3-2=\frac{10}3$."],
    check=lambda: defint(t + 2 - t**2, 0, 2, sp.Rational(10, 3), var=t), points=13)

# =====================================================================  Antiderivatives & IVPs (5.2)
DUP(94, "f22e3-2a")
N(95, "5.2", "Antiderivatives", r"""Which function is an antiderivative of $f(x)=5x^4+\ln(7)\,7^x+\cos x$?
(A) $x^5+7^x+\sin x-3$ (B) $x^5+\ln(7)7^x+\sin x$ (C) $5x^4+7^x+\sin x+1$ (D) $x^5+7^x+\cos x+5$ (E) $x^5+7^x+\arcsin x-2$""",
  r"(A) $F(x)=x^5+7^x+\sin x-3$",
  [r"Check by differentiating: $(x^5)'=5x^4$, $(7^x)'=7^x\ln7$, $(\sin x)'=\cos x$, $(-3)'=0$.",
   r"So $F'(x)=5x^4+\ln(7)7^x+\cos x=f(x)$ for (A). (B) gives $\ln^2(7)7^x$, (D) gives $-\sin x$, (E) gives $\frac1{\sqrt{1-x^2}}$."],
  check=lambda: antideriv(x**5 + 7**x + sp.sin(x) - 3, 5*x**4 + sp.log(7)*7**x + sp.cos(x)), mc=True, diff="easy")
DUP(96, "f24m3-11")
N(97, "5.2", "Initial value problem", r"Find $y(x)$ if $\dfrac{dy}{dx}=x^3-3$ and $y(0)=8$. (A) $\frac{x^4}4-3x+11$ (B) $\frac{x^4}4-\frac x3+8$ (C) $\frac{x^4}4-3x+8$ (D) $\frac{x^4}4-3x$ (E) $\frac{x^3}3-3x+8$",
  r"(C) $y=\dfrac{x^4}4-3x+8$",
  [r"$y=\displaystyle\int(x^3-3)\,dx=\frac{x^4}4-3x+C$.", r"$y(0)=C=8$ ⇒ $y=\dfrac{x^4}4-3x+8$."],
  check=lambda: all_true(antideriv(x**4/4 - 3*x + 8, x**3 - 3), (x**4/4 - 3*x + 8).subs(x, 0) == 8), mc=True, diff="easy")
DUP(98, "f17f-5b", note="Slide 99 repeats the same problem.")
DUP(100, "f18f-5b")
N(101, "5.2", "Initial value problem", r"Find an equation of the curve such that at each point $(x,y)$, $\dfrac{d^2y}{dx^2}=18x$, and the line $y=9-5x$ is tangent to the curve at the point where $x=1$.",
  r"$y=3x^3-14x+15$",
  [r"Integrate once: $y'=9x^2+C_1$. The tangent line at $x=1$ has slope $-5$: $y'(1)=9+C_1=-5\Rightarrow C_1=-14$.",
   r"Integrate again: $y=3x^3-14x+C_2$.",
   r"The tangent point is on the line: at $x=1$, $y=9-5=4$. So $3-14+C_2=4\Rightarrow C_2=15$.",
   r"$y=3x^3-14x+15$."],
  check=lambda: (lambda Y: all_true(same(sp.diff(Y, x, 2), 18*x), sp.diff(Y, x).subs(x, 1) == -5, Y.subs(x, 1) == 4))(3*x**3 - 14*x + 15), points=10)
