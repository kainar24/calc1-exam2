# "Review - Exam 2" slides by Achenef Tesfahun (Moodle, Fall 2026) — official worked solutions.
from pkit import *

paper("rev-f26", "Exam 2 Review slides · Achenef Tesfahun (Moodle, Nov 2026)", "Review F26", "review", 2026, "Fall",
      [("materials/moodle/Review - Exam 2.pdf", "Review PDF (24 slides)")], True, "Achenef Tesfahun", None,
      "Our instructor's own review for this exam: problems from Ch. 7, 5 and 4 with full solutions. Highest priority.")
S = "rev-f26"
pg = lambda i: f"assets/pages/Review_-_Exam_2_p{i}.png"
R = dict(src="official")

P("rev-7-1a", S, "Ch7 #1a", "7.2", "Integration by parts (tabular)", r"Evaluate $\displaystyle\int4x^4\sin2x\,dx$.",
  r"$-2x^4\cos2x+4x^3\sin2x+6x^2\cos2x-6x\sin2x-3\cos2x+C$",
  [r"Repeated integration by parts — use the tabular (D/I) method: differentiate $4x^4$ until $0$, integrate $\sin2x$ each time.",
   r"D column: $4x^4,\ 16x^3,\ 48x^2,\ 96x,\ 96,\ 0$. I column: $\sin2x,\ -\tfrac12\cos2x,\ -\tfrac14\sin2x,\ \tfrac18\cos2x,\ \tfrac1{16}\sin2x,\ -\tfrac1{32}\cos2x$.",
   r"Multiply along the diagonals with alternating signs $+,-,+,-,+$:",
   r"$4x^4\left(-\tfrac12\cos2x\right)-16x^3\left(-\tfrac14\sin2x\right)+48x^2\left(\tfrac18\cos2x\right)-96x\left(\tfrac1{16}\sin2x\right)+96\left(-\tfrac1{32}\cos2x\right)$",
   r"$=-2x^4\cos2x+4x^3\sin2x+6x^2\cos2x-6x\sin2x-3\cos2x+C.$"],
  check=lambda: antideriv(-2*x**4*sp.cos(2*x) + 4*x**3*sp.sin(2*x) + 6*x**2*sp.cos(2*x) - 6*x*sp.sin(2*x) - 3*sp.cos(2*x), 4*x**4*sp.sin(2*x)),
  page=pg(4), diff="exam", **R)
P("rev-7-1b", S, "Ch7 #1b", "7.2", "Integration by parts", r"Evaluate $\displaystyle\int_1^e x^2\ln x\,dx$.",
  r"$\dfrac{2e^3+1}9$",
  [r"LIATE: $u=\ln x$, $dv=x^2dx$ ⇒ $du=\dfrac1x\,dx$, $v=\dfrac{x^3}3$.",
   r"$\displaystyle\int_1^ex^2\ln x\,dx=\left[\frac{x^3}3\ln x\right]_1^e-\int_1^e\frac{x^3}3\cdot\frac1x\,dx.$",
   r"$=\left(\dfrac{e^3}3\cdot1-\dfrac13\cdot0\right)-\dfrac13\left[\dfrac{x^3}3\right]_1^e=\dfrac{e^3}3-\dfrac{e^3-1}9=\dfrac{2e^3+1}9.$"],
  check=lambda: defint(x**2*sp.log(x), 1, sp.E, (2*sp.E**3 + 1)/9), page=pg(5), **R)
P("rev-7-2", S, "Ch7 #2", "7.2", "Integration by parts (solve for the integral)", r"Evaluate $\displaystyle\int\cos(\ln x)\,dx$.",
  r"$\dfrac x2\left(\cos(\ln x)+\sin(\ln x)\right)+C$",
  [r"First time: $u=\cos(\ln x)$, $dv=dx$ ⇒ $du=-\dfrac{\sin(\ln x)}x dx$, $v=x$: $\ \int\cos(\ln x)\,dx=x\cos(\ln x)+\int\sin(\ln x)\,dx$.",
   r"Second time: $u=\sin(\ln x)$, $dv=dx$ ⇒ $du=\dfrac{\cos(\ln x)}x dx$, $v=x$: $\ \int\sin(\ln x)\,dx=x\sin(\ln x)-\int\cos(\ln x)\,dx$.",
   r"Combine: $I=x\cos(\ln x)+x\sin(\ln x)-I$ where $I=\int\cos(\ln x)\,dx$.",
   r"$2I=x\left(\cos(\ln x)+\sin(\ln x)\right)\Rightarrow I=\dfrac x2\left(\cos(\ln x)+\sin(\ln x)\right)+C.$"],
  check=lambda: antideriv(x/2*(sp.cos(sp.log(x)) + sp.sin(sp.log(x))), sp.cos(sp.log(x))), page=pg(6), diff="hard", **R)
