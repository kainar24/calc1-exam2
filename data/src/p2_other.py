# Fall 2024 midterms (instructor unknown) and Castro Castilla papers (2017–2020) — Telegram "MATH 161 All Sections".
from pkit import *

TG = "materials/telegram/MATH161_All_Sections/"
PG = "assets/pages/"
OWN = "own"

# ------------------------------------------------------------------ Fall 2024 Midterm 2
paper("f24-m2", "Fall 2024 Midterm 2 (file “Midterm 2.pdf”)", "F24 MT2", "midterm", 2024, "Fall",
      [(TG + "Midterm 2.pdf", "PDF (scan with student's marks)")], False, None, 60,
      "12 multiple-choice + 3 open problems. No official solutions; some MC answers are circled by a student. Solutions here are mine, checked with SymPy.")
S = "f24-m2"
pg = lambda i: PG + f"Midterm_2_p{i}.png"
P("f24m2-1", S, 1, "4.1", "Concavity", r"Given $f(x)=x^3-4x^2+5x$, find the open interval(s) where $f$ is concave down.",
  r"$\left(-\infty,\tfrac43\right)$", [r"$f'(x)=3x^2-8x+5$, $f''(x)=6x-8$.", r"$f''<0\iff x<\tfrac43$ ⇒ concave down on $(-\infty,\tfrac43)$, concave up on $(\tfrac43,\infty)$."],
  check=lambda: sp.solve_univariate_inequality(sp.diff(x**3 - 4*x**2 + 5*x, x, 2) < 0, x, relational=False) == sp.Interval.open(-sp.oo, sp.Rational(4, 3)),
  src=OWN, mc=True, diff="easy", page=pg(2), points=6)
P("f24m2-2", S, 2, "4.8", "MVT hypotheses", r"Explain why the Mean Value Theorem does not apply to $f(x)=|x-3|$ on $[1,4]$.",
  r"$f$ is not differentiable at $x=3\in(1,4)$",
  [r"MVT needs: continuous on $[a,b]$ and differentiable on $(a,b)$.", r"$|x-3|$ is continuous everywhere, but has a corner at $x=3$: left derivative $-1$, right derivative $+1$.",
   r"Since $3\in(1,4)$, the differentiability hypothesis fails. (Indeed the secant slope is $\frac{1-2}{3}=-\frac13$, and $f'(x)=\pm1$ never equals it.)"],
  src=OWN, mc=True, diff="easy", page=pg(2), points=6)
P("f24m2-3", S, 3, "3.6", "L'Hôpital's rule", r"Find $\displaystyle\lim_{x\to0}(1+\sin x)^{\csc x}$.", r"$e$", src=OWN, mc=True, page=pg(3), points=6)
P("f24m2-4", S, 4, "3.5", "Linear approximation", r"Let $L(x)$ be the linearization of $f(x)=\sin x+1$ at $x=\pi$. Find $L(\pi/2)$.", r"$1+\frac\pi2$", src=OWN, mc=True, page=pg(3), points=6)
P("f24m2-5", S, 5, "3.4", "Related rates", r"The side of a square increases at 3 in/min. Find the rate of change of its area when the side is 2 in.", r"$12$ in²/min", src=OWN, mc=True, page=pg(4), points=6)
P("f24m2-6", S, 6, "4.1", "Increase/decrease", r"For $f(x)=\dfrac{\ln x}{x}$, $x>0$, find where $f$ is increasing and where it is decreasing.",
  r"Increasing on $(0,e]$, decreasing on $[e,\infty)$",
  [r"Quotient rule: $f'(x)=\dfrac{\frac1x\cdot x-\ln x}{x^2}=\dfrac{1-\ln x}{x^2}$.", r"$x^2>0$, so the sign is the sign of $1-\ln x$: positive for $x<e$, negative for $x>e$.",
   r"So $f\nearrow$ on $(0,e]$ and $f\searrow$ on $[e,\infty)$; the MC answer is “decreasing for all $x>e$”."],
  check=lambda: same(sp.diff(sp.log(x)/x, x), (1 - sp.log(x))/x**2), src=OWN, mc=True, diff="easy", page=pg(4), points=6)
P("f24m2-7", S, 7, "4.1", "Inflection points", r"How many inflection points does $y=2x+\cos x$ have on $[-\pi,\pi]$?",
  r"$2$ (at $x=\pm\frac\pi2$)",
  [r"$y'=2-\sin x$, $y''=-\cos x$.", r"$y''=0$ at $x=\pm\pi/2$ in $[-\pi,\pi]$.", r"$-\cos x$ changes sign at both points ($+$ on $(-\pi,-\pi/2)$, $-$ on $(-\pi/2,\pi/2)$, $+$ on $(\pi/2,\pi)$) ⇒ two inflection points."],
  check=lambda: sorted(sp.solveset(sp.diff(2*x + sp.cos(x), x, 2), x, sp.Interval(-sp.pi, sp.pi))) == [-sp.pi/2, sp.pi/2],
  src=OWN, mc=True, diff="easy", page=pg(5), points=6)
P("f24m2-8", S, 8, "3.5", "Linear approximation", r"For small $h$, approximate $\sqrt[4]{16+h}$.", r"$2+\frac h{32}$", src=OWN, mc=True, page=pg(5), points=6)
P("f24m2-9", S, 9, "4.4", "Absolute extrema (existence)", r"""Let $f(x)=\begin{cases}x^2,&0\le x<1\\0,&1\le x\le2\end{cases}$. Does $f$ attain an absolute maximum / minimum on $[0,2]$?""",
  r"Absolute minimum $0$ is attained; no absolute maximum",
  [r"$f\ge0$ and $f(0)=f(1)=f(2)=0$ ⇒ absolute minimum value $0$.", r"Values approach $1$ as $x\to1^-$ but $f(1)=0$, so $1$ is never reached and there is no largest value.",
   r"The EVT does not apply because $f$ is discontinuous at $x=1$."], src=OWN, mc=True, diff="easy", page=pg(6), points=6)
P("f24m2-10", S, 10, "4.8", "MVT hypotheses", r"""Which function fails to satisfy the conclusion of the MVT on the interval?
(a) $3x^{2/3}-1$ on $[1,2]$; (b) $|3x-2|$ on $[1,2]$; (c) $4x^3-2x+3$ on $[0,2]$; (d) $\sqrt{x-2}$ on $[3,6]$; (e) none of these.""",
  r"(e) none of these",
  [r"(a) $x^{2/3}$ is differentiable for $x\neq0$, and $0\notin[1,2]$ ✓.", r"(b) on $[1,2]$, $3x-2>0$, so $|3x-2|=3x-2$ is linear ✓.",
   r"(c) polynomial ✓. (d) $\sqrt{x-2}$ is continuous on $[3,6]$ and differentiable for $x>2$ ✓.", r"All satisfy the hypotheses, so all satisfy the conclusion."],
  src=OWN, mc=True, diff="easy", page=pg(6), points=6)
P("f24m2-11", S, 11, "4.6", "Rectilinear motion", r"A particle's position is $s(t)=t^2+4t+4$. What is its acceleration at $t=4$?",
  r"$2$", [r"$v=2t+4$, $a=v'=2$ (constant) ⇒ $a(4)=2$."], check=lambda: sp.diff(t**2 + 4*t + 4, t, 2) == 2, src=OWN, mc=True, diff="easy", page=pg(7), points=6)
