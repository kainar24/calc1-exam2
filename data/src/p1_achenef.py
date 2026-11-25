# Papers written by our instructor Achenef Tesfahun (Fall 2025 tests, Fall 2022 exam 3) — Telegram "MATH 161 All Sections".
from pkit import *

TG = "materials/telegram/MATH161_All_Sections/"
PG = "assets/pages/"

# ------------------------------------------------------------------ Fall 2025 Test 2, version A
paper("f25-t2a", "Fall 2025 Test 2 · Version A (10:00) · Achenef", "F25 T2-A", "midterm", 2025, "Fall",
      [(TG + "Fall2025_Midterm2_Achenef_MATH161.pdf", "PDF with solutions")], True, "Achenef Tesfahun", 75,
      "Last year's Test 2: §3.4–3.6 (out of scope now) + §4.1, 4.5, 4.6, 4.8. 6 MC + 4 open problems, 80 pts.")
S = "f25-t2a"
pg = lambda i: PG + f"Fall2025_Midterm2_Achenef_MATH161_p{i}.png"
P("f25t2a-1", S, 1, "3.4", "Related rates", r"A spherical balloon is inflated so that its radius increases at 3 cm/min. At what rate is the volume increasing when $r=5$ cm?",
  r"$300\pi$ cm³/min", page=pg(2), mc=True, diff="easy", points=5)
P("f25t2a-2", S, 2, "4.6", "Rectilinear motion", r"""A particle moves along a straight line with position $s(t)=\tfrac12 t^3-3t^2+4t$ (meters, seconds).
Find the particle's velocity at the instant when its acceleration is $6\ \text{m/s}^2$.""",
  r"$v=4$ m/s",
  [r"$v(t)=s'(t)=\tfrac32t^2-6t+4,\qquad a(t)=v'(t)=3t-6.$",
   r"$a(t)=6 \Rightarrow 3t-6=6 \Rightarrow t=4$ s.",
   r"$v(4)=\tfrac32\cdot16-24+4=24-24+4=4$ m/s."],
  check=lambda: (lambda s: same(sp.diff(s, t).subs(t, sp.solve(sp.Eq(sp.diff(s, t, 2), 6), t)[0]), 4))(t**3/2 - 3*t**2 + 4*t),
  page=pg(2), mc=True, diff="easy", points=5)
P("f25t2a-3", S, 3, "4.8", "Mean Value Theorem", r"Find the value(s) $c$ that satisfy the conclusion of the Mean Value Theorem for $f(x)=x^2-2x$ on $[-3,5]$.",
  r"$c=1$",
  [r"$f$ is a polynomial, so it is continuous on $[-3,5]$ and differentiable on $(-3,5)$: MVT applies.",
   r"Secant slope: $\dfrac{f(5)-f(-3)}{5-(-3)}=\dfrac{15-15}{8}=0.$",
   r"$f'(c)=2c-2=0\Rightarrow c=1\in(-3,5).$"],
  check=lambda: same(sp.solve(sp.Eq(2*x - 2, ((x**2-2*x).subs(x, 5)-(x**2-2*x).subs(x, -3))/8), x)[0], 1),
  page=pg(2), mc=True, diff="easy", points=5)
P("f25t2a-4", S, 4, "3.2", "Logarithmic differentiation", r"Find $dy/dx$ by logarithmic differentiation: $y=\dfrac{\sin x\,\tan^2x}{\sqrt x}$.",
  r"$y'=y\left(\cot x+\dfrac{2\sec^2x}{\tan x}-\dfrac1{2x}\right)$", page=pg(2), mc=True, diff="easy", points=5)
P("f25t2a-5", S, 5, "4.1", "Reading f′ graph", r"""The graph of the derivative $f'(x)$ is shown (it has a simple zero at $x=-2$, a local max at $x=-1$, and touches the $x$-axis at $x=1$;
it matches $f'(x)=(x+2)(x-1)^2$). On which intervals is $f$ increasing?""",
  r"$[-2,\infty)$",
  [r"$f$ increases where $f'\ge 0$. From the graph, $f'<0$ only for $x<-2$; at $x=1$ it touches $0$ but does not change sign.",
   r"So $f$ is increasing on $[-2,\infty)$ (and decreasing on $(-\infty,-2]$)."],
  check=lambda: sp.solve_univariate_inequality((x+2)*(x-1)**2 >= 0, x, relational=False) == sp.Interval(-2, sp.oo),
  figure="assets/fig/fprime_t2a.svg", page=pg(3), mc=True, diff="easy", points=5)