P("rev-7-3", S, "Ch7 #3", "7.3", "Trig integrals (odd power of cos)", r"Evaluate $\displaystyle\int_0^{\pi/3}\sin^43x\cos^33x\,dx$.",
  r"$0$",
  [r"The power of cosine is odd: save one $\cos3x$ and convert the rest: $\cos^33x=(1-\sin^23x)\cos3x$.",
   r"$\displaystyle\int_0^{\pi/3}\sin^43x\,(1-\sin^23x)\cos3x\,dx$.",
   r"$u=\sin3x$, $du=3\cos3x\,dx$; $x=0\to u=0$, $x=\pi/3\to u=\sin\pi=0$.",
   r"$=\dfrac13\displaystyle\int_0^0u^4(1-u^2)\,du=0$ (equal limits)."],
  check=lambda: defint(sp.sin(3*x)**4*sp.cos(3*x)**3, 0, sp.pi/3, 0), page=pg(7), **R)
P("rev-7-4", S, "Ch7 #4", "7.3", "Trig integrals (powers of tan)", r"Evaluate $\displaystyle\int\tan^4x\,dx$.",
  r"$\dfrac{\tan^3x}3-\tan x+x+C$",
  [r"$\tan^4x=\tan^2x\,(\sec^2x-1)=\tan^2x\sec^2x-\tan^2x=\tan^2x\sec^2x-\sec^2x+1$.",
   r"$\int\tan^2x\sec^2x\,dx$: $u=\tan x$, $du=\sec^2x\,dx$ ⇒ $\dfrac{\tan^3x}3$.", r"$\int\sec^2x\,dx=\tan x$, $\int1\,dx=x$.",
   r"$\displaystyle\int\tan^4x\,dx=\frac{\tan^3x}3-\tan x+x+C.$"],
  check=lambda: antideriv(sp.tan(x)**3/3 - sp.tan(x) + x, sp.tan(x)**4), page=pg(8), **R)
P("rev-7-5", S, "Ch7 #5", "7.3", "Trig integrals (even power of sec)", r"Evaluate $\displaystyle\int\sqrt{\tan x}\,\sec^4x\,dx$.",
  r"$\dfrac23\tan^{3/2}x+\dfrac27\tan^{7/2}x+C$",
  [r"Even power of secant: save $\sec^2x$, convert the other $\sec^2x=1+\tan^2x$.", r"$\displaystyle\int\sqrt{\tan x}\,(1+\tan^2x)\sec^2x\,dx$; $u=\tan x$, $du=\sec^2x\,dx$.",
   r"$=\displaystyle\int\left(u^{1/2}+u^{5/2}\right)du=\frac23u^{3/2}+\frac27u^{7/2}+C$."],
  check=lambda: antideriv(sp.Rational(2, 3)*sp.tan(x)**sp.Rational(3, 2) + sp.Rational(2, 7)*sp.tan(x)**sp.Rational(7, 2), sp.sqrt(sp.tan(x))*sp.sec(x)**4, pts=(0.2, 0.5, 0.9, 1.2)),
  page=pg(9), **R)
P("rev-5-1", S, "Ch5 #1", "5.4", "Area as a limit (Riemann sum)", r"Find the area under $y=1-x^2$ over $[0,1]$ as a limit of Riemann sums, choosing $x_k^*$ as right endpoints.",
  r"$\dfrac23$",
  [r"$\Delta x=\dfrac{1-0}n=\dfrac1n$, $x_k^*=0+k\Delta x=\dfrac kn$, $f(x_k^*)=1-\dfrac{k^2}{n^2}$.",
   r"$A_n=\displaystyle\sum_{k=1}^n\left(1-\frac{k^2}{n^2}\right)\frac1n=\frac1n\sum_{k=1}^n1-\frac1{n^3}\sum_{k=1}^nk^2.$",
   r"Formulas: $\sum_{k=1}^n1=n$, $\sum_{k=1}^nk^2=\dfrac{n(n+1)(2n+1)}6$.",
   r"$A_n=1-\dfrac{(n+1)(2n+1)}{6n^2}=1-\dfrac{2n^2+3n+1}{6n^2}$.", r"$A=\lim_{n\to\infty}A_n=1-\dfrac26=\dfrac23.$"],
  check=lambda: same(sp.limit(sp.summation((1 - (k/n)**2)/n, (k, 1, n)), n, sp.oo), sp.Rational(2, 3)), figure="assets/fig/riemann_1mx2.svg", page=pg(11), **R)
