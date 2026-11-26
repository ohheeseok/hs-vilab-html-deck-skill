/* overview_repa — what REPA adds to SiT training, four stops.
   Storyboard (one event per beat; the slide opens still on beat 0):
   0  Vanilla SiT, raised to the middle of the empty diagram: a noisy latent → SiT-XL/2, one grey
      bar of 28 blocks → velocity. The note above says the representation is learned by denoising
      alone. (Sec. 1, Sec. 3.1)
   1  The SiT row steps down to make room and, as it lands, the encoder path draws in above, left to right: the
      same image, clean → frozen DINOv2-B → patch representation; a marker shows the two inputs
      differ. (Sec. 1 "input mismatch", Sec. 3.3)
   2  The bar splits after block 8 — blocks 1–8 and 9–28 (v = g∘f, Sec. 3.1), joined by a short
      link — and a line rises from block 8's output to the patch representation: the alignment,
      training only. (Sec. 3.3, Fig. 1; XL/2 aligns block 8, Table 7)
   3  The two questions the talk answers: ① over the encoder path, ② under the later blocks.
   No numbers (FID, speed-up) and no "later layers learn details" (the authors' hypothesis, Sec. 4.2,
   is a question on the discussion slide). The SVG file draws beat 3; render(t) sets everything
   that moves from t alone. */
DeckAnim.define("overview-repa", function (svg, lib) {
  var R = lib.ramp, L = lib.lerp;
  var el = {};
  ["q1", "q2", "top-img", "top-a1", "enc", "top-a2", "tgt", "gap", "sit-row", "whole", "front", "back",
   "front-ticks", "back-ticks", "front-label", "back-label", "sit-name", "link", "vanilla-note",
   "align", "align-dot", "align-label"].forEach(function (k) { el[k] = lib.node(k); });
  var AL = el.align.getTotalLength();
  el.align.setAttribute("stroke-dasharray", AL.toFixed(1) + " " + AL.toFixed(1));

  var X0 = 200, X1 = 1380, B8 = 537.1, GAP = 20;           /* block 8 ends at 200 + 8·1180/28 */
  var RAISE = 125;                                         /* beat 0: the SiT row sits mid-diagram */
  var SUNK = lib.css("--color-surface-sunken"), CTRL = lib.css("--color-border-control");
  var BRAND = lib.css("--color-surface-brand"), BLUE = lib.css("--color-accent");
  var NAVY = lib.css("--color-text-heading");

  var ENC = 0, SPLIT = 1.35, ASK = 2.8, END = 3.8;        /* beat k plays from beats[k-1] to beats[k] */

  var op = lib.fade;                                       /* opacity; hidden at 0 */
  function drop(e, u, dy) {                                /* fade in while settling into place */
    op(e, u);
    e.setAttribute("transform", "translate(0," + (-dy * (1 - u)).toFixed(2) + ")");
  }

  function render(t) {
    /* beat 1: the SiT row steps down, then the encoder path draws in, then the input marker */
    var down = R(t, ENC, 0.35);
    el["sit-row"].setAttribute("transform", "translate(0," + (-RAISE * (1 - down)).toFixed(2) + ")");
    op(el["top-img"], R(t, ENC + 0.15, 0.3));             /* overlaps the row's last stretch down */
    op(el["top-a1"], R(t, ENC + 0.35, 0.25));
    op(el.enc, R(t, ENC + 0.45, 0.3));
    op(el["top-a2"], R(t, ENC + 0.7, 0.2));
    op(el.tgt, R(t, ENC + 0.8, 0.3));
    drop(el.gap, R(t, ENC + 1.0, 0.3), 10);

    /* beat 2: the vanilla note leaves; the one bar becomes two parts; the alignment line rises */
    op(el["vanilla-note"], 1 - R(t, SPLIT, 0.3));
    var hand = R(t, SPLIT + 0.2, 0.25);                     /* the whole bar hands over to its two parts */
    op(el.whole, 1 - hand);
    op(el.front, hand);
    op(el.back, hand);
    op(el["sit-name"], hand);
    var u = R(t, SPLIT + 0.4, 0.5);
    lib.set(el.front, {width: L(B8 - X0, B8 - X0 - GAP, u).toFixed(1),
                       fill: lib.mix(SUNK, BRAND, u), stroke: lib.mix(CTRL, BLUE, u)});
    lib.set(el.back, {x: L(B8, B8 + GAP, u).toFixed(1), width: L(X1 - B8, X1 - B8 - GAP, u).toFixed(1),
                      fill: lib.mix(SUNK, NAVY, u), stroke: lib.mix(CTRL, NAVY, u)});
    op(el["front-ticks"], 0.55 * u);
    op(el["back-ticks"], 0.45 * u);
    op(el["front-label"], R(t, SPLIT + 0.55, 0.3));
    op(el["back-label"], R(t, SPLIT + 0.55, 0.3));
    op(el.link, R(t, SPLIT + 0.8, 0.2));
    op(el["align-dot"], R(t, SPLIT + 0.8, 0.2));
    var rise = R(t, SPLIT + 0.85, 0.4);                    /* drawn from block 8 up to the target */
    op(el.align, rise > 0 ? 1 : 0);
    el.align.setAttribute("stroke-dashoffset", (AL * (1 - rise)).toFixed(1));
    op(el["align-label"], R(t, SPLIT + 1.1, 0.3));

    /* beat 3: the two questions settle in */
    drop(el.q1, R(t, ASK, 0.5), -4);                       /* ① rises: the viewBox's top edge is close */
    drop(el.q2, R(t, ASK + 0.25, 0.5), 10);
  }

  return {beats: [0, SPLIT, ASK, END], render: render};
});
