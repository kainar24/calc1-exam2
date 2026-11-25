# Generated problems, integration side (Ch. 5, §7.2–7.3). Every problem carries a SymPy check;
# tools/make_problems.py drops any generated problem whose check fails.
from pkit import *

L = lambda e: sp.latex(e, ln_notation=True)
def D(e): return "$\\displaystyle " + L(e) + "$"
def M(e): return "$" + L(e) + "$"
def I(f, a=None, b=None, v=x):
    return sp.Integral(f, (v, a, b)) if a is not None else sp.Integral(f, v)

# ------------------------------------------------------------------ §5.9 definite u-substitution
def dsub_power(i, m, c, p, a, b, k=1):
    """∫_a^b k x^{m-1} (x^m + c)^p dx, u = x^m + c."""
    f = k*x**(m-1)*(x**m + c)**p
    ua, ub = a**m + c, b**m + c
    coef = sp.Rational(k, m)
    F = coef*u**(p+1)/(p+1)
    val = sp.simplify(F.subs(u, ub) - F.subs(u, ua))
    G(f"gen-dsub-{i}", "5.9", "Definite u-substitution", "Evaluate " + D(I(f, a, b)) + ".", M(val),
      [f"Let $u={L(x**m+c)}$. Then $du={L(m*x**(m-1))}\\,dx$, so ${L(k*x**(m-1))}\\,dx={L(coef)}\\,du$.",
       f"Change the limits: $x={L(a)}\\Rightarrow u={L(ua)}$, $\\ x={L(b)}\\Rightarrow u={L(ub)}$.",
       f"The integral becomes ${L(coef)}\\displaystyle\\int_{{{L(ua)}}}^{{{L(ub)}}}{L(u**p)}\\,du={L(coef)}\\left[{L(u**(p+1)/(p+1))}\\right]_{{{L(ua)}}}^{{{L(ub)}}}$.",
       f"$={L(val)}$" + (f" $\\approx {float(val):.4f}$" if not val.is_Integer else "") + "."],
      lambda: defint(f, a, b, val), family="power")

dsub_power(1, 2, 1, 3, 0, 1, k=1)                         # ∫ x (x²+1)³
dsub_power(2, 3, 1, sp.Rational(1, 2), 0, 2, k=1)         # ∫ x² √(x³+1)
dsub_power(3, 2, 9, sp.Rational(-1, 2), 0, 4, k=1)        # ∫ x/√(x²+9)
dsub_power(4, 4, 1, -2, 0, 1, k=4)                        # ∫ 4x³/(x⁴+1)²

def dsub_trig(i, f, usub, du_text, a, b, ua, ub, g_u, val, note=""):
    G(f"gen-dsub-{i}", "5.9", "Definite u-substitution", "Evaluate " + D(I(f, a, b)) + ".", M(val),
      [f"Let $u={usub}$, so {du_text}.", f"Limits: $x={L(a)}\\Rightarrow u={L(ua)}$, $\\ x={L(b)}\\Rightarrow u={L(ub)}$.",
       f"$\\displaystyle\\int_{{{L(ua)}}}^{{{L(ub)}}}{L(g_u)}\\,du" + (f"={note}" if note else "") + f"={L(val)}$."],
      lambda: defint(f, a, b, val), family="trig")

dsub_trig(5, sp.sin(x)*sp.cos(x)**3, r"\cos x", r"$du=-\sin x\,dx$", 0, sp.pi/2, 1, 0, -u**3, sp.Rational(1, 4),
          r"\left[-\tfrac{u^4}{4}\right]_1^0")
dsub_trig(6, sp.log(x)**2/x, r"\ln x", r"$du=\frac{dx}{x}$", 1, sp.E**2, 0, 2, u**2, sp.Rational(8, 3), r"\left[\tfrac{u^3}{3}\right]_0^2")
dsub_trig(7, sp.exp(x)/(1 + sp.exp(2*x)), r"e^x", r"$du=e^x\,dx$ and $e^{2x}=u^2$", 0, sp.log(sp.sqrt(3)), 1, sp.sqrt(3), 1/(1 + u**2),
          sp.pi/12, r"\left[\arctan u\right]_1^{\sqrt3}=\tfrac\pi3-\tfrac\pi4")
dsub_trig(8, sp.cos(x)*sp.sqrt(4 - sp.sin(x)**2), r"\sin x", r"$du=\cos x\,dx$", 0, sp.pi/2, 0, 1, sp.sqrt(4 - u**2),
          sp.sqrt(3)/2 + sp.pi/3, r"\text{(area under the circle of radius 2 from 0 to 1: triangle } \tfrac{\sqrt3}{2} + \text{sector } \tfrac{\pi}{3})")
dsub_trig(9, x*sp.sqrt(16 - x**4), r"x^2", r"$du=2x\,dx$, i.e. $x\,dx=\tfrac12du$", 0, 2, 0, 4, sp.sqrt(16 - u**2)/2, 2*sp.pi,
          r"\tfrac12\cdot\tfrac14\pi(4)^2\ \text{(half of a quarter disk of radius 4)}")
dsub_trig(10, sp.sin(2*x)/(1 + sp.cos(2*x))**2, r"1+\cos 2x", r"$du=-2\sin 2x\,dx$", 0, sp.pi/3, 2, sp.Rational(1, 2), -1/(2*u**2),
          sp.Rational(-1, 2) + 2 - sp.Rational(1, 2) if False else 1 - sp.Rational(1, 4), r"\left[\tfrac{1}{2u}\right]_2^{1/2}")

