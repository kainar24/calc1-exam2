# WeBWorK homework HW6–HW10 (MATH-161-1L Fall 2026, the owner's own randomized versions).
# Statements read from webwork-new.nu.edu.kz via Moodle; solutions are mine, checked with SymPy.
from pkit import *

L = lambda e: sp.latex(e, ln_notation=True)
HW = "https://webwork-new.nu.edu.kz/webwork2/MATH-161-1L-Calc-I-Fall26/"
WHEN = {"hw6": "Oct 12–18 (Lec 8)", "hw7": "Oct 19–25 (Lec 9)", "hw8": "Oct 26–Nov 1 (Lec 10)", "hw9": "Nov 9–15 (Lec 11–12)", "hw10": "Nov 17–24 (Lec 12–13)"}
for _hk, secs in [("hw6", "§4.1–4.6"), ("hw7", "§4.7, 4.8, 5.2"), ("hw8", "§5.3–5.5"), ("hw9", "§5.5–5.9"), ("hw10", "§7.2–7.3")]:
    paper(f"hw-{_hk}", f"WeBWorK {_hk.upper()} · {secs} · your version", _hk.upper(), "homework", 2026, "Fall",
          [], False, "WeBWorK", None,
          f"Homework set {_hk.upper()} ({WHEN[_hk]}). Numbers are from your own randomized WeBWorK version. Solutions written here and checked with SymPy.")

HOMEWORK = []
def H(id, hw, num, sec, topic, st, ans, steps, check, diff="exam", note=None):
    d = P(id, f"hw-{hw}", num, sec, topic, st, ans, steps, check, diff=diff, src="own", note=note)
    d["origin"] = "homework"
    HOMEWORK.append(id)
    return d

# ======================================================================== HW6
H("hw6-1", "hw6", 1, "4.1", "Increase/decrease & concavity",
  r"""Draw (choose) the graph of a function $f$ on $[-3,3]$ with: $f''(x)&gt;0$ for $x&lt;-1$ and $x&gt;1$; $f''(x)&lt;0$ for $-1&lt;x&lt;1$; local maximum at $x=0$; local minima at $x=2$ and $x=-2$.""",
  r"A “W”-shaped graph: down to a min at $-2$, up to a max at $0$, down to a min at $2$, up again; inflection points at $x=\pm1$",
  [r"Local min at $\pm2$ and local max at $0$: the graph falls on $(-3,-2)$, rises on $(-2,0)$, falls on $(0,2)$, rises on $(2,3)$.",
   r"Concave up for $|x|&gt;1$ (around the minima, cup-shaped) and concave down on $(-1,1)$ (around the maximum, cap-shaped).",
   r"So the concavity changes at $x=\pm1$: those are inflection points, between each minimum and the maximum.",
   r"In WeBWorK the options are pictures: choose the W-shaped one whose bends change at $x=\pm1$."],
  None, diff="easy", note="The answer options were images in WeBWorK and are not copied here.")
H("hw6-2", "hw6", 2, "4.2", "Relative extrema & curve sketching",
  r"For $f(x)=x^3-4x^2+2$ find the local extrema, intervals of increase/decrease, intervals of concavity, inflection points and asymptotes, and sketch the graph.",
  r"Local max $(0,2)$, local min $\left(\frac83,-\frac{202}{27}\right)$; $\nearrow(-\infty,0]\cup[\frac83,\infty)$, $\searrow[0,\frac83]$; CU $(\frac43,\infty)$, CD $(-\infty,\frac43)$; inflection $\left(\frac43,-\frac{74}{27}\right)$; no asymptotes",
  [r"$f'(x)=3x^2-8x=x(3x-8)$: critical points $x=0,\ \frac83$.",
   r"Signs of $f'$: $+$ on $(-\infty,0)$, $-$ on $(0,\frac83)$, $+$ on $(\frac83,\infty)$ ⇒ local max at $0$: $f(0)=2$; local min at $\frac83$: $f(\frac83)=\frac{512}{27}-\frac{256}9+2=-\frac{202}{27}$.",
   r"$f''(x)=6x-8$: negative for $x&lt;\frac43$ (concave down), positive for $x&gt;\frac43$ (concave up).",
   r"Inflection point $\left(\frac43,f(\frac43)\right)=\left(\frac43,\frac{64}{27}-\frac{64}9+2\right)=\left(\frac43,-\frac{74}{27}\right)$.",
   r"A polynomial has no horizontal or vertical asymptotes; $f\to\pm\infty$ as $x\to\pm\infty$."],
  lambda: (lambda f: all_true(crit(f) == [0, sp.Rational(8, 3)], same(f.subs(x, sp.Rational(8, 3)), sp.Rational(-202, 27)), same(f.subs(x, sp.Rational(4, 3)), sp.Rational(-74, 27))))(x**3 - 4*x**2 + 2))
H("hw6-3", "hw6", 3, "4.4", "Absolute extrema",
  r"Find the minimum and maximum values of $y=\sqrt8\,\theta-\sqrt4\sec\theta$ on $\left[0,\frac\pi3\right]$.",
  r"Min $-2$ at $\theta=0$; max $\sqrt8\left(\frac\pi4-1\right)\approx-0.607$ at $\theta=\frac\pi4$",
  [r"$f(\theta)=2\sqrt2\,\theta-2\sec\theta$ is continuous on the closed interval ⇒ EVT.",
   r"$f'(\theta)=2\sqrt2-2\sec\theta\tan\theta=0\iff\sec\theta\tan\theta=\sqrt2$. At $\theta=\frac\pi4$: $\sec=\sqrt2$, $\tan=1$ ✓ (and $\sec\theta\tan\theta$ is increasing on $[0,\frac\pi3]$, so this is the only solution).",
   r"Values: $f(0)=-2$; $f(\frac\pi4)=\frac{\sqrt2\pi}2-2\sqrt2=\sqrt8\left(\frac\pi4-1\right)\approx-0.607$; $f(\frac\pi3)=\frac{2\sqrt2\pi}3-4\approx-1.038$.",
   r"Minimum $-2$ (at $\theta=0$), maximum $\approx-0.607$ (at $\theta=\frac\pi4$)."],
  lambda: (lambda f: all_true(same(sp.diff(f, x).subs(x, sp.pi/4), 0), same(f.subs(x, 0), -2), abs(float(f.subs(x, sp.pi/4)) + 0.606986) < 1e-5, max(float(f.subs(x, sp.pi/3*j/600)) for j in range(601)) <= float(f.subs(x, sp.pi/4)) + 1e-12))(sp.sqrt(8)*x - 2*sp.sec(x)))
