#!/usr/bin/env python3
"""
extract_figures.py — pull figures out of a paper PDF at presentation quality.

Two modes, and the difference matters:

  list     what is on each page, so the narrative can decide what to use
  crop     render a page region to PNG at high DPI

A paper's figure is usually vector art. Lifting the embedded raster
(pdfimages-style) gets you the photograph inside a plot and loses the
axes; rendering the REGION at high DPI keeps axes, ticks, legend and
caption together, which is what a slide needs. So this crops and renders
rather than extracting image XObjects.

    python3 extract_figures.py paper.pdf list
    python3 extract_figures.py paper.pdf list --page 3
    python3 extract_figures.py paper.pdf crop --page 3 --bbox 55,90,540,360 \\
            --name fig1 -o work/<slug>/assets

Coordinates are PDF points from the TOP-LEFT of the page, which is what
`list` prints, so a bbox can be copied straight from it.

Every crop is recorded in <out>/index.json in the shape deck.json's
`assets.sizes` expects — placement needs the pixel size before it can
decide the rectangle.

Tables are deliberately NOT extracted. A table goes into the deck as a
native, editable table (the `table` block), not as a picture of one:
a screenshot cannot be corrected, restyled, or read by a screen reader,
and its type does not scale with the slide.
"""
import argparse, json, re, sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit("extract_figures: needs PyMuPDF.  pip install pymupdf")


def load_index(outdir):
    p = Path(outdir) / "index.json"
    if p.exists():
        try: return json.loads(p.read_text(encoding="utf-8"))
        except Exception: pass                       # noqa: BLE001
    return {"sizes": {}, "eq": {}}


def save_index(outdir, idx):
    p = Path(outdir) / "index.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(idx, indent=2), encoding="utf-8")
    return p


def raster_panels(page, gap=8.0):
    """Union the placed rasters that touch into panels, largest first."""
    rects = [pymupdf.Rect(i["bbox"]) for i in page.get_image_info()]
    rects = [r for r in rects if r.width > 4 and r.height > 4]
    groups = []
    for r in rects:
        grown = pymupdf.Rect(r.x0 - gap, r.y0 - gap, r.x1 + gap, r.y1 + gap)
        hit = [g for g in groups if g["rect"].intersects(grown)]
        merged = pymupdf.Rect(r)
        n = 1
        for g in hit:
            merged |= g["rect"]; n += g["n"]; groups.remove(g)
        groups.append({"rect": merged, "n": n})
    # one more pass: unions can now touch each other
    changed = True
    while changed:
        changed = False
        for a in groups:
            for b in groups:
                if a is not b and pymupdf.Rect(a["rect"].x0 - gap, a["rect"].y0 - gap,
                        a["rect"].x1 + gap, a["rect"].y1 + gap).intersects(b["rect"]):
                    a["rect"] |= b["rect"]; a["n"] += b["n"]; groups.remove(b)
                    changed = True; break
            if changed: break
    out = []
    for g in sorted(groups, key=lambda g: -g["rect"].get_area()):
        r = g["rect"]; r.n = g["n"]; out.append(r)
    return out


