#!/usr/bin/env python3
"""
deck_text.py — every piece of copy in a deck.json, one line each, with where
it lives, so a Korean prose pass can read the deck as text.

    python3 deck_text.py deck.json -o deck_text.md            # slides + script
    python3 deck_text.py deck.json -o slides.md --slides-only

Each line is `[<slide>.<path>] <text>`: `[7.title]`, `[7.body.1.items.2.text]`,
`[7.notes.0]`. The path is what the conductor needs to find the string
again in deck.json (or in the script that builds it). Numbers, file names,
provenance and cites are left out — they are not prose and must not change.

Adapted from hs-vilab-deck for the HTML deck schema: `groups`, `side` and table
`cells` hold prose here, so they are walked; layout and data keys are skipped.
"""
import argparse, json, re, sys
from pathlib import Path

SKIP_KEYS = {"id", "type", "layout", "section", "src", "svg", "cols", "columns_n", "start", "print",
             "signature", "pair", "dir", "metric", "better", "marks", "tags", "slug", "time", "focus",
             "numbered", "divider", "panel", "direction", "size", "height", "value", "provenance",
             "cite", "figures", "sections", "team", "url", "statementTheme", "lang", "titleLang",
             "target_minutes", "target_slides", "x", "y", "align", "tone"}
HANGUL = re.compile(r"[가-힣]")


def walk(o, path, out, need_hangul):
    if isinstance(o, str):
        t = o.strip()
        if t and (not need_hangul or HANGUL.search(t)):
            out.append((path, " ".join(t.split())))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}.{i}", out, need_hangul)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in SKIP_KEYS:
                walk(v, f"{path}.{k}", out, need_hangul)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--slides-only", action="store_true", help="leave out speaker notes")
    ap.add_argument("--all", action="store_true",
                    help="include strings with no Hangul (English labels, captions)")
    a = ap.parse_args()
    deck = json.loads(Path(a.deck).read_text(encoding="utf-8"))
    lines = [f"# Deck text — {deck.get('meta', {}).get('title', '')}", ""]
    n = 0
    for i, sl in enumerate(deck["slides"], 1):
        part = {k: v for k, v in sl.items() if not (a.slides_only and k == "notes")}
        out = []
        walk(part, str(i), out, need_hangul=not a.all)
        if not out:
            continue
        lines.append(f"## Slide {i} — {sl.get('title', '')}")
        for path, t in out:
            lines.append(f"[{path}] {t}")
            n += 1
        lines.append("")
    Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {a.out} — {n} strings from {len(deck['slides'])} slides")


if __name__ == "__main__":
    sys.exit(main())
