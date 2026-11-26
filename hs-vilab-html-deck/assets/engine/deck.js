/* hs-vilab-html-deck — stage engine. Vanilla JS, no dependencies, works from file://.
   Keys (clicker-safe):
     PageDown · → · Space   next (a stepper spends its steps first, an animation plays its beats)
     M                      motion off / on (a slow PC: every beat becomes a jump)
     PageUp · ←             previous
     Home / End             first / last slide
     1–9                    choose a state of the current slide's toggle
     G                      overview grid      F  fullscreen      Esc  back to the stage
   A toggle group that has keyboard focus takes ← / → itself (roving focus). After a
   mouse click the control lets go of focus, so a clicker keeps driving the deck. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");

  var deck = document.querySelector(".deck");
  var stage = document.querySelector(".stage");
  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  var live = document.getElementById("deck-live");
  var W = 1920, H = 1080, GAP = 64;
  var cur = 0, overview = false;
  var params = new URLSearchParams(location.search);
  /* motion: ?motion=0|1 in the address wins; otherwise the deck's own default (meta.motion,
     written by the build as <html data-motion>): "on" plays the motion even when the OS asks for
     reduced motion (Windows "Animation effects" off is common on lab machines), "off" never
     plays it, "auto" follows the OS. ?motion=0 is also what QA and the PDF use. */
  var motion = params.get("motion") || doc.getAttribute("data-motion") || "auto";
  if (motion === "0" || motion === "off") doc.classList.add("no-motion");
  if (motion === "1" || motion === "on") doc.classList.add("force-motion");
  function still() {
    if (doc.classList.contains("no-motion") || overview) return true;
    if (doc.classList.contains("force-motion")) return false;
    return !!(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches);
  }

  /* ---------- fit ---------- */
  function fit() {
    var vw = window.innerWidth, vh = window.innerHeight;
    if (overview) {
      var n = slides.length, cols = Math.ceil(Math.sqrt(n * 1.2)), rows = Math.ceil(n / cols);
      var gw = cols * W + (cols - 1) * GAP, gh = rows * H + (rows - 1) * GAP;
      var k = Math.min((vw - 48) / gw, (vh - 48) / gh);
      stage.style.transform = "translate(" + (vw - gw * k) / 2 + "px," + (vh - gh * k) / 2 + "px) scale(" + k + ")";
      slides.forEach(function (s, i) {
        s.style.transform = "translate(" + (i % cols) * (W + GAP) + "px," + Math.floor(i / cols) * (H + GAP) + "px)";
      });
      stage.style.background = "transparent";
      return;
    }
    var s = Math.min(vw / W, vh / H);
    stage.style.transform = "translate(" + (vw - W * s) / 2 + "px," + (vh - H * s) / 2 + "px) scale(" + s + ")";
    stage.style.background = "";
    slides.forEach(function (sl) { sl.style.transform = ""; });
  }

  /* ---------- steps (stepper blocks) ---------- */
  function stepCount(sl) { return parseInt(sl.getAttribute("data-steps") || "0", 10); }
  function getStep(sl) { return parseInt(sl.getAttribute("data-step") || "0", 10); }
  function setStep(sl, k, keepPicture) {
    sl.setAttribute("data-step", String(k));
    sl.querySelectorAll("[data-from-step]").forEach(function (el) {
      var from = parseInt(el.getAttribute("data-from-step"), 10);
      el.classList.toggle("is-off", from > k);
      el.classList.toggle("is-now", from === k);
    });
    if (!keepPicture) paint(sl, k);
  }

  /* ---------- animation: a diagram drawn as a function of time, paced by the clicker ----------
     figures/<name>.anim.js calls DeckAnim.define(name, function (svg, lib) { … return {beats, render} }).
     beats are the stop times in seconds (beats[0] = the picture the slide opens on, the last = the
     finished diagram, which is also what the SVG file draws without script). render(t) sets every
     changing attribute from t alone, so a jump and a played beat end on the same picture. The
     engine owns playback: the slide opens still on beat 0; each next key plays one beat; a key
     pressed while a beat plays finishes it at once; previous jumps back without playing. With
     motion off (?motion=0, meta.motion "off", the M key) every beat is a jump. */
  var animDefs = {}, play = null;
  var lib = {
    clamp: function (v) { return v < 0 ? 0 : v > 1 ? 1 : v; },
    smooth: function (v) { v = lib.clamp(v); return v * v * (3 - 2 * v); },
    /* eased progress 0→1 of a move that starts at `from` and lasts `dur` seconds */
    ramp: function (t, from, dur) { return lib.smooth((t - from) / dur); },
    lerp: function (a, b, u) { return a + (b - a) * u; },
    /* a colour token as [r, g, b] (SVG fills use var(--color-…), which cannot be interpolated) */
    css: function (name) {
      var v = getComputedStyle(doc).getPropertyValue(name).trim(), m;
      if ((m = /^#([0-9a-f]{6})$/i.exec(v))) return [0, 2, 4].map(function (i) { return parseInt(m[1].slice(i, i + 2), 16); });
      if ((m = /^#([0-9a-f]{3})$/i.exec(v))) return [0, 1, 2].map(function (i) { return parseInt(m[1][i] + m[1][i], 16); });
      m = v.match(/[\d.]+/g);
      return m ? m.slice(0, 3).map(Number) : [0, 0, 0];
    },
    mix: function (a, b, u) {
      return "rgb(" + a.map(function (v, i) { return Math.round(v + (b[i] - v) * u); }).join(",") + ")";
    },
    /* a polyline walked at constant speed: along(points)(u) → [x, y, angle°] for u in 0..1 */
    along: function (pts) {
      var len = [0];
      for (var i = 1; i < pts.length; i++) len.push(len[i - 1] + Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]));
      return function (u) {
        var d = lib.clamp(u) * len[len.length - 1], j = 1;
        while (j < pts.length - 1 && len[j] < d) j++;
        var a = pts[j - 1], b = pts[j], s = (d - len[j - 1]) / ((len[j] - len[j - 1]) || 1);
        return [a[0] + (b[0] - a[0]) * s, a[1] + (b[1] - a[1]) * s, Math.atan2(b[1] - a[1], b[0] - a[0]) * 180 / Math.PI];
      };
    },
    set: function (el, attrs) { for (var k in attrs) el.setAttribute(k, attrs[k]); },
    /* opacity, and visibility hidden at 0: an invisible label must not stay in the PDF's text
       layer (RAE run: the swapped-out "SD-VAE 디코더" printed under "ViT 디코더") */
    fade: function (el, v) {
      v = lib.clamp(v);
      el.setAttribute("opacity", v.toFixed(3));
      if (v < 0.001) el.setAttribute("visibility", "hidden"); else el.removeAttribute("visibility");
    }
  };
  function animOf(sl) { var a = sl.querySelector("[data-anim-name]"); return a && a.__anim ? a : null; }
  /* an animation that cannot run (no script, a bad script, render throws) gives the slide back as a
     static one: the SVG as drawn (the finished picture), every beat's text, no beats to spend */
  function disable(root, err) {
    if (err) console.error(err);
    if (play && play.a === root) { cancelAnimationFrame(play.raf); play = null; }
    if (root.__pristine) { root.querySelector("svg").replaceWith(root.__pristine); root.__pristine = null; }
    root.__anim = null;
    root.__dead = true;
    var sl = root.closest(".slide");
    sl.removeAttribute("data-steps");
    sl.removeAttribute("data-step");
    sl.querySelectorAll("[data-from-step]").forEach(function (el) { el.classList.remove("is-off", "is-now"); });
  }
  function draw(a, t) {
    try { a.__anim.render(t); return true; } catch (err) { disable(a, err); return false; }
  }
  function paint(sl, k) {
    var a = animOf(sl);
    if (a) draw(a, a.__anim.beats[Math.max(0, Math.min(k, a.__anim.beats.length - 1))]);
  }
  function bindAnim(root) {
    var name = root.getAttribute("data-anim-name"), f = animDefs[name];
    if (!f || root.__anim || root.__dead) return;
    var svg = root.querySelector("svg");
    root.__pristine = svg.cloneNode(true);
    try {
      var api = Object.create(lib);
      api.node = function (key) {
        var el = svg.querySelector('[data-anim="' + key + '"]');
        if (!el) throw new Error("animation " + name + ": no element data-anim=\"" + key + "\" in the SVG");
        return el;
      };
      var inst = f(svg, api), want = parseInt(root.getAttribute("data-beats"), 10);
      var b = inst && inst.beats;
      if (!inst || typeof inst.render !== "function") throw new Error("animation " + name + ": the factory returns no render(t)");
      if (!b || b.length !== want) throw new Error("animation " + name + ": " + (b ? b.length : 0) + " beats in the script, " + want + " in deck.json");
      for (var i = 0; i < b.length; i++) {
        if (typeof b[i] !== "number" || !isFinite(b[i])) throw new Error("animation " + name + ": beats are numbers (seconds)");
        if (i && !(b[i] > b[i - 1])) throw new Error("animation " + name + ": beats must increase");
      }
      root.__anim = inst;
    } catch (err) {
      disable(root, err);
      return;
    }
    var sl = root.closest(".slide");
    paint(sl, overview ? stepCount(sl) : getStep(sl));
  }
  /* a script that never called DeckAnim.define (missing, failed to load): static once the page is in */
  window.addEventListener("load", function () {
    document.querySelectorAll("[data-anim-name]").forEach(function (root) {
      if (!root.__anim && !root.__dead) disable(root, new Error("animation " + root.getAttribute("data-anim-name") + ": its script never called DeckAnim.define"));
    });
  });
  window.DeckAnim = {
    define: function (name, factory) {
      animDefs[name] = factory;
      document.querySelectorAll('[data-anim-name="' + name + '"]').forEach(bindAnim);
    }
  };
  function stopPlay(finish) {
    if (!play) return;
    var p = play;
    play = null;
    cancelAnimationFrame(p.raf);
    if (finish) draw(p.a, p.end);
  }
  function tick(now) {
    var p = play;
    if (!p) return;
    /* a long frame (a slow laptop, a 30 Hz projector link) advances at most 50 ms: no jump */
    if (p.last !== null) p.t = Math.min(p.end, p.t + Math.min(0.05, (now - p.last) / 1000));
    p.last = now;
    if (!draw(p.a, p.t)) return;
    if (p.t >= p.end) { play = null; return; }
    p.raf = requestAnimationFrame(tick);
  }
  function playBeat(sl, from, to) {
    var a = animOf(sl);
    if (!a) return;
    var b = a.__anim.beats;
    play = {a: a, from: from, to: to, t: b[from], end: b[to], last: null, raf: 0};
    if (!draw(a, b[from])) return;   /* before the next paint: the finished picture never flashes */
    play.raf = requestAnimationFrame(tick);
  }

  /* ---------- motion: one step forward cross-fades; the next key finishes it at once ---------- */
  var motionTimer = 0;
  function settle() {
    clearTimeout(motionTimer);
    slides.forEach(function (s) { s.classList.remove("is-entering", "is-leaving", "is-arriving"); });
  }

  /* ---------- navigation ---------- */
  function go(i, step, fromHash, animate) {
    i = Math.max(0, Math.min(slides.length - 1, i));
    var changed = i !== cur, from = cur;
    settle();
    stopPlay(false);
    cur = i;
    slides.forEach(function (s, j) {
      var on = j === i;
      s.classList.toggle("is-current", on);
      if (on || overview) s.removeAttribute("inert"); else s.setAttribute("inert", "");
      s.setAttribute("aria-hidden", on || overview ? "false" : "true");
    });
    var sl = slides[i];
    if (animate && changed && !still()) {
      slides[from].classList.add("is-leaving");
      void sl.offsetWidth;                      /* restart the keyframes */
      sl.classList.add("is-entering", "is-arriving");
      motionTimer = setTimeout(settle, 420);
    }
    if (stepCount(sl)) {   /* a step past the end is clamped; the overview keeps animations finished */
      var k = step == null ? 0 : Math.max(0, Math.min(step, stepCount(sl)));
      setStep(sl, overview && animOf(sl) ? stepCount(sl) : k);
    }
    var h = "#/" + (i + 1) + (stepCount(sl) && getStep(sl) ? "/" + getStep(sl) : "");
    if (!fromHash && location.hash !== h) history.replaceState(null, "", h);
    if (changed && live) live.textContent = (i + 1) + " / " + slides.length + " " + (sl.getAttribute("aria-label") || "");
    updateNotes();
  }
  function next() {
    if (play) { stopPlay(true); return; }   /* a key during a beat finishes it; it does not skip */
    var sl = slides[cur], n = stepCount(sl);
    if (n && getStep(sl) < n) {
      var k = getStep(sl);
      go(cur, k + 1);
      if (animOf(sl) && !still()) playBeat(sl, k, k + 1);
      return;
    }
    go(cur + 1, null, false, true);
  }
  function prev() {
    if (play) { var back = play.from; stopPlay(false); go(cur, back); return; }
    var sl = slides[cur], n = stepCount(sl);
    if (n && getStep(sl) > 0) { setStep(sl, getStep(sl) - 1); go(cur, getStep(sl)); return; }
    var j = cur - 1;
    if (j >= 0) go(j, stepCount(slides[j]));
  }
  function fromHash() {
    var m = /^#\/(\d+)(?:\/(\d+))?/.exec(location.hash);
    if (m) go(parseInt(m[1], 10) - 1, m[2] ? parseInt(m[2], 10) : 0, true);
    else go(0, 0, true);
  }

  /* text of a panel with each math SVG replaced by its aria-label */
  function spoken(el) {
    var c = el.cloneNode(true);
    c.querySelectorAll(".im,.dm").forEach(function (m) {
      m.replaceWith(document.createTextNode(" " + (m.getAttribute("aria-label") || "") + " "));
    });
    return c.textContent.replace(/\s+/g, " ").replace(/ ([,.)])/g, "$1").trim();
  }

  /* ---------- toggle ---------- */
  function setState(root, id, announce) {
    var ids = root.getAttribute("data-states").split(" ");
    if (ids.indexOf(id) < 0) return;
    root.setAttribute("data-state", id);
    root.querySelectorAll("[data-set-state]").forEach(function (b) {
      var on = b.getAttribute("data-set-state") === id;
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.tabIndex = on ? 0 : -1;
    });
    var scope = root.closest(".slide") || root;
    scope.querySelectorAll("[data-show]").forEach(function (el) {
      el.classList.toggle("is-off", el.getAttribute("data-show").split(" ").indexOf(id) < 0);
    });
    scope.querySelectorAll("[data-state-panel]").forEach(function (p) {
      p.hidden = p.getAttribute("data-state-panel") !== id;
    });
    var out = scope.querySelector("[data-live]");
    if (out && announce) {
      var panel = scope.querySelector('[data-state-panel="' + id + '"]');
      var parts = panel ? panel.querySelectorAll(".readout-state, .readout-text") : [];
      out.textContent = parts.length
        ? Array.prototype.map.call(parts, spoken).join(". ").replace(/\.\./g, ".")
        : id;
    }
  }
  document.querySelectorAll("[data-toggle]").forEach(function (root) {
    setState(root, root.getAttribute("data-start"), false);
    root.addEventListener("click", function (e) {
      var b = e.target.closest("[data-set-state]");
      if (!b) return;
      setState(root, b.getAttribute("data-set-state"), true);
      if (e.detail > 0) b.blur(); /* mouse: hand focus back to the deck */
    });
    root.addEventListener("keydown", function (e) {
      if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
      var bs = Array.prototype.slice.call(root.querySelectorAll("[data-set-state]"));
      var k = bs.indexOf(document.activeElement);
      if (k < 0) return;
      e.preventDefault(); e.stopPropagation();
      var j = (k + (e.key === "ArrowRight" ? 1 : -1) + bs.length) % bs.length;
      bs[j].focus();
      setState(root, bs[j].getAttribute("data-set-state"), true);
    });
  });

  /* ---------- pair marker: a delta lights up the two rows it compares ---------- */
  function pair(el, on) {
    var keys = el.getAttribute("data-pair").split("|");
    var scope = el.closest(".slide");
    el.classList.toggle("is-active", on);
    scope.querySelectorAll("[data-key]").forEach(function (r) {
      r.classList.toggle("is-paired", on && keys.indexOf(r.getAttribute("data-key")) >= 0);
    });
  }
  document.querySelectorAll(".delta[data-pair]").forEach(function (d) {
    d.addEventListener("mouseenter", function () { pair(d, true); });
    d.addEventListener("mouseleave", function () { if (document.activeElement !== d) pair(d, false); });
    d.addEventListener("focus", function () { pair(d, true); });
    d.addEventListener("blur", function () { pair(d, false); });
  });

  /* ---------- overview ---------- */
  function setOverview(on) {
    settle();
    stopPlay(true);
    overview = on;
    /* thumbnails show every animation finished; closing the grid re-enters the slide at its start */
    if (on) slides.forEach(function (s) { if (animOf(s)) setStep(s, stepCount(s)); });
    deck.classList.toggle("is-overview", on);
    slides.forEach(function (s, j) {
      if (on) { s.removeAttribute("inert"); s.tabIndex = 0; }
      else { s.removeAttribute("tabindex"); if (j !== cur) s.setAttribute("inert", ""); }
    });
    fit();
    if (on) slides[cur].focus(); else go(cur);
  }
  slides.forEach(function (s, j) {
    s.addEventListener("click", function () { if (overview) { cur = j; setOverview(false); } });
  });

  /* ---------- notes (rehearsal only) ---------- */
  var notesPanel = null;
  if (params.get("notes") === "1") {
    notesPanel = document.createElement("aside");
    notesPanel.className = "notes-panel";
    notesPanel.setAttribute("aria-label", "발표 메모");
    document.body.appendChild(notesPanel);
  }
  function updateNotes() {
    if (!notesPanel) return;
    var n = slides[cur].querySelector("template.notes");
    notesPanel.innerHTML = n ? n.innerHTML : "<p>이 슬라이드에는 메모가 없습니다.</p>";
  }

  /* ---------- keys ---------- */
  document.addEventListener("keydown", function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    var a = document.activeElement;
    var onControl = a && a !== document.body && a.matches("button, input, select, textarea, a[href]");
    var k = e.key;
    if (overview) {
      if (k === "Escape" || k === "g" || k === "G" || k === "Enter") { e.preventDefault(); setOverview(false); return; }
      if (k === "ArrowRight" || k === "ArrowDown") { e.preventDefault(); cur = Math.min(slides.length - 1, cur + 1); go(cur); slides[cur].focus(); return; }
      if (k === "ArrowLeft" || k === "ArrowUp") { e.preventDefault(); cur = Math.max(0, cur - 1); go(cur); slides[cur].focus(); return; }
      return;
    }
    if (k === "Escape") { if (onControl) a.blur(); return; }
    if ((k === " " || k === "Enter") && onControl) return; /* let the control act */
    switch (k) {
      case "PageDown": case "ArrowRight": case " ": e.preventDefault(); next(); return;
      case "PageUp": case "ArrowLeft": e.preventDefault(); prev(); return;
      case "Home": e.preventDefault(); go(0); return;
      case "End": e.preventDefault(); go(slides.length - 1); return;
      case "g": case "G": e.preventDefault(); setOverview(true); return;
      case "m": case "M":   /* motion off/on on the spot (a slow presenter PC): flips what is in effect */
        e.preventDefault();
        if (e.repeat) return;
        stopPlay(true);
        var off = !still();
        doc.classList.toggle("no-motion", off);
        doc.classList.toggle("force-motion", !off);
        if (live) live.textContent = off ? "모션 끔" : "모션 켬";
        return;
      case "f": case "F":
        e.preventDefault();
        if (!document.fullscreenElement) doc.requestFullscreen && doc.requestFullscreen();
        else document.exitFullscreen && document.exitFullscreen();
        return;
    }
    if (/^[1-9]$/.test(k)) {
      var t = slides[cur].querySelector("[data-toggle]");
      if (!t) return;
      var ids = t.getAttribute("data-states").split(" ");
      var idx = parseInt(k, 10) - 1;
      if (idx < ids.length) {
        e.preventDefault();
        setState(t, ids[idx], true);
        /* focus inside the group follows the chosen button, so ← → count from it */
        if (t.contains(a)) { var bt = t.querySelector('[data-set-state="' + ids[idx] + '"]'); if (bt) bt.focus(); }
      }
    }
  });

  window.addEventListener("resize", fit);
  window.addEventListener("hashchange", fromHash);
  fit();
  fromHash();

  /* test hook for qa_render.py: list every (slide, state) pair to capture */
  window.__deck = {
    count: slides.length,
    go: function (i, step) { go(i, step); },
    next: function () { next(); },
    states: function (i) {
      var t = slides[i].querySelector("[data-toggle]");
      return t ? t.getAttribute("data-states").split(" ") : [];
    },
    setState: function (i, id) {
      var t = slides[i].querySelector("[data-toggle]");
      if (t) setState(t, id, false);
    },
    /* animations: the stop times, a still picture at any time t (the side text of the beat being
       played), whether a beat is playing (the clicker-burst check) */
    beats: function (i) { var a = animOf(slides[i]); return a ? a.__anim.beats.slice() : []; },
    seekTime: function (i, t) {
      var a = animOf(slides[i]);
      if (!a) return;
      stopPlay(false);
      var b = a.__anim.beats, k = 0;
      while (k < b.length - 1 && t > b[k]) k++;
      setStep(slides[i], k, true);
      a.__anim.render(t);
    },
    playing: function () { return !!play; }
  };
})();
