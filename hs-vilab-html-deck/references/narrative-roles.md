# Narrative roles — who writes, who checks

A draft checked by its author passes the checks its author already had in mind. Stage [1] is a
small team: one author, reviewers who did not write it and do not see each other's findings, and
the current AI as conductor. (Adapted from hs-vilab-deck; the delegates differ.)

| role | does | reads | writes | filled by |
|---|---|---|---|---|
| **Author** | outline, then one revision | `brief.md` (paper inline) | `outline.md`, `outline_v2.md` | **codex** (`delegate.py text`) |
| **Critic** | structure and craft: does this become a good talk for this room? | `outline.md`, `references/narrative-rules.md`, paper | `review/critic.md` | **agy** (`delegate.py review`) |
| **Verifier** | truth: every claim, number, figure reference, condition — in the paper, where it says | `outline.md` then `deck.json`, `paper.pdf` | `review/verify.md`, `review/verify2.md` | **agy**, a separate call blind to the critic |
| **Researcher** | what the paper cannot say: follow-up work, claims about other papers, code release | `questions` drawn from the draft | `review/research.md` | **agy** with web |
| **Korean editor** | Korean prose after synthesis (anti-slop) | `review/deck_text.md` + the anti-slop rules | `review/korean.md` (table) | **codex** with the `heeseok-korean-anti-slop` rules, or a subagent with that skill |
| **Visual reviewer** | what only the eye sees on the captures | `qa/` + rules | `review/visual*.md` | **agy** |
| **Conductor** | dispatches, answers every finding, synthesises `deck.json`, builds, fixes | all | `review/log.md`, `deck.json` | the current AI |

A missing CLI: `delegate.py` falls back to the other one, and with neither installed the role runs
as a subagent with only that role's inputs. Name every fallback in the delivery.

## The loop

1. **Draft** — codex writes `outline.md` from `brief.md` (`handoff-narrative.md`).
2. **Review, in parallel and blind** — critic and verifier get the draft and the paper, not each
   other. The researcher runs alongside on 3–6 specific questions taken from the draft.
3. **Check the research at its source.** Open every external fact you mean to use on its page and
   write `review/research_verified.md`: the fact, the URL, what disagreed. Only that file feeds a
   slide; mark it `external` on the slide and in the script.
   *Self-Flow run*: agy reported a conference acceptance that the arXiv page does not carry and a
   baseline FID not on the abstract page — both dropped. Its follow-up paper was real and became
   a discussion point.
4. **Answer every finding** in `review/log.md`: accepted, partly, rejected — and why. Put the
   target structure (slide list) at the end of the log.
5. **Revise once** — codex gets: the brief's task and constraints, `# Revision` ("apply every
   accepted finding; list what you did not apply under `## Not applied` with the reason"), its own
   draft, the log, the critic's and verifier's full text, the verified research, the paper.
6. **Gate** (SKILL.md 1b) the revision, then **synthesise** `deck.json` yourself.
7. **Korean editor** → apply its table with `apply_text_edits.py` (a row that changes a number is
   refused).
8. **Verifier again, on `deck.json`** — synthesis and editing are where a number or a claim drifts.
9. Build, QA, **visual reviewer**, fix, repeat once (round 2 checks round 1's fixes and the new
   regressions they caused).

## What each reviewer is told

Each prompt names the folder it may read and says "do not create or edit files; print the result".
Ask for numbered findings with severity (`must` / `should`), the slide, and the paper location.

**Critic** — not the author; judge the talk for this room: titles introduce rather than conclude;
one message per slide; TL;DR second; a seminar ends on discussion points found in the paper
(inconsistencies between sections, unmeasured claims, a metric both tuned on and reported, a
missing ablation); the leading thread carries the middle; method slides carry the paper's concrete
facts; no two slides say the same thing; time per slide; block choice and legibility at 1024×768;
whether each interaction reveals more than a static slide; what a strong deck would have that this
one lacks.

**Verifier** — not the author; every claim, number, comparison and causal link, with page and
location; recompute every Δ; flag numbers without their condition (benchmark, setting, model size,
step, CFG) and results stated more generally than the paper states them; check the figure ledger
covers every main-body figure and table. *Self-Flow run*: it caught a robotics task where the
baseline actually led at 100K, written as a win.

**A finding that rests on reading a curve is checked by you, on the figure, zoomed.** In the
Self-Flow run the first verifier said a linear probe reversed in late layers and the second said
it reversed at two layers; the figure, enlarged, showed Self-Flow above at every layer. The slide
had already been written from the first claim. When two reviewers disagree, or a claim says a
result "reverses", crop the figure and look before you write.

**Korean editor** — see `korean-style.md`.

**Visual reviewer** — see `qa-checklist.md` § visual.
