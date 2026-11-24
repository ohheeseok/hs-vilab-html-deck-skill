"""Environment gate for hs-vilab-html-deck. Blocking: do not build past a FAIL.

Usage:
    python preflight.py            # report
    python preflight.py --strict   # exit 1 on any FAIL

Checks what a build, QA and PDF export actually need, by doing it rather than by guessing:
Python, PyMuPDF, Pillow, Playwright + a Chromium that launches, LaTeX + dvisvgm (math is rendered
through TeX, no fallback), the bundled fonts, and the delegate CLIs (codex, agy) — those are
optional: a missing one means that role runs as a subagent, said in the delivery.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
VERSION = (SKILL / "VERSION").read_text(encoding="utf-8").strip() if (SKILL / "VERSION").exists() else "?"
fails = 0


def line(state: str, name: str, detail: str = "") -> None:
    global fails
    if state == "FAIL":
        fails += 1
    print(f"  [{state:4s}] {name:22s} {detail}")


def main() -> int:
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass
    print(f"hs-vilab-html-deck {VERSION} — preflight")
    v = sys.version_info
    line("ok" if v >= (3, 10) else "FAIL", "Python", f"{v.major}.{v.minor}" + ("" if v >= (3, 10) else "  (need 3.10+)"))
    for mod, pip in (("pymupdf", "pymupdf"), ("PIL", "pillow"), ("numpy", "numpy")):
        try:
            __import__(mod)
            line("ok", mod)
        except ImportError:
            line("FAIL", mod, f"pip install {pip}")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch()
            ver = b.version
            b.close()
        line("ok", "Playwright Chromium", ver)
    except Exception as e:  # noqa: BLE001
        line("FAIL", "Playwright Chromium", f"pip install playwright && python -m playwright install chromium ({e.__class__.__name__})")
    for cmd in ("latex", "dvisvgm"):
        path = shutil.which(cmd)
        line("ok" if path else "FAIL", cmd, path or "install MiKTeX or TeX Live (math has no other render path)")
    if shutil.which("latex"):
        r = subprocess.run(["kpsewhich", "arev.sty"], capture_output=True, text=True)
        line("ok" if r.stdout.strip() else "FAIL", "arev.sty (math font)", r.stdout.strip() or "tlmgr install arev / MiKTeX: arev")
    fonts = SKILL / "assets" / "fonts"
    need = ["Geomini-Variable.woff2", "GmarketSans-Light.woff2", "GmarketSans-Medium.woff2", "GmarketSans-Bold.woff2"]
    miss = [f for f in need if not (fonts / f).exists()]
    line("FAIL" if miss else "ok", "bundled fonts", ", ".join(miss) if miss else "4 files")
    for cmd, role in (("codex", "draft · revision · Korean edit"), ("agy", "critique · verification · research · visual")):
        path = shutil.which(cmd) or shutil.which(cmd + ".cmd")
        line("ok" if path else "warn", cmd, f"{role}" + ("" if path else " — missing: that role runs as a subagent"))
    print("FAIL: fix before building." if fails else "ready.")
    return 1 if fails and "--strict" in sys.argv else 0


if __name__ == "__main__":
    sys.exit(main())