P("rev-5-2", S, "Ch5 #2", "5.9", "Definite u-substitution", r"Evaluate $\displaystyle\int_0^{\pi/4}\sec^2x\sqrt{1-\tan^2x}\,dx$.",
  r"$\dfrac\pi4$",
  [r"$u=\tan x$, $du=\sec^2x\,dx$; $x=0\to u=0$, $x=\pi/4\to u=1$.", r"$=\displaystyle\int_0^1\sqrt{1-u^2}\,du$.",
   r"Area interpretation: $y=\sqrt{1-u^2}$ is the upper unit semicircle ⇒ a quarter disk of radius 1: $\dfrac14\pi\cdot1^2=\dfrac\pi4$.",
   r"Alternative: $u=\sin\theta$ ⇒ $\int_0^{\pi/2}\cos^2\theta\,d\theta=\left[\frac\theta2+\frac{\sin2\theta}4\right]_0^{\pi/2}=\frac\pi4$."],
  check=lambda: numint(sp.sec(x)**2*sp.sqrt(1 - sp.tan(x)**2), 0, sp.pi/4, sp.pi/4), page=pg(12), tags=["same as F25 T3-A #8"], **R)
P("rev-5-3a", S, "Ch5 #3a", "5.5", "Piecewise definite integral", r"Evaluate $\displaystyle\int_0^4f(x)\,dx$ if $f(x)=\begin{cases}x^2,&x>2\\5-x,&x\le2\end{cases}$.",
  r"$\dfrac{80}3$",
  [r"Split at the break point $x=2$: $\displaystyle\int_0^2(5-x)\,dx+\int_2^4x^2\,dx$.", r"$=\left[5x-\dfrac{x^2}2\right]_0^2+\left[\dfrac{x^3}3\right]_2^4=8+\dfrac{56}3=\dfrac{80}3.$"],
  check=lambda: same(sp.integrate(5 - x, (x, 0, 2)) + sp.integrate(x**2, (x, 2, 4)), sp.Rational(80, 3)), page=pg(14), **R)
P("rev-5-3b", S, "Ch5 #3b", "5.3", "u-substitution", r"Evaluate $\displaystyle\int\frac{x^5+1}{\sqrt{x^6+6x}}\,dx$.",
  r"$\dfrac13\sqrt{x^6+6x}+C$",
  [r"$u=x^6+6x$ ⇒ $du=(6x^5+6)\,dx=6(x^5+1)\,dx$.", r"$\displaystyle\int\frac{x^5+1}{\sqrt{x^6+6x}}dx=\frac16\int u^{-1/2}du=\frac16\cdot2u^{1/2}+C=\frac13\sqrt{x^6+6x}+C.$"],
  check=lambda: antideriv(sp.sqrt(x**6 + 6*x)/3, (x**5 + 1)/sp.sqrt(x**6 + 6*x)), page=pg(14), diff="easy", **R)
P("rev-5-4a", S, "Ch5 #4a", "5.6", "FTC: derivative of an integral", r"Find $\dfrac{d}{dx}\displaystyle\int_1^{x^3}\sin^2t\,dt$.",
  r"$3x^2\sin^2(x^3)$", [r"$\dfrac{d}{dx}\displaystyle\int_a^{g(x)}f(t)\,dt=f(g(x))\,g'(x)$.", r"$=\sin^2(x^3)\cdot3x^2$."],
  check=lambda: antideriv(sp.Integral(sp.sin(t)**2, (t, 1, x**3)), 3*x**2*sp.sin(x**3)**2), page=pg(15), diff="easy", tags=["same as F25 T3-A #4"], **R)
P("rev-5-4b", S, "Ch5 #4b", "5.6", "FTC: both limits variable", r"Find $\dfrac{d}{dx}\displaystyle\int_{\sin x}^{x^2}\frac{1}{1+t^2}\,dt$.",
  r"$\dfrac{2x}{1+x^4}-\dfrac{\cos x}{1+\sin^2x}$",
  [r"Split at 0: $\displaystyle\int_{\sin x}^{x^2}=\int_0^{x^2}-\int_0^{\sin x}$.", r"Differentiate each with the chain rule: $\dfrac1{1+(x^2)^2}\cdot2x-\dfrac1{1+\sin^2x}\cdot\cos x$."],
  check=lambda: antideriv(sp.Integral(1/(1 + t**2), (t, sp.sin(x), x**2)), 2*x/(1 + x**4) - sp.cos(x)/(1 + sp.sin(x)**2)), page=pg(15), **R)
