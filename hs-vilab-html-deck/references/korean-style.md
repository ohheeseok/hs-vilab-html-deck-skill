# Korean editor — the anti-slop pass on deck.json

The editor is codex given the rules of the `heeseok-korean-anti-slop` skill as files, or a
subagent that has that skill. It never sees the paper; it edits prose and returns a table, and the
conductor applies it mechanically.

```bash
python $S/scripts/deck_text.py $W/deck.json -o $W/review/deck_text.md      # one line per string: [location] text
python <anti-slop>/scripts/scan_slop.py $W/review/deck_text.md > $W/review/kref/scan.txt
# kref/ = deck_text.md + scan.txt + the anti-slop SKILL.md and references/
python $S/scripts/delegate.py text --prompt-file $W/review/kref/prompt.md --dir $W/review/kref --out $W/review/korean.md
python $S/scripts/apply_text_edits.py $W/deck.json $W/review/korean.md           # dry run
python $S/scripts/apply_text_edits.py $W/deck.json $W/review/korean.md --write
```

## The prompt (`kref/prompt.md`)

- Lines whose location is `notes` are the spoken script: 합쇼체, spoken. Everything else (title,
  message, body, caption, alt) is on-screen copy: 개조식·명사형 or a short -다 sentence. Keep each
  register.
- Fix translationese, metaphor and aphorism, compressed declarations, meta sentences, over-
  justification. Scanner hits are candidates, not orders (a comma after a connective ending is
  usually fine).
- One term per concept across the deck. For a generative-model paper: loss, 층, noise, timestep,
  teacher, student, encoder, feature — English technical terms stay English.
- **Never change**: numbers, model and dataset names, technical terms, `$…$` math, `**…**`, hedges
  and attributions ("저자 설명", "해석", "약"), or what a sentence claims.
- Do not list lines that need no change. Do not force edits.
- Output one table `| location | original | edit | rule |` — location exactly as printed,
  original and edit as **whole** strings, no `|` inside cells — then the scanner hits kept and why.

`apply_text_edits.py` applies a row only when the text at that location still equals `original`,
and refuses any row whose numbers differ. After applying, the verifier reads `deck.json` again.

## On-screen copy, in short

- Titles introduce (`토큰별 noise 배치 네 방식`), they do not conclude.
- Bullets are phrases or short -다 sentences, one idea each, 1–2 lines at the column width.
- Captions start with `**Fig. n**` / `**Table n**` and a space, then the conditions.
- Mark the deck author's reading with `note` or `"note": true` (해석), the authors' own explanation
  with "저자 설명", external facts with their source.