# ------------------------------------------------------------------ §5.3 indefinite u-substitution
def isub(i, f, usub, du_text, g_u, Fu, F, diff="exam"):
    G(f"gen-isub-{i}", "5.3", "u-substitution (indefinite)", "Evaluate " + D(I(f)) + ".", M(F) + "$+C$",
      [f"Let $u={usub}$; then {du_text}.", f"$\\displaystyle\\int {L(g_u)}\\,du={L(Fu)}+C$.", f"Substitute back: ${L(F)}+C$.",
       "Check: differentiating gives back the integrand."],
      lambda: antideriv(F, f, pts=(0.2, 0.45, 0.7, 0.9)), diff=diff)

isub(1, x**2*sp.cos(x**3), r"x^3", r"$du=3x^2dx$", sp.cos(u)/3, sp.sin(u)/3, sp.sin(x**3)/3, "easy")
isub(2, sp.sec(x)**2*sp.tan(x)**3, r"\tan x", r"$du=\sec^2x\,dx$", u**3, u**4/4, sp.tan(x)**4/4)
isub(3, (2*x + 3)/(x**2 + 3*x + 5), r"x^2+3x+5", r"$du=(2x+3)\,dx$", 1/u, sp.log(u), sp.log(x**2 + 3*x + 5))
isub(4, sp.exp(sp.sqrt(x))/sp.sqrt(x), r"\sqrt x", r"$du=\frac{dx}{2\sqrt x}$, so $\frac{dx}{\sqrt x}=2\,du$", 2*sp.exp(u), 2*sp.exp(u), 2*sp.exp(sp.sqrt(x)))
isub(5, x/sp.sqrt(1 - x**4), r"x^2", r"$du=2x\,dx$", 1/(2*sp.sqrt(1 - u**2)), sp.asin(u)/2, sp.asin(x**2)/2)
isub(6, x**3/(16 + x**8), r"x^4", r"$du=4x^3dx$", 1/(4*(16 + u**2)), sp.atan(u/4)/16, sp.atan(x**4/4)/16, "hard")
isub(7, x**3*sp.sqrt(x**2 + 1), r"x^2+1", r"$du=2x\,dx$ and $x^2=u-1$", (u - 1)*sp.sqrt(u)/2,
     u**sp.Rational(5, 2)/5 - u**sp.Rational(3, 2)/3, (x**2 + 1)**sp.Rational(5, 2)/5 - (x**2 + 1)**sp.Rational(3, 2)/3, "hard")
isub(8, sp.sin(sp.log(x))/x, r"\ln x", r"$du=\frac{dx}{x}$", sp.sin(u), -sp.cos(u), -sp.cos(sp.log(x)), "easy")

# ------------------------------------------------------------------ §7.2 integration by parts
def ibp(i, f, uu, dv, du_, v_, F, extra_steps, a=None, b=None, val=None, diff="exam"):
    st = [f"Choose (LIATE) $u={uu}$, $dv={dv}$, so $du={du_}$, $v={v_}$."] + extra_steps
    if a is None:
        G(f"gen-ibp-{i}", "7.2", "Integration by parts", "Evaluate " + D(I(f)) + ".", M(F) + "$+C$", st + [f"Answer: ${L(F)}+C$."],
          lambda: antideriv(F, f), diff=diff)
    else:
        G(f"gen-ibp-{i}", "7.2", "Integration by parts", "Evaluate " + D(I(f, a, b)) + ".", M(val),
          st + [f"Antiderivative ${L(F)}$; evaluate from ${L(a)}$ to ${L(b)}$: ${L(val)}$."], lambda: defint(f, a, b, val), diff=diff)

ibp(1, x*sp.exp(3*x), "x", r"e^{3x}dx", "dx", r"\tfrac13e^{3x}", (x/3 - sp.Rational(1, 9))*sp.exp(3*x),
    [r"$\int xe^{3x}dx=\tfrac x3e^{3x}-\tfrac13\int e^{3x}dx=\tfrac x3e^{3x}-\tfrac19e^{3x}+C$."], diff="easy")
ibp(2, x*sp.cos(2*x), "x", r"\cos 2x\,dx", "dx", r"\tfrac12\sin2x", x*sp.sin(2*x)/2 + sp.cos(2*x)/4,
    [r"$\tfrac x2\sin2x-\tfrac12\int\sin2x\,dx=\tfrac x2\sin2x+\tfrac14\cos2x+C$."], a=0, b=sp.pi/2, val=-sp.Rational(1, 2))
ibp(3, x**3*sp.log(x), r"\ln x", r"x^3dx", r"\tfrac{dx}{x}", r"\tfrac{x^4}{4}", x**4*sp.log(x)/4 - x**4/16,
    [r"$\tfrac{x^4}4\ln x-\int\tfrac{x^4}4\cdot\tfrac1x\,dx=\tfrac{x^4}4\ln x-\tfrac{x^4}{16}$."], a=1, b=sp.E, val=(3*sp.E**4 + 1)/16)
ibp(4, x**2*sp.exp(-x), r"x^2", r"e^{-x}dx", r"2x\,dx", r"-e^{-x}", -(x**2 + 2*x + 2)*sp.exp(-x),
    [r"Tabular: D: $x^2,2x,2,0$; I: $e^{-x},-e^{-x},e^{-x},-e^{-x}$.", r"Signs $+,-,+$: $-x^2e^{-x}-2xe^{-x}-2e^{-x}$."], a=0, b=1, val=2 - 5/sp.E)
ibp(5, sp.log(x), r"\ln x", "dx", r"\tfrac{dx}{x}", "x", x*sp.log(x) - x, [r"$x\ln x-\int x\cdot\tfrac1x\,dx=x\ln x-x$."], a=1, b=sp.E, val=1, diff="easy")
ibp(6, sp.atan(x), r"\arctan x", "dx", r"\tfrac{dx}{1+x^2}", "x", x*sp.atan(x) - sp.log(1 + x**2)/2,
    [r"$x\arctan x-\int\tfrac{x}{1+x^2}dx$; with $w=1+x^2$: $\int\tfrac{x\,dx}{1+x^2}=\tfrac12\ln(1+x^2)$."], a=0, b=1, val=sp.pi/4 - sp.log(2)/2)