P("rev-5-5", S, "Ch5 #5", "5.8", "Average value", r"Find the average value of $f(x)=\dfrac{x^2}{\sqrt{x^3+1}}$ on $[0,2]$.",
  r"$\dfrac23$",
  [r"$f_{\text{ave}}=\dfrac1{2-0}\displaystyle\int_0^2\frac{x^2}{\sqrt{x^3+1}}dx$.", r"$u=x^3+1$, $du=3x^2dx$; $u:1\to9$.",
   r"$=\dfrac12\cdot\dfrac13\displaystyle\int_1^9u^{-1/2}du=\frac16\left[2\sqrt u\right]_1^9=\frac16\cdot2(3-1)=\frac23.$"],
  check=lambda: same(sp.integrate(x**2/sp.sqrt(x**3 + 1), (x, 0, 2))/2, sp.Rational(2, 3)), page=pg(16), **R)
P("rev-5-6", S, "Ch5 #6", "5.7", "Displacement vs distance", r"A particle moves with velocity $v(t)=\cos t$ m/s along a line. Find the displacement and the distance traveled for $0\le t\le\pi$.",
  r"Displacement $0$ m, distance $2$ m",
  [r"Displacement $=\displaystyle\int_0^\pi v\,dt=[\sin t]_0^\pi=0$ m.",
   r"Distance $=\displaystyle\int_0^\pi|\cos t|\,dt$; $\cos t\ge0$ on $[0,\pi/2]$, $\le0$ on $[\pi/2,\pi]$.",
   r"$=\displaystyle\int_0^{\pi/2}\cos t\,dt-\int_{\pi/2}^\pi\cos t\,dt=(1-0)-(0-1)=2$ m."],
  check=lambda: all_true(same(sp.integrate(sp.cos(t), (t, 0, sp.pi)), 0), same(sp.integrate(sp.Abs(sp.cos(t)), (t, 0, sp.pi)), 2)),
  figure="assets/fig/v_cos.svg", page=pg(17), **R)
P("rev-4-1", S, "Ch4 #1", "4.1", "Increase/decrease, concavity, inflection", r"Let $f(x)=e^{-x^2/2}$. Find the intervals on which $f$ is increasing, decreasing, concave up and concave down, and locate all inflection points.",
  r"$\nearrow(-\infty,0]$, $\searrow[0,\infty)$; CU on $(-\infty,-1)\cup(1,\infty)$, CD on $(-1,1)$; inflection points $\left(\pm1,\tfrac1{\sqrt e}\right)$",
  [r"$f'(x)=-xe^{-x^2/2}$; $e^{-x^2/2}>0$, so $f'>0$ for $x<0$ and $f'<0$ for $x>0$.",
   r"Increasing on $(-\infty,0]$, decreasing on $[0,\infty)$.",
   r"$f''(x)=-e^{-x^2/2}+x^2e^{-x^2/2}=(x^2-1)e^{-x^2/2}=0\Rightarrow x=\pm1$.",
   r"Sign of $x^2-1$: $+$ for $|x|>1$, $-$ for $|x|<1$ ⇒ CU on $(-\infty,-1)$ and $(1,\infty)$, CD on $(-1,1)$.",
   r"Inflection points: $f(\pm1)=e^{-1/2}$, i.e. $\left(-1,\tfrac1{\sqrt e}\right)$ and $\left(1,\tfrac1{\sqrt e}\right)$."],
  check=lambda: same(sp.diff(sp.exp(-x**2/2), x, 2), (x**2 - 1)*sp.exp(-x**2/2)), figure="assets/fig/gauss.svg", page=pg(19), **R)