P("f25t2a-6", S, 6, "4.1", "Reading f′ graph", r"Same graph of $f'(x)$ as in Problem 5. On which intervals is $f$ concave down?",
  r"$(-1,1)$",
  [r"$f$ is concave down where $f''<0$, i.e. where $f'$ is <b>decreasing</b>.",
   r"From the graph $f'$ rises up to $x=-1$, falls on $(-1,1)$ and rises again after $x=1$.",
   r"So $f$ is concave down on $(-1,1)$ (concave up on $(-\infty,-1)$ and $(1,\infty)$)."],
  check=lambda: sp.solve_univariate_inequality(sp.diff((x+2)*(x-1)**2, x) < 0, x, relational=False) == sp.Interval.open(-1, 1),
  figure="assets/fig/fprime_t2a.svg", page=pg(3), mc=True, diff="easy", points=5)
P("f25t2a-7", S, 7, "3.1", "Implicit differentiation", r"Find all points on the ellipse $x^2-xy+y^2=1$ where the tangent line is horizontal.",
  r"$\left(\tfrac1{\sqrt3},\tfrac2{\sqrt3}\right),\ \left(-\tfrac1{\sqrt3},-\tfrac2{\sqrt3}\right)$", page=pg(4), points=12)
P("f25t2a-8", S, 8, "3.5", "Linear approximation", r"Find the local linear approximation of $y=\dfrac1{\sqrt{2-x}}$ at $x_0=1$ and use it to approximate $\dfrac1{\sqrt{1.1}}$.",
  r"$f(x)\approx1+\tfrac12(x-1)$; $\ \dfrac1{\sqrt{1.1}}\approx0.95$", page=pg(5), points=12)
P("f25t2a-9", S, 9, "3.6", "L'Hôpital's rule", r"Evaluate $\displaystyle\lim_{x\to0}(1+2x)^{-3/x}$.", r"$e^{-6}$", page=pg(6), points=13)
P("f25t2a-10", S, 10, "4.5", "Optimization", r"""A rectangular box without a top must have a volume of $8\ \text{m}^3$. The length of the base is twice its width.
The material for the base costs 3 dollars per m², the material for the sides costs 4 dollars per m².
Find the width of the box that minimizes the total cost of materials. Show that your answer is a minimum.""",
  r"$w=2$ m (then $\ell=4$ m, $h=1$ m, minimal cost 72 dollars)",
  [r"Variables: width $w$, length $\ell=2w$, height $h$ (all $>0$). Volume: $V=\ell wh=2w^2h=8\Rightarrow h=\dfrac4{w^2}$.",
   r"Areas: base $\ell w=2w^2$; sides (no top) $2wh+2\ell h=2wh+4wh=6wh$.",
   r"Cost: $C=3(2w^2)+4(6wh)=6w^2+24wh=6w^2+\dfrac{96}{w},\quad w>0.$",
   r"$C'(w)=12w-\dfrac{96}{w^2}=0\Rightarrow 12w^3=96\Rightarrow w^3=8\Rightarrow w=2.$",
   r"$C''(w)=12+\dfrac{192}{w^3}$, $C''(2)=36>0$ → local min. Since $C\to\infty$ as $w\to0^+$ and as $w\to\infty$, and $w=2$ is the only critical point, it is the absolute minimum.",
   r"Width $w=2$ m (length 4 m, height 1 m, cost $C(2)=24+48=72$ dollars)."],
  check=lambda: (lambda C: all_true(crit(C, w) == [2], sp.diff(C, w, 2).subs(w, 2) > 0, same(C.subs(w, 2), 72)))(6*w**2 + 96/w),
  page=pg(7), points=13)

# ------------------------------------------------------------------ Fall 2025 Test 2, version B
paper("f25-t2b", "Fall 2025 Test 2 · Version B (12:00) · Achenef", "F25 T2-B", "midterm", 2025, "Fall",
      [(TG + "Solution_Test_2_Math_161_calc1_Version_B_12_00.pdf", "PDF with solutions")], True, "Achenef Tesfahun", 75,
      "Twin of Version A with other numbers.")
S = "f25-t2b"
pg = lambda i: PG + f"Solution_Test_2_Math_161_calc1_Version_B_12_00_p{i}.png"
P("f25t2b-1", S, 1, "3.4", "Related rates", r"A spherical balloon's volume increases at $300\pi$ cm³/min. How fast is the radius increasing when $r=5$ cm?",
  r"$3$ cm/min", page=pg(2), mc=True, diff="easy", points=5)