H("hw6-4", "hw6", 4, "4.4", "Absolute extrema",
  r"Find the exact global maximum and minimum values of $g(x)=5x-x^2-12$ on all real numbers.",
  r"Global max $-\frac{23}4$ at $x=\frac52$; no global minimum",
  [r"$g'(x)=5-2x=0\Rightarrow x=\frac52$; $g'&gt;0$ before, $&lt;0$ after ⇒ local max.", r"$g\to-\infty$ as $x\to\pm\infty$ ⇒ the local max is the global max, and there is no global min.",
   r"$g(\frac52)=\frac{25}2-\frac{25}4-12=-\frac{23}4=-5.75$."],
  lambda: same((5*x - x**2 - 12).subs(x, sp.Rational(5, 2)), sp.Rational(-23, 4)), diff="easy")
H("hw6-5", "hw6", 5, "4.4", "Absolute extrema",
  r"Find the absolute maximum and minimum values of $f(x)=\dfrac{x-6}{x+5}$ on $(-5,1]$, if any.",
  r"Absolute max $-\frac56$ at $x=1$; no absolute minimum",
  [r"$\lim_{x\to-5^+}\frac{x-6}{x+5}=\frac{-11}{0^+}=-\infty$ ⇒ no absolute minimum.", r"$f'(x)=\dfrac{(x+5)-(x-6)}{(x+5)^2}=\dfrac{11}{(x+5)^2}&gt;0$: no critical points, $f$ increasing.",
   r"So the max is at the right endpoint: $f(1)=-\frac56$."],
  lambda: all_true(same(sp.diff((x - 6)/(x + 5), x), 11/(x + 5)**2), sp.limit((x - 6)/(x + 5), x, -5, '+') == -sp.oo), diff="easy")
H("hw6-6", "hw6", 6, "4.4", "Absolute extrema",
  r"Find the absolute maximum and minimum values of $f(x)=8x-x^2$ on $[0,5]$.",
  r"Max $16$ at $x=4$; min $0$ at $x=0$",
  [r"$f'(x)=8-2x=0\Rightarrow x=4$.", r"Table: $f(0)=0$, $f(4)=16$, $f(5)=15$.", r"Max $16$ at $x=4$, min $0$ at $x=0$."],
  lambda: [(8*x - x**2).subs(x, v) for v in (0, 4, 5)] == [0, 16, 15], diff="easy")
H("hw6-7", "hw6", 7, "4.5", "Optimization",
  r"A ball thrown up on the moon has height $h=280t-\frac86t^2$ ft after $t$ s. When does it reach its maximum height, and what is that height?",
  r"$t=105$ s, $h=14\,700$ ft",
  [r"$h'(t)=280-\frac{16}6t=280-\frac83t=0\Rightarrow t=105$.", r"$h''=-\frac83&lt;0$ ⇒ maximum.", r"$h(105)=280\cdot105-\frac43\cdot105^2=29\,400-14\,700=14\,700$ ft."],
  lambda: (lambda h: all_true(sp.solve(sp.diff(h, t), t) == [105], same(h.subs(t, 105), 14700)))(280*t - sp.Rational(8, 6)*t**2), diff="easy")
H("hw6-8", "hw6", 8, "4.5", "Optimization",
  r"Find the point $P$ on the graph of $y=\sqrt x$ closest to the point $(4,0)$.",
  r"$x=\frac72$, i.e. $P=\left(\frac72,\sqrt{\frac72}\right)$",
  [r"Minimize the squared distance $D(x)=(x-4)^2+(\sqrt x)^2=x^2-7x+16$, $x\ge0$.", r"$D'(x)=2x-7=0\Rightarrow x=\frac72$; $D''=2&gt;0$ ⇒ minimum.",
   r"$D(0)=16&gt;D(\frac72)=\frac{15}4$ and $D\to\infty$ ⇒ absolute minimum at $x=\frac72$."],
  lambda: sp.solve(sp.diff((x - 4)**2 + x, x), x) == [sp.Rational(7, 2)])
H("hw6-9", "hw6", 9, "4.5", "Optimization",
  r"Find the maximal area of a right triangle with hypotenuse of length $3$.",
  r"$\frac94$ (legs $\frac3{\sqrt2}$ each)",
  [r"Legs $x,y$ with $x^2+y^2=9\Rightarrow y=\sqrt{9-x^2}$, $0&lt;x&lt;3$.", r"Area $A(x)=\frac12x\sqrt{9-x^2}$.",
   r"$A'(x)=\frac12\left(\sqrt{9-x^2}-\frac{x^2}{\sqrt{9-x^2}}\right)=\frac{9-2x^2}{2\sqrt{9-x^2}}=0\Rightarrow x=\frac3{\sqrt2}$.",
   r"$A\to0$ at both ends ⇒ maximum. $y=\frac3{\sqrt2}$ too, $A=\frac12\cdot\frac92=\frac94$."],
  lambda: (lambda A: all_true([c for c in sp.solve(sp.diff(A, x), x) if c.is_positive] == [3/sp.sqrt(2)], same(A.subs(x, 3/sp.sqrt(2)), sp.Rational(9, 4))))(x*sp.sqrt(9 - x**2)/2))