P("f24m2-12", S, 12, "4.4", "Absolute extrema (theory)", r"""Which statements are true? I. A function on a closed bounded interval must achieve an absolute max and min.
II. Every absolute extremum is also a relative extremum. III. Endpoints of closed bounded intervals can be locations of absolute extrema.""",
  r"Only III", [r"I is false without continuity (see Problem 9).", r"II is false: an absolute extremum at an endpoint is not a relative extremum (relative extrema need an open interval around the point).", r"III is true."],
  src=OWN, mc=True, diff="easy", page=pg(7), points=6)
P("f24m2-13", S, 13, "3.4", "Related rates", r"A 25-ft ladder leans against a wall; its bottom slides away at 3 ft/s. How fast does the top slide down when the bottom is 15 ft from the wall?",
  r"$\frac94$ ft/s", src=OWN, page=pg(8), points=12)
P("f24m2-14", S, 14, "4.6", "Rectilinear motion + absolute max", r"Find the maximum acceleration on $0\le t\le3$ of a particle with velocity $v(t)=\tfrac23t^3-4t^2+8t-2$.",
  r"$8$ (at $t=0$)",
  [r"$a(t)=v'(t)=2t^2-8t+8=2(t-2)^2$.", r"Critical point of $a$: $a'(t)=4t-8=0\Rightarrow t=2$.", r"Compare: $a(0)=8$, $a(2)=0$, $a(3)=2$.", r"Maximum acceleration $8$ at $t=0$."],
  check=lambda: (lambda a: max(a.subs(t, v) for v in [0, 2, 3]) == 8)(sp.diff(sp.Rational(2, 3)*t**3 - 4*t**2 + 8*t - 2, t)), src=OWN, page=pg(8), points=12)
P("f24m2-15a", S, "15(a)", "5.2", "Antiderivatives (algebra first)", r"Evaluate $\displaystyle\int\frac{1+2x^2}{x^2(1+x^2)}\,dx$.",
  r"$-\dfrac1x+\arctan x+C$",
  [r"Split the numerator: $1+2x^2=(1+x^2)+x^2$.", r"$\dfrac{(1+x^2)+x^2}{x^2(1+x^2)}=\dfrac1{x^2}+\dfrac1{1+x^2}$.", r"$\int x^{-2}dx=-\dfrac1x$, $\int\dfrac{dx}{1+x^2}=\arctan x$."],
  check=lambda: antideriv(-1/x + sp.atan(x), (1 + 2*x**2)/(x**2*(1 + x**2))), src=OWN, page=pg(9), points=8)
P("f24m2-15b", S, "15(b)", "5.3", "u-substitution", r"Evaluate $\displaystyle\int\frac{x^3}{\sqrt{1-x^8}}\,dx$.",
  r"$\dfrac14\arcsin(x^4)+C$", [r"$u=x^4$, $du=4x^3dx$, and $x^8=u^2$.", r"$\displaystyle\frac14\int\frac{du}{\sqrt{1-u^2}}=\frac14\arcsin u+C=\frac14\arcsin(x^4)+C.$"],
  check=lambda: antideriv(sp.asin(x**4)/4, x**3/sp.sqrt(1 - x**8), pts=(0.2, 0.5, 0.8)), src=OWN, page=pg(9), points=8)

# ------------------------------------------------------------------ Fall 2024 Midterm 3 (variant A)
paper("f24-m3", "Fall 2024 Midterm 3 · Variant A (file “Midterm 3.pdf”)", "F24 MT3", "midterm", 2024, "Fall",
      [(TG + "Midterm 3.pdf", "PDF (scan with a student's worked answers)")], False, None, 60,
      "18 multiple-choice questions on Ch. 5 and §7.2–7.3. A student circled answers and wrote short work; all answers re-checked with SymPy.")
S = "f24-m3"
pg = lambda i: PG + f"Midterm_3_p{i}.png"
def mc3(i, num, sec, topic, st, ans, steps, check, page, diff="easy"):
    P(f"f24m3-{num}", S, num, sec, topic, st, ans, steps, check, diff=diff, src=OWN, mc=True, page=pg(page), points=6)
mc3(1, 1, "5.5", "Properties of definite integrals", r"Suppose $\int_1^8f=12$, $\int_5^1f=3$, $\int_7^8f=4$. Find $\displaystyle\int_5^7(2f(x)-1)\,dx$.", r"$20$",
    [r"$\int_1^8=\int_1^5+\int_5^7+\int_7^8$ and $\int_1^5f=-\int_5^1f=-3$.", r"$12=-3+\int_5^7f+4\Rightarrow\int_5^7f=11$.", r"$\int_5^7(2f-1)=2\cdot11-(7-5)=20$."],
    lambda: 2*(12 + 3 - 4) - 2 == 20, 2)
mc3(2, 2, "5.5", "Integrals with absolute value", r"Evaluate $\displaystyle\int_{-2}^3|x+1|\,dx$.", r"$\dfrac{17}2$",
    [r"Split at $x=-1$: $\int_{-2}^{-1}-(x+1)\,dx+\int_{-1}^3(x+1)\,dx$.", r"Triangles: $\tfrac12\cdot1\cdot1+\tfrac12\cdot4\cdot4=\tfrac12+8=\tfrac{17}2$."],
    lambda: defint(sp.Abs(x + 1), -2, 3, sp.Rational(17, 2)), 2)
mc3(3, 3, "5.8", "Average value", r"Find the average value of $y=e^{3x}$ on $[0,4]$.", r"$\dfrac{e^{12}-1}{12}$",
    [r"$\dfrac14\displaystyle\int_0^4e^{3x}dx=\frac14\cdot\frac13\left[e^{3x}\right]_0^4=\frac{e^{12}-1}{12}.$"], lambda: same(sp.integrate(sp.exp(3*x), (x, 0, 4))/4, (sp.exp(12) - 1)/12), 3)
mc3(4, 4, "5.4", "Riemann sum ↔ integral", r"Write $\displaystyle\int_1^3\sqrt x\,dx$ as a limit of right-endpoint Riemann sums.", r"$\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac2n\sqrt{1+\frac{2k}n}$",
    [r"$\Delta x=\dfrac{3-1}n=\dfrac2n$, $x_k^*=1+k\Delta x=1+\dfrac{2k}n$.", r"Sum: $\sum f(x_k^*)\Delta x=\sum\dfrac2n\sqrt{1+\dfrac{2k}n}$."],
    lambda: same(sp.limit(sp.summation(2/n*sp.sqrt(1 + 2*k/n), (k, 1, n)), n, sp.oo), sp.integrate(sp.sqrt(x), (x, 1, 3))) if False else abs(sum(2/4000*(1 + 2*kk/4000)**0.5 for kk in range(1, 4001)) - float(sp.integrate(sp.sqrt(x), (x, 1, 3)))) < 1e-3, 3)
mc3(5, 5, "5.4", "Riemann sum ↔ integral", r"Which integral equals $\displaystyle\lim_{n\to\infty}\sum_{i=1}^n\left[\left(1+\frac{2i}n\right)^2+1\right]\frac2n$?", r"$\displaystyle\int_1^3(x^2+1)\,dx$",
    [r"$\Delta x=\dfrac2n=\dfrac{b-a}n\Rightarrow b-a=2$.", r"$x_i=1+\dfrac{2i}n$ starts at $a=1$, so $b=3$.", r"$f(x_i)=x_i^2+1$ ⇒ $\int_1^3(x^2+1)\,dx$."],
    lambda: same(sp.limit(sp.summation(((1 + 2*k/n)**2 + 1)*2/n, (k, 1, n)), n, sp.oo), sp.integrate(x**2 + 1, (x, 1, 3))), 4)
