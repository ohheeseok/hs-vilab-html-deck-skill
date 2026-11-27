"""Writes figures/overview_integral.svg (the finished picture, beat 3).

Usage: python make_overview_integral.py figures/overview_integral.svg [Q1 Q2]
The two questions must match the slide's beat 3 text in deck.json."""
import sys

out = sys.argv[1]
Q1 = sys.argv[2] if len(sys.argv) > 2 else "① 공유 표현의 생성 이득은 무엇에서 오나"
Q2 = sys.argv[3] if len(sys.argv) > 3 else "② 그 이득은 어떤 조건에서 확인됐나"
NS = 'xmlns="http://www.w3.org/1999/xhtml"'
BOLD = "font-weight:700;color:var(--color-text-heading)"
COL = "flex-direction:column;gap:0;line-height:1.15"

# geometry
VX0, VX1 = 760, 1380          # VLM and generation bars share x
VY0, VY1 = 240, 310           # VLM bar
GY0, GY1 = 370, 450           # generation bar / latent chip / decoder
GM = (GY0 + GY1) // 2
LW = (VX1 - VX0) / 32         # one VLM layer
ZX0, ZX1 = 600, 720           # z chip (top) and z_t chip (bottom)
ZY0, ZY1 = 100, 180
ZM = (ZY0 + ZY1) // 2
EX0, EX1, EY0, EY1 = 140, 320, 70, 214   # vision encoder box
STRIPS = [EY1 - 22 - 18 * i for i in range(7)]   # 7 layer groups, shallow (bottom) to deep (top)
AX0, AX1, AY0, AY1 = 364, 574, 92, 188   # Abstraction Fusion


def fo(x, y, w, h, cls, text, attrs="", style=""):
    st = f' style="{style}"' if style else ""
    return (f'<foreignObject {attrs}x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}">'
            f'<div {NS} class="{cls}"{st}>{text}</div></foreignObject>')


def fo2(x, y, w, h, top, bottom, attrs="", style=""):
    """two centred lines in one box, as two foreignObjects (the build escapes markup in labels)"""
    hh = 40
    y0 = y + (h - 2 * hh) / 2
    return (f'<g {attrs}>' + fo(x, round(y0), w, hh, "fo fo-box", top, style=style)
            + fo(x, round(y0 + hh), w, hh, "fo fo-box", bottom, style=style) + '</g>')


def arrow(x0, y, x1, color="var(--color-text-muted)", attrs=""):
    return (f'<g {attrs}stroke="{color}" stroke-width="3" fill="none"><path d="M{x0} {y}H{x1 - 2}"/>'
            f'<path d="M{x1 - 8} {y - 7}L{x1} {y}L{x1 - 8} {y + 7}"/></g>')


HIDE = 'opacity="0" visibility="hidden" '
strips = "".join(
    f'<rect x="{EX0 + 16}" y="{y}" width="{EX1 - EX0 - 32}" height="12" rx="3" fill="var(--color-text-heading)" opacity="{0.25 + 0.11 * i:.2f}"/>'
    for i, y in enumerate(STRIPS))
fan = "".join(f'<path d="M{EX1 + 4} {y + 6}L{AX0 - 4} {(AY0 + AY1) // 2}"/>' for y in STRIPS)
ticks = "".join(f"M{VX0 + k * LW:.1f} {VY0 + 4}V{VY0 + 14}M{VX0 + k * LW:.1f} {VY1 - 14}V{VY1 - 4}" for k in range(1, 32))
links_all = []
for i in range(32):
    x = VX0 + (i + 0.5) * LW
    key = "lk-b" if (i + 1) % 4 == 0 else "lk-x"
    links_all.append((key, f"M{x:.1f} {VY1 + 4}V{GY0 - 4}"))
lk_x = "".join(d for k, d in links_all if k == "lk-x")
lk_b = "".join(d for k, d in links_all if k == "lk-b")