H("hw6-10", "hw6", 10, "4.6", "Rectilinear motion (derivatives)",
  r"A particle has position $s(t)=2t^3-21t^2+72t$ ft, $t\ge0$. (A) When is it moving forward / backward? (B) When is it speeding up / slowing down?",
  r"Forward $[0,3)\cup(4,\infty)$, backward $(3,4)$; speeding up $(3,\frac72)\cup(4,\infty)$, slowing down $(0,3)\cup(\frac72,4)$",
  [r"$v(t)=6t^2-42t+72=6(t-3)(t-4)$; $a(t)=12t-42=12\left(t-\frac72\right)$.",
   r"$v&gt;0$ on $[0,3)$ and $(4,\infty)$ (forward), $v&lt;0$ on $(3,4)$ (backward).",
   r"$a&lt;0$ before $\frac72$, $a&gt;0$ after.",
   r"Same signs (speeding up): $(3,\frac72)$ [both $-$] and $(4,\infty)$ [both $+$]. Opposite (slowing down): $(0,3)$ and $(\frac72,4)$."],
  lambda: all_true(same(sp.factor(sp.diff(2*t**3 - 21*t**2 + 72*t, t)), 6*(t - 3)*(t - 4)), same(sp.diff(2*t**3 - 21*t**2 + 72*t, t, 2), 12*t - 42)))
H("hw6-11", "hw6", 11, "4.6", "Rectilinear motion (derivatives)",
  r"A particle moves along the $x$-axis with $x(t)=\dfrac{t}{1+t^2}$, $t\ge0$. (a) Find $a(t)$. (b) When is it speeding up? (c) When is it slowing down?",
  r"(a) $a(t)=\dfrac{2t(t^2-3)}{(1+t^2)^3}$; (b) $1&lt;t&lt;\sqrt3$; (c) $0&lt;t&lt;1$ and $t&gt;\sqrt3$",
  [r"$v(t)=\dfrac{(1+t^2)-2t^2}{(1+t^2)^2}=\dfrac{1-t^2}{(1+t^2)^2}$: positive for $t&lt;1$, negative for $t&gt;1$.",
   r"$a(t)=v'(t)=\dfrac{2t(t^2-3)}{(1+t^2)^3}$: negative on $(0,\sqrt3)$, positive for $t&gt;\sqrt3$.",
   r"$(0,1)$: $v&gt;0,a&lt;0$ ⇒ slowing down. $(1,\sqrt3)$: $v&lt;0,a&lt;0$ ⇒ speeding up. $(\sqrt3,\infty)$: $v&lt;0,a&gt;0$ ⇒ slowing down."],
  lambda: same(sp.diff(t/(1 + t**2), t, 2), 2*t*(t**2 - 3)/(1 + t**2)**3))

# ======================================================================== HW7
def newton(f, x0, n):
    xs, v = [], sp.Float(x0, 30)
    for _ in range(n):
        v = v - f.subs(x, v)/sp.diff(f, x).subs(x, v); xs.append(v)
    return xs
_n3 = newton(sp.log(x) + x - 4, 3, 3)
H("hw7-1", "hw7", 1, "4.7", "Newton's method", r"Use Newton's method to approximate $\sqrt{10}$ to 6 significant figures, starting with $x_0=3.5$.",
  r"$\sqrt{10}\approx3.16228$", [r"$f(x)=x^2-10$, $x_{n+1}=x_n-\frac{x_n^2-10}{2x_n}$: $x_1\approx3.17857$, $x_2\approx3.16232$, $x_3\approx3.16228$."],
  lambda: abs(float(newton(x**2 - 10, 3.5, 4)[-1]) - 3.16228) < 1e-5, diff="easy")
H("hw7-2", "hw7", 2, "4.7", "Newton's method", r"Newton's method with $f(x)=x^2-2$, $x_0=1$: find $x_1,x_2,x_3$.",
  r"$x_1=1.5$, $x_2=\frac{17}{12}\approx1.416667$, $x_3=\frac{577}{408}\approx1.414216$", [r"$x_{n+1}=x_n-\frac{x_n^2-2}{2x_n}=\frac{x_n}2+\frac1{x_n}$."],
  lambda: [sp.nsimplify(v) for v in newton(x**2 - 2, 1, 3)] == [sp.Rational(3, 2), sp.Rational(17, 12), sp.Rational(577, 408)], diff="easy")
H("hw7-3", "hw7", 3, "4.7", "Newton's method", r"Use Newton's method to solve $\ln x=4-x$, starting with $x_0=3$; give $x_1,x_2,x_3$ to 4 decimals.",
  rf"$x_1\approx{float(_n3[0]):.4f}$, $x_2\approx{float(_n3[1]):.4f}$, $x_3\approx{float(_n3[2]):.4f}$",
  [r"$f(x)=\ln x+x-4$, $f'(x)=\frac1x+1$, $x_{n+1}=x_n-\dfrac{\ln x_n+x_n-4}{1/x_n+1}$."], lambda: abs(float(sp.log(_n3[2]) + _n3[2] - 4)) < 1e-8, diff="easy")
H("hw7-4", "hw7", 4, "4.8", "Mean Value Theorem / Rolle",
  r"Find all numbers $c$ that satisfy the conclusion of Rolle's Theorem for $f(x)=8\sin(2\pi x)$ on $[-1,1]$.",
  r"$c=-\frac34,\ -\frac14,\ \frac14,\ \frac34$",
  [r"$f$ is continuous and differentiable everywhere; $f(-1)=f(1)=0$ ⇒ Rolle applies.", r"$f'(x)=16\pi\cos(2\pi x)=0\iff2\pi x=\frac\pi2+k\pi\iff x=\frac14+\frac k2$.",
   r"Inside $(-1,1)$: $x=-\frac34,-\frac14,\frac14,\frac34$."],
  lambda: sorted(sp.solveset(sp.diff(8*sp.sin(2*sp.pi*x), x), x, sp.Interval.open(-1, 1))) == [sp.Rational(-3, 4), sp.Rational(-1, 4), sp.Rational(1, 4), sp.Rational(3, 4)])