mc3(6, 6, "5.6", "Area under a curve (FTC)", r"Find the area bounded by $y=e^{2x}$, the $x$-axis, the $y$-axis and the line $x=2$.", r"$\dfrac{e^4-1}2$",
    [r"$A=\displaystyle\int_0^2e^{2x}dx=\left[\tfrac12e^{2x}\right]_0^2=\tfrac12(e^4-1).$"], lambda: defint(sp.exp(2*x), 0, 2, (sp.exp(4) - 1)/2), 4)
mc3(7, 7, "7.2", "Integration by parts", r"Evaluate $\displaystyle\int_0^\pi x^2\cos x\,dx$.", r"$-2\pi$",
    [r"Tabular method: $u=x^2$ (D: $x^2,2x,2,0$), $dv=\cos x$ (I: $\sin x,-\cos x,-\sin x$).", r"$\int x^2\cos x\,dx=x^2\sin x+2x\cos x-2\sin x+C$.",
     r"Evaluate $0\to\pi$: $(0+2\pi(-1)-0)-(0)=-2\pi$."], lambda: defint(x**2*sp.cos(x), 0, sp.pi, -2*sp.pi), 5, "exam")
mc3(8, 8, "7.2", "Integration by parts", r"Evaluate $\displaystyle\int_0^1x\tan^{-1}x\,dx$.", r"$\dfrac\pi4-\dfrac12$",
    [r"$u=\tan^{-1}x$, $dv=x\,dx$ ⇒ $du=\dfrac{dx}{1+x^2}$, $v=\dfrac{x^2}2$.", r"$\displaystyle\int_0^1x\tan^{-1}x\,dx=\left[\frac{x^2}2\tan^{-1}x\right]_0^1-\frac12\int_0^1\frac{x^2}{1+x^2}dx.$",
     r"$\dfrac{x^2}{1+x^2}=1-\dfrac1{1+x^2}$ ⇒ $\int_0^1=1-\dfrac\pi4$.", r"Result: $\dfrac\pi8-\dfrac12\left(1-\dfrac\pi4\right)=\dfrac\pi4-\dfrac12$."],
    lambda: defint(x*sp.atan(x), 0, 1, sp.pi/4 - sp.Rational(1, 2)), 5, "exam")
mc3(9, 9, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_{\pi/4}^{\pi/2}\sin^3\theta\cos\theta\,d\theta$.", r"$\dfrac3{16}$",
    [r"$u=\sin\theta$, $du=\cos\theta\,d\theta$; $u:\tfrac{\sqrt2}2\to1$.", r"$\left[\dfrac{u^4}4\right]_{\sqrt2/2}^1=\dfrac14\left(1-\dfrac14\right)=\dfrac3{16}.$"],
    lambda: defint(sp.sin(x)**3*sp.cos(x), sp.pi/4, sp.pi/2, sp.Rational(3, 16)), 6)
mc3(10, 10, "5.2", "Antiderivatives (trig)", r"Evaluate $\displaystyle\int\left(\frac1{\cos^2x}-\frac1{\sin^2x}\right)dx$.", r"$\tan x+\cot x+C=2\csc2x+C$",
    [r"$\int\sec^2x\,dx=\tan x$, $\int\csc^2x\,dx=-\cot x$ ⇒ $\tan x+\cot x+C$.", r"$\tan x+\cot x=\dfrac{\sin^2x+\cos^2x}{\sin x\cos x}=\dfrac2{\sin2x}=2\csc2x$."],
    lambda: antideriv(2/sp.sin(2*x), 1/sp.cos(x)**2 - 1/sp.sin(x)**2), 6)
mc3(11, 11, "5.2", "Initial value problem", r"$F$ is the antiderivative of $f(x)=2x^3-5x^4$ with $F(0)=1$. Find $F(1)$.", r"$\dfrac12$",
    [r"$F(x)=\dfrac{x^4}2-x^5+C$, $F(0)=C=1$.", r"$F(1)=\tfrac12-1+1=\tfrac12$."], lambda: same(1 + sp.integrate(2*x**3 - 5*x**4, (x, 0, 1)), sp.Rational(1, 2)), 7)
mc3(12, 12, "5.6", "FTC: derivative of an integral", r"If $f(x)=\displaystyle\int_1^{2x}\sqrt{1+2t}\,dt$, find $f'(2)$.", r"$6$",
    [r"$f'(x)=\sqrt{1+2(2x)}\cdot2=2\sqrt{1+4x}$.", r"$f'(2)=2\sqrt9=6$."], lambda: same(sp.diff(sp.integrate(sp.sqrt(1 + 2*t), (t, 1, 2*x)), x).subs(x, 2), 6), 7)
mc3(13, 13, "5.7", "Average velocity", r"An object starts from rest at $x=0$ with constant acceleration $2\ \text{m/s}^2$. Find its average velocity between $t=1$ s and $t=5$ s.", r"$6$ m/s",
    [r"$v(t)=2t$ (starts from rest).", r"$v_{\text{ave}}=\dfrac1{5-1}\displaystyle\int_1^5 2t\,dt=\frac14\left[t^2\right]_1^5=\frac{24}4=6$ m/s."], lambda: same(sp.integrate(2*t, (t, 1, 5))/4, 6), 8)
mc3(14, 14, "5.7", "Constant acceleration", r"A body moves with constant acceleration $a$. Express its velocity after time $t$.", r"$v=v_0+at$",
    [r"$v(t)=\int a\,dt=at+C$, and $v(0)=v_0\Rightarrow C=v_0$."], None, 8)
mc3(15, 15, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_0^1\frac{e^x}{(3-e^x)^2}\,dx$.", r"$\dfrac{e-1}{2(3-e)}$",
    [r"$u=3-e^x$, $du=-e^xdx$: $\displaystyle\int\frac{e^x}{(3-e^x)^2}dx=-\int u^{-2}du=\frac1u=\frac1{3-e^x}$.", r"$\left[\dfrac1{3-e^x}\right]_0^1=\dfrac1{3-e}-\dfrac12=\dfrac{e-1}{2(3-e)}.$"],
    lambda: defint(sp.exp(x)/(3 - sp.exp(x))**2, 0, 1, (sp.E - 1)/(2*(3 - sp.E))), 9)
mc3(16, 16, "7.2", "Substitution + integration by parts", r"Evaluate $\displaystyle\int x^5e^{x^2}\,dx$.", r"$\dfrac{e^{x^2}}2\left(x^4-2x^2+2\right)+C$",
    [r"$y=x^2$, $dy=2x\,dx$: $\displaystyle\int x^4e^{x^2}x\,dx=\frac12\int y^2e^y\,dy$.", r"By parts twice (tabular): $\int y^2e^ydy=e^y(y^2-2y+2)$.", r"Back-substitute: $\dfrac12e^{x^2}(x^4-2x^2+2)+C$."],
    lambda: antideriv(sp.exp(x**2)/2*(x**4 - 2*x**2 + 2), x**5*sp.exp(x**2)), 9, "exam")