svg = f'''<svg class="diagram" viewBox="0 0 1696 530" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="oi-title oi-desc">
  <title id="oi-title">Integral이 VLM에 생성을 붙이는 방식 (Fig. 1, Fig. 4, Fig. 5와 Sec. 2.2–2.3, App. A.1을 바탕으로 그림)</title>
  <desc id="oi-desc">기존 설계(BAGEL 등): 이해는 고정된 vision encoder의 마지막 층 표현을 VLM에 넣고, 생성은 별도 VAE latent 위에서 VLM의 층마다 짝지은 생성 expert가 맡는다. Integral은 고정된 vision encoder의 여러 층 표현을 Abstraction Fusion으로 모아 시각 토큰 z를 만들고, 이해 입력(semantic projector를 거쳐)과 생성 latent가 모두 이 z의 공간에 놓인다. 생성 결과는 pixel decoder가 이미지로 바꾼다. 생성 stream은 VLM 32층 중 4층마다, 8곳에서만 VLM의 key와 value를 읽는다(Block-wise MoT). 두 질문: {Q1[2:]}(①), {Q2[2:]}(②).</desc>
  <!-- the file draws the finished picture (beat 3); overview_integral.anim.js starts it from the
       baseline design (final-layer understanding input, a separate VAE latent, a generation expert
       at every VLM layer). Elements the script moves carry data-anim. One VLM layer = {LW:.2f} px. -->
<g transform="translate(44,0)">

  <!-- question ①: over the shared token path -->
  <g data-anim="q1">
    <path d="M{AX0} 66V52H{ZX1}V66" fill="none" stroke="var(--color-warm)" stroke-width="4"/>
    {fo(AX0 - 160, 2, ZX1 - AX0 + 320, 44, "fo fo-c fo-h", Q1)}
  </g>

  <!-- input image (an icon, not a sample) -->
  {fo(-20, 58, 160, 36, "fo fo-c", "이미지")}
  <rect x="10" y="100" width="100" height="100" rx="6" fill="var(--color-surface-sunken)" stroke="var(--color-text-heading)" stroke-width="3"/>
  <circle cx="82" cy="126" r="11" fill="var(--color-border-control)"/>
  <path d="M16 192L48 146L70 172L84 158L104 192Z" fill="var(--color-border-control)"/>
  {arrow(116, 150, EX0 - 4)}

  <!-- frozen vision encoder: seven layer groups, shallow at the bottom, deep at the top -->
  <rect x="{EX0}" y="{EY0}" width="{EX1 - EX0}" height="{EY1 - EY0}" rx="10" fill="var(--color-surface)" stroke="var(--color-text-heading)" stroke-width="3"/>
  {strips}
  {fo(EX0 - 50, EY1 + 4, EX1 - EX0 + 100, 40, "fo fo-c fo-muted", "vision encoder · 고정")}

  <!-- baseline (beat 0): only the deepest layer goes on to the VLM -->
  <path data-anim="b0-top" {HIDE}d="M{EX1 + 4} {STRIPS[-1] + 6}H740V{ZM}" fill="none" stroke="var(--color-text-muted)" stroke-width="3"/>

  <!-- Integral: every depth into Abstraction Fusion, then the shared token z -->
  <g data-anim="fan" stroke="var(--color-accent)" stroke-width="3" fill="none">{fan}</g>
  <g data-anim="af">
    <rect x="{AX0}" y="{AY0}" width="{AX1 - AX0}" height="{AY1 - AY0}" rx="10" fill="var(--color-surface-brand)" stroke="var(--color-accent)" stroke-width="3"/>
    {fo2(AX0, AY0, AX1 - AX0, AY1 - AY0, "Abstraction", "Fusion")}
  </g>
  {arrow(AX1 + 4, ZM, ZX0 - 2, "var(--color-accent)", 'data-anim="af-z" ')}
  <g data-anim="zc">
    <rect x="{ZX0}" y="{ZY0}" width="{ZX1 - ZX0}" height="{ZY1 - ZY0}" rx="10" fill="var(--color-accent)"/>
    {fo(ZX0, ZY0, ZX1 - ZX0, ZY1 - ZY0, "fo fo-box", "$z$", style="color:#fff")}
  </g>
  <path data-anim="z-out" d="M{ZX1 + 2} {ZM}H740" fill="none" stroke="var(--color-accent)" stroke-width="3"/>
  <!-- the piece both designs share: down into the VLM's visual input -->
  <path data-anim="in" d="M740 {ZM}V{(VY0 + VY1) // 2}H{VX0 - 6}" fill="none" stroke="var(--color-accent)" stroke-width="3"/>
  <path data-anim="in-head" d="M{VX0 - 12} {(VY0 + VY1) // 2 - 7}L{VX0 - 4} {(VY0 + VY1) // 2}L{VX0 - 12} {(VY0 + VY1) // 2 + 7}" fill="none" stroke="var(--color-accent)" stroke-width="3"/>

  <!-- text condition into the VLM -->
  {fo(980, 176, 300, 36, "fo fo-c fo-muted", "텍스트 조건")}
  <g stroke="var(--color-text-muted)" stroke-width="3" fill="none"><path d="M1130 212V232"/><path d="M1123 226L1130 234L1137 226"/></g>

  <!-- the pretrained VLM, frozen: 32 layers -->
  <rect x="{VX0}" y="{VY0}" width="{VX1 - VX0}" height="{VY1 - VY0}" rx="10" fill="var(--color-text-heading)"/>
  <path d="{ticks}" stroke="#fff" stroke-width="3" opacity=".35"/>
  {fo(VX0, VY0, VX1 - VX0, VY1 - VY0, "fo fo-box", "VLM · 32층 · 고정", style="color:#fff")}

  <!-- where the generation stream reads the VLM: every layer (baseline), every 4th (Block-wise MoT) -->
  <path data-anim="lk-x" {HIDE}d="{lk_x}" stroke="var(--color-text-muted)" stroke-width="3"/>
  <path data-anim="lk-b" d="{lk_b}" stroke="var(--color-accent)" stroke-width="5"/>
  {fo(VX1 + 14, VY1 + 8, 230, 40, "fo fo-muted", "층마다 K/V", 'data-anim="kv0" ' + HIDE)}
  {fo(VX1 + 14, VY1 + 8, 230, 40, "fo", "4층마다 K/V", 'data-anim="kv1" ', BOLD)}

  <!-- the generation latent: a separate VAE latent (baseline) or z_t, in z's space -->
  {fo(ZX0 - 150, GY0 + 2, 120, 36, "fo fo-c fo-muted", "noise")}
  {arrow(ZX0 - 34, GY0 + 20, ZX0 - 4)}
  <rect data-anim="gc" x="{ZX0}" y="{GY0}" width="{ZX1 - ZX0}" height="{GY1 - GY0}" rx="10" fill="var(--color-accent)" stroke="var(--color-accent)" stroke-width="3"/>
  {fo2(ZX0, GY0, ZX1 - ZX0, GY1 - GY0, "VAE", "latent", 'data-anim="gc0" ' + HIDE)}
  {fo(ZX0, GY0, ZX1 - ZX0, GY1 - GY0, "fo fo-box", "$z_t$", 'data-anim="gc1" ', "color:#fff")}
  <g data-anim="same">
    <path d="M{(ZX0 + ZX1) // 2} {ZY1 + 6}V{GY0 - 6}" stroke="var(--color-accent)" stroke-width="3" stroke-dasharray="10 8"/>
    <circle cx="{(ZX0 + ZX1) // 2}" cy="{ZY1 + 6}" r="5" fill="var(--color-accent)"/><circle cx="{(ZX0 + ZX1) // 2}" cy="{GY0 - 6}" r="5" fill="var(--color-accent)"/>
    {fo((ZX0 + ZX1) // 2 - 230, 250, 216, 40, "fo fo-r", "같은 공간", style=BOLD)}
  </g>
  {arrow(ZX1 + 4, GM, VX0 - 4)}

  <!-- the generation stream: an expert at every layer (baseline) or 8 blocks (Block-wise MoT) -->
  <rect data-anim="gbar" x="{VX0}" y="{GY0}" width="{VX1 - VX0}" height="{GY1 - GY0}" rx="10" fill="var(--color-surface-brand)" stroke="var(--color-accent)" stroke-width="3"/>
  {fo(VX0, GY0, VX1 - VX0, GY1 - GY0, "fo fo-box", "생성 expert · 층마다", 'data-anim="gn0" ' + HIDE)}
  {fo(VX0, GY0, VX1 - VX0, GY1 - GY0, "fo fo-box", "Block-wise MoT · 8블록", 'data-anim="gn1" ')}

  <!-- decoder: the VAE's own (baseline) or a pixel decoder from z -->
  {arrow(VX1 + 4, GM, 1436)}
  <rect data-anim="dec" x="1440" y="{GY0}" width="184" height="{GY1 - GY0}" rx="10" fill="var(--color-surface-brand)" stroke="var(--color-accent)" stroke-width="3"/>
  {fo2(1440, GY0, 184, GY1 - GY0, "VAE", "decoder", 'data-anim="dn0" ' + HIDE)}
  {fo2(1440, GY0, 184, GY1 - GY0, "pixel", "decoder", 'data-anim="dn1" ')}

  <!-- question ②: under the generation path -->
  <g data-anim="q2">
    <path d="M{VX0} {GY1 + 8}V{GY1 + 22}H1624V{GY1 + 8}" fill="none" stroke="var(--color-warm)" stroke-width="4"/>
    {fo(VX0, GY1 + 30, 1624 - VX0, 44, "fo fo-c fo-h", Q2)}
  </g>
</g>
</svg>
'''
open(out, "w", encoding="utf-8", newline="\n").write(svg)
print(f"LW={LW:.2f} strips={STRIPS}")