def cmd_list(a):
    doc = pymupdf.open(a.pdf)
    pages = [a.page - 1] if a.page else range(len(doc))
    for pno in pages:
        page = doc[pno]
        r = page.rect
        print(f"\n--- page {pno+1}  ({r.width:.0f} x {r.height:.0f} pt) ---")

        # Caption lines are the reliable anchor for "there is a figure here".
        text = page.get_text("dict")
        for blk in text.get("blocks", []):
            if blk.get("type") != 0: continue
            line = " ".join(sp["text"] for ln in blk.get("lines", [])
                            for sp in ln.get("spans", [])).strip()
            if is_caption(line):
                x0, y0, x1, y1 = blk["bbox"]
                print(f"  caption  bbox={x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f}  "
                      f"{line[:88]}")

        drawings = page.get_drawings()
        if drawings:
            xs = [d["rect"] for d in drawings]
            x0 = min(r.x0 for r in xs); y0 = min(r.y0 for r in xs)
            x1 = max(r.x1 for r in xs); y1 = max(r.y1 for r in xs)
            print(f"  vector   {len(drawings)} paths, extent "
                  f"{x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f}")
        for i, img in enumerate(page.get_images(full=True)):
            try:
                bb = page.get_image_bbox(img)
                print(f"  raster   #{i} bbox={bb.x0:.0f},{bb.y0:.0f},"
                      f"{bb.x1:.0f},{bb.y1:.0f}  {img[2]}x{img[3]}px")
            except Exception:                        # noqa: BLE001
                print(f"  raster   #{i} {img[2]}x{img[3]}px (no placement)")
        # [0.7.0] A grid of 15 generated images lists as 15 rasters, and the
        # extent of the grid — the bbox you actually want — is not on any
        # line. Rasters that touch (gap < 8pt) are merged into panels.
        for k, g in enumerate(raster_panels(page)):
            print(f"  panel    P{k} bbox={g.x0:.0f},{g.y0:.0f},{g.x1:.0f},{g.y1:.0f}"
                  f"  ({g.n} raster{'s' if g.n > 1 else ''})")
    doc.close()
    print("\nPick a bbox and crop it:\n"
          "  extract_figures.py <pdf> crop --page N --bbox x0,y0,x1,y1 "
          "--name figN -o <assets>\n"
          "Leave the caption OUT of the crop — the slide writes its own, and "
          "the source\nline at the floor carries the figure number.")
    return 0


# A multi-panel figure carries sub-captions — "(a) FDS yields improved …" —
# and those are captions too. Matching only the Figure/Table prefix let a
# sub-caption straight into a crop, which is how the first FDS pass caught
# "(a)", "(b)" and "(c)" inside one image.
CAPTION_RE = re.compile(
    # A NUMBER must follow the keyword. Without it, body text that merely
    # begins with the word — "algorithm (UniGRPO) tailored for…" on MMaDA's
    # page 3 — read as a caption and could clip a crop short.
    r"^(?:figure|fig\.?|table|algorithm|theorem|lemma|proposition)\s*[A-Z]?\d+"
    r"|^\(?[a-h]\)\s+\S",          # (a) …  or  a) …  — a sub-panel caption
    re.IGNORECASE)


def is_caption(line):
    return bool(CAPTION_RE.match(line.strip()))


def caption_top_below(page, y_bottom):
    """The y of the nearest caption block starting below y_bottom.

    Padding a crop downward pulls the paper's own caption into the image —
    usually just its top few pixels, which reads as a smear of cut letters
    under the figure. It happened on two of four figures in the first real
    deck, and neither the build gate nor the layout scan can see it: it is
    ink inside an image.

    The slide writes its own caption and the source line carries the figure
    number, so the paper's caption is never wanted in the crop."""
    best = None
    for blk in page.get_text("dict").get("blocks", []):
        if blk.get("type") != 0: continue
        line = " ".join(sp["text"] for ln in blk.get("lines", [])
                        for sp in ln.get("spans", [])).strip()
        if not is_caption(line):
            continue
        top = blk["bbox"][1]
        if top >= y_bottom - 1 and (best is None or top < best):
            best = top
    return best


