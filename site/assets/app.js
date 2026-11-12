(function () {
  "use strict";

  // ---- Mobile navigation drawer ----
  var toggle = document.getElementById("nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    var closeBtn = document.getElementById("nav-close");
    if (closeBtn) closeBtn.addEventListener("click", function () {
      document.body.classList.remove("nav-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.focus();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("nav-open")) {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("click", function (e) {
      if (!document.body.classList.contains("nav-open")) return;
      var side = document.getElementById("sidebar");
      if (side && !side.contains(e.target) && e.target !== toggle) {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Keep the current page visible in the sidebar
  var cur = document.querySelector('.sidebar a[aria-current="page"]');
  if (cur && cur.scrollIntoView) {
    try { cur.scrollIntoView({ block: "center" }); window.scrollTo(0, 0); } catch (e) {}
  }

  // ---- Search ----
  var input = document.getElementById("q");
  var box = document.getElementById("q-results");
  if (!input || !box) return;

  var index = null;
  var loading = false;
  var waiting = [];
  var selected = -1;

  function loadIndex(cb) {
    if (index) { cb(); return; }
    waiting.push(cb);
    if (loading) return;
    loading = true;
    var s = document.createElement("script");
    s.src = "assets/search-index.js";
    s.onload = function () {
      index = window.SEARCH_INDEX || [];
      var w = waiting; waiting = [];
      w.forEach(function (f) { f(); });
    };
    s.onerror = function () {
      index = [];
      box.innerHTML = '<div class="empty">Search could not load. Browse with the menu instead.</div>';
      box.classList.add("open");
    };
    document.head.appendChild(s);
  }

  function esc(t) {
    return t.replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function snippet(text, term) {
    var i = text.toLowerCase().indexOf(term);
    if (i < 0) return esc(text.slice(0, 140)) + (text.length > 140 ? "…" : "");
    var start = Math.max(0, i - 60);
    var part = text.slice(start, start + 170);
    var safe = esc(part);
    var re = new RegExp("(" + term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
    return (start > 0 ? "…" : "") + safe.replace(re, "<mark>$1</mark>") + "…";
  }

  function run(q) {
    var terms = q.toLowerCase().split(/\s+/).filter(function (t) { return t.length > 1; });
    if (!terms.length) { box.classList.remove("open"); return; }
    var hits = [];
    index.forEach(function (d) {
      var title = d.t.toLowerCase();
      var text = d.x.toLowerCase();
      var score = 0;
      for (var k = 0; k < terms.length; k++) {
        var term = terms[k];
        var inTitle = title.indexOf(term) >= 0;
        var count = 0, pos = text.indexOf(term);
        while (pos >= 0 && count < 8) { count++; pos = text.indexOf(term, pos + term.length); }
        if (!inTitle && !count) return;
        score += (inTitle ? 12 : 0) + count;
      }
      if (d.w) score += 3;
      hits.push({ d: d, s: score });
    });
    hits.sort(function (a, b) { return b.s - a.s; });
    hits = hits.slice(0, 12);
    selected = -1;
    if (!hits.length) {
      box.innerHTML = '<div class="empty">Nothing found for “' + esc(q) + '”.</div>';
    } else {
      box.innerHTML = hits.map(function (h) {
        return '<a href="' + h.d.u + '"><div class="r-part">' + esc(h.d.p) + (h.d.w ? " · written" : " · planned") +
          '</div><div class="r-title">' + esc(h.d.t) + '</div><div class="r-snip">' + snippet(h.d.x, terms[0]) + "</div></a>";
      }).join("");
    }
    box.classList.add("open");
  }

  var timer = null;
  input.addEventListener("focus", function () { loadIndex(function () {}); });
  input.addEventListener("input", function () {
    clearTimeout(timer);
    var q = input.value.trim();
    timer = setTimeout(function () { loadIndex(function () { run(q); }); }, 120);
  });
  input.addEventListener("keydown", function (e) {
    var links = box.querySelectorAll("a");
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      if (!links.length) return;
      e.preventDefault();
      selected = (selected + (e.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
      links.forEach(function (a, i) { a.classList.toggle("sel", i === selected); });
    } else if (e.key === "Enter") {
      var target = links[selected >= 0 ? selected : 0];
      if (target) { e.preventDefault(); window.location.href = target.getAttribute("href"); }
    } else if (e.key === "Escape") {
      box.classList.remove("open");
      input.blur();
    }
  });
  document.addEventListener("click", function (e) {
    if (!box.contains(e.target) && e.target !== input) box.classList.remove("open");
  });
})();
