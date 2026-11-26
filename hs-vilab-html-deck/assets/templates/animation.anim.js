/* TODO-name — storyboard first, one line per beat (the slide opens still on beat 0):
   0  TODO: the picture the presenter talks over first (the baseline, the first path)
   1  TODO: one event
   2  TODO: one event
   The SVG file draws the last beat; render(t) sets every moving attribute from t alone.
   Copy to work/<slug>/figures/<name>.anim.js, rename, and see references/animation.md. */
DeckAnim.define("TODO-name", function (svg, lib) {
  var R = lib.ramp, L = lib.lerp;
  var box = lib.node("box"), label = lib.node("label");   // read the DOM here, once

  var MOVE = 0, SHOW = 1.2, END = 2.2;                     // beat k plays beats[k-1] → beats[k]

  var op = lib.fade;                                       // opacity; hidden at 0 (PDF text layer)

  function render(t) {
    /* beat 1: the box slides in from the left (ends by SHOW) */
    box.setAttribute("x", L(40, 200, R(t, MOVE, 1.0)).toFixed(1));
    /* beat 2: its label settles in (ends by END) */
    var u = R(t, SHOW, 0.5);
    op(label, u);
    label.setAttribute("transform", "translate(0," + (-10 * (1 - u)).toFixed(2) + ")");
  }

  return {beats: [0, SHOW, END], render: render};
});
