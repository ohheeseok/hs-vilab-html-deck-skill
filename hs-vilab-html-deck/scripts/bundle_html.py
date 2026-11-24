"""deck/index.html (+ assets/) -> one self-contained HTML file: the deliverable.

Usage:
    python bundle_html.py <work_dir>            # -> <work_dir>/<slug>.html, <work_dir>/<slug>-script.html

Every stylesheet, the engine script, the fonts (woff2), the figures and the brand marks are inlined
as text or data: URIs, so the file opens from anywhere — a mail attachment, a USB stick, a
projector PC — with no folder next to it and no network. build_deck.py calls this after it writes
deck/; QA runs on the bundled file too (`qa_render.py <work_dir> --html <file>`).
"""
from __future__ import annotations

import base64
import io
import json
import mimetypes
import re
import sys
from pathlib import Path

MIME = {".woff2": "font/woff2", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg", ".webp": "image/webp", ".gif": "image/gif"}


MAX_SIDE = 2400        # 400-dpi crops are larger than a 1920 stage ever shows them
BIG = 250_000          # re-encode raster figures above this size


def data_uri(path: Path) -> str:
    mime = MIME.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    raw = path.read_bytes()
    if path.suffix.lower() in (".svg", ".css"):
        raw = raw.replace(b"\r\n", b"\n")   # same bytes whichever line endings git checked out
    if path.suffix.lower() in (".png", ".jpg", ".jpeg") and len(raw) > BIG:
        # one file carries every figure: WebP at high quality keeps axis text sharp at a fraction of the size
        from PIL import Image
        im = Image.open(io.BytesIO(raw))
        im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
        if max(im.size) > MAX_SIDE:
            im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=90, method=6)
        if buf.tell() < len(raw):
            raw, mime = buf.getvalue(), "image/webp"
    return f"data:{mime};base64," + base64.b64encode(raw).decode("ascii")


def inline_css(css: str, base: Path) -> str:
    def url(m):
        ref = m.group(2)
        if ref.startswith(("data:", "http:", "https:", "#")):
            return m.group(0)
        return f'url("{data_uri((base / ref).resolve())}")'
    return re.sub(r"""url\((['"]?)([^'")]+)\1\)""", url, css)


def bundle(page: Path) -> str:
    root = page.parent
    s = page.read_text(encoding="utf-8")

    def link(m):
        css_path = (root / m.group(1)).resolve()
        return "<style>\n" + inline_css(css_path.read_text(encoding="utf-8"), css_path.parent) + "\n</style>"
    s = re.sub(r'<link rel="stylesheet" href="([^"]+)">', link, s)

    scripts = []

    def script(m):
        scripts.append((root / m.group(1)).read_text(encoding="utf-8"))
        return ""
    s = re.sub(r'<script src="([^"]+)"(?: defer)?></script>', script, s)
    if scripts:  # defer: run after the document is parsed
        body = "".join(f"<script>\n{x}\n</script>\n" for x in scripts)
        s = s.replace("</body>", body + "</body>", 1)

    def img(m):
        ref = m.group(2)
        if ref.startswith(("data:", "http:", "https:")):
            return m.group(0)
        return f'{m.group(1)}"{data_uri((root / ref).resolve())}"'
    s = re.sub(r'(<img[^>]*?\bsrc=)"([^"]+)"', img, s)
    s = re.sub(r'(<image[^>]*?\b(?:xlink:)?href=)"([^"]+)"', img, s)   # rasters inside inline SVG diagrams
    left = re.findall(r'(?:src|href)="(assets/[^"]+)"', s)
    if left:
        raise SystemExit(f"bundle: references left unresolved: {left[:5]}")
    return s


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    work = Path(sys.argv[1]).resolve()
    slug = json.loads((work / "deck.json").read_text(encoding="utf-8"))["meta"].get("slug") or work.name
    outs = []
    for src, name in (("index.html", f"{slug}.html"), ("script.html", f"{slug}-script.html")):
        page = work / "deck" / src
        if page.exists():
            out = work / name
            out.write_text(bundle(page), encoding="utf-8", newline="\n")   # identical on every OS
            outs.append(f"{out.name} ({out.stat().st_size / 1e6:.1f} MB)")
    print("bundled " + ", ".join(outs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