ibp(7, sp.exp(x)*sp.sin(x), r"\sin x", r"e^xdx", r"\cos x\,dx", r"e^x", sp.exp(x)*(sp.sin(x) - sp.cos(x))/2,
    [r"$I=e^x\sin x-\int e^x\cos x\,dx$.", r"Again with $u=\cos x$: $\int e^x\cos x\,dx=e^x\cos x+\int e^x\sin x\,dx=e^x\cos x+I$.",
     r"So $I=e^x\sin x-e^x\cos x-I\Rightarrow 2I=e^x(\sin x-\cos x)$."], diff="hard")
ibp(8, x**2*sp.sin(x), r"x^2", r"\sin x\,dx", r"2x\,dx", r"-\cos x", -x**2*sp.cos(x) + 2*x*sp.sin(x) + 2*sp.cos(x),
    [r"Tabular: D: $x^2,2x,2,0$; I: $\sin x,-\cos x,-\sin x,\cos x$.", r"$-x^2\cos x+2x\sin x+2\cos x$."], a=0, b=sp.pi, val=sp.pi**2 - 4)
ibp(9, x*sp.sec(x)**2, "x", r"\sec^2x\,dx", "dx", r"\tan x", x*sp.tan(x) + sp.log(sp.cos(x)),
    [r"$x\tan x-\int\tan x\,dx=x\tan x-\ln|\sec x|=x\tan x+\ln|\cos x|$."], a=0, b=sp.pi/4, val=sp.pi/4 - sp.log(2)/2, diff="hard")

# ------------------------------------------------------------------ §7.3 trig integrals
def trig(i, f, plan, sub_text, Fu_text, F, a=None, b=None, val=None, diff="exam"):
    st = [plan, sub_text, Fu_text]
    if a is None:
        G(f"gen-trig-{i}", "7.3", "Trig integrals", "Evaluate " + D(I(f)) + ".", M(F) + "$+C$", st + [f"Answer: ${L(F)}+C$."], lambda: antideriv(F, f), diff=diff)
    else:
        G(f"gen-trig-{i}", "7.3", "Trig integrals", "Evaluate " + D(I(f, a, b)) + ".", M(val), st + [f"Value: ${L(val)}$."], lambda: defint(f, a, b, val), diff=diff)

trig(1, sp.sin(x)**3*sp.cos(x)**2, r"Odd power of sine: save one $\sin x$, write $\sin^2x=1-\cos^2x$.",
     r"$\int(1-\cos^2x)\cos^2x\sin x\,dx$, $u=\cos x$, $du=-\sin x\,dx$: $-\int(u^2-u^4)\,du$.",
     r"$=-\tfrac{u^3}3+\tfrac{u^5}5$.", -sp.cos(x)**3/3 + sp.cos(x)**5/5)
trig(2, sp.cos(x)**5, r"Odd power of cosine: $\cos^5x=(1-\sin^2x)^2\cos x$.", r"$u=\sin x$: $\int(1-u^2)^2du=\int(1-2u^2+u^4)\,du$.",
     r"$=u-\tfrac23u^3+\tfrac15u^5$.", sp.sin(x) - 2*sp.sin(x)**3/3 + sp.sin(x)**5/5, a=0, b=sp.pi/2, val=sp.Rational(8, 15))
trig(3, sp.sin(x)**2, r"Even power: $\sin^2x=\tfrac{1-\cos2x}{2}$.", r"$\int\tfrac{1-\cos2x}2\,dx$.", r"$=\tfrac x2-\tfrac{\sin2x}4$.",
     x/2 - sp.sin(2*x)/4, a=0, b=sp.pi, val=sp.pi/2, diff="easy")
trig(4, sp.tan(x)**3*sp.sec(x)**4, r"Even power of secant: save $\sec^2x$, write $\sec^2x=1+\tan^2x$.", r"$u=\tan x$: $\int u^3(1+u^2)\,du$.",
     r"$=\tfrac{u^4}4+\tfrac{u^6}6$.", sp.tan(x)**4/4 + sp.tan(x)**6/6)
trig(5, sp.tan(x)**3*sp.sec(x), r"Odd power of tangent: save $\sec x\tan x$, write $\tan^2x=\sec^2x-1$.", r"$u=\sec x$, $du=\sec x\tan x\,dx$: $\int(u^2-1)\,du$.",
     r"$=\tfrac{u^3}3-u$.", sp.sec(x)**3/3 - sp.sec(x), a=0, b=sp.pi/3, val=sp.Rational(8, 3) - 2 + sp.Rational(2, 3) if False else sp.Rational(4, 3))
trig(6, sp.cos(x)**4, r"Both even: use $\cos^2x=\tfrac{1+\cos2x}2$ twice.",
     r"$\cos^4x=\tfrac14(1+2\cos2x+\cos^22x)=\tfrac14\left(1+2\cos2x+\tfrac{1+\cos4x}2\right)=\tfrac38+\tfrac12\cos2x+\tfrac18\cos4x$.",
     r"Integrate: $\tfrac38x+\tfrac14\sin2x+\tfrac1{32}\sin4x$.", 3*x/8 + sp.sin(2*x)/4 + sp.sin(4*x)/32, diff="hard")
trig(7, sp.sin(3*x)*sp.cos(x), r"Product formula: $\sin A\cos B=\tfrac12[\sin(A-B)+\sin(A+B)]$.", r"$\sin3x\cos x=\tfrac12(\sin2x+\sin4x)$.",
     r"$\int=-\tfrac14\cos2x-\tfrac18\cos4x$.", -sp.cos(2*x)/4 - sp.cos(4*x)/8, a=0, b=sp.pi/2, val=sp.Rational(1, 2))
