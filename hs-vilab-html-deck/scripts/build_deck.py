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
    # a superscript name (DiT^{DH}-XL, RAE run) is one unbreakable unit with the suffix after it
    s = re.sub(r"(\w+)\^\{(.+?)\}((?:-[\w.]+)*)", r'<span class="nw">\1<sup>\2</sup>\3</span>', s)
    # keep hyphenated names (Self-Flow, SiT-XL/2, text-to-image) on one line
    s = re.sub(r"(?<![\w-])([A-Za-z0-9][\w.]*(?:-[\w.]+)+)", r'<span class="nw">\1</span>', s)
    # short pairs that must not split at a line end: "약 625M", "no CFG"
    s = re.sub(r"약 (?=\d)", "약 ", s)
    s = re.sub(r"\bno CFG\b", "no\u00a0CFG", s)
    # a count and its unit stay together: "1M step", "50 ODE steps", "600K step"
    s = re.sub(r"(\d[\d.,]*[KMB]?) (?=(?:ODE |SDE )?(?:steps?|epochs?|ep)\b)", "\\1\u00a0", s)
    # a measurement and its unit: "54.9 ms", "32.2 dB", "19.0 GiB", "387.6 TFLOPs" (Integral run)
    s = re.sub(r"(\d[\d.,]*) (?=(?:ms|dB|GiB|GB|MB|TFLOPs|GFLOPs)\b)", "\\1\u00a0", s)
    # a reference and its number, a metric and its value, "= 9.6": one unit each (REPA run)
    s = re.sub(r"\b(Fig\.|Figs\.|Table|Tables|Eq\.|Sec\.|App\.) (?=[\dA-Z(])", "\\1\u00a0", s)
    s = re.sub(r"\b(FID|sFID|IS|FVD|FAD|Acc\.|Pre\.|Rec\.) (?=[−+\-]?\d)", "\\1\u00a0", s)
    s = re.sub(r" = (?=[−+\-]?\d)", "\u00a0=\u00a0", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"_\{(.+?)\}", r"<sub>\1</sub>", s)
    return s


def md(s: str) -> str:
    """Escape, then a small inline syntax: **bold**, _{subscript}, ^{superscript}, $TeX math$ (\\$ = literal $)."""
    parts = re.split(r"(?<!\\)\$(.+?)(?<!\\)\$", str(s))
    out = []
    for k, part in enumerate(parts):
        out.append(math_html(part) if k % 2 else _text(part.replace("\\$", "$")))
    # keep "$s$ = 0.8" on one line, and a Korean particle on the math it follows ($\ell_1$에서)
    # brackets around math stay with it, so "($\mathrm{ESS}_t<k/2$)이면" never leaves ")이면" alone (FK run)
    return re.sub(r'(\(?)(<span class="im"(?:(?!</span>).)*</svg></span>)([ \u00a0]=[ \u00a0][\d.]+[가-힣]*|[)\]]*[가-힣]+|[)\]]+)',
                  r'<span class="nw">\1\2\3</span>', "".join(out))


