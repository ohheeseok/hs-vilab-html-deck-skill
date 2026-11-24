"""deck.json -> deck/index.html for hs-vilab-html-deck.

Usage:
    python build_deck.py <work_dir>

<work_dir> holds deck.json, figures/ (hand-authored SVG diagrams) and deck/assets/
(fig/ crops, eq/ equation SVGs from make_equations.py). The build copies the skill's
tokens, fonts, engine and brand files into deck/assets/ and writes deck/index.html.

Every gate failure is an error: the build prints all of them and writes nothing.
"""
from __future__ import annotations

import html
import json
import math
import re
import shutil
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
ASSETS = SKILL / "assets"

# --------------------------------------------------------------------------- markup

MATH_SCALE = 1.04          # Arev at 10pt = 1em, nudged to Geomini's x-height
_CTX: dict = {}            # set by main(): cache dir for rendered math


SPEAK = [(r"\\math(?:cal|rm|bf|it)\{([^}]*)\}", r"\1"), (r"\\min\b", "min"), (r"\\max\b", "max"),
         (r"\\gamma", "γ"), (r"\\tau", "τ"), (r"\\theta", "θ"), (r"\\cdot", "·"), (r"\\,", " "),
         (r"[_^]\{([^}]*)\}", r" \1"), (r"[_^]", " "), (r"[{}]", ""), (r"'", "′"), (r"\s+", " ")]


def speak(tex: str) -> str:
    r"""A readable label for a TeX string: \mathcal{L}_{\mathrm{gen}} -> 'L gen'."""
    s = tex
    for _ in range(3):
        for a, b in SPEAK:
            s = re.sub(a, b, s)
    return s.strip()


def math_html(tex: str, display: bool = False) -> str:
    from make_equations import render
    m = render(tex, _CTX["math_cache"], display=display)
    k = MATH_SCALE
    svg = re.sub(r'width="[\d.]+em" height="[\d.]+em"',
                 f'width="{m.w * k:.4f}em" height="{(m.h + m.d) * k:.4f}em"', m.svg, count=1)
    cls = "dm" if display else "im"
    style = "" if display else f' style="vertical-align:-{m.d * k:.4f}em"'
    return f'<span class="{cls}" role="img" aria-label="{html.escape(speak(tex), quote=True)}"{style}>{svg}</span>'