P("f25t2b-2", S, 2, "4.6", "Rectilinear motion", r"A particle moves along a line with $s(t)=t^3-6t^2+9t$ (m, s). Find its velocity at the instant when its acceleration is $6\ \text{m/s}^2$.",
  r"$v=0$ m/s",
  [r"$v(t)=3t^2-12t+9,\qquad a(t)=6t-12.$", r"$a=6\Rightarrow 6t-12=6\Rightarrow t=3.$", r"$v(3)=27-36+9=0$ m/s (the particle is momentarily at rest)."],
  check=lambda: (lambda s: same(sp.diff(s, t).subs(t, sp.solve(sp.Eq(sp.diff(s, t, 2), 6), t)[0]), 0))(t**3 - 6*t**2 + 9*t),
  page=pg(2), mc=True, diff="easy", points=5)
P("f25t2b-3", S, 3, "4.8", "Mean Value Theorem", r"Find the value(s) $c$ that satisfy the conclusion of the MVT for $f(x)=x^2-4x$ on $[-2,6]$.",
  r"$c=2$",
  [r"Polynomial ⇒ continuous on $[-2,6]$, differentiable on $(-2,6)$.", r"Secant slope $\dfrac{f(6)-f(-2)}{8}=\dfrac{12-12}{8}=0$.", r"$f'(c)=2c-4=0\Rightarrow c=2$."],
  check=lambda: same(sp.solve(sp.Eq(2*x - 4, ((x**2-4*x).subs(x, 6)-(x**2-4*x).subs(x, -2))/8), x)[0], 2),
  page=pg(2), mc=True, diff="easy", points=5)
P("f25t2b-4", S, 4, "3.2", "Logarithmic differentiation", r"Find $dy/dx$ by logarithmic differentiation: $y=\dfrac{\sqrt[4]{x}}{\sin^2x\,\tan x}$.",
  r"$y'=y\left(\dfrac1{4x}-2\cot x-\dfrac{\sec^2x}{\tan x}\right)$", page=pg(2), mc=True, diff="easy", points=5)
P("f25t2b-5", S, 5, "4.1", "Reading f′ graph", r"The graph of $f'(x)$ is given in the original paper (see scan; it is $\le 0$ for $x\ge-2$). On which intervals is $f$ decreasing?",
  r"$[-2,\infty)$", [r"$f$ decreases where $f'\le0$; from the graph that is $x\ge-2$ (the double zero at $x=1$ does not change the sign)."],
  page=pg(3), mc=True, diff="easy", points=5, unverified="Graph read from the scan only.")
P("f25t2b-6", S, 6, "4.1", "Reading f′ graph", r"Same graph of $f'$ (see scan). On which intervals is $f$ concave up?",
  r"$(-1,1)$", [r"$f$ is concave up where $f'$ is increasing; on the graph $f'$ rises between its turning points $x=-1$ and $x=1$."],
  page=pg(3), mc=True, diff="easy", points=5, unverified="Graph read from the scan only.")
P("f25t2b-7", S, 7, "3.1", "Implicit differentiation", r"Find the tangent line to $y^3+yx^2+x^2-3y^2=0$ at $(0,3)$.", r"$y=3$", page=pg(4), points=12)
P("f25t2b-8", S, 8, "3.5", "Linear approximation", r"Find the local linear approximation of $y=\dfrac1{\sqrt{1-x}}$ at $x_0=0$; use it to approximate $\dfrac1{\sqrt{0.9}}$.",
  r"$1+\tfrac x2$; $\approx1.05$", page=pg(5), points=12)
P("f25t2b-9", S, 9, "3.6", "L'Hôpital's rule", r"Evaluate $\displaystyle\lim_{x\to0}(e^x+x)^{1/x}$.", r"$e^2$", page=pg(6), points=13)
P("f25t2b-10", S, 10, "4.5", "Optimization", r"""A rectangular box without a top must have volume $16\ \text{m}^3$; the length of the base is twice its width.
Base material costs 2 dollars per m², side material 3 dollars per m². Find the width that minimizes the total cost and show it is a minimum.""",
  r"$w=\sqrt[3]{18}\approx2.62$ m",
  [r"$\ell=2w$, $V=2w^2h=16\Rightarrow h=\dfrac8{w^2}$.",
   r"Cost: $C=2(2w^2)+3(6wh)=4w^2+18wh=4w^2+\dfrac{144}{w}$, $w>0$.",
   r"$C'(w)=8w-\dfrac{144}{w^2}=0\Rightarrow w^3=18\Rightarrow w=\sqrt[3]{18}.$",
   r"$C''(w)=8+\dfrac{288}{w^3}$; at $w^3=18$: $C''=8+16=24>0$ → minimum (only critical point, $C\to\infty$ at both ends ⇒ absolute)."],
  check=lambda: (lambda C: all_true(same(crit(C, w)[0], sp.cbrt(18)), same(sp.diff(C, w, 2).subs(w, sp.cbrt(18)), 24)))(4*w**2 + 144/w),
  page=pg(7), points=13)

