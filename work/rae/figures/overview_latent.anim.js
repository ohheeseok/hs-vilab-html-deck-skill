/* overview_latent — SD-VAE latent → RAE latent (Fig. 2 redrawn), four stops.
   Storyboard (one event per beat; the slide opens still on beat 0):
   0  SD-VAE: 256×256 image → U-Net encoder (funnel) → 32×32×4 → DiT (patch 2) → decoder → image.
   1  The DiT reads the latent in 2×2 patches: a patch is lifted off the grid and becomes one token;
      the 256 tokens are short bars (16 channels, 0.5 px per channel).
   2  Swap the autoencoder, left to right: the funnel becomes a frozen DINOv2-B, the grid goes and the
      bars stretch to 768 channels (same 256 tokens, 48× longer), the DiT reads patch 1, the
      decoder becomes a ViT decoder. GFLOPs change with the blocks.
   3  The two questions the talk answers: ① over the autoencoder, ② under the DiT.
   The SVG file draws beat 3; render(t) sets everything that moves from t alone. */
DeckAnim.define("overview-latent", function (svg, lib) {
  var R = lib.ramp, L = lib.lerp;
  var el = {};
  ["q1", "q2", "vae-enc", "rae-enc", "vae-enc-label", "rae-enc-label", "grid", "patch", "toks",
   "vae-tok-label", "rae-tok-label", "vae-dit-label", "rae-dit-label", "vae-dec", "rae-dec",
   "vae-dec-label", "rae-dec-label", "wire", "wire-ab", "wire-tip"].forEach(function (k) { el[k] = lib.node(k); });
  var bars = Array.prototype.slice.call(el.toks.querySelectorAll("rect"));
  var barY = bars.map(function (b) { return b.y.baseVal.value; });
  var GREY = lib.css("--hs-grey-40"), BLUE = lib.css("--color-accent");
  var BAR0 = {x: 760, w: 8}, BAR1 = {x: 477, w: 384};     /* 16 and 768 channels at 0.5 px each */
  var PATCH = {x: 470, y: 146, s: 56};                      /* 2×2 cells of the front grid */

  /* beat k plays from beats[k-1] to beats[k] */
  var TOKENS = 0, SWAP = 1.4, ASK = 3.2, END = 4.2;

  var op = lib.fade;                                       /* opacity; hidden at 0 */
  /* a SD-VAE piece gives way to its RAE piece: the old one leaves, then the new one comes */
  function swap(t, a, b, from, dur) {
    op(a, 1 - R(t, from, dur / 2));
    op(b, R(t, from + dur / 2, dur / 2));
  }

  function render(t) {
    /* beat 1: one 2×2 patch flies to the first token; the 256 tokens (8 bars) appear */
    var lift = R(t, TOKENS + 0.1, 0.3), fly = R(t, TOKENS + 0.4, 0.6), land = R(t, TOKENS + 1.0, 0.3);
    op(el.patch, lift * (1 - land));
    lib.set(el.patch, {x: L(PATCH.x, BAR0.x, fly).toFixed(1), y: L(PATCH.y, barY[0], fly).toFixed(1),
                       width: L(PATCH.s, BAR0.w, fly).toFixed(1), height: L(PATCH.s, 8, fly).toFixed(1)});
    bars.forEach(function (b, i) {
      var grow = R(t, SWAP + 0.3, 0.75);   /* together: a staggered stack reads as a funnel */
      op(b, R(t, TOKENS + 0.7 + 0.04 * i, 0.3));
      lib.set(b, {x: L(BAR0.x, BAR1.x, grow).toFixed(1), width: L(BAR0.w, BAR1.w, grow).toFixed(1),
                  fill: lib.mix(GREY, BLUE, grow)});
    });
    /* grid → DiT, then grid → tokens → DiT; the arrows go when the tokens stretch over them */
    op(el["wire-ab"], 1 - R(t, SWAP + 0.3, 0.3));
    op(el.wire, 1 - R(t, TOKENS + 0.6, 0.3));
    op(el["wire-tip"], R(t, TOKENS + 0.9, 0.3));
    op(el["vae-tok-label"], R(t, TOKENS + 1.0, 0.3) * (1 - R(t, SWAP + 0.45, 0.25)));
    op(el["rae-tok-label"], R(t, SWAP + 1.0, 0.3));

    /* beat 2: the autoencoder is swapped, left to right */
    swap(t, el["vae-enc"], el["rae-enc"], SWAP, 0.7);
    swap(t, el["vae-enc-label"], el["rae-enc-label"], SWAP, 0.7);
    op(el.grid, 1 - R(t, SWAP + 0.45, 0.55));
    swap(t, el["vae-dit-label"], el["rae-dit-label"], SWAP + 0.9, 0.5);
    swap(t, el["vae-dec"], el["rae-dec"], SWAP + 1.1, 0.7);
    swap(t, el["vae-dec-label"], el["rae-dec-label"], SWAP + 1.1, 0.7);

    /* beat 3: the two questions drop in */
    [["q1", ASK], ["q2", ASK + 0.25]].forEach(function (q) {
      var u = R(t, q[1], 0.5);
      op(el[q[0]], u);
      el[q[0]].setAttribute("transform", "translate(0," + (-10 * (1 - u)).toFixed(2) + ")");
    });
  }

  return {beats: [0, SWAP, ASK, END], render: render};
});
