# Generated problems, derivative side (§4.1, 4.2, 4.4, 4.5, 4.6, 4.8). Checked with SymPy.
from pkit import *

L = lambda e: sp.latex(e, ln_notation=True)

def intervals_txt(sets):
    if sets == sp.EmptySet:
        return "nowhere"
    parts = list(sets.args) if isinstance(sets, sp.Union) else [sets]
    return r" \cup ".join(L(p) for p in parts)

# ------------------------------------------------------------------ §4.1 increase/decrease & concavity
def incdec(i, f, diff="exam", domain=sp.S.Reals, note=""):
    f1 = sp.factor(sp.diff(f, x)); f2 = sp.factor(sp.diff(f, x, 2))
    inc = sp.solve_univariate_inequality(sp.diff(f, x) > 0, x, relational=False, domain=domain)
    dec = sp.solve_univariate_inequality(sp.diff(f, x) < 0, x, relational=False, domain=domain)
    cu = sp.solve_univariate_inequality(sp.diff(f, x, 2) > 0, x, relational=False, domain=domain)
    cd = sp.solve_univariate_inequality(sp.diff(f, x, 2) < 0, x, relational=False, domain=domain)
    ip = [r for r in sp.solveset(sp.diff(f, x, 2), x, domain) if r.is_real]
    ip = [r for r in ip if sp.sign(sp.diff(f, x, 2).subs(x, r - sp.Rational(1, 1000))) != sp.sign(sp.diff(f, x, 2).subs(x, r + sp.Rational(1, 1000)))]
    ipt = ", ".join(f"\\left({L(r)},\\,{L(sp.simplify(f.subs(x, r)))}\\right)" for r in sorted(ip, key=float)) or "none"
    G(f"gen-incdec-{i}", "4.1", "Increase/decrease & concavity",
      f"Let $f(x)={L(f)}${note}. Find the intervals where $f$ is increasing, decreasing, concave up and concave down, and find all inflection points.",
      f"Increasing on ${intervals_txt(inc)}$, decreasing on ${intervals_txt(dec)}$; concave up on ${intervals_txt(cu)}$, concave down on ${intervals_txt(cd)}$; inflection points: ${ipt}$",
      [f"$f'(x)={L(f1)}$.", f"Sign of $f'$: positive on ${intervals_txt(inc)}$, negative on ${intervals_txt(dec)}$.",
       f"$f''(x)={L(f2)}$.", f"Sign of $f''$: positive on ${intervals_txt(cu)}$, negative on ${intervals_txt(cd)}$.",
       f"Inflection points (where $f''$ changes sign): ${ipt}$."],
      lambda: all_true(same(sp.diff(f, x), f1), same(sp.diff(f, x, 2), f2)), diff=diff)

incdec(1, x**3 - 6*x**2 + 9*x + 1, "easy")
incdec(2, x**4 - 4*x**3)
incdec(3, x*sp.exp(-x))
incdec(4, sp.exp(-x**2))
incdec(5, x/(x**2 + 1))
incdec(6, x**2*sp.exp(x), "hard")
incdec(7, 3*x**5 - 5*x**3, "hard")
G("gen-incdec-8", "4.1", "Increase/decrease & concavity",
  r"The derivative of $f$ is $f'(x)=(x-1)^2(x+3)$. (a) Where is $f$ increasing/decreasing? (b) Where is $f$ concave up/down? (c) Which critical points are relative extrema?",
  r"(a) $\nearrow[-3,\infty)$, $\searrow(-\infty,-3]$; (b) CU on $(-\infty,-\frac53)\cup(1,\infty)$, CD on $(-\frac53,1)$; (c) relative min at $x=-3$ only",
  [r"$(x-1)^2\ge0$, so the sign of $f'$ is the sign of $x+3$: $f\searrow$ on $(-\infty,-3]$, $\nearrow$ on $[-3,\infty)$.",
   r"$f''(x)=2(x-1)(x+3)+(x-1)^2=(x-1)(3x+5)$: positive for $x&lt;-\frac53$ or $x&gt;1$.",
   r"At $x=-3$, $f'$ changes $-\to+$ ⇒ relative minimum. At $x=1$, $f'$ does not change sign ⇒ no extremum (it is an inflection point)."],
  lambda: same(sp.factor(sp.diff((x - 1)**2*(x + 3), x)), (x - 1)*(3*x + 5)))
