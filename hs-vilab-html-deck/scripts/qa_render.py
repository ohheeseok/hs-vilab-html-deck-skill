"""Mechanical QA for an hs-vilab-html-deck build (Playwright + Chromium).

Usage:
    python qa_render.py <work_dir> [--viewport 1920x1080]

Opens deck/index.html?motion=0 over file:// with every non-file request blocked, so each
capture is the finished slide. Captures go to qa/ at 1920x1080 and qa/<W>x<H>/ otherwise.
For each slide and each toggle state:
  * screenshot -> qa/s<NN>[-<state>].png
  * overflow: any element whose box leaves the slide, or a text box that clips;
  * collide: two visible text line boxes (or text and an image) overlapping anywhere on the slide;
  * spill: content leaving its band (a direct child of the slide), or two bands overlapping;
  * type floor: any rendered glyph run under 24 stage px;
  * title wrap: a slide title taller than one line;
  * glyph faces: CDP CSS.getPlatformFontsForNode on every text-bearing element —
    Hangul must come from GmarketSans, Latin from Geomini;
  * text contrast: HTML text against its nearest opaque background, under 4.5:1;
  * console errors, failed or external requests.
Then, with motion on, a clicker burst (6 x PageDown 60ms apart) must land on one finished
slide: no half-faded slide and no slide left in a transition class.
Writes qa/scan.json and prints a summary. Exit 1 if anything failed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

MEASURE = r"""
(idx) => {
  const slide = document.querySelectorAll('.slide')[idx];
  const sr = slide.getBoundingClientRect();
  const k = sr.width / 1920;                     // stage scale
  const out = {overflow: [], small: [], titleWrap: null, clipped: [], contrast: []};
  const rgb = c => { const m = c.match(/[\d.]+/g); return m ? m.map(Number) : null; };
  const lum = c => { const v = c.slice(0, 3).map(x => { x /= 255; return x <= .03928 ? x / 12.92 : ((x + .055) / 1.055) ** 2.4; });
                     return .2126 * v[0] + .7152 * v[1] + .0722 * v[2]; };
  const bgOf = el => { for (let e = el; e; e = e.parentElement) { const c = rgb(getComputedStyle(e).backgroundColor);
                       if (c && (c.length < 4 || c[3] > .5)) return c; } return [255, 255, 255]; };
  const visible = el => {
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || +cs.opacity === 0) return false;
    if (el.closest('.is-off,[hidden],.sr-only')) return false;
    return true;
  };
  const path = el => {
    const p = [];
    for (let e = el; e && e !== slide && p.length < 4; e = e.parentElement)
      p.unshift(e.tagName.toLowerCase() + (e.classList.length ? '.' + [...e.classList].join('.') : ''));
    return p.join(' > ');
  };
  for (const el of slide.querySelectorAll('*')) {
    if (!visible(el)) continue;
    const r = el.getBoundingClientRect();
    if (!r.width && !r.height) continue;
    if (r.left < sr.left - 1 || r.right > sr.right + 1 || r.top < sr.top - 1 || r.bottom > sr.bottom + 1)
      out.overflow.push({el: path(el), box: [r.left - sr.left, r.top - sr.top, r.right - sr.left, r.bottom - sr.top].map(v => Math.round(v / k))});
    if (!(el instanceof SVGElement) && (el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2)) {
      const cs = getComputedStyle(el);
      if (cs.overflow !== 'visible' && el.clientHeight > 0) out.clipped.push(path(el));
    }
    const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (hasText) {
      let px = parseFloat(getComputedStyle(el).fontSize);
      if (el instanceof SVGElement) {
        const svg = el.ownerSVGElement;
        const vb = svg.viewBox.baseVal;
        const sr2 = svg.getBoundingClientRect();
        if (vb && vb.width) px = px * (sr2.width / k) / vb.width;
      }
      if (!(el instanceof SVGElement) && !el.closest('svg')) {
        const fg = rgb(getComputedStyle(el).color), bg = bgOf(el);
        const a = lum(fg), b = lum(bg), cr = (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
        if (cr < 4.5) out.contrast.push({el: path(el), ratio: Math.round(cr * 100) / 100, text: el.textContent.trim().slice(0, 30)});
      }
      if (px < 23.5) out.small.push({el: path(el), px: Math.round(px * 10) / 10, text: el.textContent.trim().slice(0, 40)});
    }
  }
  // bands: the slide's direct children stack top to bottom; content must stay inside its band
  // and bands must not overlap (a figure growing up over the cover rule, a body running into the footer).
  out.spill = [];
  const bands = [...slide.children].filter(c => visible(c) && getComputedStyle(c).position !== 'absolute');
  bands.forEach((c, j) => {
    const cr = c.getBoundingClientRect();
    if (j > 0) {
      const pr = bands[j - 1].getBoundingClientRect();
      if (cr.height && pr.height && cr.top < pr.bottom - 2)
        out.spill.push({el: path(c), over: path(bands[j - 1]), px: Math.round((pr.bottom - cr.top) / k)});
    }
    for (const d of c.querySelectorAll('*')) {
      if (!visible(d) || d.closest('svg') && !(d instanceof SVGSVGElement)) continue;
      const r = d.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      if (r.top < cr.top - 2 || r.bottom > cr.bottom + 2) {
        out.spill.push({el: path(d), band: path(c), px: Math.round(Math.max(cr.top - r.top, r.bottom - cr.bottom) / k)});
        break;
      }
    }
  });
  // collide: two visible pieces of text (line boxes) — or text and an image — that overlap anywhere
  // on the slide. The band check only sees a slide's direct children; this catches a caption that
  // a shrinking flex item lets run over its neighbour inside one column.
  out.collide = [];
  const boxes = [];
  const walker = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    const el = n.parentElement;
    if (!n.textContent.trim() || !el || el.closest('svg,.mark,.sr-only,template') || !visible(el)) continue;
    const rg = document.createRange(); rg.selectNodeContents(n);
    for (const r of rg.getClientRects()) if (r.width > 1 && r.height > 1) boxes.push({el, r});
  }
  for (const img of slide.querySelectorAll('img')) {
    if (!visible(img)) continue;
    const r = img.getBoundingClientRect(); if (r.width && r.height) boxes.push({el: img, r});
  }
  // line boxes include the font's full ascent/descent, so lines of one paragraph touch: compare
  // only text from different blocks, and count an overlap of at least 35% of the shorter box
  const block = el => { for (let e = el; e && e !== slide; e = e.parentElement)
                          if (!/^inline/.test(getComputedStyle(e).display)) return e; return slide; };
  boxes.forEach(b => { b.blk = b.el.tagName === 'IMG' ? b.el : block(b.el); });
  const hit = (a, b) => Math.min(a.right, b.right) - Math.max(a.left, b.left) > 3 * k &&
                        Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > 0.35 * Math.min(a.height, b.height);
  for (let i = 0; i < boxes.length && out.collide.length < 5; i++)
    for (let j = i + 1; j < boxes.length; j++) {
      const A = boxes[i], B = boxes[j];
      if (A.blk === B.blk || A.blk.contains(B.blk) || B.blk.contains(A.blk)) continue;
      if (A.el.tagName === 'IMG' && B.el.tagName === 'IMG') continue;
      if (hit(A.r, B.r)) { out.collide.push({a: path(A.el), b: path(B.el), text: (A.el.textContent || '').trim().slice(0, 24)}); break; }
    }
  const t = slide.querySelector('.slide-title, .cover-title');
  if (t) {
    const lh = parseFloat(getComputedStyle(t).lineHeight);
    const lines = Math.round(t.getBoundingClientRect().height / k / lh);
    if (t.classList.contains('slide-title') && lines > 1) out.titleWrap = lines;
    if (t.scrollWidth > t.clientWidth + 2) out.titleWrap = 'overflows';
  }
  return out;
}
"""


def faces(cdp, page, idx):
    """Return {face: sample text} for glyphs actually drawn on slide idx."""
    doc = cdp.send("DOM.getDocument", {"depth": -1, "pierce": True})
    res = cdp.send("DOM.querySelectorAll", {"nodeId": doc["root"]["nodeId"],
                                            "selector": f".slide:nth-of-type({idx + 1}) *"})
    used = {}
    for nid in res["nodeIds"]:
        try:
            f = cdp.send("CSS.getPlatformFontsForNode", {"nodeId": nid})
        except Exception:
            continue
        for x in f.get("fonts", []):
            used[x["familyName"]] = used.get(x["familyName"], 0) + x["glyphCount"]
    return used


def main() -> int:
    work = Path(sys.argv[1]).resolve()
    vp = (1920, 1080)
    if "--viewport" in sys.argv:
        w, h = sys.argv[sys.argv.index("--viewport") + 1].split("x")
        vp = (int(w), int(h))
    index = work / "deck" / "index.html"
    qa = work / "qa" if vp == (1920, 1080) else work / "qa" / f"{vp[0]}x{vp[1]}"
    qa.mkdir(parents=True, exist_ok=True)
    report = {"viewport": vp, "slides": [], "console": [], "external": [], "failed": []}
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": vp[0], "height": vp[1]}, device_scale_factor=1)
        page = ctx.new_page()

        def route(r):
            if r.request.url.startswith("file:"):
                return r.continue_()
            report["external"].append(r.request.url)
            return r.abort()
        page.route("**/*", route)
        page.on("console", lambda m: m.type == "error" and report["console"].append(m.text))
        page.on("pageerror", lambda e: report["console"].append(str(e)))
        page.on("requestfailed", lambda r: report["failed"].append(r.url))
        page.goto(index.as_uri() + "?motion=0")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        cdp = ctx.new_cdp_session(page)
        cdp.send("DOM.enable")
        cdp.send("CSS.enable")
        n = page.evaluate("window.__deck.count")
        for i in range(n):
            page.evaluate(f"window.__deck.go({i})")
            states = page.evaluate(f"window.__deck.states({i})") or [None]
            for st in states:
                if st:
                    page.evaluate(f"window.__deck.setState({i}, {json.dumps(st)})")
                page.wait_for_timeout(350)
                name = f"s{i + 1:02d}" + (f"-{st}" if st else "")
                page.screenshot(path=str(qa / f"{name}.png"))
                m = page.evaluate(MEASURE, i)
                m["name"] = name
                m["faces"] = faces(cdp, page, i)
                report["slides"].append(m)

        # clicker burst with motion on
        page.goto(index.as_uri() + "#/1")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(200)
        for _ in range(6):
            page.keyboard.press("PageDown")
            page.wait_for_timeout(60)
        page.wait_for_timeout(450)
        report["burst"] = page.evaluate("""() => {
          const shown = [...document.querySelectorAll('.slide')].filter(s => getComputedStyle(s).display !== 'none');
          const busy = [...document.querySelectorAll('.is-entering,.is-leaving,.is-arriving')].length;
          return {shown: shown.map(s => s.id), opacity: shown.map(s => +getComputedStyle(s).opacity), busy, hash: location.hash};
        }""")
        b.close()

    bad = []
    for s in report["slides"]:
        for key in ("overflow", "small", "clipped", "contrast", "spill", "collide"):
            if s[key]:
                bad.append(f"{s['name']}: {key} {s[key][:3]}")
        if s["titleWrap"]:
            bad.append(f"{s['name']}: title wraps ({s['titleWrap']})")
        stray = {f: c for f, c in s["faces"].items() if not f.lower().startswith(("geomini", "gmarket"))}
        if stray:
            bad.append(f"{s['name']}: glyphs drawn in fallback fonts {stray}")
    bu = report.get("burst", {})
    if len(bu.get("shown", [])) != 1 or bu.get("busy") or any(o < 1 for o in bu.get("opacity", [])):
        bad.append(f"clicker burst did not settle: {bu}")
    for key in ("console", "external", "failed"):
        if report[key]:
            bad.append(f"{key}: {report[key][:5]}")
    report["errors"] = bad
    (qa / "scan.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    for s in report["slides"]:
        print(s["name"], {k: v for k, v in s["faces"].items()})
    print("\n".join(bad) if bad else "QA: no mechanical defects")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
