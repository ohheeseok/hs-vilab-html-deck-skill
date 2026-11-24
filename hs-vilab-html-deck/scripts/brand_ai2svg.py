"""Convert an outlined Illustrator (PDF-compatible) logo to a tight, clean SVG.

usage: python ai2svg.py in.ai out.svg [--mono #RRGGBB]
Fills only; no strokes, shading or images are expected (checked).
"""
import sys
import pymupdf


def hexc(c):
    return "#%02X%02X%02X" % tuple(round(v * 255) for v in c)


def f(v):
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def main():
    src, out = sys.argv[1], sys.argv[2]
    mono = sys.argv[sys.argv.index("--mono") + 1] if "--mono" in sys.argv else None
    page = pymupdf.open(src)[0]
    assert not page.get_images(), "raster image inside the logo"
    draws = page.get_drawings()
    box = None
    for d in draws:
        assert d["type"] == "f" and d.get("fill") and d.get("fill_opacity", 1) == 1, d["type"]
        box = d["rect"] if box is None else box | d["rect"]
    ox, oy = box.x0, box.y0
    paths = []
    for d in draws:
        parts, cur = [], None
        for it in d["items"]:
            k = it[0]
            if k == "re":
                r = it[1]
                parts.append(f"M{f(r.x0-ox)} {f(r.y0-oy)}H{f(r.x1-ox)}V{f(r.y1-oy)}H{f(r.x0-ox)}Z")
                cur = None
                continue
            if k == "qu":
                q = it[1]
                pts = [q.ul, q.ur, q.lr, q.ll]
                parts.append("M" + "L".join(f"{f(p.x-ox)} {f(p.y-oy)}" for p in pts) + "Z")
                cur = None
                continue
            p0 = it[1]
            if cur is None or abs(cur.x - p0.x) > 1e-3 or abs(cur.y - p0.y) > 1e-3:
                parts.append(f"M{f(p0.x-ox)} {f(p0.y-oy)}")
            if k == "l":
                p1 = it[2]
                parts.append(f"L{f(p1.x-ox)} {f(p1.y-oy)}")
                cur = p1
            elif k == "c":
                a, b, p1 = it[2], it[3], it[4]
                parts.append(f"C{f(a.x-ox)} {f(a.y-oy)} {f(b.x-ox)} {f(b.y-oy)} {f(p1.x-ox)} {f(p1.y-oy)}")
                cur = p1
            else:
                raise SystemExit(f"unhandled path item {k}")
        if d.get("closePath"):
            parts.append("Z")
        rule = ' fill-rule="evenodd"' if d.get("even_odd") else ""
        paths.append((mono or hexc(d["fill"]), "".join(parts), rule))
    w, h = box.width, box.height
    body = "\n".join(f'<path fill="{c}"{r} d="{dd}"/>' for c, dd, r in paths)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" '
           f'width="{f(w)}" height="{f(h)}" role="img" aria-label="Hansung University">\n'
           f'<title>Hansung University</title>\n{body}\n</svg>\n')
    open(out, "w", encoding="utf-8").write(svg)
    print(out, f"{w:.2f}x{h:.2f}", f"ratio {w/h:.4f}", len(paths), "paths",
          sorted({c for c, _, _ in paths}))


main()
