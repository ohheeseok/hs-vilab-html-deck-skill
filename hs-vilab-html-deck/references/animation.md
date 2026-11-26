# Animation — a diagram drawn as a function of time, paced by the clicker

What an HTML deck can do and a PowerPoint cannot do well: a diagram that **changes shape** while
the room watches — a latent that swells, a path that branches, a block that is swapped for another.
The method comes from a handover that analysed a paper project page's explainer animations (inline
SVG and plain JavaScript, no video, no library): **the picture is a function of time**, `render(t)`
draws time t from t alone. The deck adds one thing the web page did not need: **the presenter's
clicker sets the pace**.

Starter: `assets/templates/animation.svg` and `animation.anim.js`. Worked examples: `work/rae/figures/overview_latent.*` (SD-VAE latent → RAE latent, Fig. 2 redrawn)
and `overview_map.*` (reconstruction and generation on RAE, and where the four changes go);
`work/repa/figures/overview_repa.*` (vanilla SiT's 28 blocks; the encoder path joins, the bar splits
after block 8 and its output is aligned to the patch representation);
`work/self-flow-full/figures/overview_selfflow.*` (REPA-style alignment to an external encoder, the
encoder swapped for the model's own EMA copy, then the two inputs' noise levels part).

## When

- Before the first research section, 1–3 slides that show the paper's machinery as one picture that
  changes — an **overview**. The user asked for it on RAE; the critic's condition holds: an
  animation earns its slide when **a continuous change is the paper's mechanism** (a latent's shape,
  a pipeline being swapped, where a fix attaches). A table of contents, a list of methods or a
  results ladder is not one — those stay static or a stepper.
- It counts in the interaction budget (⌊N×0.2⌋, one signature); at most 3 per deck (gate).
- **Where, not how much.** An overview shows what changes and where; numbers that are the paper's
  results (gFID, rFID) wait for the result slides. Sizes from a figure (GFLOPs, token shapes) are fine.
- Adding 1–2 slides for the overview is fine (the user's call); take the time from other slides so
  the talk still fits. Replace a slide only when the animation says what it said. RAE: the
  two-beliefs slide (text only) became the first animation and the second was added; the
  related-work slide stayed (an animation cannot carry it).
- Place it after the slide whose subject it takes apart. Self-Flow: the overview removes the external
  encoder, so it follows the encoder-scaling slide (Fig. 2a); put before it, the next slide would
  go back to the encoder the picture just removed. Its first stop can then be that slide's setup.
- Mark a piece "training only" only where the paper says so. REPA's projector is (App. B); Self-Flow's
  EMA copy is not — it is the teacher **and** the evaluated model (App. A.3), so its line says
  "feature 정렬 loss" instead.

## How it plays

| | |
|---|---|
| entering the slide | still, on beat 0 (the presenter starts talking first) |
| next key | plays one beat (0.8–1.5 s; QA fails a beat over 2.0 s) and stops |
| next key while a beat plays | finishes that beat at once — it never skips the next one |
| previous key | jumps back one stop, no reverse play; during a beat, back to where it started |
| after the last beat | next key leaves the slide; coming back lands on the finished picture |
| `#/n/k` | beat k, drawn at once (reload, rehearsal) |
| overview (G), PDF `default` | the finished picture; PDF `expand` prints every stop |
| motion off (`?motion=0`, `meta.motion: "off"`, **M** key) | every beat is a jump |

The engine owns time, keys and text; the script only draws. No play bar, slider, hover, click on
the picture, IntersectionObserver, loop, iframe or OS reduced-motion check (the deck's `still()`
decides) — all of which the handover's web template had and a clicker deck must not.

## Files

```
figures/<name>.svg        the FINISHED picture (last beat): what prints, what the overview shows,
                          what stays if the script fails. Transient pieces (a flying patch, the
                          SD-VAE blocks that are swapped out) are drawn with opacity="0".
                          Elements that move carry data-anim="key". Text in <foreignObject> (.fo),
                          ≥ 24 px, never rotated.
figures/<name>.anim.js    DeckAnim.define("<name>", function (svg, lib) { … return {beats, render} })
```

```js
DeckAnim.define("overview-map", function (svg, lib) {
  var R = lib.ramp, row1 = lib.node("row1");          // node(key): the data-anim element, or an error
  var GEN = 0, FIX = 1.5, HEAD = 3.1, END = 4.3;      // beat k plays beats[k-1] → beats[k]
  function render(t) {                                // every moving attribute from t alone
    row1.setAttribute("opacity", (1 - 0.65 * R(t, GEN, 0.4) + 0.65 * R(t, HEAD + 0.8, 0.4)).toFixed(3));
  }
  return {beats: [0, FIX, HEAD, END], render: render};
});
```

`lib`: `clamp(v)`, `smooth(v)` (smoothstep), `ramp(t, from, dur)` (eased 0→1), `lerp(a, b, u)`,
`css("--token")` → [r, g, b], `mix(a, b, u)` → `rgb(…)`, `along(points)` → `u ↦ [x, y, angle]` at
constant speed, `set(el, attrs)`, `node(key)`, `fade(el, v)` — opacity, and `visibility="hidden"` at 0;
use it for every fade: text at opacity 0 still sits in the PDF's text layer (RAE run: the PDF check
found the swapped-out "SD-VAE 디코더" under "ViT 디코더"). In the SVG file, a piece drawn invisible gets
both `opacity="0" visibility="hidden"`. Read the DOM once in the factory (lengths, positions);
`render` writes attributes only.

