# Interaction rules — what an HTML deck may do that a PPT cannot, and the restraint it needs

The deck is presented with a clicker. An interaction is worth its slide only when operating it
**reveals something about the paper** that a static slide shows worse: the same figure under two
or more conditions, or an ordered procedure whose steps matter.

## Budget (build gates)

- Interactive slides ≤ ⌊slides × 0.2⌋. At most **one** `signature: true` (the deck's representative
  interaction). Zero is allowed.
- Every interactive block has `reveals` (one sentence: what operating it shows about the paper),
  `start` (the state the slide opens in), `print` (`expand` = every state gets a PDF page, `default`
  = only the start state), and `provenance` per state.
- One automatic motion per slide (the engine's): slide cross-fade 180ms, bars grow 280ms, a focus
  row tints 180ms, toggle states fade 180ms. A second key press finishes a running motion at once.
  `?motion=0` turns motion off (QA, slow laptops); `?motion=1` keeps it on even when the OS asks
  for reduced motion.

## toggle

Two to four states of **one** visual — a redrawn diagram (`svg` whose elements carry
`data-show="state ids"`) or one paper figure per state (`src` on each state: image tabs).

- Buttons: `[n] label`; number keys 1–9 choose a state; ← → move between buttons while one has
  keyboard focus. A mouse click releases focus so the clicker keeps driving the deck.
- The readout beside the visual (`title`, `text`, optional `equation`, `symbols`) is the state's
  claim in words, announced through `aria-live`. Stacked in one grid cell, so the panel keeps the
  tallest state's height and nothing below it moves when the state changes.
- `side`: extra blocks under the readout (e.g. the paper's result figure for all states).
- Four or more states compact the buttons; labels must still fit one line (QA spill check).
- The script marks where to press: `[1] …`, `[2] …` in `notes`.

Good uses in the Self-Flow run: four noise schedulers on one token grid with Fig. 2(b) beside it
(signature); qualitative figures one at a time at full width (a projector cannot read three strips
side by side); Fig. 6 with the x-axis switched between steps and FLOPs.

Rejected in the same run: a weight switcher over Table 6 — a 5-row Δ table read better static.
A stepper that only re-told the next slide's figure — the critic caught that it revealed nothing.

## stepper

The next key spends the steps first, then leaves the slide; previous walks back. URL `#/n/k`.
Elements in the SVG carry `data-from-step="k"`; the side list shows step `k` from step `k` on.
Use for an algorithm or a training procedure whose order is the point. Prints fully revealed.

## Not used

Sliders, hover-only content (a projector has no hover), auto-advancing animation, video autoplay,
anything that needs the network.