G("gen-incdec-9", "4.1", "Increase/decrease & concavity", r"Find the intervals of increase/decrease and concavity of $f(x)=x-2\sin x$ on $[0,2\pi]$.",
  r"$\searrow$ on $[0,\frac\pi3]$ and $[\frac{5\pi}3,2\pi]$, $\nearrow$ on $[\frac\pi3,\frac{5\pi}3]$; CU on $(0,\pi)$, CD on $(\pi,2\pi)$; inflection point $(\pi,\pi)$",
  [r"$f'(x)=1-2\cos x=0\Rightarrow\cos x=\tfrac12\Rightarrow x=\tfrac\pi3,\tfrac{5\pi}3$.", r"$f'&lt;0$ when $\cos x&gt;\tfrac12$, i.e. near $0$ and $2\pi$.",
   r"$f''(x)=2\sin x$: positive on $(0,\pi)$, negative on $(\pi,2\pi)$.", r"Inflection at $x=\pi$: $f(\pi)=\pi$."],
  lambda: sorted(sp.solveset(1 - 2*sp.cos(x), x, sp.Interval(0, 2*sp.pi))) == [sp.pi/3, 5*sp.pi/3])

# ------------------------------------------------------------------ §4.2 relative extrema
def relext(i, f, diff="exam", test="first"):
    f1 = sp.factor(sp.diff(f, x)); cps = sorted([c for c in sp.solve(sp.diff(f, x), x) if c.is_real], key=float)
    lines, res = [], []
    for c in cps:
        f2c = sp.simplify(sp.diff(f, x, 2).subs(x, c))
        left = sp.diff(f, x).subs(x, c - sp.Rational(1, 100)); right = sp.diff(f, x).subs(x, c + sp.Rational(1, 100))
        kind = "max" if (left > 0 and right < 0) else "min" if (left < 0 and right > 0) else "neither"
        if test == "second":
            lines.append(f"$f''({L(c)})={L(f2c)}$" + (" &gt; 0 ⇒ relative min" if f2c > 0 else " &lt; 0 ⇒ relative max" if f2c < 0 else " = 0 ⇒ test inconclusive; the sign of $f'$ does not change ⇒ no extremum" if kind == "neither" else ""))
        else:
            lines.append(f"At $x={L(c)}$: $f'$ goes {'+ to −' if kind == 'max' else '− to +' if kind == 'min' else 'without a sign change'} ⇒ {('relative ' + kind) if kind != 'neither' else 'no extremum'}.")
        if kind != "neither":
            res.append(f"relative {kind} $f({L(c)})={L(sp.simplify(f.subs(x, c)))}$")
    G(f"gen-relext-{i}", "4.2", "Relative extrema & curve sketching",
      f"Find the critical points of $f(x)={L(f)}$ and classify them using the {'second' if test == 'second' else 'first'} derivative test.",
      "; ".join(res) or "no relative extrema",
      [f"$f'(x)={L(f1)}$; critical points $x={', '.join(L(c) for c in cps)}$."] + lines,
      lambda: all(sp.simplify(sp.diff(f, x).subs(x, c)) == 0 for c in cps), diff=diff)

relext(1, 2*x**3 - 3*x**2 - 12*x + 5, "easy", "second")
relext(2, x**4 - 8*x**2 + 3)
relext(3, x**3*(x - 4), "exam")
relext(4, x*sp.exp(-x/2), "exam", "second")
relext(5, x**2*sp.log(x) if False else (x**2 - 1)**3, "hard")
relext(6, x + 4/x, "easy", "second")
G("gen-relext-7", "4.2", "Relative extrema & curve sketching", r"Find and classify the critical points of $f(x)=x^{2/3}(x-5)$.",
  r"Relative max $f(0)=0$; relative min $f(2)=-3\sqrt[3]4$",
  [r"$f(x)=x^{5/3}-5x^{2/3}$, $f'(x)=\tfrac53x^{2/3}-\tfrac{10}3x^{-1/3}=\dfrac{5(x-2)}{3x^{1/3}}$.", r"Critical points: $x=2$ ($f'=0$) and $x=0$ ($f'$ undefined).",
   r"Signs: $x&lt;0$: $\frac{-}{-}=+$; $0&lt;x&lt;2$: $\frac{-}{+}=-$; $x&gt;2$: $+$.", r"Rel. max at $x=0$: $f(0)=0$ (a cusp). Rel. min at $x=2$: $f(2)=2^{2/3}(-3)=-3\sqrt[3]4$."],
  lambda: (lambda X: same(sp.diff(X**sp.Rational(5, 3) - 5*X**sp.Rational(2, 3), X), 5*(X - 2)/(3*X**sp.Rational(1, 3))))(sp.Symbol('X', positive=True)), diff="hard")