H("hw7-5", "hw7", 5, "4.8", "Mean Value Theorem / Rolle",
  r"Check whether the Mean Value Theorem applies to $f(x)=3\sin^{-1}x$ on $[-1,1]$; if so, find all $c$.",
  r"It applies; $c=\pm\sqrt{1-\frac4{\pi^2}}\approx\pm0.771$",
  [r"$\sin^{-1}x$ is continuous on $[-1,1]$ and differentiable on $(-1,1)$ (only the endpoints are bad, which is allowed) ⇒ MVT applies.",
   r"Secant slope: $\dfrac{3\cdot\frac\pi2-3\left(-\frac\pi2\right)}{2}=\dfrac{3\pi}2$.", r"$f'(c)=\dfrac3{\sqrt{1-c^2}}=\dfrac{3\pi}2\Rightarrow\sqrt{1-c^2}=\frac2\pi\Rightarrow c^2=1-\frac4{\pi^2}$.",
   r"$c=\pm\sqrt{1-4/\pi^2}\approx\pm0.7712$, both in $(-1,1)$."],
  lambda: same(sp.diff(3*sp.asin(x), x).subs(x, sp.sqrt(1 - 4/sp.pi**2)), 3*sp.pi/2), diff="hard")
H("hw7-6", "hw7", 6, "5.2", "Antiderivatives & IVPs", r"Find the most general antiderivative of $3x^4-\dfrac5{x^4}-3$.",
  r"$\frac35x^5+\dfrac5{3x^3}-3x+C$", [r"Power rule: $\int3x^4=\frac35x^5$, $\int-5x^{-4}=-5\cdot\frac{x^{-3}}{-3}=\frac5{3x^3}$, $\int-3=-3x$."],
  lambda: antideriv(sp.Rational(3, 5)*x**5 + 5/(3*x**3) - 3*x, 3*x**4 - 5/x**4 - 3), diff="easy")
H("hw7-7", "hw7", 7, "5.2", "Antiderivatives & IVPs", r"Find the most general antiderivative of $\dfrac3{\sqrt[3]x}-3\sqrt[3]{x^2}$.",
  r"$\frac92x^{2/3}-\frac95x^{5/3}+C$", [r"Write as $3x^{-1/3}-3x^{2/3}$.", r"$3\cdot\frac{x^{2/3}}{2/3}-3\cdot\frac{x^{5/3}}{5/3}=\frac92x^{2/3}-\frac95x^{5/3}$."],
  lambda: antideriv(sp.Rational(9, 2)*x**sp.Rational(2, 3) - sp.Rational(9, 5)*x**sp.Rational(5, 3), 3*x**sp.Rational(-1, 3) - 3*x**sp.Rational(2, 3)), diff="easy")
H("hw7-8", "hw7", 8, "5.2", "Antiderivatives & IVPs", r"Find $f$ if $f'(x)=\sin x$ and $f(0)=-7$.",
  r"$f(x)=-\cos x-6$", [r"$f(x)=-\cos x+C$; $f(0)=-1+C=-7\Rightarrow C=-6$."], lambda: same((-sp.cos(x) - 6).subs(x, 0), -7), diff="easy")
H("hw7-9", "hw7", 9, "5.2", "Antiderivatives & IVPs", r"Let $F$ be the antiderivative of $f(t)=4\sec^2t-9t^3$ with $F(0)=0$. Find $F(0.9)$.",
  r"$F(0.9)=4\tan0.9-\frac94(0.9)^4\approx3.564$", [r"$F(t)=4\tan t-\frac94t^4+C$, and $F(0)=C=0$.", r"$F(0.9)=4\tan(0.9)-\frac94(0.9)^4\approx5.04064-1.47623\approx3.564$."],
  lambda: abs(float(4*sp.tan(0.9) - sp.Rational(9, 4)*0.9**4) - 3.564) < 1e-3, diff="easy")
H("hw7-10", "hw7", 10, "5.2", "Antiderivatives & IVPs", r"Solve $\dfrac{dy}{dt}=\sec^2t+9\sin t$, $y\left(\frac\pi4\right)=1$.",
  r"$y=\tan t-9\cos t+\frac{9\sqrt2}2$", [r"$y=\tan t-9\cos t+C$.", r"$y(\frac\pi4)=1-\frac9{\sqrt2}+C=1\Rightarrow C=\frac9{\sqrt2}=\frac{9\sqrt2}2$."],
  lambda: (lambda Y: all_true(antideriv(Y, sp.sec(x)**2 + 9*sp.sin(x)), same(Y.subs(x, sp.pi/4), 1)))(sp.tan(x) - 9*sp.cos(x) + 9*sp.sqrt(2)/2))
H("hw7-11", "hw7", 11, "5.2", "Antiderivatives & IVPs", r"Compute $\displaystyle\int\frac{1-\sin^2x}{\cos x}\,dx$.",
  r"$\sin x+C$", [r"$1-\sin^2x=\cos^2x$, so the integrand is $\cos x$."], lambda: antideriv(sp.sin(x), (1 - sp.sin(x)**2)/sp.cos(x)), diff="easy")
H("hw7-12", "hw7", 12, "5.2", "Antiderivatives & IVPs", r"Evaluate $\displaystyle\int(3+3y^2)^2\,dy$.",
  r"$9y+6y^3+\frac95y^5+C$", [r"Expand: $9+18y^2+9y^4$.", r"Integrate term by term."], lambda: antideriv(9*x + 6*x**3 + sp.Rational(9, 5)*x**5, (3 + 3*x**2)**2), diff="easy")
H("hw7-13", "hw7", 13, "5.2", "Antiderivatives & IVPs", r"Find $\displaystyle\int\frac{(t+2)^2}{t^4}\,dt$.",
  r"$-\dfrac1t-\dfrac2{t^2}-\dfrac4{3t^3}+C$", [r"$\frac{t^2+4t+4}{t^4}=t^{-2}+4t^{-3}+4t^{-4}$.", r"$\int=-t^{-1}-2t^{-2}-\frac43t^{-3}+C$."],
  lambda: antideriv(-1/x - 2/x**2 - sp.Rational(4, 3)/x**3, (x + 2)**2/x**4))