def _text(s: str) -> str:
    s = html.escape(s, quote=False)
    # keep hyphenated names (Self-Flow, SiT-XL/2, text-to-image) on one line
    s = re.sub(r"(?<![\w-])([A-Za-z0-9][\w.]*(?:-[\w.]+)+)", r'<span class="nw">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"_\{(.+?)\}", r"<sub>\1</sub>", s)
    return s


def md(s: str) -> str:
    """Escape, then a small inline syntax: **bold**, _{subscript}, $TeX math$ (\\$ = literal $)."""
    parts = re.split(r"(?<!\\)\$(.+?)(?<!\\)\$", str(s))
    out = []
    for k, part in enumerate(parts):
        out.append(math_html(part) if k % 2 else _text(part.replace("\\$", "$")))
    # keep "$s$ = 0.8" on one line
    return re.sub(r'(<span class="im"(?:(?!</span>).)*</svg></span>)( = [\d.]+)',
                  r'<span class="nw">\1\2</span>', "".join(out))


def plain(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", str(s))
    s = re.sub(r"\$(.+?)\$", r"\1", s)
    return re.sub(r"_\{(.+?)\}", r"\1", s)


def attr(s: str) -> str:
    return html.escape(plain(s), quote=True)


# --------------------------------------------------------------------------- gates

class Gate:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def __call__(self, ok: bool, msg: str) -> None:
        if not ok:
            self.errors.append(msg)


def check(deck: dict, work: Path, gate: Gate) -> None:
    meta, slides = deck["meta"], deck["slides"]
    sec_ids = {s["id"] for s in meta.get("sections", [])}
    n = len(slides)
    interactive, signature, paneled = [], [], []
    pr = meta.get("presenter") or {}
    gate(bool(pr.get("name")), "meta.presenter.name is missing (the cover names who presents)")
    p = meta.get("paper")
    if p:
        gate(bool(p.get("authors")), "meta.paper has no authors (drop meta.paper for your own work)")
    for i, sl in enumerate(slides, 1):
        where = f"slide {i} ({sl.get('id')})"
        gate(bool(sl.get("title")), f"{where}: no title")
        if sl.get("layout") != "cover":
            gate(bool(sl.get("message")), f"{where}: no message (one key sentence per slide)")
            gate(sl.get("section") in sec_ids, f"{where}: section {sl.get('section')!r} is not in meta.sections")
            gate(bool(sl.get("cite")), f"{where}: no cite")
        for b in walk(sl.get("body", [])):
            if b["type"] in ("toggle", "stepper"):
                interactive.append(i)
                if b.get("signature"):
                    signature.append(i)
                gate(bool(b.get("reveals")), f"{where}: {b['type']} has no 'reveals' (what does operating it show about the paper?)")
                gate(b.get("print") in ("default", "expand"), f"{where}: {b['type']} 'print' must be default|expand")
                ids = [s["id"] for s in b.get("states", [])]
                gate(len(ids) >= 2, f"{where}: toggle needs at least two states")
                gate(b.get("start") in ids, f"{where}: toggle 'start' {b.get('start')!r} is not one of its states")
                for st in b.get("states", []):
                    gate(bool(st.get("provenance")), f"{where}: state {st.get('id')!r} has no provenance")
                gate((work / b.get("svg", "")).is_file(), f"{where}: diagram {b.get('svg')!r} not found")
            if b["type"] in ("bars", "table", "deltas"):
                gate(bool(b.get("provenance")), f"{where}: {b['type']} has no provenance")
            if b["type"] == "figure":
                gate((work / "deck" / b["src"]).is_file(), f"{where}: figure {b['src']!r} not found")
        if sl.get("figure"):
            gate((work / "deck" / sl["figure"]["src"]).is_file(), f"cover figure {sl['figure']['src']!r} not found")
        # zones: a panel is a region, not a card kit
        panels = [b for b in walk(sl.get("body", [])) if b["type"] == "panel"]
        panels += [b for b in walk(sl.get("body", [])) if b["type"] == "toggle" and b.get("panel")]
        gate(len(panels) <= 2, f"{where}: {len(panels)} panels; at most 2 per slide")
        for pb in panels:
            gate(not any(x["type"] == "panel" for x in walk(pb.get("body", []))), f"{where}: panel inside a panel")
        gate(not (panels and is_dark(deck, sl)), f"{where}: no panels on a dark slide (use a divider)")
        if panels:
            paneled.append(i)
        # a delta's pair must name things drawn on the same slide
        keys = set()
        for b in walk(sl.get("body", [])):
            if b["type"] == "bars":
                keys |= {it["label"] for it in b["items"]}
            if b["type"] == "table":
                keys |= {plain(r["cells"][0]) for g in b["groups"] for r in g["rows"]}
        for b in walk(sl.get("body", [])):
            if b["type"] == "deltas":
                for it in b["items"]:
                    for k in it.get("pair", []):
                        gate(k in keys, f"{where}: delta {it['value']} pairs {k!r}, which no chart or table on the slide draws")
    gate(len(signature) <= 1, f"more than one signature interaction (slides {signature})")
    gate(len(paneled) <= math.floor(n * 0.6), f"panels on {len(paneled)} of {n} slides; keep at least 40% panel-free")
    cap = math.floor(n * 0.2)
    gate(len(set(interactive)) <= cap,
         f"{len(set(interactive))} interactive slides; the cap for {n} slides is {cap} (⌊N×0.2⌋)")
    # figure ledger
    ledger = meta.get("figures")
    gate(bool(ledger), "meta.figures (figure ledger) is missing")
    for e in ledger or []:
        ref = e.get("ref")
        gate(("use" in e) != ("cut" in e), f"ledger {ref}: give exactly one of use / cut")
        if "use" in e:
            k = e["use"]
            ok = 1 <= k <= n and ref in slides[k - 1].get("cite", [])
            gate(ok, f"ledger {ref}: slide {k} does not cite it")


def is_dark(deck, sl) -> bool:
    return sl.get("layout") == "statement" and deck["meta"].get("statementTheme", "dark") == "dark"


def walk(blocks):
    for b in blocks:
        yield b
        if b.get("type") == "split":
            yield from walk(b.get("left", []))
            yield from walk(b.get("right", []))
        if b.get("type") == "panel":
            yield from walk(b.get("body", []))


# --------------------------------------------------------------------------- blocks

def r_lead(b, ctx):
    cls = "lead lead--sm" if b.get("size") == "sm" else "lead"
    return f'<p class="{cls}">{md(b["text"])}</p>'


def r_items(items, numbered=False, size=None):
    cls = "items" + (" items--numbered" if numbered else "") + (" items--sm" if size == "sm" else "")
    out = []
    for it in items:
        if isinstance(it, dict):
            label = '<span class="note-label">해석</span>' if it.get("note") else ""
            out.append(f"<li>{label}{md(it['text'])}</li>")
        else:
            out.append(f"<li>{md(it)}</li>")
    tag = "ol" if numbered else "ul"
    return f'<{tag} class="{cls}">' + "".join(out) + f"</{tag}>"


def r_groups(b, ctx):
    cols = b.get("columns", 1)
    parts = []
    for g in b["groups"]:
        parts.append(
            '<section class="group">'
            + (f'<h3>{md(g["heading"])}</h3>' if g.get("heading") else "")
            + r_items(g["items"], g.get("numbered", False), b.get("size"))
            + "</section>"
        )
    cls = "groups groups--divided" if b.get("divider") else "groups"
    return f'<div class="{cls}" style="grid-template-columns:repeat({cols},minmax(0,1fr))">' + "".join(parts) + "</div>"


def r_caption(b, ctx):
    return f'<p class="caption">{md(b["text"])}</p>'


def r_note(b, ctx):
    return f'<p class="note"><span class="note-label">해석</span>{md(b["text"])}</p>'


def r_deltas(b, ctx):
    rows = []
    for it in b["items"]:
        small = f"<small>{md(it['small'])}</small>" if it.get("small") else ""
        pair = ""
        if it.get("pair"):
            pair = f' data-pair="{attr("|".join(it["pair"]))}" tabindex="0"'
        rows.append(
            f'<div class="delta"{pair}><span class="delta-value">{md(it["value"])}</span>'
            f'<span class="delta-label">{md(it["label"])}{small}</span></div>'
        )
    return '<div class="deltas">' + "".join(rows) + "</div>"


def r_figure(b, ctx):
    cap = f'<figcaption class="caption">{md(b["caption"])}</figcaption>' if b.get("caption") else ""
    return (f'<figure class="figure"><div class="figure-mat"><img src="{b["src"]}" alt="{attr(b.get("alt", ""))}"></div>'
            f"{cap}</figure>")


def r_table(b, ctx):
    head = "".join(
        f'<th scope="col">{md(c["label"])}' + (f' <span class="dir">{c["dir"]}</span>' if c.get("dir") else "") + "</th>"
        for c in b["columns"]
    )
    body = []
    ncol = len(b["columns"])
    for g in b["groups"]:
        if g.get("label"):
            body.append(f'<tr class="group-row"><td colspan="{ncol}">{md(g["label"])}</td></tr>')
        for r in g["rows"]:
            cells = []
            for j, c in enumerate(r["cells"]):
                best = c.startswith("**") and c.endswith("**")
                txt = md(c[2:-2] if best else c)
                cls = ' class="best"' if best else ""
                tag = "th" if j == 0 else "td"
                scope = ' scope="row"' if j == 0 else ""
                cells.append(f"<{tag}{scope}{cls}>{txt}</{tag}>")
            focus = ' class="is-focus"' if r.get("focus") else ""
            focus += f' data-key="{attr(r["cells"][0])}"'
            body.append(f"<tr{focus}>{''.join(cells)}</tr>")
    return f'<table class="table"><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table>'


def r_bars(b, ctx):
    items = b["items"]
    W, label_w, val_w = 1000, 300, 120
    row_h, bar_h, axis_h = 108, 52, 52
    x0, x1 = label_w, W - val_w
    vmax = max(i["value"] for i in items)
    step = 1 if vmax <= 6 else 10 ** math.floor(math.log10(vmax))
    top = math.ceil(vmax / step) * step
    sx = lambda v: x0 + (x1 - x0) * v / top
    H = len(items) * row_h + axis_h
    g = []
    ticks = [k * step for k in range(int(top / step) + 1)]
    for t in ticks:
        x = sx(t)
        g.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{len(items) * row_h}" stroke="var(--chart-grid)" stroke-width="2"/>')
        g.append(f'<text x="{x:.1f}" y="{len(items) * row_h + 38}" font-size="24" fill="var(--chart-axis)" text-anchor="middle">{t:g}</text>')
    g.append(f'<line x1="{x0}" y1="0" x2="{x0}" y2="{len(items) * row_h}" stroke="var(--chart-axis)" stroke-width="2"/>')
    for k, it in enumerate(items):
        yc = k * row_h + row_h / 2
        focus = it.get("focus")
        fill = "var(--chart-highlight)" if focus else "var(--hs-grey-70)"
        wgt = "700" if focus else "500"
        col = "var(--color-text-heading)" if focus else "var(--color-text)"
        g.append(f'<g data-key="{html.escape(it["label"], quote=True)}">')
        g.append(f'<rect class="pair-mark" x="-16" y="{k * row_h + 6}" width="{W + 32}" height="{row_h - 12}" rx="4" '
                 f'fill="none" stroke="var(--color-warm)" stroke-width="3"/>')
        g.append(f'<text x="0" y="{yc - 4:.1f}" font-size="28" font-weight="{wgt}" fill="{col}">{html.escape(it["label"])}</text>')
        if it.get("sub"):
            g.append(f'<text x="0" y="{yc + 28:.1f}" font-size="24" fill="var(--color-text-muted)">{html.escape(it["sub"])}</text>')
        g.append(f'<rect class="bar" x="{x0}" y="{yc - bar_h / 2:.1f}" width="{sx(it["value"]) - x0:.1f}" height="{bar_h}" fill="{fill}"/>')
        g.append(f'<text class="val" x="{sx(it["value"]) + 16:.1f}" y="{yc + 10:.1f}" font-size="28" font-weight="{wgt}" fill="{col}" '
                 f'style="font-variant-numeric:tabular-nums">{it["value"]:.2f}</text>')
        g.append("</g>")
    desc = ", ".join(f'{i["label"]} {i["value"]:.2f}' for i in items)
    title = plain(b.get("title", b.get("metric", "")))
    return (f'<figure class="figure"><figcaption class="chart-title">{md(b.get("title", ""))}</figcaption>'
            f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="{attr(title)}">'
            f"<title>{html.escape(title)}</title><desc>{html.escape(desc)}</desc>"
            + "".join(g) + "</svg></figure>")


def inline_svg(path: Path) -> str:
    """Inline a hand-drawn diagram. Text that needs math goes in
    <foreignObject><div xmlns="http://www.w3.org/1999/xhtml" class="fo ...">…$x$…</div></foreignObject>;
    its content is run through md() like slide text."""
    s = path.read_text(encoding="utf-8")
    s = re.sub(r"<\?xml[^>]*\?>\s*", "", s)
    s = re.sub(r'(<div xmlns="http://www.w3.org/1999/xhtml"[^>]*>)(.*?)(</div>)',
               lambda m: m.group(1) + '<span class="fo-in">' + md(html.unescape(m.group(2))) + '</span>' + m.group(3), s, flags=re.S)
    return s.strip()


def r_toggle(b, ctx):
    work: Path = ctx["work"]
    states = b["states"]
    start = b["start"]
    ids = " ".join(s["id"] for s in states)
    svg = inline_svg(work / b["svg"])

    # static default: mark everything that is not in the start state as off
    def off(m):
        show = m.group(2).split()
        tag = m.group(0)
        if start in show:
            return tag
        if 'class="' in tag:
            return tag.replace('class="', 'class="is-off ', 1)
        return tag.replace(m.group(1), f'{m.group(1)} class="is-off"', 1)
    svg = re.sub(r'(<\w+)\b[^>]*\bdata-show="([^"]+)"[^>]*>', off, svg)

    buttons = "".join(
        f'<button type="button" data-set-state="{s["id"]}" aria-pressed="{"true" if s["id"] == start else "false"}"'
        f' tabindex="{0 if s["id"] == start else -1}"><span class="key" aria-hidden="true">{k + 1}</span>{md(s["label"])}</button>'
        for k, s in enumerate(states)
    )
    panels = []
    for s in states:
        eq = ""
        if s.get("equation"):
            eq = f'<div class="equation">{math_html(s["equation"], display=True)}</div>'
        sym = ""
        if s.get("symbols"):
            sym = '<dl class="symbols">' + "".join(f"<dt>{md(a)}</dt><dd>{md(d)}</dd>" for a, d in s["symbols"]) + "</dl>"
        hidden = "" if s["id"] == start else " hidden"
        panels.append(
            f'<div data-state-panel="{s["id"]}"{hidden}>'
            f'<p class="readout-state">{md(s["title"])}</p><p class="readout-text">{md(s["text"])}</p>{eq}{sym}</div>'
        )
    cap = f'<p class="caption col-push">{md(b["caption"])}</p>' if b.get("caption") else ""
    return (
        f'<div class="toggle-grid" data-toggle data-states="{ids}" data-start="{start}" data-print="{b["print"]}">'
        f'<div class="toggle"><div class="seg" role="group" aria-label="비교할 방식">{buttons}</div>{svg}</div>'
        + (f'<div class="toggle-side readout"><div class="panel panel--sm">{"".join(panels)}</div>{cap}'
           if b.get("panel") else f'<div class="toggle-side readout">{"".join(panels)}{cap}')
        + f'<p class="sr-only" data-live aria-live="polite"></p></div></div>'
    )


def r_split(b, ctx):
    a, c = b.get("cols", [1, 1])
    left = "".join(render(x, ctx) for x in b.get("left", []))
    right = "".join(render(x, ctx) for x in b.get("right", []))
    return (f'<div class="split" style="grid-template-columns:minmax(0,{a}fr) minmax(0,{c}fr)">'
            f"<div>{left}</div><div>{right}</div></div>")


def r_panel(b, ctx):
    cls = "panel panel--sm" if b.get("size") == "sm" else "panel"
    head = f'<h3 class="panel-title">{md(b["heading"])}</h3>' if b.get("heading") else ""
    return f'<div class="{cls}">{head}' + "".join(render(x, ctx) for x in b.get("body", [])) + "</div>"


RENDER = {
    "lead": r_lead, "groups": r_groups, "caption": r_caption, "note": r_note, "deltas": r_deltas,
    "figure": r_figure, "table": r_table, "bars": r_bars, "toggle": r_toggle, "split": r_split,
    "panel": r_panel,
}


def render(b, ctx):
    fn = RENDER.get(b["type"])
    if not fn:
        raise SystemExit(f"unknown block type {b['type']!r}")
    return fn(b, ctx)


# --------------------------------------------------------------------------- slides

def footer(deck, i, dark=False):
    secs = deck["meta"]["sections"]
    slides = deck["slides"]
    counts = {s["id"]: 0 for s in secs}
    for sl in slides:
        if sl.get("section") in counts:
            counts[sl["section"]] += 1
    cur = slides[i].get("section")
    order = [s["id"] for s in secs]
    ci = order.index(cur) if cur in order else -1
    lis = []
    for k, s in enumerate(secs):
        cls = "is-current" if k == ci else ("is-past" if k < ci else "")
        aria = ' aria-current="step"' if k == ci else ""
        lis.append(f'<li class="{cls}" style="flex-grow:{max(1, counts[s["id"]])}"{aria}><span>{md(s["label"])}</span></li>')
    return (
        '<footer class="foot">'
        f'<ol class="progress" aria-label="발표 구간">{"".join(lis)}</ol>'
        f'<span class="folio">{i + 1} / {len(slides)}</span>'
        f'<img class="foot-logo" src="assets/brand/hsu-signature-en{"-white" if dark else ""}.svg" alt="Hansung University">'
        "</footer>"
    )


def cover_credit(meta) -> str:
    """The reviewed paper's authors, small, under the subtitle. Omitted for one's own talk
    (no meta.paper) or when meta.coverCredit is false."""
    p = meta.get("paper")
    if not p or not meta.get("coverCredit", True) or not p.get("authors"):
        return ""
    bits = [x for x in (p.get("affiliations"), p.get("venue")) if x]
    if "*" in p["authors"]:
        bits.append("* 공동 1저자")
    tail = ". ".join(bits)
    return (
        '<p class="cover-credit">'
        f'<span class="credit-authors">{html.escape(p["authors"])}</span>'
        + (f'<span>{md(tail)}</span>' if tail else "")
        + "</p>"
    )


def cover(deck, sl):
    meta = deck["meta"]
    pr = meta["presenter"]
    fig = sl.get("figure")
    aff = "".join(f'<span class="presenter-aff">{md(a)}</span>'
                  for a in ([pr["affiliation"]] if isinstance(pr.get("affiliation"), str) else pr.get("affiliation", [])))
    when = "".join(f'<span>{md(x)}</span>' for x in (meta.get("event"), meta.get("date")) if x)
    return (
        f'<h1 class="cover-title">{md(sl["title"])}</h1>'
        f'<p class="cover-sub">{md(sl["subtitle"])}</p>'
        f'{cover_credit(meta)}'
        '<div class="cover-rule" aria-hidden="true"></div>'
        '<div class="cover-grid">'
        f'{r_figure(fig, None) if fig else "<div></div>"}'
        '<div class="byline">'
        f'<p class="presenter"><span class="presenter-name">{md(pr["name"])}</span>{aff}</p>'
        + (f'<p class="cover-event">{when}</p>' if when else "")
        + '<img class="cover-logo" src="assets/brand/hsu-signature-en.svg" alt="Hansung University">'
        "</div></div>"
    )


def slide_html(deck, i, ctx):
    sl = deck["slides"][i]
    layout = sl.get("layout", "content")
    cls = ["slide"]
    dark = is_dark(deck, sl)
    if layout == "cover":
        cls.append("slide--cover")
        inner = cover(deck, sl)
    else:
        if layout == "statement":
            cls.append("slide--statement")
        if sl.get("tone") == "wash":
            cls.append("slide--wash")
        body = "".join(render(b, ctx) for b in sl.get("body", []))
        inner = (f'<h2 class="slide-title">{md(sl["title"])}</h2>'
                 f'<div class="slide-body">{body}</div>{footer(deck, i, dark)}')
    notes = ""
    if sl.get("notes"):
        notes = '<template class="notes">' + "".join(f"<p>{md(x)}</p>" for x in sl["notes"]) + "</template>"
    hidden = "" if i == 0 else " inert"
    return (f'<section class="{" ".join(cls)}{" is-current" if i == 0 else ""}" id="s{i + 1}" '
            f'data-id="{sl["id"]}"{' data-theme="dark"' if dark else ""} aria-label="{attr(sl["title"])}" aria-roledescription="slide"{hidden}>'
            f"{inner}{notes}</section>")


PAGE = """<!doctype html>
<html lang="{lang}" data-theme="light" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="assets/tokens.css">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/base.css">
<link rel="stylesheet" href="assets/deck.css">
<script src="assets/deck.js" defer></script>
</head>
<body>
<main class="deck" aria-roledescription="slide deck" aria-label="{title}">
<div class="stage">
{slides}
</div>
</main>
<p id="deck-live" class="sr-only" aria-live="polite"></p>
</body>
</html>
"""


def copy_assets(out: Path) -> None:
    a = out / "assets"
    a.mkdir(parents=True, exist_ok=True)
    for f in ("tokens.css", "fonts.css", "base.css"):
        shutil.copy2(ASSETS / f, a / f)
    shutil.copy2(ASSETS / "engine/deck.css", a / "deck.css")
    shutil.copy2(ASSETS / "engine/deck.js", a / "deck.js")
    for d in ("fonts", "brand"):
        if (a / d).exists():
            shutil.rmtree(a / d)
        shutil.copytree(ASSETS / d, a / d)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    work = Path(sys.argv[1]).resolve()
    deck = json.loads((work / "deck.json").read_text(encoding="utf-8"))
    gate = Gate()
    check(deck, work, gate)
    if gate.errors:
        print("build refused:", file=sys.stderr)
        for e in gate.errors:
            print("  - " + e, file=sys.stderr)
        return 1
    out = work / "deck"
    _CTX["math_cache"] = out / "assets" / "math"
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    copy_assets(out)
    ctx = {"work": work}
    slides = "\n".join(slide_html(deck, i, ctx) for i in range(len(deck["slides"])))
    page = PAGE.format(lang=deck["meta"].get("lang", "ko"), title=html.escape(deck["meta"]["title"]), slides=slides)
    (out / "index.html").write_text(page, encoding="utf-8")
    print(f"wrote {out / 'index.html'} ({len(deck['slides'])} slides)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