G("gen-relext-8", "4.2", "Relative extrema & curve sketching", r"Find constants $a,b$ so that $f(x)=x^3+ax^2+b$ has a relative extremum at $(2,3)$. Is it a max or a min?",
  r"$a=-3$, $b=7$; relative minimum",
  [r"$f'(x)=3x^2+2ax$, and $f'(2)=12+4a=0\Rightarrow a=-3$.", r"$f(2)=8-12+b=3\Rightarrow b=7$.", r"$f''(x)=6x-6$, $f''(2)=6&gt;0$ ⇒ relative minimum."],
  lambda: all_true(same(sp.diff(x**3 - 3*x**2 + 7, x).subs(x, 2), 0), same((x**3 - 3*x**2 + 7).subs(x, 2), 3)))

# ------------------------------------------------------------------ §4.4 absolute extrema
def absext(i, f, a, b, extra_cps=(), diff="exam"):
    cps = sorted({c for c in sp.solve(sp.diff(f, x), x) if c.is_real and a < c < b} | set(extra_cps), key=float)
    cand = [a] + cps + [b]; vals = [(c, sp.simplify(f.subs(x, c))) for c in cand]
    mx = max(vals, key=lambda p: float(p[1])); mn = min(vals, key=lambda p: float(p[1]))
    table = ", ".join(f"$f({L(c)})={L(v)}$" for c, v in vals)
    cpt = ", ".join(L(c) for c in cps) or r"\text{none}"
    G(f"gen-abs-{i}", "4.4", "Absolute extrema", f"Find the absolute maximum and minimum values of $f(x)={L(f)}$ on $[{L(a)},{L(b)}]$.",
      f"Max ${L(mx[1])}$ at $x={L(mx[0])}$; min ${L(mn[1])}$ at $x={L(mn[0])}$",
      [r"$f$ is continuous on the closed interval, so by the Extreme Value Theorem both extrema exist.",
       f"$f'(x)={L(sp.factor(sp.diff(f, x)))}$; critical points in the interval: ${cpt}$.",
       f"Candidates: {table}.", f"Absolute max ${L(mx[1])}$ at $x={L(mx[0])}$; absolute min ${L(mn[1])}$ at $x={L(mn[0])}$."],
      lambda: (lambda xs: abs(max(xs) - float(mx[1])) < 1e-6 and abs(min(xs) - float(mn[1])) < 1e-6)(
          [float(f.subs(x, a + (b - a)*j/4000)) for j in range(4001)]), diff=diff)

absext(1, x**3 - 12*x + 1, -3, 5, diff="easy")
absext(2, x**4 - 2*x**2 + 3, -2, 3)
absext(3, x*sp.exp(-x), 0, 3)
absext(4, x/(x**2 + 4), 0, 3)
absext(5, sp.sin(x) + sp.cos(x), 0, sp.pi)
absext(6, x - 2*sp.log(x), 1, sp.E)
absext(7, (x**2 - 4)**sp.Rational(2, 3) if False else x**sp.Rational(2, 3)*(5 - x) if False else 2*x**3 - 3*x**2 - 12*x, -2, 3, diff="easy")
G("gen-abs-8", "4.4", "Absolute extrema", r"Find the absolute extrema of $f(x)=4x^{1/3}-x^{4/3}$ on $[-1,8]$.",
  r"Max $3$ at $x=1$; min $-8$ at $x=8$",
  [r"$f'(x)=\tfrac43x^{-2/3}-\tfrac43x^{1/3}=\dfrac{4(1-x)}{3x^{2/3}}$: zero at $x=1$, undefined at $x=0$.",
   r"Candidates: $f(-1)=-4-1=-5$, $f(0)=0$, $f(1)=3$, $f(8)=8-16=-8$.", r"Max $3$ at $x=1$, min $-8$ at $x=8$."],
  lambda: (lambda F: abs(max(F(-1 + 9*j/9000) for j in range(9001)) - 3) < 1e-6 and abs(min(F(-1 + 9*j/9000) for j in range(9001)) + 8) < 1e-9)(lambda v: 4*(abs(v)**(1/3))*(1 if v >= 0 else -1) - abs(v)**(4/3)), diff="hard")
G("gen-abs-9", "4.4", "Absolute extrema", r"Does $f(x)=\dfrac{x}{x^2+1}$ have absolute extrema on $(0,\infty)$? If so, find them.",
  r"Absolute max $\frac12$ at $x=1$; no absolute minimum",
  [r"$f'(x)=\dfrac{1-x^2}{(x^2+1)^2}$: the only critical point in $(0,\infty)$ is $x=1$.", r"$f\nearrow$ on $(0,1]$ and $\searrow$ on $[1,\infty)$ ⇒ absolute max $f(1)=\tfrac12$.",
   r"$f(x)&gt;0$ but $f\to0$ as $x\to0^+$ and as $x\to\infty$, and $0$ is never reached ⇒ no absolute minimum."],
  lambda: same(sp.maximum(x/(x**2 + 1), x, sp.Interval.open(0, sp.oo)), sp.Rational(1, 2)), diff="hard")

