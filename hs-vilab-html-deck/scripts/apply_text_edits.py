#!/usr/bin/env python3
"""
apply_text_edits.py — apply the Korean editor's table to deck.json.

    python3 apply_text_edits.py deck.json review/korean.md            # dry run
    python3 apply_text_edits.py deck.json review/korean.md --write

The table is the one `narrative-roles.md` asks the Korean editor for:

    | location | original | edit | rule |
    | 9.body.0.items.2.text | <full original> | <full edit> | L1-5 |

`location` is the path `deck_text.py` printed (slide number, then keys and
list indices). An edit is applied only when the string found there equals
`original` (whitespace-normalised) — a stale or mistyped row is reported and
skipped, never guessed at. Every row whose numbers differ between original and
edit is refused: the editor may not change a number.

Adapted from hs-vilab-deck (same table contract).
"""
import argparse, json, re, sys
from pathlib import Path

NUM = re.compile(r"\d+(?:[.,]\d+)*")


def norm(t):
    return " ".join(str(t).split())


def rows(md):
    out = []
    for line in md.splitlines():
        if not line.startswith("|") or set(line.replace("|", "").strip()) <= set("-: "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() in ("location", "위치"):
            continue
        loc = cells[0].strip("`[] ")
        if not re.match(r"^\d+(\.[A-Za-z0-9_]+)+$", loc):
            continue
        out.append((loc, cells[1].strip("` "), cells[2].strip("` ")))
    return out


def resolve(deck, loc):
    parts = loc.split(".")
    node = deck["slides"][int(parts[0]) - 1]
    for k in parts[1:-1]:
        node = node[int(k)] if isinstance(node, list) else node[k]
    last = parts[-1]
    return node, (int(last) if isinstance(node, list) else last)


def main():
    for st in (sys.stdout, sys.stderr):
        try: st.reconfigure(encoding="utf-8")
        except Exception: pass  # noqa: BLE001
    ap = argparse.ArgumentParser()
    ap.add_argument("deck"); ap.add_argument("table")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    deck = json.loads(Path(a.deck).read_text(encoding="utf-8"))
    done = skipped = 0
    for loc, orig, edit in rows(Path(a.table).read_text(encoding="utf-8")):
        try:
            node, key = resolve(deck, loc)
            cur = node[key]
        except (KeyError, IndexError, ValueError, TypeError):
            print(f"  skip  {loc}: no such location"); skipped += 1; continue
        if norm(cur) != norm(orig):
            print(f"  skip  {loc}: text there no longer matches the table's original"); skipped += 1; continue
        if sorted(NUM.findall(orig)) != sorted(NUM.findall(edit)):
            print(f"  REFUSE {loc}: the edit changes a number"); skipped += 1; continue
        node[key] = edit
        done += 1
    print(f"{done} edit(s) applicable, {skipped} skipped")
    if a.write and done:
        Path(a.deck).write_text(json.dumps(deck, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
        print(f"wrote {a.deck}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
