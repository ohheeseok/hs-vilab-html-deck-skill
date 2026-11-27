"""Writes figures/overview_fk.svg (the finished picture, beat 3) for overview_fk.anim.js.

Usage: python make_overview_fk.py figures/overview_fk.svg
Redrawn from Fig. 1 (middle and right panels) with the resampling reduced to one intermediate
column. Particle heights are illustrative, not data."""
import sys

out = sys.argv[1]
NS = 'xmlns="http://www.w3.org/1999/xhtml"'
HIDE = 'opacity="0" visibility="hidden" '

# columns: x_T, two steps, the scored step, one step, x_0
XS = [170, 430, 690, 950, 1210, 1470]
CS = 3                                  # index of the scored column (resampling happens here)
# four best-of-n paths (y down = lower reward); index = column
P = {
    "p1": [300, 288, 262, 246, 226, 206],
    "p2": [352, 344, 330, 322, 334, 326],
    "p3": [400, 414, 430, 452, 446, 452],
    "p4": [444, 430, 404, 388, 396, 392],
}
BEST_OLD = "p1"
SCORE = {"p1": 50, "p2": 34, "p3": 8, "p4": 16}       # bar lengths at the scored column
CUT = ["p3", "p4"]
# after resampling: p1 drawn three times (two copies), p2 once; each continues on its own
COPY_DY = [-34, 34]
NEW = [  # (start key, start dy, ys for columns CS+1.. end)
    ("p1", -34, [196, 150]),
    ("p1", 0, [228, 196]),
    ("p1", 34, [268, 252]),
    ("p2", 0, [312, 300]),
]


def fo(x, y, w, h, cls, text, attrs="", style=""):
    st = f' style="{style}"' if style else ""
    return (f'<foreignObject {attrs}x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}">'
            f'<div {NS} class="{cls}"{st}>{text}</div></foreignObject>')


def node(x, y, fill, stroke, attrs=""):
    return f'<rect {attrs}x="{x - 11}" y="{y - 11}" width="22" height="22" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'


def path(pts):
    return "M" + "L".join(f"{x} {y}" for x, y in pts)


def star(cx, cy, r, attrs=""):
    import math
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = -math.pi / 2 + i * math.pi / 5
        pts.append(f"{cx + rr * math.cos(a):.1f} {cy + rr * math.sin(a):.1f}")
    return f'<path {attrs}d="M{"L".join(pts)}Z" fill="var(--color-warm)" stroke="var(--color-text-heading)" stroke-width="2"/>'


GREY_F, GREY_S = "var(--color-surface-sunken)", "var(--color-text-muted)"
BLUE = "var(--color-accent)"
HEAD = "var(--color-text-heading)"

parts = []
# axes
parts.append(f'<path d="M100 470V70" stroke="{HEAD}" stroke-width="3" fill="none"/>'
             f'<path d="M92 82L100 66L108 82" stroke="{HEAD}" stroke-width="3" fill="none"/>')
parts.append(fo(118, 40, 400, 40, "fo fo-muted", "중간 보상 높음"))
for i, x in enumerate(XS):
    dash = ' stroke-dasharray="8 8"' if i in (0, len(XS) - 1) else ""
    parts.append(f'<path d="M{x} 86V470" stroke="var(--color-border-subtle)" stroke-width="2"{dash} fill="none"/>')
parts.append(fo(XS[0] - 60, 482, 120, 40, "fo fo-c", "$x_T$"))
parts.append(fo(XS[-1] - 60, 482, 120, 40, "fo fo-c", "$x_0$"))
parts.append(fo(XS[1] - 40, 482, XS[-2] - XS[1] + 80, 40, "fo fo-c fo-muted", "노이즈 제거 단계 →"))

# the scored column: bracket and its label; the label swaps in beat 2 (score -> resample)
xc = XS[CS]
parts.append(f'<path data-anim="mark" d="M{xc - 70} 130V474M{xc + 70} 130V474" stroke="var(--color-warm)" stroke-width="4" stroke-dasharray="10 8" fill="none"/>')
parts.append(fo(xc - 170, 84, 400, 40, "fo fo-c fo-h", "중간 단계에서 점수", attrs=f'data-anim="lab-score" {HIDE}'))
parts.append(fo(xc - 170, 84, 400, 40, "fo fo-c fo-h", "점수에 따라 다시 뽑기", attrs='data-anim="lab-res" '))