# ------------------------------------------------------------------ §4.5 optimization
def box(i, V, ratio, cb, cs, diff="exam"):
    h = V/(ratio*w**2); C = cb*ratio*w**2 + cs*(2*w*h + 2*ratio*w*h); C = sp.simplify(C)
    wc = [r for r in sp.solve(sp.diff(C, w), w) if r.is_positive][0]
    G(f"gen-opt-{i}", "4.5", "Optimization",
      f"An open-top rectangular box must have volume ${V}\\ \\text{{m}}^3$, and the length of its base is {ratio} times its width. The base costs {cb} dollars per m² and the sides cost {cs} dollars per m². Find the width that minimizes the cost and show it is a minimum.",
      f"$w={L(sp.nsimplify(wc))}$ m" + ("" if wc.is_Integer else f" $\\approx{float(wc):.3f}$ m"),
      [f"Width $w$, length ${ratio}w$, height $h$. Volume: ${ratio}w^2h={V}\\Rightarrow h={L(h)}$.",
       f"Cost $=({cb})(\\text{{base}})+({cs})(\\text{{4 sides}})={cb}\\cdot{ratio}w^2+{cs}\\left(2wh+2\\cdot{ratio}wh\\right)={L(C)}$, $w&gt;0$.",
       f"$C'(w)={L(sp.simplify(sp.diff(C, w)))}=0\\Rightarrow w={L(wc)}$.",
       f"$C''(w)={L(sp.simplify(sp.diff(C, w, 2)))}&gt;0$ for $w&gt;0$ ⇒ minimum; it is the only critical point and $C\\to\\infty$ at both ends, so it is the absolute minimum."],
      lambda: all_true(same(sp.diff(C, w).subs(w, wc), 0), sp.diff(C, w, 2).subs(w, wc) > 0), diff=diff)

box(1, 12, 3, 4, 2)
box(2, 36, 2, 5, 3)
G("gen-opt-3", "4.5", "Optimization", r"A farmer has 600 m of fencing to enclose a rectangular field next to a straight river (no fence along the river). What dimensions maximize the area?",
  r"$150$ m (perpendicular to the river) by $300$ m; area $45\,000$ m²",
  [r"Let $x$ = side perpendicular to the river, $y$ = side parallel: $2x+y=600\Rightarrow y=600-2x$, $0\le x\le300$.", r"$A(x)=x(600-2x)=600x-2x^2$.",
   r"$A'(x)=600-4x=0\Rightarrow x=150$.", r"Closed interval: $A(0)=0$, $A(300)=0$, $A(150)=45\,000$ ⇒ maximum at $x=150$, $y=300$."],
  lambda: same(sp.solve(sp.diff(600*x - 2*x**2, x), x)[0], 150), diff="easy")
G("gen-opt-4", "4.5", "Optimization", r"Find the point on the curve $y=\sqrt x$ that is closest to the point $(3,0)$.",
  r"$\left(\frac52,\sqrt{\frac52}\right)$",
  [r"Minimize the squared distance $D(x)=(x-3)^2+(\sqrt x)^2=x^2-5x+9$, $x\ge0$.", r"$D'(x)=2x-5=0\Rightarrow x=\tfrac52$; $D''=2&gt;0$ ⇒ minimum.",
   r"$D\to\infty$ as $x\to\infty$ and $D(0)=9&gt;D(\tfrac52)=\tfrac{11}4$ ⇒ absolute minimum. Point $\left(\tfrac52,\sqrt{5/2}\right)$."],
  lambda: same(sp.solve(sp.diff((x - 3)**2 + x, x), x)[0], sp.Rational(5, 2)))
G("gen-opt-5", "4.5", "Optimization", r"A cylindrical can (with top and bottom) must hold $250\pi$ cm³. Find the radius and height that minimize the surface area.",
  r"$r=5$ cm, $h=10$ cm",
  [r"$\pi r^2h=250\pi\Rightarrow h=\dfrac{250}{r^2}$.", r"$S=2\pi r^2+2\pi rh=2\pi r^2+\dfrac{500\pi}{r}$, $r&gt;0$.",
   r"$S'(r)=4\pi r-\dfrac{500\pi}{r^2}=0\Rightarrow r^3=125\Rightarrow r=5$.", r"$S''=4\pi+\dfrac{1000\pi}{r^3}&gt;0$ ⇒ minimum; $h=\dfrac{250}{25}=10$."],
  lambda: (lambda S: all_true([c for c in sp.solve(sp.diff(S, x), x) if c.is_positive] == [5]))(2*sp.pi*x**2 + 500*sp.pi/x))
