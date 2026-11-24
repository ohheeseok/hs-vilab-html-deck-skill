"""deck/index.html -> deck.pdf, one 1920x1080 page per slide, vector text.

Usage:
    python export_pdf.py <work_dir> [-o deck.pdf]

A toggle with "print": "expand" gets one page per state (pages 6a, 6b, ...), so every state a
conclusion depends on is in the handout; "print": "default" prints only its start state.
A stepper prints fully revealed. Chromium prints through the deck's own @media print rules;
this script shows one slide at a time and merges the pages with PyMuPDF.

Needs: playwright (+ chromium), pymupdf.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import pymupdf
from playwright.sync_api import sync_playwright

ONLY_CURRENT = "@media print{.slide:not(.is-current){display:none !important}}"


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
              return {{steps: +(s.getAttribute('data-steps') || 0),
                       expand: t ? t.getAttribute('data-print') === 'expand' : false,
                       start: t ? t.getAttribute('data-start') : null}};
            }}""")
            states = page.evaluate(f"window.__deck.states({i})") or [None]
            if not info["expand"]:
                states = [info["start"]] if info["start"] else [None]
            if info["steps"]:
                page.evaluate(f"location.hash = '#/{i + 1}/{info['steps']}'")
            for k, st in enumerate(states):
                if st:
                    page.evaluate(f"window.__deck.setState({i}, {json.dumps(st)})")
                page.wait_for_timeout(150)
                f = Path(tmp) / f"{i:03d}-{k}.pdf"
                page.pdf(path=str(f), width="1920px", height="1080px", print_background=True,
                         margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
                with pymupdf.open(f) as one:
                    merged.insert_pdf(one, from_page=0, to_page=0)
                labels.append(f"{i + 1}{chr(97 + k) if len(states) > 1 else ''}")
        b.close()
    merged.set_metadata({"title": page_title(index), "creator": "hs-vilab-html-deck"})
    merged.save(out)
    print(f"wrote {out} — {len(labels)} pages ({', '.join(labels)})")
    return 0


def page_title(index: Path) -> str:
    import re
    m = re.search(r"<title>(.*?)</title>", index.read_text(encoding="utf-8"))
    return m.group(1) if m else ""


if __name__ == "__main__":
    sys.exit(main())