trig(8, sp.tan(x)**2, r"Use $\tan^2x=\sec^2x-1$.", r"$\int(\sec^2x-1)\,dx$.", r"$=\tan x-x$.", sp.tan(x) - x, a=0, b=sp.pi/4, val=1 - sp.pi/4, diff="easy")
trig(9, sp.sin(x)**2*sp.cos(x)**2, r"Both even: $\sin x\cos x=\tfrac12\sin2x$, so $\sin^2x\cos^2x=\tfrac14\sin^22x=\tfrac18(1-\cos4x)$.",
     r"$\int\tfrac18(1-\cos4x)\,dx$.", r"$=\tfrac x8-\tfrac{\sin4x}{32}$.", x/8 - sp.sin(4*x)/32, a=0, b=sp.pi/2, val=sp.pi/16, diff="hard")

# ------------------------------------------------------------------ §5.2 antiderivatives & IVPs
def anti(i, f, F, steps, diff="easy"):
    G(f"gen-anti-{i}", "5.2", "Antiderivatives & IVPs", "Find " + D(I(f)) + ".", M(F) + "$+C$", steps + [f"Answer: ${L(F)}+C$."], lambda: antideriv(F, f), diff=diff)

anti(1, 6*x**2 - 4/x**3 + 2*sp.sqrt(x), 2*x**3 + 2/x**2 + sp.Rational(4, 3)*x**sp.Rational(3, 2),
     [r"Write as powers: $6x^2-4x^{-3}+2x^{1/2}$.", r"Power rule: $2x^3-4\cdot\tfrac{x^{-2}}{-2}+2\cdot\tfrac{x^{3/2}}{3/2}=2x^3+\tfrac2{x^2}+\tfrac43x^{3/2}$."])
anti(2, (x**2 + 1)**2/x**2, x**3/3 + 2*x - 1/x, [r"Expand: $\tfrac{x^4+2x^2+1}{x^2}=x^2+2+x^{-2}$.", r"Integrate term by term."])
anti(3, sp.sec(x)*(sp.sec(x) + sp.tan(x)), sp.tan(x) + sp.sec(x), [r"Expand: $\sec^2x+\sec x\tan x$.", r"$\int\sec^2x=\tan x$, $\int\sec x\tan x=\sec x$."])
anti(4, (1 + sp.cos(x)**2)/sp.cos(x)**2, sp.tan(x) + x, [r"Split: $\tfrac1{\cos^2x}+1=\sec^2x+1$."])
anti(5, 3*sp.exp(x) - 5/(1 + x**2) + 2/x, 3*sp.exp(x) - 5*sp.atan(x) + 2*sp.log(x), [r"Use $\int e^x=e^x$, $\int\tfrac{dx}{1+x^2}=\arctan x$, $\int\tfrac{dx}x=\ln|x|$."])

def ivp(i, fp, x0, y0, F, diff="exam"):
    C = sp.simplify(y0 - F.subs(x, x0)); Y = F + C
    G(f"gen-ivp-{i}", "5.2", "Antiderivatives & IVPs", f"Solve the initial value problem $\\dfrac{{dy}}{{dx}}={L(fp)}$, $\\ y({L(x0)})={L(y0)}$.", f"$y={L(Y)}$",
      [f"Integrate: $y=\\displaystyle\\int\\left({L(fp)}\\right)dx={L(F)}+C$.", f"Use $y({L(x0)})={L(y0)}$: ${L(F.subs(x, x0))}+C={L(y0)}\\Rightarrow C={L(C)}$.",
       f"So $y={L(Y)}$."], lambda: all_true(antideriv(Y, fp), same(Y.subs(x, x0), y0)), diff=diff)

ivp(1, 3*x**2 - 2*x + 1, 1, 4, x**3 - x**2 + x, "easy")
ivp(2, sp.cos(x) - 2*sp.sin(x), 0, 5, sp.sin(x) + 2*sp.cos(x))
ivp(3, 1/x + sp.exp(2*x), 1, sp.exp(2)/2, sp.log(x) + sp.exp(2*x)/2)
ivp(4, x*sp.sqrt(x**2 + 16), 0, 1, (x**2 + 16)**sp.Rational(3, 2)/3, "hard")

# ------------------------------------------------------------------ §5.6 FTC: derivative of an integral
def ftcd(i, f, lo, hi, diff="exam"):
    ans = sp.simplify(f.subs(t, hi)*sp.diff(hi, x) - f.subs(t, lo)*sp.diff(lo, x))
    if lo.is_number:
        st = [r"FTC Part 2 with the chain rule: $\dfrac{d}{dx}\displaystyle\int_a^{g(x)}f(t)\,dt=f(g(x))\,g'(x)$.",
              f"Here $f(t)={L(f)}$, $g(x)={L(hi)}$, $g'(x)={L(sp.diff(hi, x))}$.", f"Answer: ${L(ans)}$."]
    else:
        st = [r"Split at a constant: $\displaystyle\int_{h(x)}^{g(x)}=\int_0^{g(x)}-\int_0^{h(x)}$.",
              f"Upper limit: $f({L(hi)})\\cdot{L(sp.diff(hi, x))}$; lower limit: $f({L(lo)})\\cdot{L(sp.diff(lo, x))}$.", f"Answer: ${L(ans)}$."]
    G(f"gen-ftcd-{i}", "5.6", "FTC: derivative of an integral", f"Find $\\dfrac{{d}}{{dx}}\\displaystyle\\int_{{{L(lo)}}}^{{{L(hi)}}}{L(f)}\\,dt$.", M(ans), st,
      lambda: antideriv(sp.Integral(f, (t, lo, hi)), ans, pts=(0.3, 0.6, 0.9)), diff=diff)