# ======================================================================== HW8
H("hw8-1", "hw8", 1, "5.3", "u-substitution (indefinite)", r"Evaluate (a) $\displaystyle\int e^{x^9}x^8\,dx$ and (b) $\displaystyle\int e^{x^2-2x+8}(x-1)\,dx$.",
  r"(a) $\frac19e^{x^9}+C$; (b) $\frac12e^{x^2-2x+8}+C$",
  [r"(a) $u=x^9$, $du=9x^8dx$: $\frac19\int e^udu=\frac19e^{x^9}+C$.", r"(b) $u=x^2-2x+8$, $du=(2x-2)dx=2(x-1)dx$: $\frac12\int e^udu=\frac12e^{x^2-2x+8}+C$."],
  lambda: all_true(antideriv(sp.exp(x**9)/9, sp.exp(x**9)*x**8, pts=(0.2, 0.5, 0.9)), antideriv(sp.exp(x**2 - 2*x + 8)/2, sp.exp(x**2 - 2*x + 8)*(x - 1))), diff="easy")
H("hw8-2", "hw8", 2, "5.3", "u-substitution (indefinite)", r"Evaluate $\displaystyle\int\frac{9e^x-5e^{-x}}{9e^x+5e^{-x}}\,dx$.",
  r"$\ln\left(9e^x+5e^{-x}\right)+C$", [r"$u=9e^x+5e^{-x}$, $du=(9e^x-5e^{-x})\,dx$ — exactly the numerator.", r"$\int\frac{du}u=\ln|u|+C$, and $u&gt;0$."],
  lambda: antideriv(sp.log(9*sp.exp(x) + 5*sp.exp(-x)), (9*sp.exp(x) - 5*sp.exp(-x))/(9*sp.exp(x) + 5*sp.exp(-x))))
H("hw8-3", "hw8", 3, "5.3", "u-substitution (indefinite)", r"Evaluate $\displaystyle\int\frac{(\tan^{-1}x)^2}{1+x^2}\,dx$.",
  r"$\frac13(\tan^{-1}x)^3+C$", [r"$u=\tan^{-1}x$, $du=\frac{dx}{1+x^2}$: $\int u^2du=\frac{u^3}3+C$."], lambda: antideriv(sp.atan(x)**3/3, sp.atan(x)**2/(1 + x**2)), diff="easy")
H("hw8-4", "hw8", 4, "5.3", "u-substitution (indefinite)", r"Evaluate $\displaystyle\int\frac{\sin4x}{4+\cos4x}\,dx$.",
  r"$-\frac14\ln(4+\cos4x)+C$", [r"$u=4+\cos4x$, $du=-4\sin4x\,dx$: $-\frac14\int\frac{du}u=-\frac14\ln|u|+C$ ($u\ge3&gt;0$)."],
  lambda: antideriv(-sp.log(4 + sp.cos(4*x))/4, sp.sin(4*x)/(4 + sp.cos(4*x))))
H("hw8-5", "hw8", 5, "5.3", "u-substitution (indefinite)",
  r"Convert to $du$ (no $x$ left): (A) $\int x\ln(5x^2+2)\,dx$ with $u=5x^2+2$; (B) $\int x^3\ln(5x^2+2)\,dx$ with $u=5x^2+2$; (C) $\int5\dfrac{\ln(\cos2x)}{\sin2x}\,dx$ with $u=\cos2x$.",
  r"(A) $\int\frac{\ln u}{10}\,du$; (B) $\int\frac{(u-2)\ln u}{50}\,du$; (C) $\int-\frac{5\ln u}{2(1-u^2)}\,du$",
  [r"(A) $du=10x\,dx\Rightarrow x\,dx=\frac{du}{10}$: $\int\frac{\ln u}{10}du$.", r"(B) $x^3dx=x^2\cdot x\,dx$ and $x^2=\frac{u-2}5$: $\int\frac{u-2}5\ln u\cdot\frac{du}{10}=\int\frac{(u-2)\ln u}{50}du$.",
   r"(C) $du=-2\sin2x\,dx\Rightarrow dx=-\frac{du}{2\sin2x}$, so the integrand becomes $-\frac{5\ln u}{2\sin^22x}du$, and $\sin^22x=1-u^2$: $\int-\frac{5\ln u}{2(1-u^2)}du$."],
  lambda: all_true(same((sp.log(u)/10).subs(u, 5*x**2 + 2)*sp.diff(5*x**2 + 2, x), x*sp.log(5*x**2 + 2)), same(((u - 2)*sp.log(u)/50).subs(u, 5*x**2 + 2)*sp.diff(5*x**2 + 2, x), x**3*sp.log(5*x**2 + 2)),
                   abs(float(((-5*sp.log(u)/(2*(1 - u**2))).subs(u, sp.cos(2*x))*sp.diff(sp.cos(2*x), x) - 5*sp.log(sp.cos(2*x))/sp.sin(2*x)).subs(x, 0.3))) < 1e-12), diff="hard")
H("hw8-6", "hw8", 6, "5.3", "u-substitution (indefinite)", r"Evaluate $\displaystyle\int\tan^3x\sec^2x\,dx$.",
  r"$\frac14\tan^4x+C$", [r"$u=\tan x$, $du=\sec^2x\,dx$: $\int u^3du=\frac{u^4}4+C$."], lambda: antideriv(sp.tan(x)**4/4, sp.tan(x)**3*sp.sec(x)**2), diff="easy")
H("hw8-8", "hw8", 8, "5.5", "Definite integral: properties & geometry",
  r"The limit $\displaystyle\lim_{n\to\infty}\sum_{i=1}^n\sqrt{2x_i^*+(x_i^*)^2}\,\Delta x$ on $[1,8]$ equals $\int_a^bf(x)\,dx$. Find $a$, $b$, $f$.",
  r"$a=1$, $b=8$, $f(x)=\sqrt{2x+x^2}$", [r"By the definition $\int_a^bf=\lim\sum f(x_i^*)\Delta x$: the interval gives $a,b$ and the expression evaluated at $x_i^*$ is $f$."],
  None, diff="easy")
