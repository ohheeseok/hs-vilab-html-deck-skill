"""Writes figures/potentials.svg: three illustrative reward histories and which one each potential
favours (toggle states diff / max / sum). Values are illustrative, not data.

Usage: python make_potentials.py figures/potentials.svg"""
import sys

out = sys.argv[1]
NS = 'xmlns="http://www.w3.org/1999/xhtml"'


def fo(x, y, w, h, cls, t):
    return f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}"><div {NS} class="{cls}">{t}</div></foreignObject>'


X = [300, 560, 820]
Y = lambda r: 560 - 450 * r
D = {"A": [0, .2, .8], "B": [.9, .1, .2], "C": [.6, .6, .6]}
HL = {"diff": "A", "max": "B", "sum": "C"}
p = []
p.append('<path d="M180 580V90" stroke="var(--color-text-heading)" stroke-width="3" fill="none"/>')
for r in (0, .5, 1):
    y = Y(r)
    p.append(f'<path d="M180 {y}H900" stroke="var(--color-border-subtle)" stroke-width="2" fill="none"/>')
    p.append(fo(90, y - 20, 80, 40, "fo fo-r fo-muted", f"{r:g}"))
p.append(fo(190, 30, 420, 40, "fo fo-muted", "중간 보상 $r_\\phi$ (설명용)"))
for i, x in enumerate(X):
    p.append(fo(x - 90, 590, 180, 40, "fo fo-c fo-muted", f"단계 {i + 1}"))
p.append(fo(380, 630, 360, 40, "fo fo-c fo-muted", "노이즈 제거 →"))


def pl(k):
    return "M" + "L".join(f"{x} {Y(r):.0f}" for x, r in zip(X, D[k]))


for k in D:  # base lines, grey
    p.append(f'<path d="{pl(k)}" stroke="var(--color-text-muted)" stroke-width="3" fill="none" opacity="0.55"/>')
    for x, r in zip(X, D[k]):
        p.append(f'<circle cx="{x}" cy="{Y(r):.0f}" r="8" fill="var(--color-text-muted)" opacity="0.55"/>')
# names at the start of each line (left of step 1), where the three start apart
for k in D:
    p.append(fo(X[0] - 82, Y(D[k][0]) - 20, 50, 40, "fo fo-r fo-h", k))
for s, k in HL.items():
    g = [f'<path d="{pl(k)}" stroke="var(--color-accent)" stroke-width="6" fill="none"/>']
    g += [f'<circle cx="{x}" cy="{Y(r):.0f}" r="11" fill="var(--color-accent)"/>' for x, r in zip(X, D[k])]
    p.append(f'<g data-show="{s}">' + "".join(g) + '</g>')
# diff: the last rise of A, to the right of step 3
yA2, yA3 = Y(.2), Y(.8)
xa = X[2] + 44
p.append(f'<g data-show="diff"><path d="M{X[1] + 14} {yA2:.0f}H{xa}" stroke="var(--color-warm)" stroke-width="3" stroke-dasharray="8 6" fill="none"/>'
         f'<path d="M{xa} {yA2:.0f}V{yA3 + 6:.0f}" stroke="var(--color-warm)" stroke-width="4" fill="none"/>'
         f'<path d="M{xa - 8} {yA3 + 16:.0f}L{xa} {yA3 + 2:.0f}L{xa + 8} {yA3 + 16:.0f}" stroke="var(--color-warm)" stroke-width="4" fill="none"/>'
         + fo(xa + 14, (yA2 + yA3) / 2 - 20, 200, 40, "fo fo-h", "증가량 0.6") + '</g>')
yB = Y(.9)
p.append(f'<g data-show="max"><circle cx="{X[0]}" cy="{yB:.0f}" r="24" fill="none" stroke="var(--color-warm)" stroke-width="4"/>'
         + fo(X[0] + 36, yB - 20, 260, 40, "fo fo-h", "최고값 0.9") + '</g>')
yC = Y(.6)
p.append('<g data-show="sum">' + "".join(
    f'<rect x="{x - 14}" y="{yC:.0f}" width="28" height="{560 - yC:.0f}" fill="var(--color-warm)" opacity="0.45"/>' for x in X)
    + fo(560, 30, 480, 40, "fo fo-h", "누적값 0.6 + 0.6 + 0.6 = 1.8") + '</g>')

svg = f'''<svg class="diagram" viewBox="0 0 1060 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="pot-t pot-d">
<title id="pot-t">설명용 보상 이력 세 개와 potential 세 종류</title>
<desc id="pot-d">입자 A의 중간 보상은 0, 0.2, 0.8, B는 0.9, 0.1, 0.2, C는 0.6, 0.6, 0.6이다. Difference는 최근 증가량이 큰 A를, Max는 최고값이 큰 B를, Sum은 누적값이 큰 C를 가장 높게 매긴다. 설명용 수치다.</desc>
{"".join(p)}
</svg>
'''
open(out, "w", encoding="utf-8").write(svg)
print("wrote", out)