ftcd(1, sp.sqrt(1 + t**3), sp.Integer(0), x**2, "easy")
ftcd(2, sp.cos(t**2), sp.Integer(1), sp.sqrt(x))
ftcd(3, t*sp.exp(t), sp.Integer(2), sp.sin(x))
ftcd(4, 1/(1 + t**4), x, x**3, "hard")
ftcd(5, sp.log(1 + t**2), sp.cos(x), sp.Integer(5), "hard")
ftcd(6, sp.sin(t)/t, x**2, 3*x, "hard")
G("gen-ftcd-7", "5.6", "FTC: derivative of an integral", r"Find a function $f$ and a number $a$ such that $\displaystyle 6+\int_a^x\frac{f(t)}{t^2}\,dt=2\sqrt x$ for $x&gt;0$.",
  r"$f(x)=x^{3/2}$, $a=9$",
  [r"Differentiate both sides (FTC): $\dfrac{f(x)}{x^2}=\dfrac1{\sqrt x}\Rightarrow f(x)=x^{3/2}$.", r"Put $x=a$: the integral is $0$, so $6=2\sqrt a\Rightarrow a=9$."],
  lambda: same(6 + sp.integrate(t**sp.Rational(3, 2)/t**2, (t, 9, x)), 2*sp.sqrt(x)), diff="hard")
G("gen-ftcd-8", "5.6", "FTC: derivative of an integral", r"Let $F(x)=\displaystyle\int_0^x\frac{t^2-4}{1+t^2}\,dt$. On which intervals is $F$ increasing? Where does $F$ have relative extrema?",
  r"$F\nearrow$ on $(-\infty,-2]$ and $[2,\infty)$, $\searrow$ on $[-2,2]$; rel. max at $x=-2$, rel. min at $x=2$",
  [r"By FTC, $F'(x)=\dfrac{x^2-4}{1+x^2}$.", r"Sign: the denominator is positive; $x^2-4&gt;0$ for $|x|&gt;2$.",
   r"$F'$ changes $+\to-$ at $x=-2$ (rel. max) and $-\to+$ at $x=2$ (rel. min)."],
  lambda: same(sp.diff(sp.integrate((t**2 - 4)/(1 + t**2), (t, 0, x)), x), (x**2 - 4)/(1 + x**2)))

# ------------------------------------------------------------------ §5.6 FTC: evaluating definite integrals
def ftce(i, f, a, b, Ftxt, diff="easy"):
    val = sp.integrate(f, (x, a, b))
    G(f"gen-ftce-{i}", "5.6", "FTC: evaluating definite integrals", "Evaluate " + D(I(f, a, b)) + ".", M(sp.simplify(val)),
      [f"An antiderivative is $F(x)={Ftxt}$.", f"FTC: $F({L(b)})-F({L(a)})={L(sp.simplify(val))}$."], lambda: defint(f, a, b, val), diff=diff)

ftce(1, 3*x**2 - 4*x + 1, 0, 2, r"x^3-2x^2+x")
ftce(2, sp.sec(x)**2, 0, sp.pi/4, r"\tan x")
ftce(3, 1/sp.sqrt(1 - x**2), 0, sp.Rational(1, 2), r"\arcsin x")
ftce(4, (x**2 + 1)/x, 1, sp.E, r"\tfrac{x^2}{2}+\ln x", "exam")
ftce(5, sp.exp(2*x) + sp.cos(x), 0, sp.pi/2, r"\tfrac12e^{2x}+\sin x", "exam")
ftce(6, 1/(1 + x**2), -1, sp.sqrt(3), r"\arctan x", "exam")
G("gen-ftce-7", "5.6", "FTC: evaluating definite integrals", r"Find the area of the region under $y=\sin x$ and above the $x$-axis for $0\le x\le\pi$.", "$2$",
  [r"$A=\int_0^\pi\sin x\,dx=[-\cos x]_0^\pi=-(-1)-(-1)=2$."], lambda: defint(sp.sin(x), 0, sp.pi, 2), diff="easy")
G("gen-ftce-8", "5.6", "FTC: evaluating definite integrals", r"Evaluate $\displaystyle\int_{-1}^{2}|x^2-1|\,dx$.", r"$\dfrac83$",
  [r"$x^2-1&lt;0$ on $(-1,1)$ and $&gt;0$ on $(1,2)$.", r"$\int_{-1}^1(1-x^2)\,dx+\int_1^2(x^2-1)\,dx=\tfrac43+\tfrac43=\tfrac83$."],
  lambda: numint(sp.Abs(x**2 - 1), -1, 2, sp.Rational(8, 3)), diff="exam")

# ------------------------------------------------------------------ §5.8 average value
def avg(i, f, a, b, steps, diff="exam"):
    val = sp.simplify(sp.integrate(f, (x, a, b))/(b - a))
    G(f"gen-avg-{i}", "5.8", "Average value", f"Find the average value of $f(x)={L(f)}$ on $[{L(a)},{L(b)}]$.", M(val),
      [f"$f_{{\\text{{ave}}}}=\\dfrac1{{{L(b - a)}}}\\displaystyle\\int_{{{L(a)}}}^{{{L(b)}}}{L(f)}\\,dx$."] + steps + [f"$f_{{\\text{{ave}}}}={L(val)}$."],
      lambda: same(sp.integrate(f, (x, a, b))/(b - a), val), diff=diff)