# ------------------------------------------------------------------ Fall 2025 Test 3, version A (10:00)
paper("f25-t3a", "Fall 2025 Test 3 · Version A (10:00) · Achenef", "F25 T3-A", "midterm", 2025, "Fall",
      [(TG + "Solution_Test_3_Math_161_calc1_Version_A_10_00Fall25.pdf", "PDF with solutions + marking scheme")], True, "Achenef Tesfahun", 75,
      "Covers Ch. 5 + area/arc length (Ch. 6, out of scope now). Includes the official marking scheme.")
S = "f25-t3a"
pg = lambda i: PG + f"Solution_Test_3_Math_161_calc1_Version_A_10_00Fall25_p{i}.png"
P("f25t3a-1", S, 1, "5.5", "Definite integral as a limit", r"Express $\displaystyle\int_0^3\frac{x}{9x+8}\,dx$ as a limit of Riemann sums (do not evaluate).",
  r"$\displaystyle\lim_{\max\Delta x_k\to0}\sum_{k=1}^{n}\frac{x_k^*}{9x_k^*+8}\,\Delta x_k$ on $[0,3]$",
  [r"Definition: $\displaystyle\int_a^bf(x)\,dx=\lim_{\max\Delta x_k\to0}\sum_{k=1}^n f(x_k^*)\Delta x_k$.",
   r"Here $f(x)=\dfrac{x}{9x+8}$, $a=0$, $b=3$, so the sum is $\sum f(x_k^*)\Delta x_k=\sum\dfrac{x_k^*}{9x_k^*+8}\Delta x_k$ (note: the sum runs to $n$, not to 3, and keeps $\Delta x_k$)."],
  page=pg(2), mc=True, diff="easy", points=5)
P("f25t3a-2", S, 2, "5.5", "Properties of definite integrals", r"Given $\int_{-4}^0f=-2$, $\int_{31}^0f=29$ and $\int_{20}^{31}f=-31$, find $\int_{-4}^{20}f(x)\,dx$.",
  r"$0$",
  [r"$\int_{-4}^{20}f=\int_{-4}^{0}f+\int_{0}^{31}f+\int_{31}^{20}f.$",
   r"$\int_0^{31}f=-\int_{31}^0f=-29,\qquad \int_{31}^{20}f=-\int_{20}^{31}f=31.$",
   r"Total: $-2-29+31=0$."], check=lambda: -2 - 29 + 31 == 0, page=pg(2), mc=True, diff="easy", points=5)
P("f25t3a-3", S, 3, "5.7", "Position from acceleration", r"An object has acceleration $a(t)=-\dfrac4{t^2}$, $t>0$, with $s(1)=2$ and $s(3)=4\ln3$. Find the position function $s(t)$.",
  r"$s(t)=4\ln t-t+3$",
  [r"$v(t)=\int-4t^{-2}\,dt=\dfrac4t+C_1$.", r"$s(t)=\int\left(\dfrac4t+C_1\right)dt=4\ln t+C_1t+C_2$.",
   r"$s(1)=C_1+C_2=2$ and $s(3)=4\ln3+3C_1+C_2=4\ln3\Rightarrow 3C_1+C_2=0$.",
   r"Subtract: $2C_1=-2\Rightarrow C_1=-1,\ C_2=3$. So $s(t)=4\ln t-t+3$."],
  check=lambda: (lambda s: all_true(same(sp.diff(s, t, 2), -4/t**2), same(s.subs(t, 1), 2), same(s.subs(t, 3), 4*sp.log(3))))(4*sp.log(t) - t + 3),
  page=pg(2), mc=True, diff="easy", points=5)