G("gen-opt-6", "4.5", "Optimization", r"A rectangle has its base on the $x$-axis and its upper two vertices on the parabola $y=12-x^2$. Find the largest possible area.",
  r"$32$ (vertices at $x=\pm2$)",
  [r"Vertices $(\pm x,12-x^2)$, $0\le x\le\sqrt{12}$; area $A(x)=2x(12-x^2)=24x-2x^3$.", r"$A'(x)=24-6x^2=0\Rightarrow x=2$.",
   r"$A(0)=A(\sqrt{12})=0$, $A(2)=2\cdot2\cdot8=32$ ⇒ maximum area $32$."],
  lambda: same((24*x - 2*x**3).subs(x, 2), 32) and sp.solve(24 - 6*x**2, x) == [-2, 2])
G("gen-opt-7", "4.5", "Optimization", r"Find two positive numbers whose product is $64$ and whose sum is as small as possible.", r"$8$ and $8$",
  [r"$xy=64\Rightarrow y=\dfrac{64}x$; $S(x)=x+\dfrac{64}x$, $x&gt;0$.", r"$S'(x)=1-\dfrac{64}{x^2}=0\Rightarrow x=8$; $S''=\dfrac{128}{x^3}&gt;0$ ⇒ minimum.", r"$y=8$."],
  lambda: [c for c in sp.solve(1 - 64/x**2, x) if c > 0] == [8], diff="easy")
G("gen-opt-8", "4.5", "Optimization", r"A box with a square base and no top is made from $108$ cm² of material. Find the dimensions that give the largest volume.",
  r"Base $6\times6$ cm, height $3$ cm (volume $108$ cm³)",
  [r"Base side $x$, height $h$: $x^2+4xh=108\Rightarrow h=\dfrac{108-x^2}{4x}$, $0&lt;x&lt;\sqrt{108}$.", r"$V=x^2h=\dfrac{108x-x^3}{4}$.",
   r"$V'(x)=\dfrac{108-3x^2}4=0\Rightarrow x=6$; $V''=-\tfrac{3x}2&lt;0$ ⇒ maximum.", r"$h=\dfrac{108-36}{24}=3$."],
  lambda: [c for c in sp.solve(sp.diff((108*x - x**3)/4, x), x) if c > 0] == [6])
G("gen-opt-9", "4.5", "Optimization", r"Find the point $P$ in the first quadrant on $y=\dfrac{4}{x}$ for which the sum of the coordinates $x+y$ is smallest.", r"$P(2,2)$, sum $4$",
  [r"$S(x)=x+\dfrac4x$, $x&gt;0$.", r"$S'(x)=1-\dfrac4{x^2}=0\Rightarrow x=2$; $S''=\dfrac8{x^3}&gt;0$ ⇒ minimum.", r"$y=2$, $S=4$."],
  lambda: [c for c in sp.solve(1 - 4/x**2, x) if c > 0] == [2], diff="easy")

# ------------------------------------------------------------------ §4.6 rectilinear motion
def rect(i, s, question, diff="exam"):
    v = sp.diff(s, t); a = sp.diff(v, t)
    vz = sorted([r for r in sp.solve(v, t) if r.is_real and r >= 0], key=float)
    az = sorted([r for r in sp.solve(a, t) if r.is_real and r >= 0], key=float)
    if question == "speed":
        pts = sorted(set(vz + az), key=float); bounds = [0] + pts + [sp.oo]; up, down = [], []
        for j in range(len(bounds) - 1):
            mid = (bounds[j] + bounds[j + 1])/2 if bounds[j + 1] != sp.oo else bounds[j] + 1
            (up if v.subs(t, mid)*a.subs(t, mid) > 0 else down).append(sp.Interval.open(bounds[j], bounds[j + 1]))
        CUP = r" \cup "
        upt, downt = CUP.join(L(I) for I in up), CUP.join(L(I) for I in down)
        G(f"gen-rect-{i}", "4.6", "Rectilinear motion (derivatives)",
          f"A particle moves along an $s$-axis with $s(t)={L(s)}$, $t\\ge0$. Find $v(t)$ and $a(t)$, when the particle is stopped, and when it is speeding up / slowing down.",
          f"Stopped at $t={', '.join(L(r) for r in vz)}$; speeding up on ${upt}$, slowing down on ${downt}$",
          [f"$v(t)=s'(t)={L(sp.factor(v))}$, $\\ a(t)=v'(t)={L(sp.factor(a))}$.", f"$v=0$ at $t={', '.join(L(r) for r in vz)}$ (stopped); $a=0$ at $t={', '.join(L(r) for r in az)}$.",
           "Speeding up when $v$ and $a$ have the same sign, slowing down when the signs differ (compare the two sign lines).",
           f"Speeding up: ${upt}$; slowing down: ${downt}$."],
          lambda: all(sp.simplify(v.subs(t, r)) == 0 for r in vz), diff=diff)