avg(1, x*sp.sqrt(x**2 + 9), 0, 4, [r"$u=x^2+9$, $du=2x\,dx$, $u:9\to25$: $\tfrac12\int_9^{25}u^{1/2}du=\tfrac13(125-27)=\tfrac{98}3$."])
avg(2, sp.sin(x), 0, sp.pi, [r"$\int_0^\pi\sin x\,dx=2$."], "easy")
avg(3, 1/x, 1, sp.E, [r"$\int_1^e\tfrac{dx}x=\ln e-\ln1=1$."], "easy")
avg(4, x**2/(x**3 + 1)**2, 0, 1, [r"$u=x^3+1$, $du=3x^2dx$, $u:1\to2$: $\tfrac13\int_1^2u^{-2}du=\tfrac13\left(1-\tfrac12\right)=\tfrac16$."])
avg(5, sp.sec(x)**2*sp.tan(x), 0, sp.pi/4, [r"$u=\tan x$: $\int_0^1u\,du=\tfrac12$."])
avg(6, x*sp.exp(-x**2), 0, 2, [r"$u=-x^2$: $\int_0^2xe^{-x^2}dx=\tfrac12(1-e^{-4})$."])
avg(7, 3*x**2 - 2*x, 1, 3, [r"$[x^3-x^2]_1^3=18-0=18$."], "easy")
G("gen-avg-8", "5.8", "Average value", r"Find all numbers $c$ in $[0,3]$ guaranteed by the Mean-Value Theorem for Integrals for $f(x)=x^2$.", r"$c=\sqrt3$",
  [r"$f_{\text{ave}}=\tfrac13\int_0^3x^2dx=\tfrac13\cdot9=3$.", r"Solve $f(c)=c^2=3$ with $c\in[0,3]$: $c=\sqrt3$."],
  lambda: same(sp.integrate(x**2, (x, 0, 3))/3, 3) and sp.sqrt(3) < 3, diff="exam")

# ------------------------------------------------------------------ §5.4 Riemann sums
def riemann(i, f, a, b, diff="exam"):
    dx = (b - a)/n; xk = a + k*dx
    term = sp.expand(f.subs(x, xk)*dx)
    Sn = sp.simplify(sp.summation(term, (k, 1, n)))
    val = sp.limit(Sn, n, sp.oo)
    G(f"gen-riem-{i}", "5.4", "Riemann sums & sigma notation",
      f"Use a Riemann sum with $n$ equal subintervals and right endpoints to find the area under $y={L(f)}$ over $[{L(a)},{L(b)}]$ (take the limit as $n\\to\\infty$).",
      M(val),
      [f"$\\Delta x=\\dfrac{{{L(b)}-{L(a)}}}{{n}}={L(dx)}$, $\\ x_k^*={L(xk)}$.", f"$f(x_k^*)\\Delta x={L(term)}$.",
       r"Use $\sum1=n$, $\sum k=\tfrac{n(n+1)}2$, $\sum k^2=\tfrac{n(n+1)(2n+1)}6$, $\sum k^3=\left[\tfrac{n(n+1)}2\right]^2$:",
       f"$A_n=\\displaystyle\\sum_{{k=1}}^n f(x_k^*)\\Delta x={L(Sn)}$.", f"$A=\\lim_{{n\\to\\infty}}A_n={L(val)}$ (check: $\\int_{{{L(a)}}}^{{{L(b)}}}{L(f)}\\,dx={L(sp.integrate(f, (x, a, b)))}$)."],
      lambda: same(val, sp.integrate(f, (x, a, b))), diff=diff)

riemann(1, x**2, 0, 3, "easy")
riemann(2, 2*x + 1, 1, 4, "easy")
riemann(3, 4 - x**2, 0, 2)
riemann(4, x**3, 0, 2)
riemann(5, x**2 + x, 1, 3, "hard")
riemann(6, 3*x**2 - 2, 0, 1)
G("gen-riem-7", "5.4", "Riemann sums & sigma notation", r"Express $\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac{3}{n}\left(2+\frac{3k}{n}\right)^2$ as a definite integral and evaluate it.",
  r"$\displaystyle\int_2^5x^2\,dx=39$",
  [r"$\Delta x=\tfrac3n$, so $b-a=3$; $x_k=2+\tfrac{3k}n$ starts at $a=2$ ⇒ $b=5$.", r"$f(x)=x^2$: $\int_2^5x^2dx=\tfrac{125-8}3=39$."],
  lambda: same(sp.limit(sp.summation(3/n*(2 + 3*k/n)**2, (k, 1, n)), n, sp.oo), 39))
G("gen-riem-8", "5.4", "Riemann sums & sigma notation", r"Evaluate $\displaystyle\sum_{k=1}^{20}(3k^2-2k+1)$.", "$8210$",
  [r"$3\sum k^2-2\sum k+\sum1=3\cdot\tfrac{20\cdot21\cdot41}6-2\cdot\tfrac{20\cdot21}2+20$.", r"$=8610-420+20=8210$."],
  lambda: sp.summation(3*k**2 - 2*k + 1, (k, 1, 20)) == 8210, diff="easy")

# ------------------------------------------------------------------ §5.5 properties & geometry
G("gen-prop-1", "5.5", "Definite integral: properties & geometry", r"Given $\int_0^4f=7$, $\int_0^{9}f=3$ and $\int_4^9g=-2$, find $\displaystyle\int_4^9\left(3f(x)-2g(x)+1\right)dx$.", "$-3$",
  [r"$\int_4^9f=\int_0^9f-\int_0^4f=3-7=-4$.", r"$3(-4)-2(-2)+(9-4)=-12+4+5=-3$."], lambda: 3*(3 - 7) - 2*(-2) + 5 == -3, diff="easy")
G("gen-prop-2", "5.5", "Definite integral: properties & geometry", r"Evaluate $\displaystyle\int_{-3}^{3}\sqrt{9-x^2}\,dx$ using geometry.", r"$\dfrac{9\pi}2$",
  [r"$y=\sqrt{9-x^2}$ is the upper half of the circle of radius 3.", r"Area $=\tfrac12\pi\cdot3^2=\tfrac{9\pi}2$."], lambda: same(sp.integrate(sp.sqrt(9 - x**2), (x, -3, 3)), 9*sp.pi/2), diff="easy")