P("f25t3a-4", S, 4, "5.6", "FTC: derivative of an integral", r"Find $\dfrac{d}{dx}\displaystyle\int_1^{x^3}\sin^2t\,dt$.",
  r"$3x^2\sin^2(x^3)$", [r"FTC + chain rule: $\dfrac{d}{dx}\int_a^{g(x)}f(t)\,dt=f(g(x))\,g'(x)$.", r"$=\sin^2(x^3)\cdot3x^2$."],
  check=lambda: same(sp.diff(sp.Integral(sp.sin(t)**2, (t, 1, x**3)).doit(), x), 3*x**2*sp.sin(x**3)**2),
  page=pg(3), mc=True, diff="easy", points=5)
P("f25t3a-5", S, 5, "5.3", "u-substitution", r"Evaluate $\displaystyle\int\frac{x^2}{2+x^6}\,dx$.",
  r"$\dfrac1{3\sqrt2}\arctan\dfrac{x^3}{\sqrt2}+C$",
  [r"Let $u=x^3$, $du=3x^2dx$: $\displaystyle\int\frac{x^2\,dx}{2+x^6}=\frac13\int\frac{du}{2+u^2}.$",
   r"$\displaystyle\int\frac{du}{a^2+u^2}=\frac1a\arctan\frac ua+C$ with $a=\sqrt2$.",
   r"Answer: $\dfrac1{3\sqrt2}\arctan\dfrac{x^3}{\sqrt2}+C$."],
  check=lambda: antideriv(sp.atan(x**3/sp.sqrt(2))/(3*sp.sqrt(2)), x**2/(2 + x**6)),
  page=pg(3), mc=True, diff="easy", points=5,
  solution_note="In the original paper none of the five options was exactly right, and the key accepted every answer (A–E). The correct antiderivative is shown here.")
P("f25t3a-6", S, 6, "5.2", "Antiderivatives (trig)", r"Evaluate $\displaystyle\int\csc x\,(\cot x+\sin x)\,dx$.",
  r"$-\csc x+x+C$", [r"Expand: $\csc x\cot x+\csc x\sin x=\csc x\cot x+1$.", r"$\int\csc x\cot x\,dx=-\csc x$, $\int1\,dx=x$ ⇒ $-\csc x+x+C$."],
  check=lambda: antideriv(-1/sp.sin(x) + x, (1/sp.sin(x))*(sp.cos(x)/sp.sin(x) + sp.sin(x))), page=pg(3), mc=True, diff="easy", points=5)
P("f25t3a-7", S, 7, "5.8", "Average value", r"Find the average value of $f(x)=x^2\sqrt{3x^3+1}$ on $[0,2]$.",
  r"$\dfrac{124}{27}$",
  [r"$f_{\text{ave}}=\dfrac1{2-0}\displaystyle\int_0^2x^2\sqrt{3x^3+1}\,dx.$",
   r"$u=3x^3+1$, $du=9x^2dx$; $x=0\to u=1$, $x=2\to u=25$.",
   r"$\displaystyle\int_0^2x^2\sqrt{3x^3+1}\,dx=\frac19\int_1^{25}u^{1/2}du=\frac19\cdot\frac23\left[u^{3/2}\right]_1^{25}=\frac2{27}(125-1)=\frac{248}{27}.$",
   r"$f_{\text{ave}}=\dfrac12\cdot\dfrac{248}{27}=\dfrac{124}{27}.$"],
  check=lambda: same(sp.integrate(x**2*sp.sqrt(3*x**3 + 1), (x, 0, 2))/2, sp.Rational(124, 27)), page=pg(4), points=12,
  solution_note="Marking scheme: setup 2 pts, substitution 3 pts, evaluation 4 pts, final value 3 pts.")
P("f25t3a-8", S, 8, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_0^{\pi/4}\sec^2x\sqrt{1-\tan^2x}\,dx$.",
  r"$\dfrac\pi4$",
  [r"$u=\tan x$, $du=\sec^2x\,dx$; $x=0\to u=0$, $x=\pi/4\to u=1$.", r"Integral becomes $\displaystyle\int_0^1\sqrt{1-u^2}\,du$.",
   r"$y=\sqrt{1-u^2}$ is the upper unit semicircle, so on $[0,1]$ the integral is the area of a quarter of the unit disk: $\dfrac\pi4$."],
  check=lambda: numint(sp.sec(x)**2*sp.sqrt(1 - sp.tan(x)**2), 0, sp.pi/4, sp.pi/4), page=pg(6), points=12,
  solution_note="Marking scheme: substitution + limits 3, new integral 3, quarter-circle interpretation 3, value 3.")