Block (`block-vocabulary.md`): `type: "animation"`, `name`, `svg`, `script`, `beats: [{title,
text}]` (one per stop, beat 0 first — the side list), `side: "below" | "right"`, `cols`, `caption`,
`print`, `reveals`, `provenance`. `below` suits a pipeline across the slide (one column per beat
under it); `right` is the stepper's layout. In `notes`, `[1]`, `[2]` … mark where to press.

## Writing one

1. **Storyboard first, in prose**, numbered by beat, at the top of the script: what appears, moves,
   steps back; why in that order. Names come from the storyboard (`SWAP`, `ASK`, `HEAD`).
2. **Draw the finished picture** as the SVG. Redrawn from a paper figure: keep its blocks and labels,
   say so in the caption ("Fig. 2를 바탕으로 다시 그림").
3. **Beat 0 is a picture the presenter can talk over** (the baseline, the first path), not an empty
   stage. The last beat reads alone.
4. **Times are constants joined end to end**; every move inside a beat ends by that beat's stop
   (nothing moves after `beats[k]`, or a jump and a played beat end differently — QA compares them).
5. One event per beat. A cascade of one change (encoder, latent, decoder swapped left to right,
   0.2–0.5 s apart) is one event; two unrelated regions moving at once are two.
6. A piece that steps back keeps **opacity ≥ 0.25** (0.35 in RAE) — never the handover's 0.07,
   which vanishes on a projector; something that leaves goes to 0. Labels of a dimmed row stay full.
7. Two labels in one place swap **in sequence** (old out over the first half, new in over the
   second), never cross-faded on top of each other.
8. Lines ≥ 2.5 px (3 px used), colours from tokens with fixed meaning: grey = the baseline,
   sky blue = the paper's method, dark blue = structure, warm = a marker (never text).
9. No per-frame filters (`feTurbulence` seeds, blur): opacity, transform, width, dash offset.
10. From the RAE visual rounds: a stack that grows with a stagger reads as a funnel — grow it
    together; an arrowhead fades in when its line reaches it, not with the line; a line that a later
    piece will cover is drawn in pieces, so only the covered piece fades (one fading line next to a
    solid one shows a seam); a mark of size (a bar's length) gets a thin other side, or it reads as
    a dotted line; names swap inside their blocks, specs on the shared label line under them.

## Techniques (from the handover, in deck terms)

| effect | how |
|---|---|
| appear / settle in | `opacity = u`, `translate(0, -dy·(1−u))`, u = `ramp(t, from, dur)` |
| a shape becomes another | draw both; the old one leaves over the first half, the new one comes over the second |
| a bar grows / a block widens | interpolate `x`, `width` (RAE: token bars 8 → 384 px = 16 → 768 channels) |
| one piece flies to its place | interpolate `x, y, width, height` from the source box to the target box |
| a line draws itself | `stroke-dasharray = L L`, `stroke-dashoffset = L·(1−u)` (L = `getTotalLength()` once) |
| a colour changes | `mix(css("--hs-grey-40"), css("--color-accent"), u)` on `fill` |
| move along a path | `along([[x0,y0], …])(u)` → x, y, heading |
| zoom into a part | a group's `translate(…) scale(k)`, labels drawn at the arriving size (≥ 24 px there) |

## QA (`qa_render.py`, automatic)

Every stop is captured (`sNN-step<k>.png`) and measured like a slide; the middle of every beat too
(`sNN-beat<k>-mid.png`) — the room sees it. A beat over 2.0 s fails. Each stop is drawn twice, after
playing from 0 and after jumping back to it; a difference fails ("render(t) depends on what was drawn
before"). Text inside the SVG is not part of the collide check: look at the mid-beat captures for two
labels on top of each other. The build refuses a script that keeps its own clock, reads the OS,
listens for input, writes text or reaches the network, and a `node("key")` the SVG does not draw.