# best-of-n tails after the scored column (beat 0's paths, leave in beats 1–3)
for k, ys in P.items():
    pts = list(zip(XS[CS:], ys[CS:]))
    nodes = "".join(node(x, y, GREY_F, GREY_S) for x, y in pts[1:])
    parts.append(f'<g data-anim="tail-{k}" {HIDE}><path d="{path(pts)}" stroke="{GREY_S}" stroke-width="3" fill="none"/>{nodes}</g>')
parts.append(f'<g data-anim="star-old" {HIDE}>{star(XS[-1], P[BEST_OLD][-1], 24)}</g>')

# score bars at the scored column, to the right of each node (beat 1)
for k, L in SCORE.items():
    y = P[k][CS]
    parts.append(f'<rect data-anim="bar-{k}" {HIDE}x="{xc + 16}" y="{y - 7}" width="{L}" height="14" rx="3" fill="var(--color-warm)"/>')

# cut marks (beat 2)
for k in CUT:
    y = P[k][CS]
    parts.append(f'<g data-anim="x-{k}" stroke="var(--color-danger-border)" stroke-width="5" stroke-linecap="round">'
                 f'<path d="M{xc - 15} {y - 15}L{xc + 15} {y + 15}M{xc + 15} {y - 15}L{xc - 15} {y + 15}"/></g>')

# new branches from the resampled particles (beat 3), drawn under the nodes
for i, (k, dy, ys) in enumerate(NEW):
    y0 = P[k][CS] + dy
    pts = [(xc, y0)] + list(zip(XS[CS + 1:], ys))
    parts.append(f'<path data-anim="br{i}" d="{path(pts)}" stroke="{BLUE}" stroke-width="3.5" fill="none"/>')
# heads up to the scored column (always there)
for k, ys in P.items():
    pts = list(zip(XS[:CS + 1], ys[:CS + 1]))
    nodes = "".join(node(x, y, GREY_F, GREY_S) for x, y in pts)
    dim = ' opacity="0.35"' if k in CUT else ""
    parts.append(f'<g data-anim="head-{k}"{dim}><path d="{path(pts)}" stroke="{GREY_S}" stroke-width="3" fill="none"/>{nodes}</g>')

# copies of the best particle (beat 2): two nodes beside the parent, joined to it by short arcs
y1 = P["p1"][CS]
arcs = "".join(f'<path d="M{xc - 11} {y1}C{xc - 40} {y1},{xc - 40} {y1 + dy},{xc - 11} {y1 + dy}"/>' for dy in COPY_DY)
parts.append(f'<g data-anim="arcs" stroke="{BLUE}" stroke-width="3" fill="none">{arcs}</g>')
for i, dy in enumerate(COPY_DY):
    parts.append(f'<g data-anim="copy{i}">{node(xc, y1 + dy, "var(--color-surface-brand)", BLUE)}</g>')
for i, (k, dy, ys) in enumerate(NEW):
    nodes = "".join(node(x, y, "var(--color-surface-brand)", BLUE) for x, y in zip(XS[CS + 1:], ys))
    parts.append(f'<g data-anim="bn{i}">{nodes}</g>')
best = min(NEW, key=lambda n: n[2][-1])
parts.append(f'<g data-anim="star-new">{star(XS[-1], best[2][-1], 26)}</g>')

svg = f'''<svg class="diagram" viewBox="0 0 1600 530" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="ofk-title ofk-desc">
  <title id="ofk-title">best-of-n과 FK steering의 입자 경로 (Fig. 1 가운데·오른쪽 패널을 바탕으로 다시 그림)</title>
  <desc id="ofk-desc">입자 4개가 x_T에서 출발해 노이즈를 제거하며 x_0로 간다. best-of-n은 네 경로를 끝까지 따로 만든 뒤 보상이 가장 높은 하나를 고른다. FK steering은 중간 단계에서 각 입자의 중간 보상으로 점수를 매기고, 점수가 낮은 두 입자를 버리고 가장 높은 입자를 복제한 뒤, 복제된 입자들이 각자 다시 갈라져 x_0까지 간다. 높이는 설명용이며 데이터가 아니다.</desc>
  <!-- the file draws the finished picture (beat 3); overview_fk.anim.js starts it from beat 0
       (four best-of-n paths to x_0). Elements the script moves carry data-anim. -->
  {"".join(parts)}
</svg>
'''
open(out, "w", encoding="utf-8").write(svg)
print("wrote", out)