mc3(17, 17, "5.9", "Substitution (recognize the form)", r"Which integral is equivalent to $\displaystyle\int_0^\pi\frac{(\sin x+\cos x)\,dx}{\sqrt{1-(\sin x-\cos x)^2}}$? Evaluate it.",
    r"$\displaystyle\int_{-1}^1\frac{d\theta}{\sqrt{1-\theta^2}}=\pi$",
    [r"$\theta=\sin x-\cos x$, $d\theta=(\cos x+\sin x)\,dx$.", r"$x=0\to\theta=-1$, $x=\pi\to\theta=1$.", r"$\displaystyle\int_{-1}^1\frac{d\theta}{\sqrt{1-\theta^2}}=\arcsin1-\arcsin(-1)=\pi$."],
    lambda: same(sp.integrate(1/sp.sqrt(1 - theta**2), (theta, -1, 1)), sp.pi), 10, "exam")
mc3(18, 18, "5.9", "Substitution in definite integrals (theory)", r"If $\displaystyle\int_0^{2a}f(x)\,dx=2\int_0^af(x)\,dx$ for all such $f$-type questions, which condition makes it true: $f(2a-x)=f(x)$, $f(2a-x)=-f(x)$, $f$ odd, $f$ even?",
    r"$f(2a-x)=f(x)$",
    [r"$\int_0^{2a}f=\int_0^af+\int_a^{2a}f$.", r"In $\int_a^{2a}f(x)dx$ put $u=2a-x$: it becomes $\int_0^af(2a-u)\,du$.", r"If $f(2a-u)=f(u)$ the two halves are equal ⇒ total $=2\int_0^af$."],
    None, 10, "hard")

# ------------------------------------------------------------------ Castro Castilla (2017, 2018, 2020)
def castro(id, title, short, kind, year, file, duration, notes, split=True):
    paper(id, title, short, kind, year, "Fall", [(TG + file, "PDF")], False, "Alejandro J. Castro Castilla", duration, notes, split)

castro("f17-m2", "Fall 2017 Midterm 2 · MATH 161 3L · Castro", "F17 MT2", "midterm", 2017, "Fall2017_Midterm2_MATH161_3L.pdf", 50, "4 problems + bonus. No solutions (mine, checked with SymPy).")
S = "f17-m2"; pg = lambda i: PG + "Fall2017_Midterm2_MATH161_3L_p1.png"
P("f17m2-1", S, 1, "3.2", "Logarithmic differentiation", r"(a) For $y=(\sin t)^{\ln t}$ find $dy/dt$. (b) Inverse-function derivative problem with $f(x)=e^{4-x^2}/x$ (see scan).", page=pg(1))
P("f17m2-2", S, 2, "3.5", "Linear approximation", r"Use a local linear approximation to estimate $85^{1/4}$.", r"$\approx3+\frac4{108}\approx3.037$", src=OWN, page=pg(1))
P("f17m2-3", S, 3, "3.6", "L'Hôpital's rule", r"(a) $\displaystyle\lim_{x\to\infty}\left(1+\sin\tfrac3x\right)^x$. (b) Find $k,\ell$ with $\displaystyle\lim_{x\to0}\frac{k+\cos(\ell x)}{x^2}=-4$.", r"(a) $e^3$; (b) $k=-1$, $\ell=\pm2\sqrt2$", src=OWN, page=pg(1))
P("f17m2-4a", S, "4(a)", "4.4", "Absolute extrema on a closed interval", r"Find the absolute maximum and minimum values of $f(x)=3x^{2/3}-2x$ on $[-1,1]$.",
  r"Max $f(-1)=5$; min $f(0)=0$",
  [r"$f'(x)=2x^{-1/3}-2=\dfrac{2(1-x^{1/3})}{x^{1/3}}$.", r"Critical points: $f'=0$ at $x=1$ (an endpoint); $f'$ undefined at $x=0$.",
   r"Values: $f(-1)=3(1)+2=5$, $f(0)=0$, $f(1)=3-2=1$.", r"Absolute max $5$ at $x=-1$, absolute min $0$ at $x=0$."],
  check=lambda: (lambda f: all_true(same(f(-1), 5), same(f(0), 0), same(f(1), 1)))(lambda v: 3*sp.cbrt(sp.Integer(v)**2) - 2*v),
  src=OWN, page=pg(1))
P("f17m2-4b", S, "4(b)", "4.3", "Graphing rational functions", r"Sketch $f(x)=\dfrac{x^3-4x-8}{x+2}$ (vertical and curvilinear asymptotes).", page=pg(1))
P("f17m2-5", S, "5 (bonus)", "4.8", "MVT inequality", r"""(a) Use the Mean-Value Theorem to show that $\sqrt y-\sqrt x<\dfrac{y-x}{2\sqrt x}$ for $0<x<y$.
(b) Use (a) to show that $\sqrt{xy}<\dfrac{x+y}2$ for $0<x<y$.""",
  r"Proof (see steps)",
  [r"(a) $g(s)=\sqrt s$ is continuous on $[x,y]$ and differentiable on $(x,y)$ (since $x>0$).",
   r"MVT: there is $c\in(x,y)$ with $\dfrac{\sqrt y-\sqrt x}{y-x}=g'(c)=\dfrac1{2\sqrt c}$.",
   r"Because $c>x>0$: $\dfrac1{2\sqrt c}<\dfrac1{2\sqrt x}$. Multiply by $y-x>0$: $\sqrt y-\sqrt x<\dfrac{y-x}{2\sqrt x}$. ∎",
   r"(b) Multiply (a) by $2\sqrt x>0$: $2\sqrt{xy}-2x<y-x$, i.e. $2\sqrt{xy}<x+y$, so $\sqrt{xy}<\dfrac{x+y}2$. ∎"],
  check=lambda: all(float(sp.sqrt(b) - sp.sqrt(a)) < float((b - a)/(2*sp.sqrt(a))) for a, b in [(1, 2), (0.3, 5), (4, 9)]), src=OWN, diff="hard", page=pg(1))