rect(1, t**3 - 9*t**2 + 24*t, "speed")
rect(2, 2*t**3 - 15*t**2 + 36*t - 10, "speed")
rect(3, t**3 - 6*t**2 + 9*t + 2, "speed", "easy")
G("gen-rect-4", "4.6", "Rectilinear motion (derivatives)", r"A particle has position $s(t)=t^3-12t+5$ (m). Find the velocity when the acceleration is $18\ \text{m/s}^2$.", r"$15$ m/s",
  [r"$v=3t^2-12$, $a=6t$.", r"$6t=18\Rightarrow t=3$.", r"$v(3)=27-12=15$ m/s."], lambda: same((3*t**2 - 12).subs(t, 3), 15), diff="easy")
G("gen-rect-5", "4.6", "Rectilinear motion (derivatives)", r"For $s(t)=\dfrac{t}{t^2+4}$, $t\ge0$, find the time when the particle is farthest from the origin in the positive direction, and that position.",
  r"$t=2$, $s=\frac14$",
  [r"$v(t)=\dfrac{4-t^2}{(t^2+4)^2}$; $v=0$ at $t=2$.", r"$v&gt;0$ for $t&lt;2$, $v&lt;0$ for $t&gt;2$ ⇒ $s$ is largest at $t=2$.", r"$s(2)=\dfrac2{8}=\dfrac14$."],
  lambda: same(sp.diff(t/(t**2 + 4), t).subs(t, 2), 0), diff="exam")
G("gen-rect-6", "4.6", "Rectilinear motion (derivatives)", r"A particle has velocity $v(t)=t^3-6t^2+9t$ for $0\le t\le4$. Find the maximum and minimum acceleration on this interval.",
  r"Max $a=9$ at $t=0$ and $t=4$; min $a=-3$ at $t=2$",
  [r"$a(t)=3t^2-12t+9$; $a'(t)=6t-12=0\Rightarrow t=2$.", r"Candidates: $a(0)=9$, $a(2)=-3$, $a(4)=9$.", r"Max $9$ (at $t=0$ and $t=4$), min $-3$ (at $t=2$)."],
  lambda: (lambda a_: [a_.subs(t, v) for v in (0, 2, 4)] == [9, -3, 9])(sp.diff(t**3 - 6*t**2 + 9*t, t)))
G("gen-rect-7", "4.6", "Rectilinear motion (derivatives)", r"A ball thrown upward has height $s(t)=-4.9t^2+19.6t+2$ m. When does it reach its maximum height, and what is that height?",
  r"$t=2$ s, height $21.6$ m",
  [r"$v(t)=-9.8t+19.6=0\Rightarrow t=2$.", r"$a=-9.8&lt;0$ ⇒ maximum.", r"$s(2)=-19.6+39.2+2=21.6$ m."],
  lambda: abs(float((-4.9*t**2 + 19.6*t + 2).subs(t, 2)) - 21.6) < 1e-9, diff="easy")
G("gen-rect-8", "4.6", "Rectilinear motion (derivatives)", r"For $s(t)=te^{-t}$, $t\ge0$, find when the particle is speeding up.",
  r"Speeding up only on $(1,2)$",
  [r"$v=(1-t)e^{-t}$, $a=(t-2)e^{-t}$.", r"$v&gt;0$ on $(0,1)$, $&lt;0$ after; $a&lt;0$ on $(0,2)$, $&gt;0$ after.",
   r"On $(0,1)$: $v&gt;0$, $a&lt;0$ ⇒ slowing down. On $(1,2)$: $v&lt;0$, $a&lt;0$ ⇒ speeding up. On $(2,\infty)$: $v&lt;0$, $a&gt;0$ ⇒ slowing down."],
  lambda: same(sp.diff(t*sp.exp(-t), t, 2), (t - 2)*sp.exp(-t)), diff="hard")

