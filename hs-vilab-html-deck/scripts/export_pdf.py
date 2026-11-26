"""deck/index.html -> deck.pdf, one 1920x1080 page per slide, vector text.

Usage:
    python export_pdf.py <work_dir> [-o deck.pdf]

A toggle with "print": "expand" gets one page per state (pages 6a, 6b, ...), so every state a
conclusion depends on is in the handout; "print": "default" prints only its start state.
A stepper with "print": "expand" gets one page per step; with "default" it prints fully revealed. Chromium prints through the deck's own @media print rules;
this script shows one slide at a time and merges the pages with PyMuPDF.

Needs: playwright (+ chromium), pymupdf.
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

import pymupdf
from playwright.sync_api import sync_playwright

ONLY_CURRENT = "@media print{.slide:not(.is-current){display:none !important}}"

# Chromium's paginated print layout resolves percentage heights (an image fitted with max-height:100%
# inside a grid cell) differently from the screen, so a fitted figure grew and pushed its caption
# past the page. Freeze every image and svg at the size the screen gave it before printing.
FREEZE = """(i) => {
  const s = document.querySelectorAll('.slide')[i];
  const k = s.getBoundingClientRect().width / 1920;
  for (const el of s.querySelectorAll('img, svg.chart, .figure--diagram > svg, .toggle-media')) {
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) continue;
    el.style.width = (r.width / k) + 'px';
    el.style.height = (r.height / k) + 'px';
    el.style.maxWidth = 'none'; el.style.maxHeight = 'none'; el.style.flex = 'none';
  }
}"""


def overlaps(pdf: Path) -> list[str]:
    """Text lines from different blocks that overlap on a printed page (≥ 35% of the shorter line)."""
    bad = []
    with pymupdf.open(pdf) as d:
        for n, pg in enumerate(d, 1):
            lines = []
            for b in pg.get_text("dict")["blocks"]:
                for ln in b.get("lines", []):
                    t = "".join(sp["text"] for sp in ln["spans"]).strip()
                    if t:
                        lines.append((b["number"], pymupdf.Rect(ln["bbox"]), t))
            for a in range(len(lines)):
                for c in range(a + 1, len(lines)):
                    ba, ra, ta = lines[a]
                    bc, rc, tc = lines[c]
                    if ba == bc:
                        continue
                    # a text-shadow halo prints the same glyphs again at the same place (RAE run:
                    # the ladder's value labels) — a copy is not an overlap
                    if ta == tc and max(abs(ra.x0 - rc.x0), abs(ra.y0 - rc.y0)) < 1.5:
                        continue
                    x = ra & rc
                    if x.width > 2 and x.height > 0.35 * min(ra.height, rc.height):
                        bad.append(f"page {n}: '{ta[:24]}' overlaps '{tc[:24]}'")
                        break
            if pg.rect.width and any(r.y1 > pg.rect.height + 1 or r.x1 > pg.rect.width + 1 for _, r, _ in lines):
                bad.append(f"page {n}: text beyond the page edge")
            # the footer's progress bar is a row of thin rules near the bottom; a body line must not cross it
            rules = [dr["rect"] for dr in pg.get_drawings()
                     if dr["rect"].y0 > 0.85 * pg.rect.height and dr["rect"].height < 6 and dr["rect"].width > 20]
            if rules:
                bar = min(r.y0 for r in rules)
                for _, r, t in lines:
                    if r.y0 < bar < r.y1 - 1:
                        bad.append(f"page {n}: '{t[:24]}' runs into the footer")
                        break
    return bad


def main() -> int:
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    work = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[sys.argv.index("-o") + 1]) if "-o" in sys.argv else work / "deck.pdf"
    index = work / "deck" / "index.html"
    labels = []
    merged = pymupdf.open()
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": 1920, "height": 1080})
        page.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())
        page.goto(index.as_uri() + "?motion=0")
        page.evaluate("document.fonts.ready")
        page.add_style_tag(content=ONLY_CURRENT)
        n = page.evaluate("window.__deck.count")
        for i in range(n):
            page.evaluate(f"window.__deck.go({i})")
            info = page.evaluate(f"""() => {{
              const s = document.querySelectorAll('.slide')[{i}];
              const t = s.querySelector('[data-toggle]');
              const p = s.querySelector('[data-stepper]');
              return {{steps: +(s.getAttribute('data-steps') || 0),
                       expand: t ? t.getAttribute('data-print') === 'expand' : false,
                       stepExpand: p ? p.getAttribute('data-print') === 'expand' : false,
                       start: t ? t.getAttribute('data-start') : null}};
            }}""")
            states = page.evaluate(f"window.__deck.states({i})") or [None]
            if not info["expand"]:
                states = [info["start"]] if info["start"] else [None]
            # one page per view: a toggle state, or a stepper step. A stepper with print "expand"
            # gets every step — its last step need not show everything (REPA run: the last step
            # greys out the training path to show inference, and the fully revealed page did too)
            views = [("state", st) for st in states]
            if info["steps"]:
                ks = range(info["steps"] + 1) if info["stepExpand"] else [info["steps"]]
                views = [("step", k) for k in ks]
            for k, (kind, v) in enumerate(views):
                if kind == "step":
                    page.evaluate(f"location.hash = '#/{i + 1}/{v}'")
                elif v:
                    page.evaluate(f"window.__deck.setState({i}, {json.dumps(v)})")
                page.wait_for_timeout(150)
                page.evaluate(FREEZE, i)
                f = Path(tmp) / f"{i:03d}-{k}.pdf"
                page.pdf(path=str(f), width="1920px", height="1080px", print_background=True,
                         margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
                with pymupdf.open(f) as one:
                    merged.insert_pdf(one, from_page=0, to_page=0)
                labels.append(f"{i + 1}{chr(97 + k) if len(views) > 1 else ''}")
        b.close()
    merged.set_metadata({"title": page_title(index), "creator": "hs-vilab-html-deck"})
    merged.save(out)
    print(f"wrote {out} — {len(labels)} pages ({', '.join(labels)})")
    bad = overlaps(out)
    for x in bad:
        print("  " + x)
    print("PDF check: " + ("text overlaps or leaves the page — look before distributing" if bad else "no overlapping text"))
    return 1 if bad else 0


def page_title(index: Path) -> str:
    import re
    m = re.search(r"<title>(.*?)</title>", index.read_text(encoding="utf-8"))
    return m.group(1) if m else ""


if __name__ == "__main__":
    sys.exit(main())
