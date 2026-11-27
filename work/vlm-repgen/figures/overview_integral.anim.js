/* overview_integral — how Integral attaches generation to a pretrained VLM, four stops.
   Storyboard (one event per beat; the slide opens still on beat 0):
   0  The design the paper sets itself against (Sec. 1, Sec. 3.2: BAGEL pairs a generation expert with
      the VLM and generates in a separate FLUX.1-VAE latent): the frozen vision encoder's last layer
      feeds the VLM; generation runs in a VAE latent, through an expert at every VLM layer, out of the
      VAE's decoder. Grey = the baseline.
   1  The representation is shared: every depth of the frozen encoder fans into Abstraction Fusion,
      which makes the visual token z; z (through the semantic projector) is now the VLM's visual
      input, and the generation latent becomes z_t in z's space, decoded by a pixel decoder.
      One change, cascaded left to right. (Sec. 2.2, Eq. 1–2, Fig. 4; Sec. 2.3)
   2  The generation stream is thinned: of the 32 VLM layers it reads keys and values at every
      fourth, 8 places (Block-wise MoT). (Sec. 2.3, Eq. 4, Fig. 5b; App. A.1)
   3  The two questions the analysis section answers: ① over the shared path, ② under generation.
   No numbers (GenEval, PSNR, 0.89B) and no propagation bottleneck (a hypothesis, Sec. 2.1 — the next
   slide weighs it). The SVG file draws beat 3; render(t) sets everything that moves from t alone. */
DeckAnim.define("overview-integral", function (svg, lib) {
  var R = lib.ramp;
  var el = {};
  ["q1", "q2", "b0-top", "fan", "af", "af-z", "zc", "z-out", "in", "in-head", "lk-x", "lk-b", "kv0", "kv1",
   "gc", "gc0", "gc1", "same", "gbar", "gn0", "gn1", "dec", "dn0", "dn1"
  ].forEach(function (k) { el[k] = lib.node(k); });

  var SUNK = lib.css("--color-surface-sunken"), CTRL = lib.css("--color-border-control");
  var BRAND = lib.css("--color-surface-brand"), BLUE = lib.css("--color-accent");
  var MUTED = lib.css("--color-text-muted");

  var AF = 1.6, MOT = 3.0, END = 4.0;                       /* beat k plays from beats[k-1] to beats[k] */
  var op = lib.fade;
  function drop(e, u, dy) {                                  /* fade in while settling into place */
    op(e, u);
    e.setAttribute("transform", "translate(0," + (-dy * (1 - u)).toFixed(2) + ")");
  }
  function box(e, u) {                                       /* grey baseline box → the method's sky blue */
    lib.set(e, {fill: lib.mix(SUNK, BRAND, u), stroke: lib.mix(CTRL, BLUE, u)});
  }

  function render(t) {
    /* beat 1: the shared token z, from the encoder's every depth to both paths */
    op(el["b0-top"], 1 - R(t, 0, 0.25));                     /* the last-layer-only path leaves */
    op(el.fan, R(t, 0.2, 0.3));                              /* all depths at once, not a funnel */
    drop(el.af, R(t, 0.35, 0.3), 8);
    op(el["af-z"], R(t, 0.55, 0.2));
    drop(el.zc, R(t, 0.6, 0.25), 8);
    op(el["z-out"], R(t, 0.7, 0.25));                       /* with the shared piece, so the corner joins */
    var c = R(t, 0.7, 0.25);                                 /* the shared piece into the VLM turns blue */
    el.in.setAttribute("stroke", lib.mix(MUTED, BLUE, c));
    el["in-head"].setAttribute("stroke", lib.mix(MUTED, BLUE, c));
    var g = R(t, 0.9, 0.3);                                  /* the generation latent: VAE latent → z_t */
    lib.set(el.gc, {fill: lib.mix(SUNK, BLUE, g), stroke: lib.mix(CTRL, BLUE, g)});
    op(el.gc0, 1 - R(t, 0.85, 0.15));
    op(el.gc1, R(t, 1.05, 0.15));
    op(el.same, R(t, 1.15, 0.3));
    box(el.dec, R(t, 1.2, 0.3));                             /* and its decoder: the VAE's → pixel decoder */
    op(el.dn0, 1 - R(t, 1.2, 0.15));
    op(el.dn1, R(t, 1.38, 0.17));

    /* beat 2: Block-wise MoT — every layer → every fourth layer */
    op(el["lk-x"], 1 - R(t, AF, 0.4));
    var b = R(t, AF + 0.3, 0.3);
    lib.set(el["lk-b"], {stroke: lib.mix(MUTED, BLUE, b), "stroke-width": (3 + 2 * b).toFixed(2)});
    box(el.gbar, R(t, AF + 0.4, 0.3));
    op(el.gn0, 1 - R(t, AF + 0.45, 0.15));
    op(el.gn1, R(t, AF + 0.6, 0.18));
    op(el.kv0, 1 - R(t, AF + 0.25, 0.15));                  /* the label changes as the links do */
    op(el.kv1, R(t, AF + 0.42, 0.18));

    /* beat 3: the two questions settle in, from outside toward the picture */
    drop(el.q1, R(t, MOT, 0.5), -4);
    drop(el.q2, R(t, MOT + 0.25, 0.5), -8);
  }

  return {beats: [0, AF, MOT, END], render: render};
});