H("hw8-9", "hw8", 9, "5.4", "Riemann sums & sigma notation",
  r"(a) Which expression is the area under $f(x)=x^3$ from $0$ to $1$: A. $\lim\sum\left(\frac in\right)^3\frac1n$; B. $\lim\sum\left(\frac in\right)^3\frac5n$; C. $\lim\sum\frac in\cdot\frac1n$; D. $\lim\sum\frac in\cdot\frac5n$? (b) Evaluate it.",
  r"(a) A; (b) $\frac14$",
  [r"$\Delta x=\frac{1-0}n=\frac1n$, right endpoints $x_i=\frac in$, $f(x_i)=\left(\frac in\right)^3$ ⇒ A.",
   r"$\sum_{i=1}^n\frac{i^3}{n^4}=\frac1{n^4}\left(\frac{n(n+1)}2\right)^2=\frac{(n+1)^2}{4n^2}\to\frac14$."],
  lambda: same(sp.limit(sp.summation((k/n)**3/n, (k, 1, n)), n, sp.oo), sp.Rational(1, 4)), diff="easy")
H("hw8-10", "hw8", 10, "5.4", "Riemann sums & sigma notation",
  r"Find in terms of $n$: $\sum_{k=1}^nk$, $\ \sum_{k=1}^n\frac k{n^2}$, $\ \sum_{k=1}^n\frac8n$, $\ \sum_{k=1}^n\left(\frac{4k}{n^2}-\frac8n\right)$; then evaluate $\lim_{n\to\infty}\sum_{k=1}^n\left(\frac{4k}{n^2}-\frac8n\right)$.",
  r"$\frac{n(n+1)}2$; $\frac{n+1}{2n}$; $8$; $\frac{2(n+1)}n-8$; limit $-6$",
  [r"$\sum k=\frac{n(n+1)}2$.", r"$\sum\frac k{n^2}=\frac1{n^2}\cdot\frac{n(n+1)}2=\frac{n+1}{2n}$.", r"$\sum\frac8n=n\cdot\frac8n=8$.",
   r"$\sum\left(\frac{4k}{n^2}-\frac8n\right)=4\cdot\frac{n+1}{2n}-8=\frac{2(n+1)}n-8\to2-8=-6$."],
  lambda: same(sp.limit(sp.summation(4*k/n**2 - 8/n, (k, 1, n)), n, sp.oo), -6), diff="easy")

# ======================================================================== HW9
H("hw9-1", "hw9", 1, "5.5", "Definite integral: properties & geometry", r"Evaluate $\displaystyle\int_0^{12}|x-6|\,dx$ by interpreting it as an area.",
  "$36$", [r"Two triangles with legs $6$ and $6$: $2\cdot\frac12\cdot6\cdot6=36$."], lambda: numint(sp.Abs(x - 6), 0, 12, 36), diff="easy")
H("hw9-2", "hw9", 2, "5.6", "FTC: evaluating definite integrals", r"Find $b&gt;1$ if the area under $f(x)=9x$ between $x=1$ and $x=b$ equals $216$.",
  "$b=7$", [r"$\int_1^b9x\,dx=\frac92(b^2-1)=216\Rightarrow b^2-1=48\Rightarrow b=7$."], lambda: same(sp.integrate(9*x, (x, 1, 7)), 216), diff="easy")
H("hw9-3", "hw9", 3, "5.6", "FTC: evaluating definite integrals", r"Evaluate $\displaystyle\int_0^{\pi/4}\frac{5+\cos^3u}{\cos^2u}\,du$.",
  r"$5+\frac{\sqrt2}2$", [r"Split: $\frac5{\cos^2u}+\cos u=5\sec^2u+\cos u$.", r"$[5\tan u+\sin u]_0^{\pi/4}=5+\frac{\sqrt2}2$."],
  lambda: numint((5 + sp.cos(x)**3)/sp.cos(x)**2, 0, sp.pi/4, 5 + sp.sqrt(2)/2))
H("hw9-4", "hw9", 4, "5.6", "FTC: evaluating definite integrals",
  r"Evaluate $\displaystyle\int_{\pi/2}^{\pi}3\cos x\,dx$, $\ \displaystyle\int_0^{\pi/4}-14\sec^2\theta\,d\theta$, $\ \displaystyle\int_{\pi/6}^{\pi/3}12\csc t\cot t\,dt$.",
  r"$-3$; $\ -14$; $\ 24-8\sqrt3$",
  [r"$3[\sin x]_{\pi/2}^\pi=3(0-1)=-3$.", r"$-14[\tan\theta]_0^{\pi/4}=-14$.", r"$12[-\csc t]_{\pi/6}^{\pi/3}=-12\left(\frac2{\sqrt3}-2\right)=24-8\sqrt3$."],
  lambda: all_true(defint(3*sp.cos(x), sp.pi/2, sp.pi, -3), defint(-14*sp.sec(x)**2, 0, sp.pi/4, -14), numint(12/sp.sin(x)*sp.cos(x)/sp.sin(x), sp.pi/6, sp.pi/3, 24 - 8*sp.sqrt(3))), diff="easy")
H("hw9-5", "hw9", 5, "5.6", "FTC: derivative of an integral", r"$G(x)=\displaystyle\int_1^x\tan t\,dt$. Find $G(1)$ and $G'\left(\frac\pi4\right)$.",
  r"$G(1)=0$, $G'(\frac\pi4)=1$", [r"$G(1)=\int_1^1=0$.", r"FTC: $G'(x)=\tan x$, so $G'(\frac\pi4)=1$."], None, diff="easy")
H("hw9-6", "hw9", 6, "5.7", "Motion via integrals", r"$v(t)=t-\sqrt t$ m/s on $0\le t\le4$. Find the displacement and the distance traveled.",
  r"Displacement $\frac83$ m, distance $3$ m",
  [r"Displacement $=\int_0^4(t-t^{1/2})\,dt=\left[\frac{t^2}2-\frac23t^{3/2}\right]_0^4=8-\frac{16}3=\frac83$.",
   r"$v=\sqrt t(\sqrt t-1)$: negative on $(0,1)$, positive on $(1,4)$.",
   r"$\int_0^1v=\frac12-\frac23=-\frac16$, $\int_1^4v=\frac83+\frac16=\frac{17}6$.", r"Distance $=\frac16+\frac{17}6=3$."],
  lambda: all_true(same(sp.integrate(t - sp.sqrt(t), (t, 0, 4)), sp.Rational(8, 3)), numint(sp.Abs(t - sp.sqrt(t)), 0, 4, 3, t)))
