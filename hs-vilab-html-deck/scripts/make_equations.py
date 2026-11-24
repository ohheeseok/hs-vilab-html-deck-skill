"""LaTeX -> inline-ready SVG for hs-vilab-html-deck.

Math is set in Arev Sans (package arev): a sans math face whose weight matches
Geomini 500 / GmarketSans Medium on the stage; Computer Modern looked hairline beside it.

One render path for all math in a deck: display equations, inline `$...$` in slide
text, and math inside hand-drawn diagrams all come from TeX through dvisvgm, so a
symbol looks the same everywhere it appears. No KaTeX, no web fonts for math.

Library use (build_deck.py):
    from make_equations import render
    m = render(r"\\mathcal{L}_{\\mathrm{gen}}", cache_dir)   # -> Math(svg, w, h, d) in em

CLI (pre-render a named set, e.g. to inspect them):
    python make_equations.py equations.json out_dir

Each SVG:
  * glyphs as paths (dvisvgm --no-fonts), so nothing is needed at show time;
  * the default (black) foreground becomes currentColor, so it takes the colour of
    the text around it; any other explicit colour is kept;
  * ids are prefixed per equation (references updated), so two inlined copies never
    collide;
  * the box is TeX's own box (width, height + depth), sized in em with 10pt TeX = 1em,
    and the depth is returned so inline math sits on the text baseline.

Needs latex and dvisvgm on PATH (MiKTeX or TeX Live). preflight.py checks this.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

TEMPLATE = r"""\documentclass[10pt,border=0pt]{standalone}
\usepackage{amsmath,amssymb,bm}
\usepackage{arev}
\begin{document}
\sbox0{$%(style)s %(tex)s$}%%
\typeout{HDW:\the\ht0:\the\dp0:\the\wd0}%%
\usebox0
\end{document}
"""

BLACK = re.compile(r"""(fill|stroke)\s*=\s*(['"])(#000|#000000|black)\2""", re.I)
ID_ATTR = re.compile(r"""\bid\s*=\s*(['"])([^'"]+)\1""")
HREF = re.compile(r"""((?:xlink:)?href\s*=\s*(['"]))#([^'"]+)\2""")
URL_REF = re.compile(r"""url\(#([^)]+)\)""")
VERSION = "3"  # bump to invalidate caches when the output format changes


@dataclass
class Math:
    svg: str      # <svg ...> with width/height in em, fill=currentColor
    w: float      # em
    h: float      # em, height above baseline
    d: float      # em, depth below baseline


def _run(cmd: list[str], cwd: Path) -> str:
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"{cmd[0]} failed:\n{r.stdout[-2500:]}\n{r.stderr[-2500:]}")
    return r.stdout


def _pt(s: str) -> float:
    return float(s.replace("pt", ""))


def render(tex: str, cache_dir: Path, display: bool = False) -> Math:
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(f"{VERSION}|{display}|{tex}".encode("utf-8")).hexdigest()[:12]
    eid = f"m{key}"
    cj = cache_dir / f"{eid}.json"
    if cj.exists():
        meta = json.loads(cj.read_text(encoding="utf-8"))
        return Math((cache_dir / f"{eid}.svg").read_text(encoding="utf-8"), meta["w"], meta["h"], meta["d"])

    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        style = r"\displaystyle" if display else r"\textstyle"
        (tdp / "eq.tex").write_text(TEMPLATE % {"style": style, "tex": tex}, encoding="utf-8")
        log = _run(["latex", "-interaction=nonstopmode", "-halt-on-error", "eq.tex"], tdp)
        m = re.search(r"HDW:([\d.]+pt):([\d.]+pt):([\d.]+pt)", log + (tdp / "eq.log").read_text(errors="replace"))
        if not m:
            raise RuntimeError(f"could not read box size for {tex!r}")
        ht, dp, wd = (_pt(x) for x in m.groups())
        _run(["dvisvgm", "--no-fonts", "--bbox=papersize", "--zoom=1", "eq.dvi", "-o", "eq.svg"], tdp)
        svg = (tdp / "eq.svg").read_text(encoding="utf-8")

    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    svg = re.sub(r"<!--.*?-->\s*", "", svg, flags=re.S)
    svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg)
    ids = set(x.group(2) for x in ID_ATTR.finditer(svg))
    svg = ID_ATTR.sub(lambda x: f"id={x.group(1)}{eid}-{x.group(2)}{x.group(1)}", svg)
    svg = HREF.sub(lambda x: f"{x.group(1)}#{eid}-{x.group(3)}{x.group(2)}" if x.group(3) in ids else x.group(0), svg)
    svg = URL_REF.sub(lambda x: f"url(#{eid}-{x.group(1)})" if x.group(1) in ids else x.group(0), svg)
    svg = BLACK.sub(lambda x: f"{x.group(1)}={x.group(2)}currentColor{x.group(2)}", svg)

    w, h, d = wd / 10.0, ht / 10.0, dp / 10.0
    head = re.search(r"<svg\b[^>]*>", svg).group(0)
    new = re.sub(r"""\s(width|height)\s*=\s*['"][^'"]+['"]""", "", head)
    new = new.replace("<svg", f'<svg width="{w:.4f}em" height="{h + d:.4f}em" fill="currentColor" '
                              f'aria-hidden="true" focusable="false" style="overflow:visible"', 1)
    svg = svg.replace(head, new, 1).strip()
    svg = re.sub(r">\s+<", "><", svg)
    (cache_dir / f"{eid}.svg").write_text(svg, encoding="utf-8")
    cj.write_text(json.dumps({"tex": tex, "w": w, "h": h, "d": d}), encoding="utf-8")
    return Math(svg, w, h, d)


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    for tool in ("latex", "dvisvgm"):
        if not shutil.which(tool):
            print(f"error: {tool} not found on PATH. Install MiKTeX or TeX Live.", file=sys.stderr)
            return 1
    eqs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path(sys.argv[2])
    for name, tex in eqs.items():
        m = render(tex, out, display=True)
        print(f"{name}: {m.w:.2f}em x {m.h + m.d:.2f}em (depth {m.d:.2f}em)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