castro("f17-fin", "Fall 2017 Final · MATH 161 3L · Castro", "F17 Final", "final", 2017, "Fall2017_FinalExam_MATH161_3L.pdf", 120, "Whole-course final; in-scope parts are problems 4–5.")
S = "f17-fin"; pg = lambda i: PG + f"Fall2017_FinalExam_MATH161_3L_p{i}.png"
P("f17f-1", S, 1, "1.3", "Limits and continuity", r"(a) One-sided limits of $f(x)=\dfrac{x-5}{|x-5|}$; (b) IVT: $x^4+5x^3+5x-1=0$ has two roots in $[-6,2]$.", page=pg(1))
P("f17f-2", S, 2, "2.2", "Derivatives", r"(a) Lines through the origin tangent to $y=x^3-9x^2-16x$. (b) Derivative of $\sqrt{\cos f(x)/\sin g(x)}$.", page=pg(1))
P("f17f-3", S, 3, "3.6", "L'Hôpital's rule", r"(a) $\displaystyle\lim_{x\to0}\frac{2\sin x-\sin2x}{2e^x-2-2x-x^2}$; (b) linearization of $\sqrt{3+x^2}$ at $x_0=1$.", page=pg(1))
P("f17f-4a", S, "4(a)", "4.1", "Curve analysis", r"Analyze where $f(x)=xe^{-x^2}$ is increasing/decreasing and concave up/down, and sketch its graph.",
  r"$\nearrow$ on $\left[-\tfrac1{\sqrt2},\tfrac1{\sqrt2}\right]$, $\searrow$ outside; CU on $\left(-\sqrt{3/2},0\right)\cup\left(\sqrt{3/2},\infty\right)$, CD on $\left(-\infty,-\sqrt{3/2}\right)\cup\left(0,\sqrt{3/2}\right)$",
  [r"$f$ is odd, defined for all $x$, $f(x)\to0$ as $x\to\pm\infty$ (horizontal asymptote $y=0$).",
   r"$f'(x)=e^{-x^2}+x(-2x)e^{-x^2}=(1-2x^2)e^{-x^2}$; zero at $x=\pm\frac1{\sqrt2}$.",
   r"Sign of $1-2x^2$: $+$ between the roots, $-$ outside ⇒ increasing on $[-\frac1{\sqrt2},\frac1{\sqrt2}]$, decreasing on $(-\infty,-\frac1{\sqrt2}]$ and $[\frac1{\sqrt2},\infty)$.",
   r"Rel. max $f(\tfrac1{\sqrt2})=\tfrac1{\sqrt2}e^{-1/2}=\tfrac1{\sqrt{2e}}$, rel. min $f(-\tfrac1{\sqrt2})=-\tfrac1{\sqrt{2e}}$.",
   r"$f''(x)=(-4x)e^{-x^2}+(1-2x^2)(-2x)e^{-x^2}=(4x^3-6x)e^{-x^2}=2x(2x^2-3)e^{-x^2}$; zeros $0,\pm\sqrt{3/2}$.",
   r"Sign table of $2x(2x^2-3)$: $-$ on $(-\infty,-\sqrt{3/2})$, $+$ on $(-\sqrt{3/2},0)$, $-$ on $(0,\sqrt{3/2})$, $+$ on $(\sqrt{3/2},\infty)$.",
   r"Inflection points at $x=0,\pm\sqrt{3/2}$."],
  check=lambda: (lambda f: all_true(same(sp.diff(f, x), (1 - 2*x**2)*sp.exp(-x**2)), same(sp.diff(f, x, 2), 2*x*(2*x**2 - 3)*sp.exp(-x**2))))(x*sp.exp(-x**2)),
  src=OWN, figure="assets/fig/xexp.svg", page=pg(1))
P("f17f-4b", S, "4(b)", "4.4", "Absolute extrema on a closed interval", r"Find the absolute minimum and maximum of $f(x)=x-\tan x$ on $[-\pi/4,\pi/4]$.",
  r"Max $1-\frac\pi4$ at $x=-\frac\pi4$; min $\frac\pi4-1$ at $x=\frac\pi4$",
  [r"$f'(x)=1-\sec^2x=-\tan^2x\le0$; it is $0$ only at $x=0$ (no sign change).", r"So $f$ is decreasing on the whole interval: the max is at the left end, the min at the right end.",
   r"$f(-\tfrac\pi4)=-\tfrac\pi4+1$, $f(\tfrac\pi4)=\tfrac\pi4-1$; also $f(0)=0$ lies between them."],
  check=lambda: (lambda f: all_true(same(sp.diff(f, x), -sp.tan(x)**2), same(f.subs(x, -sp.pi/4), 1 - sp.pi/4)))(x - sp.tan(x)), src=OWN, page=pg(1))
P("f17f-5a", S, "5(a)", "5.5", "Integrals with absolute value", r"Compute $\displaystyle\int_{-3}^{4}\left(|x+1|-|x-1|+|x+2|\right)dx$.",
  r"$\dfrac{41}2$",
  [r"Integrate each term separately, splitting at its zero (or use triangle areas).",
   r"$\int_{-3}^4|x+1|\,dx=\tfrac12(2)^2+\tfrac12(5)^2=2+12.5=14.5$.",
   r"$\int_{-3}^4|x-1|\,dx=\tfrac12(4)^2+\tfrac12(3)^2=8+4.5=12.5$.",
   r"$\int_{-3}^4|x+2|\,dx=\tfrac12(1)^2+\tfrac12(6)^2=0.5+18=18.5$.", r"Total: $14.5-12.5+18.5=20.5=\dfrac{41}2$."],
  check=lambda: defint(sp.Abs(x + 1) - sp.Abs(x - 1) + sp.Abs(x + 2), -3, 4, sp.Rational(41, 2)), src=OWN, page=pg(2))
P("f17f-5b", S, "5(b)", "5.3", "Initial value problem", r"Solve the initial value problem $\dfrac{dy}{dx}=xe^{x^2}$, $y(0)=0$.",
  r"$y=\tfrac12\left(e^{x^2}-1\right)$", [r"$u=x^2$: $\int xe^{x^2}dx=\tfrac12e^{x^2}+C$.", r"$y(0)=\tfrac12+C=0\Rightarrow C=-\tfrac12$."],
  check=lambda: all_true(antideriv((sp.exp(x**2) - 1)/2, x*sp.exp(x**2))), src=OWN, diff="easy", page=pg(2))
P("f17f-5c", S, "5(c)", "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_{e^{-3}}^{e^3}\frac{\sqrt{9-(\ln x)^2}}{x}\,dx$.",
  r"$\dfrac{9\pi}2$", [r"$u=\ln x$, $du=dx/x$; $u:-3\to3$.", r"$\displaystyle\int_{-3}^3\sqrt{9-u^2}\,du$ = area of the upper half-disk of radius 3 $=\tfrac12\pi\cdot9=\tfrac{9\pi}2$."],
  check=lambda: same(sp.integrate(sp.sqrt(9 - u**2), (u, -3, 3)), 9*sp.pi/2), src=OWN, page=pg(2))
P("f17f-5d", S, "5(d)", "5.6", "FTC: derivative of an integral", r"Let $F(x)=\displaystyle\int_0^x\cos(t^2)\,dt$. Find $\dfrac{d}{dx}\left[F(\sqrt x)\right]$.",
  r"$\dfrac{\cos x}{2\sqrt x}$", [r"$F'(x)=\cos(x^2)$ by FTC.", r"Chain rule: $F'(\sqrt x)\cdot\dfrac1{2\sqrt x}=\cos\left((\sqrt x)^2\right)\dfrac1{2\sqrt x}=\dfrac{\cos x}{2\sqrt x}$."],
  check=lambda: antideriv(sp.Integral(sp.cos(t**2), (t, 0, sp.sqrt(x))), sp.cos(x)/(2*sp.sqrt(x))), src=OWN, page=pg(2))
P("f17f-6", S, 6, "6.1", "Area between curves", r"Find a horizontal line $y=k$ that divides the area between $y=x^2$ and $y=9$ into two equal parts.", r"$k=9/2^{2/3}$", src=OWN, page=pg(2))
P("f17f-7", S, "7 (bonus)", "7.7", "Simpson's rule", r"Simpson's rule for $\int_0^2\cos x\,dx$ with error $<10^{-3}$.", page=pg(2))

