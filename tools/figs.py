"""Generate SVG figures for problems and lessons (matplotlib)."""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "fig"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "font.family": "DejaVu Sans"})
BLUE, ORANGE, GRAY, GREEN, RED = "#2f5bd3", "#e0663a", "#5d6679", "#1f8a4c", "#c0392b"


def axes(ax, xl=None, yl=None):
    ax.axhline(0, color=GRAY, lw=0.8); ax.axvline(0, color=GRAY, lw=0.8)
    if xl: ax.set_xlim(*xl)
    if yl: ax.set_ylim(*yl)
    ax.grid(alpha=0.25)


def save(fig, name):
    fig.tight_layout(); fig.savefig(OUT / name, transparent=False, facecolor="white"); plt.close(fig)


def fig_fprime():
    fig, ax = plt.subplots(figsize=(5.2, 3.2)); x = np.linspace(-3, 3, 400)
    ax.plot(x, (x + 2)*(x - 1)**2, color=BLUE, lw=2); axes(ax, (-3, 3), (-6, 10))
    ax.set_title("y = f′(x)", color=BLUE); save(fig, "fprime_t2a.svg")


def fig_xexp():
    fig, ax = plt.subplots(figsize=(5.2, 3)); x = np.linspace(-3, 3, 400)
    ax.plot(x, x*np.exp(-x**2), color=BLUE, lw=2); axes(ax, (-3, 3), (-0.6, 0.6))
    for p in [-np.sqrt(1.5), 0, np.sqrt(1.5)]:
        ax.plot(p, p*np.exp(-p**2), "o", color=ORANGE)
    for p in [-1/np.sqrt(2), 1/np.sqrt(2)]:
        ax.plot(p, p*np.exp(-p**2), "o", color=GREEN)
    ax.set_title(r"$f(x)=xe^{-x^2}$ (green: extrema, orange: inflection)", fontsize=10); save(fig, "xexp.svg")


def fig_cusp():
    fig, ax = plt.subplots(figsize=(5.2, 3)); x = np.linspace(-4, 1.5, 600)
    ax.plot(x, 2*x + 3*np.cbrt(x**2), color=BLUE, lw=2); axes(ax, (-4, 1.5), (-3, 7))
    ax.plot([-1, 0, -27/8], [1, 0, 0], "o", color=ORANGE)
    ax.set_title(r"$f(x)=2x+3x^{2/3}$: max at $-1$, cusp min at $0$", fontsize=10); save(fig, "cusp_2x3x23.svg")


def fig_riemann():
    fig, ax = plt.subplots(figsize=(5.2, 3.2)); x = np.linspace(0, 1, 200); n = 6
    for kk in range(1, n + 1):
        xr = kk/n; ax.add_patch(plt.Rectangle(((kk-1)/n, 0), 1/n, 1 - xr**2, facecolor="#f3c6a8", edgecolor=ORANGE))
        ax.plot(xr, 1 - xr**2, "o", color=RED, ms=4)
    ax.plot(x, 1 - x**2, color=BLUE, lw=2); axes(ax, (-0.05, 1.1), (-0.05, 1.1))
    ax.set_title(r"Right-endpoint sum for $y=1-x^2$, $n=6$", fontsize=10); save(fig, "riemann_1mx2.svg")


def fig_vcos():
    fig, ax = plt.subplots(figsize=(5.2, 3)); t = np.linspace(0, np.pi, 300)
    ax.plot(t, np.cos(t), color=BLUE, lw=2)
    ax.fill_between(t, np.cos(t), where=np.cos(t) >= 0, color=GREEN, alpha=0.3)
    ax.fill_between(t, np.cos(t), where=np.cos(t) <= 0, color=RED, alpha=0.3)
    axes(ax, (0, 3.3), (-1.2, 1.2)); ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(["0", "π/2", "π"])
    ax.set_title("v(t)=cos t: areas +1 and −1 (displacement 0, distance 2)", fontsize=9.5); save(fig, "v_cos.svg")


def fig_gauss():
    fig, ax = plt.subplots(figsize=(5.2, 3)); x = np.linspace(-3.2, 3.2, 400)
    ax.plot(x, np.exp(-x**2/2), color=BLUE, lw=2); ax.plot([-1, 1], [np.exp(-.5)]*2, "o", color=ORANGE)
    axes(ax, (-3.2, 3.2), (-0.1, 1.15)); ax.set_title(r"$y=e^{-x^2/2}$, inflection at $x=\pm1$", fontsize=10); save(fig, "gauss.svg")


def fig_x2x():
    fig, ax = plt.subplots(figsize=(5.2, 3)); x = np.linspace(-1.6, 0.6, 400)
    ax.plot(x, (x**2 + x)**2, color=BLUE, lw=2); ax.plot([-1, 0], [0, 0], "o", color=GREEN); ax.plot([-0.5], [1/16], "o", color=ORANGE)
    axes(ax, (-1.6, 0.6), (-0.05, 0.6)); ax.set_title(r"$f(x)=(x^2+x)^2$", fontsize=10); save(fig, "x2x_sq.svg")


def fig_mvt():
    fig, ax = plt.subplots(figsize=(5.2, 3.2)); x = np.linspace(0, np.pi, 300)
    ax.plot(x, x + np.sin(x), color="black", lw=2, label="y = x + sin x")
    ax.plot([0, np.pi], [0, np.pi], "--", color=ORANGE, label="secant")
    c = np.pi/2; xx = np.linspace(0.3, 2.9, 10); ax.plot(xx, (c + 1) + (xx - c), color=BLUE, label="tangent at c=π/2")
    ax.plot(c, c + 1, "o", color=BLUE); axes(ax, (0, 3.3), (0, 4.2)); ax.legend(fontsize=8, loc="lower right")
    ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(["0", "π/2", "π"]); save(fig, "mvt_xsinx.svg")


for f in [fig_fprime, fig_xexp, fig_cusp, fig_riemann, fig_vcos, fig_gauss, fig_x2x, fig_mvt]:
    f()
print(sorted(p.name for p in OUT.iterdir()))