H("hw9-7", "hw9", 7, "5.8", "Average value", r"A yacht's value after $t$ years is $V(t)=200\,000e^{-0.27t}$ dollars. Find its average value over the first 20 years.",
  r"$V_{\rm ave}=\dfrac{10\,000}{0.27}\left(1-e^{-5.4}\right)\approx36\,870$ dollars",
  [r"$V_{\rm ave}=\frac1{20}\int_0^{20}200\,000e^{-0.27t}dt=\frac{10\,000}{1}\left[\frac{e^{-0.27t}}{-0.27}\right]_0^{20}$.", r"$=\frac{10\,000}{0.27}\left(1-e^{-5.4}\right)\approx37\,037\cdot0.99548\approx36\,870$."],
  lambda: abs(float(sp.Integral(200000*sp.exp(-sp.Rational(27, 100)*t), (t, 0, 20)).evalf()/20) - 10000/0.27*(1 - float(sp.exp(-5.4)))) < 1e-6)
H("hw9-8", "hw9", 8, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_1^{\sqrt2}xe^{7x^2}\,dx$.",
  r"$\dfrac{e^{14}-e^7}{14}$", [r"$u=7x^2$, $du=14x\,dx$; $x=1\to u=7$, $x=\sqrt2\to u=14$.", r"$\frac1{14}\int_7^{14}e^udu=\frac{e^{14}-e^7}{14}$."],
  lambda: defint(x*sp.exp(7*x**2), 1, sp.sqrt(2), (sp.exp(14) - sp.exp(7))/14))
H("hw9-9", "hw9", 9, "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_{-4}^0(x+2)e^{x^2+4x-5}\,dx$.",
  "$0$", [r"$u=x^2+4x-5$, $du=2(x+2)\,dx$.", r"$x=-4\Rightarrow u=-5$; $x=0\Rightarrow u=-5$: equal limits ⇒ the integral is $0$."],
  lambda: defint((x + 2)*sp.exp(x**2 + 4*x - 5), -4, 0, 0))
H("hw9-10", "hw9", 10, "5.6", "FTC: derivative of an integral", r"Find $\dfrac{d}{dx}\displaystyle\int_{4\cos x}^{4}\sqrt{16-t^2}\,dt$.",
  r"$16\sin x\,|\sin x|$, i.e. $16\sin^2x$ when $\sin x\ge0$",
  [r"The variable is in the lower limit: $\frac{d}{dx}\int_{h(x)}^4f(t)\,dt=-f(h(x))h'(x)$.", r"$=-\sqrt{16-16\cos^2x}\cdot(-4\sin x)=4\sin x\cdot4|\sin x|$.",
   r"For $0\le x\le\pi$ (where WeBWorK expects it) this is $16\sin^2x$."],
  lambda: abs(float(sp.diff(sp.Integral(sp.sqrt(16 - t**2), (t, 4*sp.cos(x), 4)), x).doit().subs(x, 1.0)) - 16*float(sp.sin(1.0))**2) < 1e-9, diff="hard")

# ======================================================================== HW10
H("hw10-1", "hw10", 1, "7.2", "Integration by parts", r"Find $\displaystyle\int\frac{x^2}{e^{3x}}\,dx$.",
  r"$-e^{-3x}\left(\frac{x^2}3+\frac{2x}9+\frac2{27}\right)+C$",
  [r"$=\int x^2e^{-3x}dx$. Tabular: D: $x^2,\ 2x,\ 2,\ 0$; I: $e^{-3x},\ -\frac13e^{-3x},\ \frac19e^{-3x},\ -\frac1{27}e^{-3x}$.",
   r"$+x^2\left(-\frac13e^{-3x}\right)-2x\left(\frac19e^{-3x}\right)+2\left(-\frac1{27}e^{-3x}\right)$."],
  lambda: antideriv(-sp.exp(-3*x)*(x**2/3 + 2*x/9 + sp.Rational(2, 27)), x**2*sp.exp(-3*x)))
H("hw10-2", "hw10", 2, "7.2", "Integration by parts", r"Find $\displaystyle\int(\ln6x)^2\,dx$.",
  r"$x(\ln6x)^2-2x\ln6x+2x+C$",
  [r"$u=(\ln6x)^2$, $dv=dx$ ⇒ $du=\frac{2\ln6x}x\,dx$, $v=x$: $x(\ln6x)^2-2\int\ln6x\,dx$.", r"$\int\ln6x\,dx$: $u=\ln6x$, $dv=dx$ ⇒ $x\ln6x-x$.",
   r"Total: $x(\ln6x)^2-2x\ln6x+2x+C$."],
  lambda: antideriv(x*sp.log(6*x)**2 - 2*x*sp.log(6*x) + 2*x, sp.log(6*x)**2))
H("hw10-3", "hw10", 3, "7.2", "Integration by parts", r"Evaluate $\displaystyle\int e^{4x}\sin3x\,dx$ by parts, taking $u=e^{4x}$ first.",
  r"$\dfrac{e^{4x}(4\sin3x-3\cos3x)}{25}+C$",
  [r"Step 1: $u=e^{4x}$, $dv=\sin3x\,dx$ ⇒ $du=4e^{4x}dx$, $v=-\frac13\cos3x$: $I=-\frac13e^{4x}\cos3x+\frac43\int e^{4x}\cos3x\,dx$.",
   r"Step 2: $u=e^{4x}$, $dv=\cos3x\,dx$ ⇒ $v=\frac13\sin3x$: $\int e^{4x}\cos3x\,dx=\frac13e^{4x}\sin3x-\frac43I$.",
   r"Step 3: $I=-\frac13e^{4x}\cos3x+\frac49e^{4x}\sin3x-\frac{16}9I\Rightarrow\frac{25}9I=\frac{e^{4x}}9(4\sin3x-3\cos3x)$.",
   r"$I=\frac{e^{4x}(4\sin3x-3\cos3x)}{25}+C$."],
  lambda: antideriv(sp.exp(4*x)*(4*sp.sin(3*x) - 3*sp.cos(3*x))/25, sp.exp(4*x)*sp.sin(3*x)), diff="hard")