castro("f18-m2", "Fall 2018 Midterm 2 · MATH 161 1L · Castro", "F18 MT2", "midterm", 2018, "Fall2018_Midterm2_MATH161_1L.pdf", 50, "4 problems + bonus.")
S = "f18-m2"; pg = lambda i: PG + "Fall2018_Midterm2_MATH161_1L_p1.png"
P("f18m2-1", S, 1, "3.3", "Inverse functions", r"$f(x)=e^{9-x^2}/x$, $x>0$: show $f$ is one-to-one; compute $F'(1/3)$ for $F(x)=f([g(x)]^3)$, $g=f^{-1}$.", page=pg(1))
P("f18m2-2", S, 2, "3.6", "L'Hôpital's rule", r"(a) $\displaystyle\lim_{x\to0^+}\left(\frac1x-\frac1{\sin x}\right)$; (b) $\displaystyle\lim_{x\to0^+}x^{\sqrt x}$.", r"(a) $0$; (b) $1$", src=OWN, page=pg(1))
P("f18m2-3", S, 3, "4.5", "Optimization", r"""A rectangle $R$ has corners $(\pm8,\pm12)$. A $100\times100$ square $S$ has sides parallel to the axes and its lower-left corner on the line $y=-6x$.
What is the largest possible area of the region contained in both $R$ and $S$?""",
  r"$144$ (lower-left corner at $(2,-12)$)",
  [r"Let the lower-left corner be $(a,-6a)$. The square is huge, so it covers everything of $R$ to the right of $x=a$ and above $y=-6a$.",
   r"Overlap needs $a<8$ and $-6a<12$, i.e. $a>-2$.",
   r"For $-2\le a\le2$ (so $-12\le-6a\le12$): $A(a)=(8-a)(12+6a)=96+36a-6a^2$.",
   r"For $2\le a<8$ the corner is below $R$: $A(a)=24(8-a)$, decreasing in $a$.",
   r"On $[-2,2]$: $A'(a)=36-12a>0$ (critical point $a=3$ is outside), so $A$ increases and is largest at $a=2$: $A(2)=6\cdot24=144$.",
   r"Combining both pieces, the maximum overlap is $144$ at $a=2$."],
  check=lambda: same(((8 - k)*(12 + 6*k)).subs(k, 2), 144) and sp.solve(sp.diff((8 - k)*(12 + 6*k), k), k) == [3], src=OWN, diff="hard", page=pg(1))
P("f18m2-4", S, 4, "4.3", "Graphing rational functions", r"Sketch $f(x)=\dfrac{x^2+2x+4}{2x}$.", page=pg(1))
P("f18m2-5", S, "5 (bonus)", "4.7", "Newton's method", r"$p(x)=x^3-x-1$: find an interval of length 1 containing a root (IVT) and do five Newton iterations.", page=pg(1))

castro("f18-fin", "Fall 2018 Final · MATH 161 1L · Castro", "F18 Final", "final", 2018, "Fall2018_FinalExam_MATH161_1L.pdf", 120,
       "Whole-course final (header date says Nov 28, 2017 although the file is named Fall 2018).")
S = "f18-fin"; pg = lambda i: PG + f"Fall2018_FinalExam_MATH161_1L_p{i}.png"
P("f18f-1", S, 1, "1.5", "Limits and continuity", r"(a) Continuity of $|x|/|x+1|$; (b) true/false about $\lim(f+g)$.", page=pg(1))
P("f18f-2", S, 2, "2.2", "Derivatives", r"(a) $\lim_{x\to2}\frac{x^3f(x)-24}{x-2}=28$: find $f(2),f'(2)$; (b) derivative of $f(x+g(x)^2)$.", page=pg(1))
P("f18f-3", S, 3, "3.6", "L'Hôpital's rule", r"(a) $\displaystyle\lim_{t\to0}\frac{3\sin t-\sin3t}{3\tan t-\tan3t}$; (b) logarithmic differentiation of $\left(\frac{x^2-1}{x^2+1}\right)^{3/2}$.", page=pg(1))
P("f18f-4a", S, "4(a)", "4.2", "Curve sketching", r"Sketch the graph of $f(x)=2x+3x^{2/3}$.",
  r"$\nearrow(-\infty,-1]$, $\searrow[-1,0]$, $\nearrow[0,\infty)$; rel. max $f(-1)=1$, rel. min $f(0)=0$ (cusp); concave down on $(-\infty,0)$ and $(0,\infty)$; zeros $x=-\tfrac{27}8,0$",
  [r"$f'(x)=2+2x^{-1/3}=\dfrac{2(x^{1/3}+1)}{x^{1/3}}$: zero at $x=-1$, undefined at $x=0$.",
   r"Signs: $x<-1$: $\frac{-}{-}=+$; $-1<x<0$: $\frac{+}{-}=-$; $x>0$: $+$.",
   r"Rel. max $f(-1)=-2+3=1$; rel. min $f(0)=0$ — a cusp, since $f'\to-\infty$ from the left and $+\infty$ from the right.",
   r"$f''(x)=-\tfrac23x^{-4/3}<0$ for $x\ne0$ ⇒ concave down on both sides, no inflection point.",
   r"Intercepts: $x^{2/3}(2x^{1/3}+3)=0\Rightarrow x=0$ or $x=-\tfrac{27}8$. As $x\to\pm\infty$, $f\to\pm\infty$."],
  check=lambda: (lambda f: all_true(same(f.subs(x, -1), 1), same(f.subs(x, sp.Rational(-27, 8)), 0), same(sp.diff(f, x).subs(x, -1), 0)))(2*x + 3*sp.real_root(x**2, 3)),
  src=OWN, note="The cusp at $x=0$ is §4.3 material; the rest is §4.1–4.2.", figure="assets/fig/cusp_2x3x23.svg", page=pg(1))
P("f18f-4b", S, "4(b)", "4.5", "Optimization", r"""Find the $x$-coordinate of the point $P$ on the parabola $y=1-x^2$, $0<x\le1$, for which the triangle enclosed by the tangent line at $P$ and the coordinate axes has the smallest area.""",
  r"$x=\dfrac1{\sqrt3}$ (area $\frac{4\sqrt3}9$)",
  [r"$P=(a,1-a^2)$, slope $-2a$. Tangent: $y=1-a^2-2a(x-a)=1+a^2-2ax$.",
   r"Intercepts: $y$-int $1+a^2$, $x$-int $\dfrac{1+a^2}{2a}$.", r"Area $A(a)=\dfrac12\cdot\dfrac{1+a^2}{2a}(1+a^2)=\dfrac{(1+a^2)^2}{4a}$, $0<a\le1$.",
   r"$A'(a)=\dfrac{(1+a^2)(3a^2-1)}{4a^2}=0\Rightarrow a=\dfrac1{\sqrt3}$.",
   r"$A'<0$ for $a<\frac1{\sqrt3}$ and $>0$ after ⇒ minimum; compare $A(1)=1>A(\tfrac1{\sqrt3})=\tfrac{4\sqrt3}9\approx0.77$."],
  check=lambda: (lambda A: all_true(same(sp.solve(sp.diff(A, x), x)[0] if len(sp.solve(sp.diff(A, x), x)) == 1 else [r for r in sp.solve(sp.diff(A, x), x) if r.is_positive][0], 1/sp.sqrt(3)), same(A.subs(x, 1/sp.sqrt(3)), 4*sp.sqrt(3)/9)))((1 + x**2)**2/(4*x)),
  src=OWN, diff="hard", page=pg(1))