P("f25t3a-9", S, 9, "6.1", "Area between curves", r"Find the area of the region enclosed by $x=2-y^2$, the $x$-axis and the line $y=-x$.", r"$\dfrac{10}{3}$", page=pg(8), points=13)
P("f25t3a-10", S, 10, "6.4", "Arc length", r"Find the arc length of $y=\tfrac12(e^x+e^{-x})$, $0\le x\le1$.", r"$\tfrac12(e-e^{-1})$", page=pg(10), points=13)

# ------------------------------------------------------------------ Fall 2025 Test 3, 12:00 version
paper("f25-t3b", "Fall 2025 Test 3 · 12:00 version · Achenef", "F25 T3-B", "midterm", 2025, "Fall",
      [(TG + "Fall2025_Midterm3_Achenef_MATH161.pdf", "PDF with solutions")], True, "Achenef Tesfahun", 75,
      "Second version of Test 3 (12:00–13:15, 29 Nov 2025).")
S = "f25-t3b"
pg = lambda i: PG + f"Fall2025_Midterm3_Achenef_MATH161_p{i}.png"
P("f25t3b-1", S, 1, "5.5", "Properties of definite integrals", r"Given $\int_{-3}^0f=5$, $\int_{10}^0f=-7$ and $\int_4^{10}f=12$, find $\int_{-3}^4f(x)\,dx$.",
  r"$0$", [r"$\int_{-3}^4f=\int_{-3}^0f+\int_0^{10}f+\int_{10}^4f$.", r"$\int_0^{10}f=7$, $\int_{10}^4f=-12$.", r"$5+7-12=0$."],
  check=lambda: 5 + 7 - 12 == 0, page=pg(2), mc=True, diff="easy", points=5)
P("f25t3b-2", S, 2, "5.7", "Position from acceleration", r"An object has $a(t)=-\dfrac6{t^2}$, $t>0$, with $s(1)=1$ and $s(2)=6\ln2$. Find $s(t)$.",
  r"$s(t)=6\ln t-t+2$",
  [r"$v=\dfrac6t+C_1$, $s=6\ln t+C_1t+C_2$.", r"$s(1)=C_1+C_2=1$, $s(2)=6\ln2+2C_1+C_2=6\ln2\Rightarrow2C_1+C_2=0$.", r"$C_1=-1$, $C_2=2$."],
  check=lambda: (lambda s: all_true(same(sp.diff(s, t, 2), -6/t**2), same(s.subs(t, 1), 1), same(s.subs(t, 2), 6*sp.log(2))))(6*sp.log(t) - t + 2),
  page=pg(2), mc=True, diff="easy", points=5)
P("f25t3b-3", S, 3, "5.4", "Limit of a Riemann sum", r"Evaluate $\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac1n\left(1-\frac kn\right)$.",
  r"$\dfrac12$",
  [r"$\displaystyle\sum_{k=1}^n\frac1n\left(1-\frac kn\right)=\frac1n\cdot n-\frac1{n^2}\cdot\frac{n(n+1)}2=1-\frac{n+1}{2n}.$",
   r"As $n\to\infty$: $1-\tfrac12=\tfrac12$. (It is the right-endpoint sum of $\int_0^1(1-x)\,dx=\tfrac12$.)"],
  check=lambda: same(sp.limit(sp.summation((1 - k/n)/n, (k, 1, n)), n, sp.oo), sp.Rational(1, 2)), page=pg(2), mc=True, diff="easy", points=5)
P("f25t3b-4", S, 4, "5.3", "u-substitution", r"Evaluate $\displaystyle\int\frac{4x^3}{9+x^8}\,dx$.",
  r"$\dfrac13\arctan\dfrac{x^4}{3}+C$", [r"$u=x^4$, $du=4x^3dx$: $\displaystyle\int\frac{du}{9+u^2}=\frac13\arctan\frac u3+C.$"],
  check=lambda: antideriv(sp.atan(x**4/3)/3, 4*x**3/(9 + x**8)), page=pg(3), mc=True, diff="easy", points=5)
P("f25t3b-5", S, 5, "5.6", "FTC: derivative of an integral", r"Find $\dfrac{d}{dx}\displaystyle\int_1^{\sin x}\sqrt{1+t^2}\,dt$.",
  r"$\cos x\sqrt{1+\sin^2x}$", [r"$f(g(x))g'(x)$ with $g=\sin x$: $\sqrt{1+\sin^2x}\cdot\cos x$."],
  check=lambda: antideriv(sp.Integral(sp.sqrt(1 + t**2), (t, 1, sp.sin(x))), sp.cos(x)*sp.sqrt(1 + sp.sin(x)**2)), page=pg(3), mc=True, diff="easy", points=5)
