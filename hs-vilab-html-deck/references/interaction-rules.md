# Interaction rules — what an HTML deck may do that a PPT cannot, and the restraint it needs

The deck is presented with a clicker. An interaction is worth its slide only when operating it
**reveals something about the paper** that a static slide shows worse: the same figure under two
or more conditions, an ordered procedure whose steps matter, or a diagram whose change of shape is
the paper's mechanism (`animation`).

## Budget (build gates)

- Interactive slides ≤ ⌊slides × 0.2⌋ — toggles, steppers and animations together; one interaction
  per slide. At most **one** `signature: true` (the deck's representative interaction). Zero is
  allowed. At most 3 animations.
- Every interactive block has `reveals` (one sentence: what operating it shows about the paper),
  `start` (the state the slide opens in), `print` (`expand` = every state gets a PDF page, `default`
  = only the start state), and `provenance` per state.
- One automatic motion per slide (the engine's): slide cross-fade 180ms, bars grow 280ms, a focus
  row tints 180ms, toggle states fade 180ms. A second key press finishes a running motion at once.
  Motion plays by default, even when the OS asks for reduced motion (lab and lecture-room PCs often
  have Windows animation effects off): `meta.motion` is `on` unless set to `auto` (follow the OS) or
  `off`. In the address, `?motion=0` turns it off (QA, PDF, slow laptops), `?motion=1` on,
  `?motion=auto` follows the OS; the address wins over `meta.motion`.

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
Use for an algorithm or a training procedure whose order is the point. `print: "expand"` gives every
step a PDF page (6a–6e); `"default"` prints the last step. A step may also take things away (REPA run:
the last step greys out the training path to show what inference keeps) — then print `expand`, or
the handout shows only that last view. QA captures every step (`sNN-step<k>.png`).

## animation

A diagram drawn as a function of time (`render(t)`), one beat per next key: the slide opens still
on beat 0, each key plays one beat (≤ 2.0 s) and stops, a key during a beat finishes it, previous
jumps back, **M** turns motion off on the spot. For an overview before the research sections (1–3
slides) or a mechanism whose change of shape is the point. Everything else — writing one, the
library, the design rules, QA — is in `animation.md`.

RAE run: two overview animations replaced the text-only "two beliefs" slide — SD-VAE's latent
becoming RAE's (Fig. 2 redrawn; the tokens stretch 48×, their count stays 256), then the
reconstruction and generation paths on RAE with the four changes placed where they act. Rejected in
the same discussion: a "map" of which slides cover what (a table of contents — the progress bar
does it) and putting gFID numbers in the overview (they belong to the ladder slide).

REPA run: one overview, added before the diagnosis slides (22 slides, 4 interactions =
⌊22×0.2⌋) — vanilla SiT as one bar of 28 blocks, the clean image's DINOv2 path and the input
mismatch, the bar splitting after block 8 with the alignment line rising from it, two questions. One
slide, because the method adds one regularization term: a second animation would have pushed the
interactions to 5 or cost a working figure toggle. Left out: the authors' hypothesis that the later
layers learn details (Sec. 4.2 "we hypothesize"; the discussion slide questions it) and the
stepper's MLP, patch matching and inference. The method stepper after it now opens on both paths
instead of rebuilding them.

Self-Flow run: one overview, added after the encoder-scaling slide (22 slides, 4 interactions) —
REPA-style alignment to a frozen external encoder, the encoder swapped for the model's own EMA
teacher (same depth; the line re-routes from 0.3D to the teacher's 0.7D), the student's tokens
taking two noise levels while the teacher's keep the lower one, two questions. Rejected: a token
grid (the noise-placement toggle and the next two slides already use one) and a map of the three
modalities (a table of contents that would also hide their different autoencoders and mask ratios).
Left out: the authors' "local correlations" explanation, which the probe and discussion slides weigh.

Integral run, the first deck planned with the overview from the start (the brief asks codex for its
slot and beats; 21 slides, 3 interactions of 4): the overview at the end of the background section
(a separate VAE latent and a per-layer generation expert → the shared token z → links at every fourth
layer → two questions), a two-state image toggle for knowledge generation and editing, and the
signature, a four-state toggle over the paper's controlled comparisons (Fig. 6a, 6b, 10a, 7: one
axis, 10K–50K steps and GenEval from 0), each state saying what changed and which explanation it
aims at. Rejected: the draft's overview, an empty stage that added one arrow per press (a stepper
dressed as an animation), and a static slide per comparison (five slides of one curve each).
Image tabs of different aspects were padded to one with the figure's own background colour.

## Not used

Sliders, hover-only content (a projector has no hover), animation that plays by itself (on entering
the slide, in a loop, advancing to the next slide), video autoplay, anything that needs the network.