P("f18f-5a", S, "5(a)", "5.9", "Definite integrals (substitution + geometry)", r"Compute $\displaystyle\int_0^3\left(x\sqrt{x^2+1}-\sqrt{9-x^2}\right)dx$.",
  r"$\dfrac{10\sqrt{10}-1}3-\dfrac{9\pi}4$",
  [r"$\int_0^3x\sqrt{x^2+1}\,dx$: $u=x^2+1$, $\tfrac12\int_1^{10}u^{1/2}du=\tfrac13\left(10^{3/2}-1\right)$.", r"$\int_0^3\sqrt{9-x^2}\,dx$ = quarter disk of radius 3 $=\tfrac{9\pi}4$.", r"Difference: $\dfrac{10\sqrt{10}-1}3-\dfrac{9\pi}4$."],
  check=lambda: numint(x*sp.sqrt(x**2 + 1) - sp.sqrt(9 - x**2), 0, 3, (10*sp.sqrt(10) - 1)/3 - 9*sp.pi/4), src=OWN, page=pg(2))
P("f18f-5b", S, "5(b)", "5.2", "Initial value problem", r"Find the curve whose slope at each point $(x,y)$ is $(x+1)^2$ and which passes through $(-2,8)$.",
  r"$y=\dfrac{(x+1)^3}3+\dfrac{25}3$", [r"$y=\int(x+1)^2dx=\dfrac{(x+1)^3}3+C$.", r"$8=\dfrac{(-1)^3}3+C\Rightarrow C=\dfrac{25}3$."],
  check=lambda: (lambda Y: all_true(antideriv(Y, (x + 1)**2), same(Y.subs(x, -2), 8)))((x + 1)**3/3 + sp.Rational(25, 3)), src=OWN, diff="easy", page=pg(2))
P("f18f-5c", S, "5(c)", "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_{\ln2}^{\ln(2/\sqrt3)}\frac{e^{-x}}{\sqrt{1-e^{-2x}}}\,dx$.",
  r"$-\dfrac\pi6$", [r"$u=e^{-x}$, $du=-e^{-x}dx$; $x=\ln2\to u=\tfrac12$, $x=\ln\tfrac2{\sqrt3}\to u=\tfrac{\sqrt3}2$.",
   r"$=-\displaystyle\int_{1/2}^{\sqrt3/2}\frac{du}{\sqrt{1-u^2}}=-\left(\arcsin\tfrac{\sqrt3}2-\arcsin\tfrac12\right)=-\left(\tfrac\pi3-\tfrac\pi6\right)=-\tfrac\pi6.$",
   r"(Negative because the upper limit $\ln(2/\sqrt3)$ is smaller than the lower limit $\ln 2$.)"],
  check=lambda: numint(sp.exp(-x)/sp.sqrt(1 - sp.exp(-2*x)), sp.log(2), sp.log(2/sp.sqrt(3)), -sp.pi/6), src=OWN, page=pg(2))
P("f18f-5d", S, "5(d)", "5.6", "FTC: derivative of an integral", r"Find $\dfrac{d}{dt}\displaystyle\int_{-\pi}^{t}\frac{\cos y}{1+y^2}\,dy$.",
  r"$\dfrac{\cos t}{1+t^2}$", [r"FTC part 2 with a constant lower limit: just substitute $t$."], check=lambda: antideriv(sp.Integral(sp.cos(y)/(1 + y**2), (y, -sp.pi, x)), sp.cos(x)/(1 + x**2)), src=OWN, diff="easy", page=pg(2))
P("f18f-6", S, 6, "6.1", "Area between curves", r"Find the area enclosed by $f(x)=\dfrac2{1+x^2}$ and $g(x)=|x|$.", r"$\pi-1$", src=OWN, page=pg(2))
P("f18f-7", S, "7 (bonus)", "6.4", "Arc length", r"Length of $y=x^4+\dfrac1{32x^2}$ on $[1,2]$.", page=pg(2))

castro("f20-m2", "Fall 2020 Midterm 2 · MATH 161 9L · Castro", "F20 MT2", "midterm", 2020, "Fall2020_Midterm2_MATH161_9L.pdf", 50, "Ch. 2–4 (mostly Ch. 3).")
S = "f20-m2"; pg = lambda i: PG + "Fall2020_Midterm2_MATH161_9L_p1.png"
P("f20m2-1", S, 1, "2.6", "Chain rule", r"(a) $f'(1)$ for a nested power; (b) horizontal tangents of $\dfrac{\sec x}{1+\tan x}$.", page=pg(1))
P("f20m2-2", S, 2, "3.1", "Implicit differentiation", r"(a) $y'$ if $\sin(x+y)=y^2\cos x$; (b) derivative of $\csc^{-1}x$.", page=pg(1))
P("f20m2-3", S, 3, "3.5", "Linear approximation", r"Estimate $\cot 46^\circ$ by local linear approximation.", page=pg(1))
P("f20m2-4", S, 4, "3.6", "L'Hôpital's rule", r"(a) $\displaystyle\lim_{x\to1^-}\frac{\ln\sin\pi x}{\csc\pi x}$; (b) $\displaystyle\lim_{x\to1}(x^2-2x+1)^{x-1}$.", page=pg(1))
P("f20m2-5", S, 5, "4.3", "Graphing with cusps", r"Graph $f(x)=(1+x)^{2/3}(3-x)^{1/3}$: relative extrema, inflection points, asymptotes, monotonicity, concavity.", page=pg(1),
  note="Uses cusps / vertical tangents and an oblique asymptote, i.e. §4.3 material.")

castro("f20-m3", "Fall 2020 Midterm 3 · MATH 161 9L · Castro", "F20 MT3", "midterm", 2020, "Fall2020_Midterm3_MATH161_9L.pdf", 50, "Ch. 4–5. The closest old paper to our Exam 2 topics.")
S = "f20-m3"; pg = lambda i: PG + "Fall2020_Midterm3_MATH161_9L_p1.png"
P("f20m3-1", S, 1, "4.5", "Optimization", r"Design a one-liter oil can shaped like a right circular cylinder. What dimensions use the least material?",
  r"$r=\sqrt[3]{500/\pi}\approx5.42$ cm, $h=2r\approx10.84$ cm",
  [r"Volume $1\ \text{L}=1000\ \text{cm}^3$: $\pi r^2h=1000\Rightarrow h=\dfrac{1000}{\pi r^2}$.", r"Material = surface area $S=2\pi r^2+2\pi rh=2\pi r^2+\dfrac{2000}r$, $r>0$.",
   r"$S'(r)=4\pi r-\dfrac{2000}{r^2}=0\Rightarrow r^3=\dfrac{500}\pi$.", r"$S''(r)=4\pi+\dfrac{4000}{r^3}>0$ ⇒ minimum (absolute: only critical point, $S\to\infty$ at both ends).",
   r"$h=\dfrac{1000}{\pi r^2}=\dfrac{2\cdot500}{\pi r^3}\,r=2r$: height equals the diameter."],
  check=lambda: (lambda r: same(1000/(sp.pi*r**2), 2*r))(sp.cbrt(500/sp.pi)), src=OWN, page=pg(1))
P("f20m3-2", S, 2, "4.7", "Newton's method", r"$e^{5-x}=10-x$: number of solutions and Newton approximations.", page=pg(1))
P("f20m3-3", S, 3, "4.8", "MVT inequality", r"Use the Mean Value Theorem to show that $\sqrt{1+x}<1+\dfrac x2$ for $x>0$.",
  r"Proof (see steps)",
  [r"Let $f(s)=\sqrt{1+s}$ on $[0,x]$, $x>0$: continuous on $[0,x]$, differentiable on $(0,x)$.",
   r"MVT: $\dfrac{\sqrt{1+x}-1}{x-0}=f'(c)=\dfrac1{2\sqrt{1+c}}$ for some $c\in(0,x)$.",
   r"Since $c>0$: $\sqrt{1+c}>1$, so $f'(c)<\dfrac12$.", r"Hence $\sqrt{1+x}-1<\dfrac x2$, i.e. $\sqrt{1+x}<1+\dfrac x2$. ∎"],
  check=lambda: all(float(sp.sqrt(1 + v)) < 1 + v/2 for v in [0.01, 1, 10, 100]), src=OWN, page=pg(1))