# ------------------------------------------------------------------ §4.8 MVT: find c
def mvt(i, f, a, b, diff="exam"):
    slope = sp.simplify((f.subs(x, b) - f.subs(x, a))/(b - a))
    cs = sorted([c for c in sp.solve(sp.Eq(sp.diff(f, x), slope), x) if c.is_real and a < c < b], key=float)
    G(f"gen-mvt-{i}", "4.8", "Mean Value Theorem / Rolle",
      f"Verify that $f(x)={L(f)}$ satisfies the hypotheses of the Mean-Value Theorem on $[{L(a)},{L(b)}]$ and find all numbers $c$ that satisfy its conclusion.",
      "$c=" + ",\\ ".join(L(c) for c in cs) + "$",
      [f"$f$ is continuous on $[{L(a)},{L(b)}]$ and differentiable on $({L(a)},{L(b)})$ (no division by zero or roots of negative numbers there).",
       f"Secant slope: $\\dfrac{{f({L(b)})-f({L(a)})}}{{{L(b)}-{L(a)}}}={L(slope)}$.",
       f"$f'(x)={L(sp.diff(f, x))}$; solve $f'(c)={L(slope)}$.", f"Solutions inside the interval: $c={', '.join(L(c) for c in cs)}$."],
      lambda: len(cs) > 0 and all(same(sp.diff(f, x).subs(x, c), slope) for c in cs), diff=diff)

mvt(1, x**3 - x, 0, 2, "easy")
mvt(2, sp.sqrt(x), 1, 9)
mvt(3, 1/x, 1, 3)
mvt(4, x**3 - 3*x + 2, -2, 2)
mvt(5, sp.log(x), 1, sp.E, "hard")
G("gen-mvt-6", "4.8", "Mean Value Theorem / Rolle", r"Verify Rolle's Theorem for $f(x)=x^2-6x+5$ on $[1,5]$ and find $c$.", "$c=3$",
  [r"Polynomial ⇒ continuous and differentiable; $f(1)=0=f(5)$.", r"$f'(c)=2c-6=0\Rightarrow c=3\in(1,5)$."], lambda: same((x**2 - 6*x + 5).subs(x, 1), 0) and same((x**2 - 6*x + 5).subs(x, 5), 0), diff="easy")
G("gen-mvt-7", "4.8", "Mean Value Theorem / Rolle", r"Explain why the Mean-Value Theorem does not apply to $f(x)=x^{2/3}$ on $[-1,8]$, and show that no $c$ satisfies its conclusion.",
  r"$f$ is not differentiable at $x=0$; $f'(c)=\frac{2}{3c^{1/3}}=\frac{3}{9}$ gives $c=8$, which is not in $(-1,8)$",
  [r"$f'(x)=\tfrac23x^{-1/3}$ does not exist at $x=0\in(-1,8)$ (cusp) ⇒ hypothesis fails.", r"Secant slope $\dfrac{4-1}{9}=\dfrac13$.",
   r"$\dfrac{2}{3c^{1/3}}=\dfrac13\Rightarrow c^{1/3}=2\Rightarrow c=8$, an endpoint, not inside $(-1,8)$."],
  lambda: same((sp.Integer(8)**sp.Rational(2, 3) - 1)/9, sp.Rational(1, 3)))
G("gen-mvt-8", "4.8", "Mean Value Theorem / Rolle", r"Use Rolle's Theorem to show that $x^3+3x-1=0$ has exactly one real root.",
  r"At least one root by the IVT ($f(0)=-1&lt;0&lt;f(1)=3$); two roots would give $f'(c)=0$ by Rolle, but $f'(x)=3x^2+3&gt;0$",
  [r"Existence: $f(0)=-1$, $f(1)=3$, $f$ continuous ⇒ a root in $(0,1)$ by the IVT.", r"Suppose there were two roots $a&lt;b$. Then $f(a)=f(b)=0$ and Rolle gives $c$ with $f'(c)=0$.",
   r"But $f'(x)=3x^2+3\ge3&gt;0$ for all $x$: contradiction. So there is exactly one root."],
  lambda: len([r for r in sp.solve(x**3 + 3*x - 1, x) if r.is_real]) == 1, diff="hard")

# ------------------------------------------------------------------ §4.8 MVT inequality proofs
def proof(i, st, ans, steps, check, diff="hard"):
    G(f"gen-mvtp-{i}", "4.8", "MVT inequality proofs", st, ans, steps, check, diff=diff)

proof(1, r"Use the Mean-Value Theorem to show that $\sin x&lt;x$ for all $x&gt;0$.", "Proof (see steps)",
      [r"For $0&lt;x\le1$: apply the MVT to $f(t)=\sin t$ on $[0,x]$: $\dfrac{\sin x-0}{x-0}=\cos c$ for some $c\in(0,x)$.",
       r"$0&lt;c&lt;x\le1&lt;2\pi$ ⇒ $\cos c&lt;1$, so $\sin x&lt;x$.", r"For $x&gt;1$: $\sin x\le1&lt;x$. ∎"],
      lambda: all(float(sp.sin(v)) < v for v in [0.001, 0.5, 1, 3, 10]))