def plain(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", str(s))
    s = re.sub(r"\$(.+?)\$", r"\1", s)
    s = re.sub(r"\^\{(.+?)\}", r"\1", s)
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
    interactive, signature, paneled, animations = [], [], [], []
    gate(meta.get("motion", "on") in ("on", "auto", "off"), f"meta.motion is {meta.get('motion')!r}; use on | auto | off")
    pr = meta.get("presenter") or {}
    gate(bool(pr.get("name")), "meta.presenter.name is missing (the cover names who presents)")
    p = meta.get("paper")
    if p:
        gate(bool(p.get("authors")), "meta.paper has no authors (drop meta.paper for your own work)")
        gate("*" not in p.get("authors", "") or bool(p.get("authorNote")),
             "meta.paper.authors has * but no authorNote saying what it marks (e.g. \"* 공동 1저자\", \"* 공동 지도\")")
    # the spoken script must fit the talk. Korean is read aloud at about 4–5 characters (no spaces) a
    # second; the five decks before this gate ran 3.8–5.0. The FK run's first script ran 7.8 (about 31
    # minutes for a 20-minute talk) and nothing said so.
    if str(meta.get("lang", "ko")).startswith("ko") and meta.get("target_minutes"):
        chars = sum(len(re.sub(r"\s", "", "".join(sl.get("notes", [])))) for sl in slides)
        rate = chars / (meta["target_minutes"] * 60)
        gate(3.0 <= rate <= 5.5,
             f"script is {chars} characters for {meta['target_minutes']} min = {rate:.1f}/s; "
             f"spoken Korean runs about 4–5/s (keep it within 3.0–5.5): cut or add script, not slides")
    for i, sl in enumerate(slides, 1):
        where = f"slide {i} ({sl.get('id')})"
        gate(bool(sl.get("title")), f"{where}: no title")
        if sl.get("layout") not in ("cover", "ending"):
            gate(bool(sl.get("message")), f"{where}: no message (one key sentence per slide)")
            gate(sl.get("section") in sec_ids, f"{where}: section {sl.get('section')!r} is not in meta.sections")
            gate(bool(sl.get("cite")), f"{where}: no cite")
        kinds = [b["type"] for b in walk(sl.get("body", [])) if b["type"] in ("toggle", "stepper", "animation")]
        gate(len(kinds) <= 1, f"{where}: {' + '.join(kinds)} on one slide; one interaction per slide")
        for b in walk(sl.get("body", [])):
            if b["type"] == "animation":
                interactive.append(i)
                animations.append(i)
                if b.get("signature"):
                    signature.append(i)
                check_animation(b, work, where, gate)
                continue
            if b["type"] in ("toggle", "stepper"):
                interactive.append(i)
                if b.get("signature"):
                    signature.append(i)
                gate(bool(b.get("reveals")), f"{where}: {b['type']} has no 'reveals' (what does operating it show about the paper?)")
                gate(b.get("print") in ("default", "expand"), f"{where}: {b['type']} 'print' must be default|expand")
                if b.get("svg") or b["type"] == "stepper":
                    gate((work / b.get("svg", "")).is_file(), f"{where}: diagram {b.get('svg')!r} not found")
                else:
                    for st in b.get("states", []):
                        gate((work / "deck" / st.get("src", "")).is_file(), f"{where}: state {st.get('id')!r} needs svg on the block or src on the state")
                if b["type"] == "stepper":
                    gate(2 <= len(b.get("steps", [])) <= 6, f"{where}: a stepper has 2–6 steps")
                    gate(bool(b.get("provenance")), f"{where}: stepper has no provenance")
                    continue
                ids = [s["id"] for s in b.get("states", [])]
                gate(len(ids) >= 2, f"{where}: toggle needs at least two states")
                gate(b.get("start") in ids, f"{where}: toggle 'start' {b.get('start')!r} is not one of its states")
                for st in b.get("states", []):
                    gate(bool(st.get("provenance")), f"{where}: state {st.get('id')!r} has no provenance")
            if b["type"] in ("bars", "table", "deltas"):
                gate(bool(b.get("provenance")), f"{where}: {b['type']} has no provenance")
            if b["type"] in ("figure", "figureNumbered"):
                gate((work / "deck" / b["src"]).is_file(), f"{where}: figure {b['src']!r} not found")
            if b["type"] == "figureNumbered":
                gate(len(b.get("marks", [])) == len(b.get("items", [])), f"{where}: figureNumbered needs one item per mark")
            if b["type"] == "diagram":
                gate((work / b.get("svg", "")).is_file(), f"{where}: diagram {b.get('svg')!r} not found")
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
    gate(len(animations) <= 3, f"{len(animations)} animation slides (slides {animations}); at most 3 per deck")
    # one name, one pair of files: the build copies one script per name, so two scripts under one name
    # would leave the first slide playing the second one's animation
    named: dict = {}
    for sl in slides:
        for b in walk(sl.get("body", [])):
            if b["type"] == "animation":
                named.setdefault(b.get("name"), set()).add((b.get("script"), b.get("svg")))
    for nm, files in named.items():
        gate(len(files) == 1, f"animation name {nm!r} is used for different files {sorted(files)}; give each its own name")
    content = [sl for sl in slides if sl.get("layout") not in ("cover", "ending")]
    gate(slides[-1].get("layout") == "ending", "the last slide is not an ending (layout: \"ending\" — 감사합니다 / Q&A)")
    notes = sum(1 for sl in slides for b in walk(sl.get("body", [])) if b["type"] == "note")
    cap_n = max(2, math.ceil(len(content) / 4))
    gate(notes <= cap_n, f"{notes} note blocks; at most {cap_n} (one per four content slides) — note marks interpretation only")
    if meta.get("target_slides"):
        gate(n == meta["target_slides"], f"{n} slides; meta.target_slides is {meta['target_slides']}")
    if meta.get("target_minutes") and any("time" in sl for sl in slides):
        total = sum(int(sl.get("time", 0)) for sl in slides)
        goal = meta["target_minutes"] * 60
        gate(abs(total - goal) <= goal * 0.1, f"slide times add up to {total // 60}:{total % 60:02d}; the talk is {meta['target_minutes']} min (±10%)")
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
    # every character on the stage must be in the bundled fonts (RAE run: ✓/✗ in a table fell back
    # to Segoe UI Symbol and Noto Sans KR — a different look on every PC, a box on some)
    for where, ch, text in uncovered(deck, work):
        gate(False, f"{where}: {ch!r} (U+{ord(ch):04X}) is not in the bundled fonts — in {text[:40]!r}; "
                    "write it another way (a word, ○/×, bold) or put it in math")


# an animation script draws; the engine plays. Anything that keeps its own clock, reads the OS,
# listens for input, writes text or reaches the network breaks "the picture is a function of t"
ANIM_FORBIDDEN = ["requestAnimationFrame", "setTimeout", "setInterval", "Date.now", "performance.now",
                  "Math.random", "matchMedia", "addEventListener", "textContent", "innerHTML", "innerText",
                  "fetch(", "XMLHttpRequest", "http:", "https:", "document.write", "createElementNS",
                  "IntersectionObserver"]


def check_animation(b, work: Path, where: str, gate) -> None:
    name = b.get("name", "")
    gate(bool(re.fullmatch(r"[a-z][a-z0-9-]*", name)), f"{where}: animation name {name!r} (lowercase, digits, -)")
    svg, js = work / b.get("svg", ""), work / b.get("script", "")
    gate(svg.is_file() and svg.suffix == ".svg", f"{where}: animation svg {b.get('svg')!r} not found")
    gate(js.is_file() and js.suffix == ".js", f"{where}: animation script {b.get('script')!r} not found")
    beats = b.get("beats", [])
    gate(3 <= len(beats) <= 5, f"{where}: an animation has 3–5 beats (the opening picture and 2–4 key presses), not {len(beats)}")
    gate(all(x.get("title") for x in beats), f"{where}: every beat needs a title")
    gate(bool(b.get("reveals")), f"{where}: animation has no 'reveals' (what does playing it show about the paper?)")
    gate(b.get("print") in ("default", "expand"), f"{where}: animation 'print' must be default|expand")
    gate(bool(b.get("provenance")), f"{where}: animation has no provenance")
    gate(b.get("side", "right") in ("right", "below"), f"{where}: animation side must be right|below")
    if js.is_file():
        # comments may say what the engine does ("the engine owns setTimeout"); only code is checked
        code = re.sub(r"/\*.*?\*/", "", js.read_text(encoding="utf-8"), flags=re.S)
        code = re.sub(r"(?m)(^|[^:\\])//.*$", r"\1", code)
        gate(re.search(r"DeckAnim\.define\(\s*[\"']" + re.escape(name) + r"[\"']", code) is not None,
             f"{where}: {b['script']} does not call DeckAnim.define({name!r}, …)")
        for word in ANIM_FORBIDDEN:
            gate(word not in code, f"{where}: {b['script']} uses {word!r} — the engine owns time, input and text; "
                                   "render(t) only sets attributes of elements drawn in the SVG")
    if svg.is_file():
        s = svg.read_text(encoding="utf-8")
        remote = (re.search(r"(?:href|src)\s*=\s*[\"']\s*(?:https?:)?//", s)
                  or re.search(r"url\(\s*[\"']?\s*(?:https?:)?//", s))
        gate("<script" not in s and not remote, f"{where}: {b['svg']} has a script or a remote link")
        drawn = set(re.findall(r"data-anim\s*=\s*[\"']([^\"']+)[\"']", s))
        for key in set(re.findall(r"node\(\s*[\"']([^\"']+)[\"']", js.read_text(encoding="utf-8") if js.is_file() else "")):
            gate(key in drawn, f"{where}: the script asks for data-anim={key!r}, which {b['svg']} does not draw")


# keys whose strings are never set in the stage fonts (spoken, alt text, paths, ids, TeX)
NOT_STAGE = {"notes", "provenance", "alt", "src", "svg", "id", "cite", "message", "reveals", "start",
             "print", "type", "cols", "layout", "section", "tone", "valign", "lines", "tags", "url",
             "slug", "team", "figures", "lang", "titleLang", "statementTheme", "motion", "occasion",
             "name", "script", "side"}


def _font_cover() -> set[int] | None:
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return None     # QA's glyph-face check still catches a fallback font
    cover: set[int] = set()
    for f in (ASSETS / "fonts").glob("*.woff2"):
        cover |= set(TTFont(f).getBestCmap())
    return cover


def uncovered(deck: dict, work: Path):
    cover = _font_cover()
    if cover is None:
        return
    seen = set()

    def strings(x, where):
        if isinstance(x, str):
            yield where, x
        elif isinstance(x, list):
            for v in x:
                yield from strings(v, where)
        elif isinstance(x, dict):
            for k, v in x.items():
                if k not in NOT_STAGE:
                    yield from strings(v, where)

    items = list(strings({k: v for k, v in deck["meta"].items()}, "meta"))
    for i, sl in enumerate(deck["slides"], 1):
        items += list(strings(sl, f"slide {i}"))
        for b in walk(sl.get("body", [])):
            if b.get("svg") and (work / b["svg"]).is_file():
                svg = (work / b["svg"]).read_text(encoding="utf-8")
                svg = re.sub(r"<(title|desc)\b.*?</\1>", "", svg, flags=re.S)
                items.append((f"slide {i} {b['svg']}", " ".join(re.findall(r">([^<]+)<", svg))))
    for where, s in items:
        s = re.sub(r"\$[^$]*\$", "", s)          # inline math is drawn as SVG
        for ch in s:
            if ord(ch) > 0x7F and ord(ch) not in cover and not ch.isspace() and (where, ch) not in seen:
                seen.add((where, ch))
                yield where, ch, s


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
    size = f' style="max-height:{int(b["height"])}px;width:auto;max-width:100%"' if b.get("height") else ""
    # a figure given a height keeps it: shrinking the box but not the image pushed its caption
    # into the block below (REPA run, slide 18); if it does not fit, QA reports the spill
    cls = "figure figure--fixed" if b.get("height") else "figure"
    return (f'<figure class="{cls}"><div class="figure-mat"><img src="{b["src"]}" alt="{attr(b.get("alt", ""))}"{size}></div>'
            f"{cap}</figure>")


# a number cell: "0.41", "+0.3", "약 0.28", "600K", "9.8B", a range "256–512" or "48–64", a bound "≤ 512"
# (Integral run: the step, resolution and GPU columns of Table 7 and a Params column aligned left)
NUMERIC = re.compile(r"^\**\s*(?:[≤≥<>]\s*)?[−+\-]?(?:약\s*)?[\d.,]+(?:\s*[–\-]\s*[\d.,]+)?[ %×MKkB]*(?:초|배|ms|s)?\s*\**$")
PLACEHOLDER = {"—", "–", "-", "N/A", "n/a"}


def r_table(b, ctx):
    # numbers align right (decimals line up); a column of words aligns left
    ncol = len(b["columns"])
    left = []
    for j in range(ncol):
        cells = [r["cells"][j] for g in b["groups"] for r in g["rows"] if j < len(r["cells"]) and r["cells"][j].strip()]
        # a "—" (not reported) does not make a number column a word column (RAE run: the gFID and
        # IS columns with "—" rows aligned left while the next gFID column aligned right)
        nums = [c for c in cells if c.strip("* ") not in PLACEHOLDER]
        auto = j == 0 or not nums or not all(NUMERIC.match(c) for c in nums)
        left.append(b["columns"][j].get("align", "left" if auto else "right") == "left")
    lc = lambda j: ' class="l"' if left[j] and j else ""
    head = "".join(
        f'<th scope="col"{lc(j)}>{md(c["label"])}' + (f' <span class="dir">{c["dir"]}</span>' if c.get("dir") else "") + "</th>"
        for j, c in enumerate(b["columns"])
    )
    body = []
    for g in b["groups"]:
        if g.get("label"):
            body.append(f'<tr class="group-row"><td colspan="{ncol}">{md(g["label"])}</td></tr>')
        for r in g["rows"]:
            cells = []
            for j, c in enumerate(r["cells"]):
                best = c.startswith("**") and c.endswith("**")
                txt = md(c[2:-2] if best else c)
                names = (["best"] if best else []) + (["l"] if left[j] and j else [])
                cls = f' class="{" ".join(names)}"' if names else ""
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
    if b.get("svg"):
        svg = inline_svg(work / b["svg"])
    else:
        # image tabs: one paper figure per state, stacked in one cell so the slide keeps the tallest height
        svg = '<div class="toggle-media">' + "".join(
            f'<figure class="figure" data-show="{s["id"]}"><div class="figure-mat">'
            f'<img src="{s["src"]}" alt="{attr(s.get("alt", ""))}"></div></figure>' for s in states) + "</div>"

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
    cap = "".join(render(x, ctx) for x in b.get("side", [])) + cap
    return (
        f'<div class="toggle-grid" data-toggle data-states="{ids}" data-start="{start}" data-print="{b["print"]}"'
        + (f' style="grid-template-columns:minmax(0,{b["cols"][0]}fr) minmax(0,{b["cols"][1]}fr)"' if b.get("cols") else "")
        + '>'
        f'<div class="seg{" seg--compact" if len(states) >= 4 else ""}" role="group" aria-label="비교할 방식">{buttons}</div>'
        f'<div class="toggle">{svg}'
        + (f'<p class="caption media-caption">{md(b["mediaCaption"])}</p>' if b.get("mediaCaption") else "")
        + '</div>'
        + (f'<div class="toggle-side readout"><div class="panel panel--sm">{"".join(panels)}</div>{cap}'
           if b.get("panel") else f'<div class="toggle-side readout"><div class="readout-states">{"".join(panels)}</div>{cap}')
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


def r_bullets(b, ctx):
    return r_items(b["items"], b.get("numbered", False), b.get("size"))


def r_cards(b, ctx):
    """Parallel items as columns divided by rules — not boxes (a panel is the only surface)."""
    cols = b.get("columns", len(b["items"]))
    parts = []
    for k, it in enumerate(b["items"], 1):
        num = f'<span class="card-num" aria-hidden="true">{k}</span>' if b.get("numbered") else ""
        parts.append(f'<section class="card">{num}<h3 class="card-title">{md(it["title"])}</h3>'
                     + (f'<p class="card-text">{md(it["text"])}</p>' if it.get("text") else "")
                     + "</section>")
    return f'<div class="cards" style="grid-template-columns:repeat({cols},minmax(0,1fr))">' + "".join(parts) + "</div>"


def r_callout(b, ctx):
    return f'<p class="callout">{md(b["text"])}</p>'


def r_equation(b, ctx):
    lines = b.get("lines") or [b["tex"]]
    eqs = "".join(f'<div class="equation-line">{math_html(t, display=True)}'
                  + (f'<span class="eq-tag">({md(tag)})</span>' if tag else "") + "</div>"
                  for t, tag in zip(lines, b.get("tags", [None] * len(lines))))
    sym = ""
    if b.get("symbols"):
        sym = '<dl class="symbols">' + "".join(f"<dt>{md(a)}</dt><dd>{md(d)}</dd>" for a, d in b["symbols"]) + "</dl>"
    return f'<div class="equation-block"><div class="equation">{eqs}</div>{sym}</div>'


def r_process(b, ctx):
    steps = []
    for k, s in enumerate(b["steps"], 1):
        steps.append(f'<li class="process-step"><span class="process-num" aria-hidden="true">{k}</span>'
                     f'<h3 class="process-title">{md(s["title"])}</h3>'
                     + (f'<p class="process-text">{md(s["text"])}</p>' if s.get("text") else "") + "</li>")
    cls = "process process--v" if b.get("direction") == "vertical" else "process"
    return f'<ol class="{cls}">' + "".join(steps) + "</ol>"


def r_compare(b, ctx):
    """Two (or three) approaches side by side, divided by a rule."""
    return r_groups({"groups": b["items"], "columns": len(b["items"]), "divider": True, "size": b.get("size")}, ctx)


def r_figure_numbered(b, ctx):
    """A paper figure with numbered marks on it and a numbered list of what each mark shows."""
    marks = "".join(
        f'<span class="mark" style="left:{m["x"] * 100:.2f}%;top:{m["y"] * 100:.2f}%" aria-hidden="true">{k}</span>'
        for k, m in enumerate(b["marks"], 1))
    cap = f'<figcaption class="caption">{md(b["caption"])}</figcaption>' if b.get("caption") else ""
    fig = (f'<figure class="figure"><div class="figure-mat"><div class="mark-wrap">'
           f'<img src="{b["src"]}" alt="{attr(b.get("alt", ""))}">{marks}</div></div>{cap}</figure>')
    return fig + r_items(b["items"], numbered=True, size=b.get("size"))


def r_diagram(b, ctx):
    svg = inline_svg(ctx["work"] / b["svg"])
    cap = f'<figcaption class="caption">{md(b["caption"])}</figcaption>' if b.get("caption") else ""
    return f'<figure class="figure figure--diagram">{svg}{cap}</figure>'


def r_stepper(b, ctx):
    """Next-key steps over one diagram. Elements carry data-from-step="k" in the SVG; step 0 is the start.
    The side list shows each step's line from its step on, so the slide reads complete when expanded."""
    svg = inline_svg(ctx["work"] / b["svg"])
    items = []
    for k, s in enumerate(b["steps"]):
        attr_ = f' data-from-step="{k}"' + (' class="is-off"' if k > 0 else "")
        items.append(f'<li{attr_}><span class="step-num" aria-hidden="true">{k + 1}</span>'
                     f'<span class="step-title">{md(s["title"])}</span>'
                     + (f'<span class="step-text">{md(s["text"])}</span>' if s.get("text") else "") + "</li>")
    # hide everything that appears from a later step in the static (no-JS, step 0) render
    svg = re.sub(r'(<\w+)\b([^>]*\bdata-from-step="([1-9]\d*)"[^>]*)>',
                 lambda m: (m.group(0).replace('class="', 'class="is-off ', 1) if 'class="' in m.group(2)
                            else f'{m.group(1)} class="is-off"{m.group(2)}>'), svg)
    # the caption names the figure, so it sits under the figure (not under the step list)
    cap = f'<figcaption class="caption">{md(b["caption"])}</figcaption>' if b.get("caption") else ""
    side = '<ol class="steps">' + "".join(items) + "</ol>"
    return (f'<div class="stepper" data-stepper data-print="{b["print"]}" style="grid-template-columns:minmax(0,{b.get("cols", [3, 2])[0]}fr) minmax(0,{b.get("cols", [3, 2])[1]}fr)">'
            f'<figure class="figure figure--diagram">{svg}{cap}</figure><div class="stepper-side">{side}</div></div>')


IDREF_ATTRS = ("aria-labelledby", "aria-describedby", "aria-controls", "aria-owns", "aria-details",
               "aria-flowto", "aria-activedescendant", "aria-errormessage", "for")


def _attr(name: str) -> str:
    """name="value" or name='value' as a whole attribute (not data-name, not xlink:name)."""
    return r"(?<![\w:-])(" + name + r")\s*=\s*([\"'])(.*?)\2"


def prefix_ids(svg: str, pre: str) -> str:
    """Give every id in an inlined SVG (and each reference to it) a per-slide prefix: two SVGs on one
    page must not share a clipPath, mask, gradient or title id. Only real id attributes are renamed
    (not data-id), and only references to them: a local fragment in href / xlink:href, url(#…) in an
    attribute or a style, and the tokens of ARIA id-reference lists."""
    ids = {m.group(3) for m in re.finditer(_attr("id"), svg)}
    if not ids:
        return svg

    def ren(m, value):
        return f"{m.group(1)}={m.group(2)}{value}{m.group(2)}"

    svg = re.sub(_attr("id"), lambda m: ren(m, pre + m.group(3)), svg)
    svg = re.sub(_attr("(?:xlink:)?href"),
                 lambda m: ren(m, "#" + pre + m.group(3)[1:]) if m.group(3)[:1] == "#" and m.group(3)[1:] in ids
                 else m.group(0), svg)
    svg = re.sub(r"url\(\s*#([^)\s]+)\s*\)", lambda m: f"url(#{pre}{m.group(1)})" if m.group(1) in ids else m.group(0), svg)
    for a in IDREF_ATTRS:
        svg = re.sub(_attr(re.escape(a)), lambda m: ren(m, " ".join(pre + x if x in ids else x for x in m.group(3).split())), svg)
    return svg


def r_animation(b, ctx):
    """A diagram drawn as a function of time (figures/<name>.anim.js), one beat per next key. The SVG
    file is the finished picture (no script, the PDF's default page, the overview grid); the script
    moves its data-anim elements. The beat list reads like a stepper's: beat k from beat k on."""
    pre = f"a{ctx['slide']}-"
    svg = prefix_ids(inline_svg(ctx["work"] / b["svg"]), pre)
    items = []
    for k, s in enumerate(b["beats"]):
        attr_ = f' data-from-step="{k}"' + (' class="is-off"' if k > 0 else ' class="is-now"')
        items.append(f'<li{attr_}><span class="step-num" aria-hidden="true">{k + 1}</span>'
                     f'<span class="step-title">{md(s["title"])}</span>'
                     + (f'<span class="step-text">{md(s["text"])}</span>' if s.get("text") else "") + "</li>")
    cap = f'<figcaption class="caption">{md(b["caption"])}</figcaption>' if b.get("caption") else ""
    head = (f'data-stepper data-print="{b["print"]}" data-anim-name="{attr(b["name"])}" data-beats="{len(b["beats"])}"')
    fig = f'<figure class="figure figure--diagram">{svg}{cap}</figure>'
    steps = '<ol class="steps">' + "".join(items) + "</ol>"
    ctx.setdefault("scripts", []).append(b)
    if b.get("side", "right") == "below":
        return f'<div class="anim anim--below" {head} style="--beats:{len(b["beats"])}">{fig}{steps}</div>'
    c = b.get("cols", [3, 2])
    return (f'<div class="anim stepper" {head} style="grid-template-columns:minmax(0,{c[0]}fr) minmax(0,{c[1]}fr)">'
            f'{fig}<div class="stepper-side">{steps}</div></div>')


RENDER = {
    "animation": r_animation,
    "lead": r_lead, "groups": r_groups, "caption": r_caption, "note": r_note, "deltas": r_deltas,
    "figure": r_figure, "table": r_table, "bars": r_bars, "toggle": r_toggle, "split": r_split,
    "panel": r_panel, "bullets": r_bullets, "cards": r_cards, "callout": r_callout,
    "equation": r_equation, "process": r_process, "compare": r_compare,
    "figureNumbered": r_figure_numbered, "diagram": r_diagram, "stepper": r_stepper,
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
    # what the asterisk means is the paper's to say (co-first authors, equal advising, …)
    if p.get("authorNote"):
        bits.append(p["authorNote"])
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


def ending(deck, sl):
    """The closing slide: thanks, Q&A, the presenter and the signature, a few links. No footer."""
    meta = deck["meta"]
    pr = meta["presenter"]
    aff = "".join(f'<span class="presenter-aff">{md(a)}</span>'
                  for a in ([pr["affiliation"]] if isinstance(pr.get("affiliation"), str) else pr.get("affiliation", [])))
    links = "".join(f"<li>{md(x)}</li>" for x in sl.get("links", []))
    return (
        '<div class="ending-main">'
        f'<h1 class="cover-title ending-title">{md(sl.get("title", "감사합니다"))}</h1>'
        f'<p class="ending-sub">{md(sl.get("subtitle", "Q&A"))}</p>'
        "</div>"
        '<div class="cover-rule" aria-hidden="true"></div>'
        '<div class="ending-foot">'
        + (f'<ul class="ending-links">{links}</ul>' if links else "<div></div>")
        + '<div class="byline">'
        f'<p class="presenter"><span class="presenter-name">{md(pr["name"])}</span>{aff}</p>'
        + (f'<p class="presenter-contact">{md(pr["contact"])}</p>' if pr.get("contact") else "")
        + '<img class="cover-logo" src="assets/brand/hsu-signature-en.svg" alt="Hansung University">'
        "</div></div>"
    )


def slide_html(deck, i, ctx):
    sl = deck["slides"][i]
    layout = sl.get("layout", "content")
    cls = ["slide"]
    dark = is_dark(deck, sl)
    steppers = []
    if layout == "cover":
        cls.append("slide--cover")
        inner = cover(deck, sl)
    elif layout == "ending":
        cls.append("slide--cover slide--ending")
        inner = ending(deck, sl)
    else:
        if layout == "statement":
            cls.append("slide--statement")
        if sl.get("tone") == "wash":
            cls.append("slide--wash")
        if sl.get("valign") == "center":
            cls.append("slide--center")
        ctx["slide"] = i + 1
        body = "".join(render(b, ctx) for b in sl.get("body", []))
        steppers = [b if b["type"] == "stepper" else {"steps": b["beats"]}
                    for b in walk(sl.get("body", [])) if b["type"] in ("stepper", "animation")]
        inner = (f'<h2 class="slide-title">{md(sl["title"])}</h2>'
                 f'<div class="slide-body">{body}</div>{footer(deck, i, dark)}')
    notes = ""
    if sl.get("notes"):
        notes = '<template class="notes">' + "".join(f"<p>{md(x)}</p>" for x in sl["notes"]) + "</template>"
    hidden = "" if i == 0 else " inert"
    if steppers:
        hidden += f' data-steps="{len(steppers[0]["steps"]) - 1}" data-step="0"'
    return (f'<section class="{" ".join(cls)}{" is-current" if i == 0 else ""}" id="s{i + 1}" '
            f'data-id="{sl["id"]}"{' data-theme="dark"' if dark else ""} aria-label="{attr(sl["title"])}" aria-roledescription="slide"{hidden}>'
            f"{inner}{notes}</section>")


PAGE = """<!doctype html>
<html lang="{lang}" data-theme="light" data-motion="{motion}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="assets/tokens.css">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/base.css">
<link rel="stylesheet" href="assets/deck.css">
<script src="assets/deck.js" defer></script>
{scripts}</head>
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


SCRIPT_PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>대본 · {title}</title>
<link rel="stylesheet" href="assets/tokens.css">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/base.css">
<style>
body{{max-width:880px;margin:0 auto;padding:48px 24px 96px;font-size:20px;line-height:1.7;color:var(--color-text)}}
h1{{font-size:32px;line-height:1.3;color:var(--color-text-heading);margin-bottom:8px}}
.total{{color:var(--color-text-muted);margin-bottom:40px}}
.slide-script{{padding:28px 0;border-top:1px solid var(--color-border-subtle);break-inside:avoid}}
.slide-script h2{{font-size:24px;line-height:1.4;color:var(--color-text-heading);display:flex;gap:16px;align-items:baseline}}
.slide-script h2 .n{{font-variant-numeric:tabular-nums;color:var(--color-text-muted);min-width:2.5em}}
.slide-script h2 .t{{margin-left:auto;font-size:18px;font-weight:var(--weight-medium);color:var(--color-text-muted);font-variant-numeric:tabular-nums;white-space:nowrap}}
.msg{{margin:8px 0 12px;font-weight:var(--weight-bold);color:var(--color-text-heading)}}
.cue{{font-size:18px;color:var(--color-info-fg);background:var(--color-info-bg);border-radius:var(--radius-control);padding:8px 14px;margin:8px 0}}
.slide-script p{{margin:8px 0}}
.im svg{{display:inline-block;vertical-align:baseline}}
@media print{{body{{padding:0;font-size:12pt}}.cue{{border:1px solid var(--color-info-border)}}}}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="total">발표 대본 · {n}장 · 합계 {total}</p>
{body}
</body>
</html>
"""


def mmss(sec: int) -> str:
    return f"{sec // 60}:{sec % 60:02d}"


def script_html(deck) -> str:
    """The speaker script: one section per slide with its time, key sentence, interaction cues
    ([1], [2] … in the notes match the state keys) and the spoken text. Never shown on the stage."""
    parts, total = [], 0
    for i, sl in enumerate(deck["slides"], 1):
        t = int(sl.get("time", 0))
        total += t
        cues = []
        for b in walk(sl.get("body", [])):
            if b["type"] == "toggle":
                keys = " · ".join(f"[{k + 1}] {plain(s['label'])}" for k, s in enumerate(b["states"]))
                cues.append(f"토글: {keys}. 숫자 키로 상태를 고른다. 시작 상태 {plain(next(s['label'] for s in b['states'] if s['id'] == b['start']))}.")
            if b["type"] == "stepper":
                cues.append(f"단계 {len(b['steps'])}개: 다음 키가 단계를 먼저 넘긴다.")
            if b["type"] == "animation":
                beats = " · ".join(f"[{k}] {plain(x['title'])}" for k, x in enumerate(b["beats"]) if k)
                cues.append(f"애니메이션: 첫 그림에서 멈춘 채 열린다. 다음 키마다 한 구간 재생 — {beats}. "
                            "재생 중 다음 키는 그 구간을 끝내고, M은 모션을 끈다.")
        cue = "".join(f'<p class="cue">{html.escape(c)}</p>' for c in cues)
        notes = "".join(f"<p>{md(x)}</p>" for x in sl.get("notes", []))
        msg = f'<p class="msg">{md(sl["message"])}</p>' if sl.get("message") else ""
        parts.append(f'<section class="slide-script"><h2><span class="n">{i}</span>{md(sl["title"])}'
                     f'<span class="t">{mmss(t)} · 누적 {mmss(total)}</span></h2>{msg}{cue}{notes}</section>')
    return SCRIPT_PAGE.format(lang=deck["meta"].get("lang", "ko"), title=html.escape(deck["meta"]["title"]),
                              n=len(deck["slides"]), total=mmss(total), body="\n".join(parts))


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
    for st in (sys.stdout, sys.stderr):   # Korean paths and labels on a cp949 console
        try:
            st.reconfigure(encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass
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
    # motion plays by default: a presenter opens the file on a lab PC with OS animations off and
    # expects the deck's motion; meta.motion "auto" follows the OS, "off" never animates
    # animation scripts run after the engine (defer keeps document order): DeckAnim.define binds them
    anim_dir = out / "assets" / "anim"
    if anim_dir.exists():
        shutil.rmtree(anim_dir)
    tags = []
    for b in {b["name"]: b for b in ctx.get("scripts", [])}.values():
        anim_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(work / b["script"], anim_dir / f"{b['name']}.js")
        tags.append(f'<script src="assets/anim/{b["name"]}.js" defer></script>\n')
    page = PAGE.format(lang=deck["meta"].get("lang", "ko"), title=html.escape(deck["meta"]["title"]), slides=slides,
                       motion=deck["meta"].get("motion", "on"), scripts="".join(tags))
    (out / "index.html").write_text(page, encoding="utf-8")
    print(f"wrote {out / 'index.html'} ({len(deck['slides'])} slides)")
    if any(sl.get("notes") for sl in deck["slides"]):
        (out / "script.html").write_text(script_html(deck), encoding="utf-8")
        print(f"wrote {out / 'script.html'}")
    # the deliverable: one self-contained file at the top of the work folder
    import bundle_html
    bundle_html.main.__globals__["sys"].argv = ["bundle_html.py", str(work)]
    bundle_html.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