P("rev-4-2", S, "Ch4 #2", "4.2", "First derivative test", r"Find the stationary points of $f(x)=(x^2+x)^2$. Use the first derivative test to find the relative minima and maxima.",
  r"Stationary points $x=-1,-\tfrac12,0$; rel. min $f(-1)=f(0)=0$; rel. max $f(-\tfrac12)=\tfrac1{16}$",
  [r"$f'(x)=2(x^2+x)(2x+1)=2x(x+1)(2x+1)$.", r"Stationary points: $x=-1,\ -\tfrac12,\ 0$.",
   r"Sign of $f'$: $-$ on $(-\infty,-1)$, $+$ on $(-1,-\tfrac12)$, $-$ on $(-\tfrac12,0)$, $+$ on $(0,\infty)$.",
   r"$-\to+$ at $x=-1$ and $x=0$: relative minima $f(-1)=f(0)=0$.", r"$+\to-$ at $x=-\tfrac12$: relative maximum $f(-\tfrac12)=\left(\tfrac14-\tfrac12\right)^2=\tfrac1{16}$."],
  check=lambda: (lambda f: all_true(crit(f) == [-1, sp.Rational(-1, 2), 0], same(f.subs(x, sp.Rational(-1, 2)), sp.Rational(1, 16))))((x**2 + x)**2),
  figure="assets/fig/x2x_sq.svg", page=pg(20), **R)
P("rev-4-3", S, "Ch4 #3", "4.4", "Absolute extrema on an open interval", r"Determine whether $f(x)=\dfrac1{x^3-3x^2}$ has any absolute extrema on $(0,3)$. If so, find them and state where they occur.",
  r"No absolute minimum; absolute maximum $f(2)=-\tfrac14$",
  [r"$f(x)=\dfrac1{x^2(x-3)}<0$ on $(0,3)$; $\lim_{x\to0^+}f=-\infty$, $\lim_{x\to3^-}f=-\infty$ ⇒ no absolute minimum.",
   r"$f'(x)=-\dfrac{3x^2-6x}{(x^3-3x^2)^2}=-\dfrac{3x(x-2)}{(x^3-3x^2)^2}$; the only critical point in $(0,3)$ is $x=2$.",
   r"$f'>0$ on $(0,2)$ and $f'<0$ on $(2,3)$ ⇒ $f$ rises then falls, so $x=2$ is the absolute maximum.",
   r"$f(2)=\dfrac1{8-12}=-\dfrac14$."],
  check=lambda: (lambda f: all_true([c for c in crit(f) if 0 < c < 3] == [2], same(f.subs(x, 2), sp.Rational(-1, 4)), sp.limit(f, x, 0, '+') == -sp.oo, sp.limit(f, x, 3, '-') == -sp.oo))(1/(x**3 - 3*x**2)),
  page=pg(21), **R)
P("rev-4-4", S, "Ch4 #4", "4.5", "Optimization", r"Find the point $P(x,y)$ in the first quadrant on the curve $y=\dfrac1x$ such that the rectangle with sides on the coordinate axes and a vertex at $P$ has the smallest possible perimeter.",
  r"$P(1,1)$, smallest perimeter $4$",
  [r"Width $x$, height $y=\dfrac1x$ ⇒ perimeter $P(x)=2x+\dfrac2x$, $x>0$.", r"$P'(x)=2-\dfrac2{x^2}=0\Rightarrow x^2=1\Rightarrow x=1$ ($x>0$).",
   r"$P''(x)=\dfrac4{x^3}>0$ ⇒ minimum; and $P\to\infty$ as $x\to0^+$ or $x\to\infty$, so it is the absolute minimum.", r"$x=1\Rightarrow y=1$, perimeter $P(1)=4$."],
  check=lambda: (lambda Pp: all_true([c for c in crit(Pp) if c > 0] == [1], same(Pp.subs(x, 1), 4)))(2*x + 2/x), page=pg(22), **R)
P("rev-4-5", S, "Ch4 #5", "4.8", "Mean Value Theorem", r"Let $f(x)=x+\sin x$ on $[0,\pi]$. Find the point $c$ in $(0,\pi)$ where the tangent line is parallel to the secant line joining $(0,0)$ and $(\pi,\pi)$.",
  r"$c=\dfrac\pi2$",
  [r"Secant slope $m=\dfrac{f(\pi)-f(0)}{\pi-0}=\dfrac{\pi-0}\pi=1$.", r"$f'(x)=1+\cos x$, so we need $1+\cos c=1\Rightarrow\cos c=0$.",
   r"In $(0,\pi)$ the only solution is $c=\dfrac\pi2$; the tangent at $\left(\tfrac\pi2,\tfrac\pi2+1\right)$ has slope 1."],
  check=lambda: list(sp.solveset(sp.Eq(1 + sp.cos(x), 1), x, sp.Interval.open(0, sp.pi))) == [sp.pi/2], figure="assets/fig/mvt_xsinx.svg", page=pg(23), **R)