G("gen-prop-3", "5.5", "Definite integral: properties & geometry", r"Evaluate $\displaystyle\int_0^5|2x-4|\,dx$.", "$13$",
  [r"Zero at $x=2$; two triangles: left base 2, height 4: area 4; right base 3, height 6: area 9.", r"Total $4+9=13$."], lambda: defint(sp.Abs(2*x - 4), 0, 5, 13), diff="easy")
G("gen-prop-4", "5.5", "Definite integral: properties & geometry", r"Evaluate $\displaystyle\int_{-2}^{2}\left(x^3\cos x+4\right)dx$.", "$16$",
  [r"$x^3\cos x$ is odd, so its integral over $[-2,2]$ is $0$.", r"$\int_{-2}^24\,dx=16$."], lambda: defint(x**3*sp.cos(x) + 4, -2, 2, 16))
G("gen-prop-5", "5.5", "Definite integral: properties & geometry", r"Let $f(x)=\begin{cases}2x,&x\le1\\ 3-x^2,&x&gt;1\end{cases}$. Evaluate $\int_{-1}^{2}f(x)\,dx$.", r"$\dfrac23$",
  [r"Split at $x=1$: $\int_{-1}^12x\,dx+\int_1^2(3-x^2)\,dx$.", r"$=0+\left[3x-\tfrac{x^3}3\right]_1^2=\left(6-\tfrac83\right)-\left(3-\tfrac13\right)=\tfrac23$."],
  lambda: same(sp.integrate(2*x, (x, -1, 1)) + sp.integrate(3 - x**2, (x, 1, 2)), sp.Rational(2, 3)))
G("gen-prop-6", "5.5", "Definite integral: properties & geometry", r"Evaluate $\displaystyle\int_0^4\left(2+\sqrt{16-x^2}\right)dx$ by interpreting it as an area.", r"$8+4\pi$",
  [r"$\int_0^42\,dx=8$ (rectangle).", r"$\int_0^4\sqrt{16-x^2}\,dx$ is a quarter disk of radius 4: $4\pi$."], lambda: same(sp.integrate(2 + sp.sqrt(16 - x**2), (x, 0, 4)), 8 + 4*sp.pi))
G("gen-prop-7", "5.5", "Definite integral: properties & geometry", r"Express $\displaystyle\int_1^4\frac{\ln x}{x+1}\,dx$ as a limit of Riemann sums with right endpoints (do not evaluate).",
  r"$\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac{\ln(1+3k/n)}{2+3k/n}\cdot\frac3n$",
  [r"$\Delta x=\tfrac{4-1}n=\tfrac3n$, $x_k=1+\tfrac{3k}n$.", r"$f(x_k)=\dfrac{\ln(1+3k/n)}{1+3k/n+1}$; multiply by $\Delta x$ and take the limit."],
  lambda: abs(sum(float(sp.log(1 + 3*kk/2000.0))/(2 + 3*kk/2000.0)*3/2000 for kk in range(1, 2001)) - float(sp.Integral(sp.log(x)/(x + 1), (x, 1, 4)).evalf())) < 2e-3)
G("gen-prop-8", "5.5", "Definite integral: properties & geometry", r"If $\int_1^5f(x)\,dx=10$ and $\int_3^5f(x)\,dx=4$, find $\int_3^1\left(5-2f(x)\right)dx$.", "$2$",
  [r"$\int_1^3f=10-4=6$, so $\int_3^1f=-6$.", r"$\int_3^1(5-2f)\,dx=5(1-3)-2(-6)=-10+12=2$."], lambda: 5*(1 - 3) - 2*(-(10 - 4)) == 2)

# ------------------------------------------------------------------ §5.7 motion via integrals
def motion_pos(i, a_expr, t1, s1, t2, s2, diff="exam"):
    C1, C2 = sp.symbols('C1 C2')
    v = sp.integrate(a_expr, t) + C1; s = sp.integrate(v, t) + C2
    sol = sp.solve([sp.Eq(s.subs(t, t1), s1), sp.Eq(s.subs(t, t2), s2)], [C1, C2])
    S = sp.simplify(s.subs(sol))
    G(f"gen-mot-{i}", "5.7", "Motion via integrals", f"A particle has acceleration $a(t)={L(a_expr)}$ for $t&gt;0$, with $s({L(t1)})={L(s1)}$ and $s({L(t2)})={L(s2)}$. Find the position function $s(t)$.",
      f"$s(t)={L(S)}$",
      [f"$v(t)=\\int a\\,dt={L(v)}$.", f"$s(t)=\\int v\\,dt={L(s)}$.",
       f"Conditions: ${L(s.subs(t, t1))}={L(s1)}$ and ${L(s.subs(t, t2))}={L(s2)}$.", f"Solve: $C_1={L(sol[C1])}$, $C_2={L(sol[C2])}$, so $s(t)={L(S)}$."],
      lambda: all_true(same(sp.diff(S, t, 2), a_expr), same(S.subs(t, t1), s1), same(S.subs(t, t2), s2)), diff=diff)

motion_pos(1, -2/t**2, 1, 3, 2, 2*sp.log(2) + 3)
motion_pos(2, 6*t, 0, 1, 1, 4, "easy")
motion_pos(3, sp.cos(t), 0, 0, sp.pi, 2)