def cmd_crop(a):
    doc = pymupdf.open(a.pdf)
    page = doc[a.page - 1]
    x0, y0, x1, y1 = [float(v) for v in a.bbox.split(",")]
    pad = a.pad
    bottom = y1 + pad
    cap = caption_top_below(page, y1)
    if cap is not None and bottom > cap - 1:
        bottom = cap - 1.5
        print(f"  clipped bottom to {bottom:.0f}pt — the paper's own caption "
              f"starts at {cap:.0f}pt")
    # [0.7.0] The pad must not reach a neighbouring panel. Janus's Figure 1
    # puts (a) and (b) side by side ~17pt apart and Figure 4 its two image
    # pairs ~7pt apart; a flat 4pt pad on a tight bbox let a sliver of the
    # next panel into the crop. Each side's pad stops halfway to the nearest
    # raster that lies outside the box and faces that side.
    pads = {"l": pad, "t": pad, "r": pad}
    for info in page.get_image_info():
        r = pymupdf.Rect(info["bbox"])
        if r.intersects(pymupdf.Rect(x0, y0, x1, y1)):
            continue
        overlaps_v = r.y0 < y1 and r.y1 > y0
        overlaps_h = r.x0 < x1 and r.x1 > x0
        if overlaps_v and r.x1 <= x0:
            pads["l"] = min(pads["l"], max(0.0, (x0 - r.x1) / 2))
        if overlaps_v and r.x0 >= x1:
            pads["r"] = min(pads["r"], max(0.0, (r.x0 - x1) / 2))
        if overlaps_h and r.y1 <= y0:
            pads["t"] = min(pads["t"], max(0.0, (y0 - r.y1) / 2))
        if overlaps_h and r.y0 >= y1:
            bottom = min(bottom, y1 + max(0.0, (r.y0 - y1) / 2))
    rect = pymupdf.Rect(x0 - pads["l"], y0 - pads["t"], x1 + pads["r"], bottom) & page.rect

    # High DPI, because a figure that is sharp at 100% in QA is soft on a
    # projector. 300 is the floor for anything with a tick label in it.
    pix = page.get_pixmap(clip=rect, dpi=a.dpi, alpha=False)
    out = Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
    name = f"{a.name}.png"
    pix.save(out / name)

    idx = load_index(out)
    idx["sizes"][name] = [pix.width, pix.height]
    save_index(out, idx)

    ar = pix.width / pix.height
    print(f"wrote {out / name}  {pix.width}x{pix.height}px  aspect {ar:.2f}:1")
    print(f"  recorded in {out / 'index.json'}")
    if ar < 1.3:
        print(f"  ! aspect {ar:.2f}:1 is tall. In a wide body region this will "
              f"be\n    height-limited, and every label inside it shrinks by "
              f"that factor.\n    Put a figure this shape in one column of a "
              f"`split` (text beside it), or use figureNumbered.")
    doc.close()
    return 0


def cmd_text(a):
    """[0.7.2] The paper's text, page by page — what brief.md carries inline
    and every reviewer reads. Tables come out as broken lines; check numbers
    against the rendered page, not this file."""
    doc = pymupdf.open(a.pdf)
    parts = [f"\n=== PAGE {i} ===\n{p.get_text()}" for i, p in enumerate(doc, 1)]
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(parts), encoding="utf-8")
    print(f"wrote {out} — {len(doc)} pages, {sum(len(x) for x in parts):,} characters")
    doc.close()
    return 0


def main():
    for st in (sys.stdout, sys.stderr):
        try: st.reconfigure(encoding="utf-8")   # Windows consoles default to cp949
        except Exception: pass                    # noqa: BLE001
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    sub = ap.add_subparsers(dest="cmd", required=True)

    l = sub.add_parser("list", help="what is on each page")
    l.add_argument("--page", type=int)

    c = sub.add_parser("crop", help="render a page region to PNG")
    c.add_argument("--page", type=int, required=True)
    c.add_argument("--bbox", required=True, help="x0,y0,x1,y1 in PDF points")
    c.add_argument("--name", required=True)
    c.add_argument("-o", "--outdir", required=True)
    c.add_argument("--dpi", type=int, default=300)
    c.add_argument("--pad", type=float, default=4.0,
                   help="points of breathing room, so nothing is shaved")

    t = sub.add_parser("text", help="the paper's text, page by page, to a file")
    t.add_argument("-o", "--out", required=True)

    a = ap.parse_args()
    if not Path(a.pdf).exists(): sys.exit(f"extract_figures: no such file: {a.pdf}")
    return {"list": cmd_list, "crop": cmd_crop, "text": cmd_text}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