proof(2, r"Show that $\ln(1+x)&lt;x$ for $x&gt;0$.", "Proof (see steps)",
      [r"$f(t)=\ln(1+t)$ on $[0,x]$: continuous and differentiable.", r"MVT: $\dfrac{\ln(1+x)-0}{x}=\dfrac1{1+c}$ with $0&lt;c&lt;x$.",
       r"$1+c&gt;1\Rightarrow\dfrac1{1+c}&lt;1$, so $\ln(1+x)&lt;x$. ∎"], lambda: all(float(sp.log(1 + v)) < v for v in [0.01, 1, 5, 50]))
proof(3, r"Show that $|\sin a-\sin b|\le|a-b|$ for all real $a,b$.", "Proof (see steps)",
      [r"If $a=b$ it is trivial. Otherwise apply the MVT to $\sin$ on the interval between $a$ and $b$.", r"$\sin a-\sin b=\cos c\,(a-b)$ for some $c$.",
       r"$|\cos c|\le1\Rightarrow|\sin a-\sin b|\le|a-b|$. ∎"], lambda: all(abs(float(sp.sin(p) - sp.sin(q))) <= abs(p - q) for p, q in [(0, 1), (2, -3), (5, 5.1)]), diff="exam")
proof(4, r"Show that $e^x&gt;1+x$ for $x&gt;0$.", "Proof (see steps)",
      [r"$f(t)=e^t$ on $[0,x]$: $\dfrac{e^x-1}{x}=e^c$ with $0&lt;c&lt;x$.", r"$e^c&gt;e^0=1$, so $e^x-1&gt;x$. ∎"], lambda: all(float(sp.exp(v)) > 1 + v for v in [0.01, 1, 4]), diff="exam")
proof(5, r"Show that $\sqrt{1+x}&gt;1+\dfrac{x}{2\sqrt{1+x}}$ for $x&gt;0$.", "Proof (see steps)",
      [r"$f(t)=\sqrt{1+t}$ on $[0,x]$: $\dfrac{\sqrt{1+x}-1}{x}=\dfrac1{2\sqrt{1+c}}$, $0&lt;c&lt;x$.",
       r"$c&lt;x\Rightarrow\sqrt{1+c}&lt;\sqrt{1+x}\Rightarrow\dfrac1{2\sqrt{1+c}}&gt;\dfrac1{2\sqrt{1+x}}$.", r"Multiply by $x&gt;0$: $\sqrt{1+x}-1&gt;\dfrac{x}{2\sqrt{1+x}}$. ∎"],
      lambda: all(float(sp.sqrt(1 + v)) > 1 + v/(2*float(sp.sqrt(1 + v))) for v in [0.01, 1, 8]))
proof(6, r"Show that $\dfrac{x}{1+x^2}&lt;\arctan x&lt;x$ for $x&gt;0$.", "Proof (see steps)",
      [r"$f(t)=\arctan t$ on $[0,x]$: $\dfrac{\arctan x}{x}=\dfrac1{1+c^2}$ with $0&lt;c&lt;x$.", r"$0&lt;c&lt;x\Rightarrow1&lt;1+c^2&lt;1+x^2\Rightarrow\dfrac1{1+x^2}&lt;\dfrac1{1+c^2}&lt;1$.",
       r"Multiply by $x&gt;0$. ∎"], lambda: all(v/(1 + v**2) < float(sp.atan(v)) < v for v in [0.1, 1, 7]))
proof(7, r"Use the MVT to show that if $f'(x)=0$ for all $x$ in $(a,b)$, then $f$ is constant on $(a,b)$.", "Proof (see steps)",
      [r"Take any $x_1&lt;x_2$ in $(a,b)$; $f$ is differentiable, hence continuous, on $[x_1,x_2]$.", r"MVT: $f(x_2)-f(x_1)=f'(c)(x_2-x_1)=0$.",
       r"So all values of $f$ are equal: $f$ is constant. ∎"], None, diff="exam")
proof(8, r"Use the MVT to show that $\tan x&gt;x$ for $0&lt;x&lt;\dfrac\pi2$.", "Proof (see steps)",
      [r"$f(t)=\tan t$ on $[0,x]$: $\dfrac{\tan x}{x}=\sec^2c$, $0&lt;c&lt;x&lt;\tfrac\pi2$.", r"$\sec^2c&gt;1$ for $c\ne0$, so $\tan x&gt;x$. ∎"],
      lambda: all(float(sp.tan(v)) > v for v in [0.01, 0.7, 1.5]), diff="exam")