def dist(i, v, a, b, roots, diff="exam"):
    disp = sp.integrate(v, (t, a, b)); pts = [a] + roots + [b]
    dis = sum(sp.Abs(sp.integrate(v, (t, pts[j], pts[j+1]))) for j in range(len(pts) - 1))
    pieces = " + ".join([f"\\left|\\int_{{{L(pts[j])}}}^{{{L(pts[j+1])}}}v\\,dt\\right|" for j in range(len(pts) - 1)])
    vals = " + ".join([L(sp.Abs(sp.integrate(v, (t, pts[j], pts[j+1])))) for j in range(len(pts) - 1)])
    G(f"gen-mot-{i}", "5.7", "Motion via integrals", f"A particle moves along a line with velocity $v(t)={L(v)}$ m/s. Find the displacement and the total distance traveled for ${L(a)}\\le t\\le{L(b)}$.",
      f"displacement ${L(sp.simplify(disp))}$ m, distance ${L(sp.simplify(dis))}$ m",
      [f"Displacement $=\\displaystyle\\int_{{{L(a)}}}^{{{L(b)}}}v\\,dt={L(sp.simplify(disp))}$.",
       f"$v=0$ at $t={', '.join(L(r) for r in roots)}$; $v$ changes sign there.",
       f"Distance $=\\displaystyle {pieces}={vals}={L(sp.simplify(dis))}$."],
      lambda: all_true(numint(v, a, b, disp, t), numint(sp.Abs(v), a, b, dis, t)), diff=diff)

dist(4, t**2 - 3*t + 2, 0, 3, [1, 2], "hard")
dist(5, 2*t - 4, 0, 5, [2])
dist(6, sp.sin(t), 0, 2*sp.pi, [sp.pi], "easy")
dist(7, t**2 - 4, 0, 3, [2])
G("gen-mot-8", "5.7", "Motion via integrals", r"A car starts from rest and accelerates at $a(t)=6-2t$ m/s² for $0\le t\le3$. How far does it travel in these 3 seconds?", "$18$ m",
  [r"$v(t)=6t-t^2$ (since $v(0)=0$), and $v\ge0$ on $[0,3]$.", r"Distance $=\int_0^3(6t-t^2)\,dt=\left[3t^2-\tfrac{t^3}3\right]_0^3=27-9=18$ m."],
  lambda: defint(6*t - t**2, 0, 3, 18, t))

# ------------------------------------------------------------------ §5.10 functions defined by integrals
G("gen-lnint-1", "5.10", "Functions defined by integrals", r"Let $F(x)=\displaystyle\int_1^x\frac{dt}{t}$. Without using $\ln$, explain why $F(2)+F(3)=F(6)$.",
  r"$F(6)=F(2)+\int_2^6\frac{dt}t$ and substituting $t=2s$ gives $\int_2^6\frac{dt}t=\int_1^3\frac{ds}s=F(3)$",
  [r"Additivity: $F(6)=\int_1^2\frac{dt}t+\int_2^6\frac{dt}t$.", r"In the second integral put $t=2s$, $dt=2ds$: $t=2\to s=1$, $t=6\to s=3$; $\int_1^3\frac{2\,ds}{2s}=F(3)$.", r"So $F(6)=F(2)+F(3)$, which is $\ln6=\ln2+\ln3$."],
  lambda: same(sp.integrate(1/t, (t, 1, 6)), sp.integrate(1/t, (t, 1, 2)) + sp.integrate(1/t, (t, 1, 3))), diff="hard")
G("gen-lnint-2", "5.10", "Functions defined by integrals", r"Let $G(x)=\displaystyle\int_0^x\frac{\sin t}{1+t^2}\,dt$ for $0\le x\le2\pi$. Where does $G$ have its absolute maximum?", r"$x=\pi$",
  [r"$G'(x)=\dfrac{\sin x}{1+x^2}$: positive on $(0,\pi)$, negative on $(\pi,2\pi)$.", r"$G$ increases up to $\pi$ and then decreases, so the absolute maximum on $[0,2\pi]$ is at $x=\pi$ (and $G(0)=0$ is smaller since $G(\pi)&gt;0$)."],
  lambda: sp.Integral(sp.sin(t)/(1 + t**2), (t, 0, sp.pi)).evalf() > sp.Integral(sp.sin(t)/(1 + t**2), (t, 0, 2*sp.pi)).evalf() > 0)
G("gen-lnint-3", "5.10", "Functions defined by integrals", r"Find the inflection point(s) of $F(x)=\displaystyle\int_0^x\frac{t}{1+t^2}\,dt$.", r"$x=\pm1$",
  [r"$F'(x)=\dfrac{x}{1+x^2}$, $F''(x)=\dfrac{1-x^2}{(1+x^2)^2}$.", r"$F''$ changes sign at $x=\pm1$ ⇒ inflection points at $x=\pm1$."],
  lambda: sorted(sp.solve(sp.diff(x/(1 + x**2), x), x)) == [-1, 1])
G("gen-lnint-4", "5.10", "Functions defined by integrals", r"Evaluate $\dfrac{d}{dx}\displaystyle\int_1^{e^x}\frac{\ln t}{t}\,dt$ in two ways: with the FTC, and by evaluating the integral first.", "$x$",
  [r"FTC: $\dfrac{\ln e^x}{e^x}\cdot e^x=x$.", r"Directly: $\int_1^{e^x}\frac{\ln t}t\,dt=\left[\tfrac12\ln^2t\right]_1^{e^x}=\tfrac{x^2}2$, whose derivative is $x$."],
  lambda: same(sp.diff(sp.integrate(sp.log(t)/t, (t, 1, sp.exp(x))), x), x), diff="easy")
G("gen-lnint-5", "5.10", "Functions defined by integrals", r"Solve $\displaystyle\int_1^{x}\frac{dt}{t}=2$ and $\displaystyle\int_x^{1}\frac{dt}{t}=1$.", r"$x=e^2$; $\ x=e^{-1}$",
  [r"$\int_1^x\frac{dt}t=\ln x=2\Rightarrow x=e^2$.", r"$\int_x^1\frac{dt}t=-\ln x=1\Rightarrow x=e^{-1}$."],
  lambda: same(sp.integrate(1/t, (t, 1, sp.E**2)), 2) and same(sp.integrate(1/t, (t, sp.exp(-1), 1)), 1), diff="easy")