P("f25t3b-6", S, 6, "5.2", "Antiderivatives (trig)", r"Evaluate $\displaystyle\int\sec x\,(\tan x+\cos x)\,dx$.",
  r"$\sec x+x+C$", [r"$\sec x\tan x+\sec x\cos x=\sec x\tan x+1$.", r"$\int\sec x\tan x\,dx=\sec x$ ⇒ $\sec x+x+C$."],
  check=lambda: antideriv(sp.sec(x) + x, sp.sec(x)*(sp.tan(x) + sp.cos(x))), page=pg(3), mc=True, diff="easy", points=5)
P("f25t3b-7", S, 7, "5.8", "Average value", r"Find the average value of $f(x)=x^3\sqrt{4x^4+1}$ on $[0,2]$.",
  r"$\dfrac{65^{3/2}-1}{48}\approx10.88$",
  [r"$f_{\text{ave}}=\dfrac12\displaystyle\int_0^2x^3\sqrt{4x^4+1}\,dx$.", r"$u=4x^4+1$, $du=16x^3dx$; $u:1\to65$.",
   r"$\displaystyle\int_0^2x^3\sqrt{4x^4+1}\,dx=\frac1{16}\int_1^{65}u^{1/2}du=\frac1{24}\left(65^{3/2}-1\right).$",
   r"$f_{\text{ave}}=\dfrac1{48}\left(65^{3/2}-1\right)\approx10.88.$"],
  check=lambda: same(sp.integrate(x**3*sp.sqrt(4*x**4 + 1), (x, 0, 2))/2, (65**sp.Rational(3, 2) - 1)/48), page=pg(4), points=12)
P("f25t3b-8", S, 8, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_1^e\frac{\sqrt{1-(\ln x)^2}}{x}\,dx$.",
  r"$\dfrac\pi4$",
  [r"$u=\ln x$, $du=dx/x$; $x=1\to u=0$, $x=e\to u=1$.", r"$\displaystyle\int_0^1\sqrt{1-u^2}\,du$ = area of a quarter unit disk $=\dfrac\pi4$.",
   r"(Alternative: $u=\sin\theta$ gives $\int_0^{\pi/2}\cos^2\theta\,d\theta=\pi/4$.)"],
  check=lambda: numint(sp.sqrt(1 - sp.log(x)**2)/x, 1, sp.E, sp.pi/4), page=pg(5), points=12)
P("f25t3b-9", S, 9, "6.1", "Area between curves", r"Find the area in the first quadrant bounded above by $y=\sqrt x$ and below by the $x$-axis and $y=x-2$.", r"$\dfrac{10}3$", page=pg(6), points=13)
P("f25t3b-10", S, 10, "6.4", "Arc length", r"Find the arc length of $y=\dfrac{x^4}{16}+\dfrac1{2x^2}$, $1\le x\le2$.", r"$\dfrac{21}{16}$", page=pg(7), points=13)

# ------------------------------------------------------------------ Fall 2022 Exam 3 (3L) — file "Final math 161 Achenef (2).pdf"
paper("f22-e3", "Fall 2022 Exam 3 · Math 161-3L (file: “Final math 161 Achenef (2)”)", "F22 E3", "midterm", 2022, "Fall",
      [(TG + "Final math 161 Achenef (2).pdf", "PDF with solutions")], True, None, 70,
      "Posted 21 Nov 2026 as “Final math 161 Achenef”, but the header says Exam 3, Math 161-3L, Fall 2022 (25 Nov 2022). Instructor not named in the file.")
