/* overview_fk — best-of-n against FK steering on the same four particles, four stops.
   Storyboard (one event per beat; the slide opens still on beat 0):
   0  best-of-n (Fig. 1 middle): four particles leave x_T and are denoised to x_0 on their own; the
      one with the highest final reward is kept (the star). Grey = the baseline. The slide before
      (importance sampling, best-of-n) sets this up.
   1  Score at an intermediate step: the paths after that step step back, a bracket marks the step,
      and each particle gets a bar for its intermediate reward there (the bars leave in beat 3). (Fig. 1 right "Resample
      promising particles at intermediate steps"; Sec. 3.3)
   2  Resample: the two low particles are cut (red ×, their old paths leave), the highest one is
      copied twice. One change — the four slots refilled. (Fig. 1 right, Algorithm 1 "Resample")
   3  Propose: each surviving particle is denoised on its own again, so the copies part; the old
      best-of-n tails leave and the best x_0 is starred. (Algorithm 1 "Propose")
   No symbols beyond x_T, x_0 (G_t, τ, Eq. 5 come on the next slides), no results. Heights are
   illustrative. The SVG file draws beat 3; render(t) sets everything that moves from t alone. */
DeckAnim.define("overview-fk", function (svg, lib) {
  var R = lib.ramp, op = lib.fade;
  var K = ["p1", "p2", "p3", "p4"];
  var el = {};
  ["mark", "lab-score", "lab-res", "arcs", "star-old", "star-new", "copy0", "copy1", "x-p3", "x-p4",
   "tail-p1", "tail-p2", "tail-p3", "tail-p4", "head-p1", "head-p2", "head-p3", "head-p4",
   "bar-p1", "bar-p2", "bar-p3", "bar-p4", "br0", "br1", "br2", "br3", "bn0", "bn1", "bn2", "bn3"
  ].forEach(function (k) { el[k] = lib.node(k); });
  var br = [el.br0, el.br1, el.br2, el.br3], bn = [el.bn0, el.bn1, el.bn2, el.bn3], blen = [];
  for (var i = 0; i < 4; i++) { blen.push(br[i].getTotalLength()); }
  var barW = {};
  K.forEach(function (k) { barW[k] = parseFloat(el["bar-" + k].getAttribute("width")); });

  var SCORE = 1.2, RES = 2.4, END = 3.8;                    /* beat k plays from beats[k-1] to beats[k] */

  function render(t) {
    /* beat 1: the tails after the scored step step back, the step is marked, bars grow together */
    var back = R(t, 0, 0.4);
    var gone = R(t, RES, 0.4);                               /* beat 3: old tails leave */
    var cut = R(t, SCORE + 0.05, 0.35);                      /* beat 2: cut particles' tails leave */
    K.forEach(function (k) {
      var isCut = (k === "p3" || k === "p4");
      var o = (1 - 0.7 * back) * (isCut ? 1 - cut : 1 - gone);
      op(el["tail-" + k], o);
    });
    op(el["star-old"], (1 - 0.7 * back) * (1 - gone));
    op(el.mark, R(t, 0.3, 0.3));
    op(el["lab-score"], R(t, 0.3, 0.3) * (1 - R(t, SCORE, 0.2)));   /* beat 2: the label swaps in sequence */
    op(el["lab-res"], R(t, SCORE + 0.2, 0.2));
    var g = R(t, 0.55, 0.55);
    K.forEach(function (k) { el["bar-" + k].setAttribute("width", (barW[k] * g).toFixed(1)); });

    /* beat 2: cut the low two, copy the high one */
    var x = R(t, SCORE + 0.05, 0.3);
    op(el["x-p3"], x); op(el["x-p4"], x);
    var dim = R(t, SCORE + 0.15, 0.4);
    var barsOut = 1 - R(t, RES, 0.35);                      /* beat 3: the scores have been used */
    ["p3", "p4"].forEach(function (k) {
      op(el["head-" + k], 1 - 0.65 * dim);
      op(el["bar-" + k], g > 0 ? (1 - 0.65 * dim) * barsOut : 0);
    });
    ["p1", "p2"].forEach(function (k) { op(el["bar-" + k], g > 0 ? barsOut : 0); });
    var c = R(t, SCORE + 0.55, 0.5);
    [-34, 34].forEach(function (dy, j) {
      var e = el["copy" + j];
      op(e, c);
      e.setAttribute("transform", "translate(0," + (-dy * (1 - c)).toFixed(2) + ")");
    });

    op(el.arcs, R(t, SCORE + 0.85, 0.2));                  /* the links appear once the copies have settled */

    /* beat 3: each particle is denoised on its own again; the copies part */
    var d = R(t, RES + 0.2, 0.9);
    for (var i = 0; i < 4; i++) {
      var L = blen[i];
      lib.set(br[i], {"stroke-dasharray": L.toFixed(1) + " " + L.toFixed(1),
                      "stroke-dashoffset": (L * (1 - d)).toFixed(1)});
      op(br[i], d > 0 ? 1 : 0);
      op(bn[i], R(t, RES + 0.85, 0.3));
    }
    op(el["star-new"], R(t, END - 0.35, 0.3));
  }
  return {beats: [0, SCORE, RES, END], render: render};
});