P("f20m3-4", S, 4, "5.3", "u-substitution", r"By an appropriate substitution compute $\displaystyle\int\sqrt{1+x^2}\,x^5\,dx$.",
  r"$\dfrac17(1+x^2)^{7/2}-\dfrac25(1+x^2)^{5/2}+\dfrac13(1+x^2)^{3/2}+C$",
  [r"$u=1+x^2$, $du=2x\,dx$, and $x^4=(u-1)^2$.", r"$\displaystyle\int x^4\sqrt{1+x^2}\,x\,dx=\frac12\int(u-1)^2u^{1/2}du=\frac12\int\left(u^{5/2}-2u^{3/2}+u^{1/2}\right)du.$",
   r"$=\dfrac12\left(\dfrac27u^{7/2}-\dfrac45u^{5/2}+\dfrac23u^{3/2}\right)+C$.", r"$=\dfrac17u^{7/2}-\dfrac25u^{5/2}+\dfrac13u^{3/2}+C$ with $u=1+x^2$."],
  check=lambda: (lambda U: antideriv(U**sp.Rational(7, 2)/7 - sp.Rational(2, 5)*U**sp.Rational(5, 2) + U**sp.Rational(3, 2)/3, sp.sqrt(1 + x**2)*x**5))(1 + x**2), src=OWN, page=pg(1))
P("f20m3-5", S, 5, "5.4", "Riemann sum → definite integral", r"Calculate $\displaystyle\int_0^3(x^3-6x)\,dx$ using a Riemann sum with equal subintervals and right endpoints $x_k^*$.",
  r"$-\dfrac{27}4$",
  [r"$\Delta x=\dfrac3n$, $x_k^*=\dfrac{3k}n$.", r"$f(x_k^*)\Delta x=\left(\dfrac{27k^3}{n^3}-\dfrac{18k}n\right)\dfrac3n=\dfrac{81k^3}{n^4}-\dfrac{54k}{n^2}$.",
   r"Use $\sum k=\dfrac{n(n+1)}2$, $\sum k^3=\left[\dfrac{n(n+1)}2\right]^2$: $\ \dfrac{81}{n^4}\cdot\dfrac{n^2(n+1)^2}4-\dfrac{54}{n^2}\cdot\dfrac{n(n+1)}2$.",
   r"$=\dfrac{81}4\left(1+\dfrac1n\right)^2-27\left(1+\dfrac1n\right)\ \to\ \dfrac{81}4-27=-\dfrac{27}4$ as $n\to\infty$."],
  check=lambda: same(sp.limit(sp.summation(((3*k/n)**3 - 6*(3*k/n))*3/n, (k, 1, n)), n, sp.oo), sp.Rational(-27, 4)), src=OWN, page=pg(1))

castro("f20-fin", "Fall 2020 Final · MATH 161 9L · Castro", "F20 Final", "final", 2020, "Fall2020_FinalExam_MATH161_9L.pdf", 120, "Whole-course final; problem 5 is in scope.")
S = "f20-fin"; pg = lambda i: PG + f"Fall2020_FinalExam_MATH161_9L_p{i}.png"
P("f20f-1", S, 1, "1.3", "Limits and continuity", r"(a) $\displaystyle\lim_{x\to\infty}\frac{(2x-1)^5}{(3x^2+7x-9)(2x^3-8x)}$; (b) discontinuities of $\dfrac{x+3}{|x^2+3x|}$.", page=pg(1))
P("f20f-2", S, 2, "2.2", "Derivatives", r"(a) continuity/differentiability of a piecewise function; (b) tangent slope of $x^2$ at $(a+b)/2$ equals the secant slope.", page=pg(1))
P("f20f-3", S, 3, "3.1", "Implicit differentiation", r"Point in the first quadrant where the tangent to $x^3-xy+y^3=0$ is horizontal.", page=pg(1))
P("f20f-4", S, 4, "4.3", "Graphing rational functions", r"Graph $f(x)=\dfrac{2x^3+x^2-15x+7}{(2x-1)(3x^2+x-1)}$ with extrema and asymptotes.", page=pg(1))
P("f20f-5a", S, "5(a)", "5.3", "Initial value problem", r"Solve the initial-value problem $y'(x)=xe^{x^2}$, $y(0)=0$.",
  r"$y=\tfrac12\left(e^{x^2}-1\right)$", [r"$\int xe^{x^2}dx=\tfrac12e^{x^2}+C$ ($u=x^2$).", r"$y(0)=0\Rightarrow C=-\tfrac12$."],
  check=lambda: antideriv((sp.exp(x**2) - 1)/2, x*sp.exp(x**2)), src=OWN, diff="easy", page=pg(2), tags=["duplicate of F17 Final 5(b)"])
P("f20f-5b", S, "5(b)", "5.6", "FTC: find f and a", r"Find a function $f$ and a number $a$ such that $2+\displaystyle\int_a^xf(t)\,dt=e^{3x}$.",
  r"$f(x)=3e^{3x}$, $a=\dfrac{\ln2}3$",
  [r"Differentiate both sides (FTC): $f(x)=3e^{3x}$.", r"Put $x=a$: the integral vanishes, so $2=e^{3a}\Rightarrow a=\dfrac{\ln 2}3$."],
  check=lambda: same(2 + sp.integrate(3*sp.exp(3*t), (t, sp.log(2)/3, x)), sp.exp(3*x)), src=OWN, page=pg(2))
P("f20f-6", S, 6, "6.1", "Area between curves", r"Sketch and find the area enclosed by $y=\dfrac2{1+x^2}$ and $y=|x|$.", r"$\pi-1$", src=OWN, page=pg(2))

# ------------------------------------------------------------------ Exam-1-only papers (listed, not split)
for pid, title, short, year, f in [
    ("f25-t1", "Fall 2025 Test 1 · Achenef (two versions)", "F25 T1", 2025, "Fall2025_Midterm1_Achenef_MATH161.pdf"),
    ("f24-m1", "Fall 2024 Midterm 1", "F24 MT1", 2024, "Midterm 1.pdf"),
    ("f20-m1", "Fall 2020 Midterm 1 · Castro", "F20 MT1", 2020, "Fall2020_Midterm1_MATH161_9L.pdf"),
    ("f18-m1", "Fall 2018 Midterm 1 · Castro", "F18 MT1", 2018, "Fall2018_Midterm1_MATH161_1L.pdf"),
    ("f17-m1", "Fall 2017 Midterm 1 · Castro", "F17 MT1", 2017, "Fall2017_Midterm1_MATH161_3L.pdf")]:
    files = [(TG + f, "PDF")]
    if pid == "f25-t1":
        files.append((TG + "Test_1_Version_A_Math_161_calc1_Solution.pdf", "Version A with solutions"))
    paper(pid, title, short, "midterm", year, "Fall", files, pid == "f25-t1", None, None,
          "Exam 1 material (limits, continuity, derivatives — Ch. 1–3). Out of scope, so it is not split into problems.", split=False)