S = "f22-e3"
pg = lambda i: PG + f"Final_math_161_Achenef_(2)_p{i}.png"
P("f22e3-1a", S, "1(a)", "3.6", "L'Hôpital's rule", r"Use L'Hospital's rule to evaluate $\displaystyle\lim_{x\to0^+}\sin x\ln x$.", r"$0$", page=pg(1), points=3)
P("f22e3-1b", S, "1(b)", "4.4", "Absolute extrema on a closed interval", r"Find the absolute maximum and minimum values of $f(x)=x^3-3x^2+1$ on $-\tfrac12\le x\le4$.",
  r"Max $f(4)=17$, min $f(2)=-3$",
  [r"$f$ is continuous on the closed interval ⇒ the Extreme Value Theorem applies.", r"$f'(x)=3x^2-6x=3x(x-2)=0\Rightarrow x=0,\ x=2$ (both inside).",
   r"Values: $f(-\tfrac12)=\tfrac18$, $f(0)=1$, $f(2)=-3$, $f(4)=17$.", r"Absolute max $17$ at $x=4$; absolute min $-3$ at $x=2$."],
  check=lambda: (lambda f: all_true(max(f.subs(x, v) for v in [sp.Rational(-1, 2), 0, 2, 4]) == 17, min(f.subs(x, v) for v in [sp.Rational(-1, 2), 0, 2, 4]) == -3, crit(f) == [0, 2]))(x**3 - 3*x**2 + 1),
  page=pg(1), points=3)
P("f22e3-2a", S, "2(a)", "5.2", "Antiderivatives", r"Find the general antiderivative of $f(x)=8x^4-\dfrac3{x^6}-3$.",
  r"$F(x)=\dfrac85x^5+\dfrac3{5x^5}-3x+C$", [r"Power rule term by term: $\int8x^4=\tfrac85x^5$, $\int-3x^{-6}=-3\cdot\dfrac{x^{-5}}{-5}=\dfrac3{5x^5}$, $\int-3=-3x$."],
  check=lambda: antideriv(sp.Rational(8, 5)*x**5 + 3/(5*x**5) - 3*x, 8*x**4 - 3/x**6 - 3), page=pg(1), diff="easy", points=4)
P("f22e3-2b", S, "2(b)", "5.8", "Average value", r"A particle moves along a line with velocity $v(t)=e^{2t}+\sin t$. Find its average velocity on $0\le t\le\pi$.",
  r"$\dfrac{e^{2\pi}+3}{2\pi}$",
  [r"$v_{\text{ave}}=\dfrac1{\pi}\displaystyle\int_0^\pi(e^{2t}+\sin t)\,dt=\frac1\pi\left[\tfrac12e^{2t}-\cos t\right]_0^\pi.$",
   r"$=\dfrac1\pi\left[\left(\tfrac12e^{2\pi}+1\right)-\left(\tfrac12-1\right)\right]=\dfrac1{2\pi}\left(e^{2\pi}+3\right).$"],
  check=lambda: same(sp.integrate(sp.exp(2*t) + sp.sin(t), (t, 0, sp.pi))/sp.pi, (sp.exp(2*sp.pi) + 3)/(2*sp.pi)), page=pg(2), points=4)
P("f22e3-3a", S, "3(a)", "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_0^1\frac{x}{(x^2+1)^4}\,dx$.",
  r"$\dfrac7{48}$", [r"$u=x^2+1$, $du=2x\,dx$, $u:1\to2$.", r"$\dfrac12\displaystyle\int_1^2u^{-4}du=-\frac16\left[u^{-3}\right]_1^2=-\frac16\left(\frac18-1\right)=\frac7{48}.$"],
  check=lambda: defint(x/(x**2 + 1)**4, 0, 1, sp.Rational(7, 48)), page=pg(2), points=4)
P("f22e3-3b", S, "3(b)", "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_0^{\pi/4}\sin(2x)\sqrt{1-\cos^2(2x)}\,dx$.",
  r"$\dfrac\pi8$",
  [r"$u=\cos2x$, $du=-2\sin2x\,dx$; $x=0\to u=1$, $x=\pi/4\to u=0$.", r"$=-\dfrac12\displaystyle\int_1^0\sqrt{1-u^2}\,du=\frac12\int_0^1\sqrt{1-u^2}\,du.$",
   r"Quarter unit disk: $\int_0^1\sqrt{1-u^2}\,du=\pi/4$, so the answer is $\pi/8$."],
  check=lambda: numint(sp.sin(2*x)*sp.sqrt(1 - sp.cos(2*x)**2), 0, sp.pi/4, sp.pi/8), page=pg(2), points=4)
P("f22e3-4a", S, "4(a)", "6.1", "Area between curves", r"Find the area of the region bounded by $y=x$ and $y=x^2$.", r"$\dfrac16$", page=pg(3), points=4)
P("f22e3-4b", S, "4(b)", "6.4", "Arc length", r"Find the arc length of $y^2=\tfrac23x^3$ between $x=0$ and $x=1$.", r"$\tfrac49\left[(5/2)^{3/2}-1\right]$", page=pg(3), points=4)
