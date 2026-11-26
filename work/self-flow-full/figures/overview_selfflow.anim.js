/* overview_selfflow — where Self-Flow gets its alignment target, four stops.
   Storyboard (one event per beat; the slide opens still on beat 0):
   0  REPA-style alignment, the baseline: a noise latent → flow model → velocity, and a frozen external
      encoder that turns a clean input into a representation target; a grey line takes the model's
      middle layer up to that target. (Sec. 1, Sec. 3.1 Eq. 3, Sec. 3.2)
   1  The external path leaves and the model's own EMA copy takes its place, the same depth as the
      student: its input is a noise latent too, the student is named, and the alignment line re-routes
      from the student's middle layer (l = 0.3D) to the teacher's deep layer (k = 0.7D). No "training
      only": the EMA copy is also the model they evaluate (App. A.3).
      (Sec. 3.4, Eq. 6, l < k; App. A.3)
   2  The inputs part: a quarter of the student's tokens get the other, higher noise level, and the
      teacher's label becomes "lower noise only" — every teacher token at min(t, s). A marker says the
      two noise levels differ. (Sec. 3.3 Eq. 4–5, Sec. 3.4, Fig. 3; R_M = 0.25 for images, App. A.3)
   3  The two questions the talk answers: ① over the teacher row, ② under the whole student and its output.
   No numbers (FID, 2.8×), and no "local correlations" or "infer the noisy tokens from the clean ones"
   (the authors' explanation, Sec. 3.3–3.4, is weighed on the probe and discussion slides). The picture
   shows the case where the second timestep is the higher one. The SVG file draws beat 3; render(t)
   sets everything that moves from t alone. */
DeckAnim.define("overview-selfflow", function (svg, lib) {
  var R = lib.ramp, L = lib.lerp;
  var el = {};
  ["q1", "q2", "lt0", "lt1", "lt2", "tc", "ext", "teacher", "lb0", "lb2", "sc-hi", "sc-ring", "sn0", "sn1",
   "sfront", "sdot", "l-tick", "k-tick", "ema", "ema-label", "gap", "stem", "run", "align-label"
  ].forEach(function (k) { el[k] = lib.node(k); });
  var RL = el.run.getTotalLength();
  el.run.setAttribute("stroke-dasharray", RL.toFixed(1) + " " + RL.toFixed(1));

  var B = 554, RUN = 262, TOP = 196;                       /* stem: layer l's dot up to the REPA target */
  var SUNK = lib.css("--color-surface-sunken"), CTRL = lib.css("--color-border-control");
  var BRAND = lib.css("--color-surface-brand"), INK = lib.css("--color-text");
  var MUTED = lib.css("--color-text-muted"), BLUE = lib.css("--color-accent");

  var SWAP = 0, PART = 1.5, ASK = 2.75, END = 3.75;        /* beat k plays from beats[k-1] to beats[k] */

  var op = lib.fade;                                       /* opacity; hidden at 0 */
  function drop(e, u, dy) {                                /* fade in while settling into place */
    op(e, u);
    e.setAttribute("transform", "translate(0," + (-dy * (1 - u)).toFixed(2) + ")");
  }

  function render(t) {
    /* beat 1: the external path leaves, the EMA teacher takes its place, the line re-routes */
    op(el.ext, 1 - R(t, SWAP, 0.3));
    var n = R(t, SWAP + 0.2, 0.3);                          /* the teacher's input: clean → noise latent */
    el.tc.setAttribute("fill", lib.mix(SUNK, CTRL, n));
    op(el.lt0, 1 - R(t, SWAP + 0.2, 0.15));
    op(el.lt1, R(t, SWAP + 0.35, 0.2) * (1 - R(t, PART + 0.15, 0.15)));
    op(el.teacher, R(t, SWAP + 0.25, 0.3));
    op(el.sn0, 1 - R(t, SWAP + 0.3, 0.15));
    op(el.sn1, R(t, SWAP + 0.45, 0.2));
    var s = R(t, SWAP + 0.35, 0.2);                         /* the stem lets go of the REPA target, turns blue */
    el.stem.setAttribute("d", "M" + B + " 355V" + L(TOP, RUN, s).toFixed(1));
    el.stem.setAttribute("stroke", lib.mix(MUTED, BLUE, s));
    lib.set(el.sfront, {fill: lib.mix(SUNK, BRAND, s), stroke: lib.mix(CTRL, BLUE, s)});
    el.sdot.setAttribute("fill", lib.mix(MUTED, BLUE, s));
    op(el["l-tick"], s);
    op(el.ema, R(t, SWAP + 0.45, 0.25));
    op(el["ema-label"], R(t, SWAP + 0.45, 0.25));
    var run = R(t, SWAP + 0.55, 0.4);                      /* then drawn on, from layer l over to layer k */
    op(el.run, run > 0 ? 1 : 0);
    el.run.setAttribute("stroke-dashoffset", (RL * (1 - run)).toFixed(1));
    op(el["k-tick"], R(t, SWAP + 0.9, 0.25));
    op(el["align-label"], R(t, SWAP + 0.95, 0.3));

    /* beat 2: a quarter of the student's tokens take the higher noise; the teacher keeps the lower */
    op(el.lb0, 1 - R(t, PART, 0.15));
    el["sc-hi"].setAttribute("fill", lib.mix(CTRL, INK, R(t, PART + 0.1, 0.4)));
    op(el["sc-ring"], R(t, PART + 0.3, 0.25));
    op(el.lb2, R(t, PART + 0.15, 0.2));
    op(el.lt2, R(t, PART + 0.3, 0.2));
    drop(el.gap, R(t, PART + 0.5, 0.3), 10);

    /* beat 3: the two questions settle in, each from outside toward the picture */
    drop(el.q1, R(t, ASK, 0.5), -4);                       /* ① rises: the viewBox's top edge is close */
    drop(el.q2, R(t, ASK + 0.25, 0.5), -8);                /* ② rises from below, clear of the bars */
  }

  return {beats: [0, PART, ASK, END], render: render};
});
