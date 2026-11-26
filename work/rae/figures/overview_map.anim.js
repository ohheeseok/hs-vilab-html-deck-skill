/* overview_map — the two paths on RAE and where the high-dimensional fixes go, four stops.
   Storyboard (one event per beat; the slide opens still on beat 0):
   0  ① Reconstruction alone: input image → frozen encoder → representation tokens → ViT decoder →
      reconstructed image. (Sec. 3)
   1  ② Generation draws in under it, left to right: noise → DiT → generated tokens → the same ViT
      decoder → generated image. The reconstruction row steps back (lines and fills, not labels).
      (Sec. 4)
   2  The three things that change in high dimension light up where they act, one after another:
      the DiT's width (Sec. 4.1), the noise schedule shift (Sec. 4.2), noise augmentation in the
      decoder's training (Sec. 4.3).
   3  DiT^DH: a shallow, wide head drops in after the DiT and also takes the noisy input
      (Sec. 5, Fig. 5); the reconstruction row comes back — the finished map.
   The SVG file draws beat 3; render(t) sets everything that moves from t alone. */
DeckAnim.define("overview-map", function (svg, lib) {
  var R = lib.ramp;
  var el = {};
  ["row1", "r2-0", "r2-1", "r2-2", "r2-3", "r2-4", "r2-5", "tag2", "m-width", "m-shift", "m-noise",
   "head", "mid", "xt", "xt-arrow", "xt-label", "dec", "dec-label", "head-tip"].forEach(function (k) { el[k] = lib.node(k); });
  var XT = el.xt.getTotalLength();
  el.xt.setAttribute("stroke-dasharray", XT.toFixed(1) + " " + XT.toFixed(1));

  var GEN = 0, FIX = 1.5, HEAD = 3.1, END = 4.3;           /* beat k plays from beats[k-1] to beats[k] */
  var BACK = 0.5;                                            /* a row that steps back stays readable */

  var op = lib.fade;                                       /* opacity; hidden at 0 */
  function drop(e, u, dy) {                                /* fade in while settling into place */
    op(e, u);
    e.setAttribute("transform", "translate(0," + (-dy * (1 - u)).toFixed(2) + ")");
  }

  function render(t) {
    /* beat 1 */
    op(el.row1, 1 - (1 - BACK) * R(t, GEN, 0.4) + (1 - BACK) * R(t, HEAD + 0.8, 0.4));
    for (var i = 0; i <= 5; i++) op(el["r2-" + i], R(t, GEN + 0.2 + 0.2 * i, 0.3));
    op(el.tag2, R(t, GEN + 1.2, 0.3));
    /* the decoder both rows share grows down from the reconstruction row before ② reaches it */
    var h = lib.lerp(120, 360, R(t, GEN + 0.6, 0.5)).toFixed(1);
    el.dec.setAttribute("height", h);
    el["dec-label"].setAttribute("height", h);
    /* the arrow from the DiT runs straight through until the head takes its middle */
    op(el.mid, R(t, GEN + 0.8, 0.3) * (1 - R(t, HEAD, 0.3)));

    /* beat 2: width, schedule shift, decoder noise augmentation */
    drop(el["m-width"], R(t, FIX, 0.45), 8);
    drop(el["m-shift"], R(t, FIX + 0.5, 0.45), 8);
    drop(el["m-noise"], R(t, FIX + 1.0, 0.5), 8);

    /* beat 3: the DDT head, and the noisy input it also reads */
    drop(el.head, R(t, HEAD, 0.5), 14);
    op(el["head-tip"], R(t, HEAD + 0.15, 0.3));   /* in place, not dropping with the head */
    var draw = R(t, HEAD + 0.4, 0.5);
    op(el.xt, R(t, HEAD + 0.4, 0.05));
    el.xt.setAttribute("stroke-dashoffset", (XT * (1 - draw)).toFixed(1));
    op(el["xt-arrow"], R(t, HEAD + 0.85, 0.1));
    op(el["xt-label"], R(t, HEAD + 0.6, 0.3));
  }

  return {beats: [0, FIX, HEAD, END], render: render};
});
