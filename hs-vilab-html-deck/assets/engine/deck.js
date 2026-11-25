/* hs-vilab-html-deck — stage engine. Vanilla JS, no dependencies, works from file://.
   Keys (clicker-safe):
     PageDown · → · Space   next (a stepper spends its steps first)
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
  function setStep(sl, k) {
    sl.setAttribute("data-step", String(k));
    sl.querySelectorAll("[data-from-step]").forEach(function (el) {
      el.classList.toggle("is-off", parseInt(el.getAttribute("data-from-step"), 10) > k);
    });
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
    if (stepCount(sl)) setStep(sl, step == null ? 0 : step);
    var h = "#/" + (i + 1) + (stepCount(sl) && getStep(sl) ? "/" + getStep(sl) : "");
    if (!fromHash && location.hash !== h) history.replaceState(null, "", h);
    if (changed && live) live.textContent = (i + 1) + " / " + slides.length + " " + (sl.getAttribute("aria-label") || "");
    updateNotes();
  }
  function next() {
    var sl = slides[cur], n = stepCount(sl);
    if (n && getStep(sl) < n) { setStep(sl, getStep(sl) + 1); go(cur, getStep(sl)); return; }
    go(cur + 1, null, false, true);
  }
  function prev() {
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
    overview = on;
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
      if (idx < ids.length) { e.preventDefault(); setState(t, ids[idx], true); }
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
    }
  };
})();