H("hw10-4", "hw10", 4, "7.2", "Integration by parts", r"Evaluate $\displaystyle\int x^2\arctan(7x)\,dx$.",
  r"$\frac{x^3}3\arctan7x-\frac{x^2}{42}+\frac{\ln(1+49x^2)}{2058}+C$",
  [r"$u=\arctan7x$, $dv=x^2dx$ ⇒ $du=\frac{7\,dx}{1+49x^2}$, $v=\frac{x^3}3$.", r"$I=\frac{x^3}3\arctan7x-\frac73\int\frac{x^3}{1+49x^2}dx$.",
   r"Divide: $\frac{x^3}{1+49x^2}=\frac x{49}-\frac{x}{49(1+49x^2)}$, so $\int=\frac{x^2}{98}-\frac{\ln(1+49x^2)}{4802}$.",
   r"$I=\frac{x^3}3\arctan7x-\frac{x^2}{42}+\frac{\ln(1+49x^2)}{2058}+C$."],
  lambda: antideriv(x**3/3*sp.atan(7*x) - x**2/42 + sp.log(1 + 49*x**2)/2058, x**2*sp.atan(7*x)), diff="hard")
H("hw10-5", "hw10", 5, "7.2", "Integration by parts", r"Compute $\displaystyle\int_0^{\pi/4}x^2\sin2x\,dx$ (exact).",
  r"$\frac\pi8-\frac14$",
  [r"Tabular: D: $x^2,2x,2,0$; I: $\sin2x,-\frac12\cos2x,-\frac14\sin2x,\frac18\cos2x$.", r"Antiderivative: $-\frac{x^2}2\cos2x+\frac x2\sin2x+\frac14\cos2x$.",
   r"At $\frac\pi4$: $0+\frac\pi8+0$; at $0$: $\frac14$. Result $\frac\pi8-\frac14$."],
  lambda: defint(x**2*sp.sin(2*x), 0, sp.pi/4, sp.pi/8 - sp.Rational(1, 4)))
H("hw10-6", "hw10", 6, "7.3", "Trig integrals", r"Evaluate $\displaystyle\int\cos2x\cos5x\,dx$ by first writing the product as a sum.",
  r"$\int\left(\frac12\cos3x+\frac12\cos7x\right)dx=\frac16\sin3x+\frac1{14}\sin7x+C$",
  [r"$\cos\alpha\cos\beta=\frac12[\cos(\alpha-\beta)+\cos(\alpha+\beta)]$: $\cos2x\cos5x=\frac12\cos3x+\frac12\cos7x$.", r"Integrate: $\frac16\sin3x+\frac1{14}\sin7x+C$."],
  lambda: antideriv(sp.sin(3*x)/6 + sp.sin(7*x)/14, sp.cos(2*x)*sp.cos(5*x)))
H("hw10-7", "hw10", 7, "7.3", "Trig integrals", r"Evaluate $\displaystyle\int\sin^5x\cos^2x\,dx$.",
  r"$-\frac13\cos^3x+\frac25\cos^5x-\frac17\cos^7x+C$",
  [r"Odd power of sine: $\sin^5x=(1-\cos^2x)^2\sin x$.", r"$u=\cos x$, $du=-\sin x\,dx$: $-\int(1-u^2)^2u^2du=-\int(u^2-2u^4+u^6)du$.", r"$=-\frac{u^3}3+\frac{2u^5}5-\frac{u^7}7+C$."],
  lambda: antideriv(-sp.cos(x)**3/3 + 2*sp.cos(x)**5/5 - sp.cos(x)**7/7, sp.sin(x)**5*sp.cos(x)**2))
H("hw10-8", "hw10", 8, "7.3", "Trig integrals", r"Evaluate $\displaystyle\int\cos^9x\tan^3x\,dx$.",
  r"$-\frac17\cos^7x+\frac19\cos^9x+C$",
  [r"$\cos^9x\tan^3x=\sin^3x\cos^6x$; odd power of sine: $\sin^3x=(1-\cos^2x)\sin x$.", r"$u=\cos x$: $-\int(1-u^2)u^6du=-\frac{u^7}7+\frac{u^9}9+C$."],
  lambda: antideriv(-sp.cos(x)**7/7 + sp.cos(x)**9/9, sp.cos(x)**9*sp.tan(x)**3))
H("hw10-9", "hw10", 9, "7.3", "Trig integrals", r"Evaluate $\displaystyle\int6\sec^4\left(\frac x2\right)dx$.",
  r"$12\tan\frac x2+4\tan^3\frac x2+C$",
  [r"$w=\frac x2$, $dx=2\,dw$: $12\int\sec^4w\,dw$.", r"Even power of secant: $\sec^4w=(1+\tan^2w)\sec^2w$, $u=\tan w$: $12\int(1+u^2)du=12u+4u^3$.",
   r"$=12\tan\frac x2+4\tan^3\frac x2+C$."],
  lambda: antideriv(12*sp.tan(x/2) + 4*sp.tan(x/2)**3, 6*sp.sec(x/2)**4))
H("hw10-10", "hw10", 10, "7.3", "Trig integrals", r"Evaluate $\displaystyle\int\tan^6x\sec^2x\,dx$.",
  r"$\frac17\tan^7x+C$", [r"$u=\tan x$, $du=\sec^2x\,dx$: $\int u^6du=\frac{u^7}7+C$."], lambda: antideriv(sp.tan(x)**7/7, sp.tan(x)**6*sp.sec(x)**2), diff="easy")
