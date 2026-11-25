/* Core helpers: storage, routing, math rendering, search. Classic script (works on file://). */
(function () {
  'use strict';
  var D = window.DATA || { sections: [], problems: [], papers: [], resources: [], plan: [], stats: {}, lessons: {}, notes: {}, slides: {}, cheatsheet: '' };
  D.notes = D.notes || {}; D.slides = D.slides || {};
  window.DATA = D;

  var EXAM_START = new Date('2026-11-28T12:00:00+05:00');
  var EXAM_END = new Date('2026-11-28T13:30:00+05:00');

  /* ---------- storage (always guarded) ---------- */
  var PREFIX = 'c1e2.';
  var Store = {
    get: function (k, def) {
      try { var v = localStorage.getItem(PREFIX + k); return v == null ? def : JSON.parse(v); } catch (e) { return def; }
    },
    set: function (k, v) {
      try { localStorage.setItem(PREFIX + k, JSON.stringify(v)); } catch (e) {}
    },
    status: function (pid) { return (Store.get('status', {}) || {})[pid] || null; },
    setStatus: function (pid, s) {
      var m = Store.get('status', {}) || {};
      if (m[pid] === s) delete m[pid]; else m[pid] = s;
      Store.set('status', m);
      return m[pid] || null;
    }
  };

  /* ---------- small DOM helpers ---------- */
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function h(html) { var t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstElementChild; }
  function qs(sel, root) { return (root || document).querySelector(sel); }
  function qsa(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  function renderMath(el) {
    if (!window.renderMathInElement || !el) return;
    try {
      window.renderMathInElement(el, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '\\[', right: '\\]', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false,
        ignoredClasses: ['no-math']
      });
    } catch (e) { console.warn(e); }
  }

  /* ---------- data helpers ---------- */
  var secById = {};
  D.sections.forEach(function (s) { secById[s.id] = s; });
  var probById = {};
  D.problems.forEach(function (p) { probById[p.id] = p; });
  var paperById = {};
  D.papers.forEach(function (p) { paperById[p.id] = p; });

  function inScope(p) { return !p.out_of_scope; }
  function listed(p) { return !p.out_of_scope && !p.duplicate_of; }
  function sectionProblems(sec) { return D.problems.filter(function (p) { return p.section === sec && listed(p); }); }
  function sectionProgress(sec) {
    var ps = sectionProblems(sec), st = Store.get('status', {}) || {};
    var r = { total: ps.length, solved: 0, unsure: 0, unsolved: 0 };
    ps.forEach(function (p) { var s = st[p.id]; if (s) r[s]++; });
    return r;
  }
  function topics() {
    var m = {};
    D.problems.forEach(function (p) { if (p.topic && listed(p)) m[p.topic] = (m[p.topic] || 0) + 1; });
    return Object.keys(m).sort();
  }
  function lessonHref(sec) { return '#/lesson/' + sec; }

  /* Weak topics: topics with "unsolved"/"unsure" marks or wrong mock answers, weighted. */
  function weakTopics() {
    var st = Store.get('status', {}) || {}, score = {};
    Object.keys(st).forEach(function (pid) {
      var p = probById[pid]; if (!p || !p.topic) return;
      var w = st[pid] === 'unsolved' ? 2 : st[pid] === 'unsure' ? 1 : -1;
      score[p.topic] = (score[p.topic] || 0) + w;
    });
    (Store.get('mockHistory', []) || []).forEach(function (m) {
      (m.results || []).forEach(function (r) {
        var p = probById[r.id]; if (!p || !p.topic) return;
        var w = r.self === 'wrong' ? 2 : r.self === 'partial' ? 1 : -1;
        score[p.topic] = (score[p.topic] || 0) + w;
      });
    });
    return Object.keys(score).filter(function (t) { return score[t] > 0; })
      .sort(function (a, b) { return score[b] - score[a]; });
  }

  /* ---------- router ---------- */
  var routes = [];
  function route(pattern, fn) { routes.push({ re: pattern, fn: fn }); }
  var cleanup = [];
  function onLeave(fn) { cleanup.push(fn); }
  function navigate() {
    cleanup.splice(0).forEach(function (f) { try { f(); } catch (e) {} });
    var hash = location.hash.replace(/^#/, '') || '/home';
    var path = hash.split('?')[0], query = {};
    (hash.split('?')[1] || '').split('&').forEach(function (kv) {
      if (!kv) return; var i = kv.indexOf('=');
      query[decodeURIComponent(i < 0 ? kv : kv.slice(0, i))] = i < 0 ? '' : decodeURIComponent(kv.slice(i + 1));
    });
    var app = qs('#app');
    for (var i = 0; i < routes.length; i++) {
      var m = path.match(routes[i].re);
      if (m) {
        app.innerHTML = '';
        routes[i].fn(app, m.slice(1), query);
        renderMath(app);
        if (window.Plots) window.Plots.init(app);
        var top = path.split('/')[1];
        qsa('.sidebar a').forEach(function (a) {
          var n = a.getAttribute('data-nav');
          a.classList.toggle('active', n === top || (n === 'lessons' && top === 'lesson') || (n === 'papers' && top === 'paper'));
        });
        qs('#sidebar').classList.remove('open');
        if (!query.keepScroll) window.scrollTo(0, 0);
        return;
      }
    }
    app.innerHTML = '<div class="empty">Page not found. <a href="#/home">Go home</a></div>';
  }
  function setQuery(path, q) {
    var parts = Object.keys(q).filter(function (k) { return q[k] !== '' && q[k] != null; })
      .map(function (k) { return encodeURIComponent(k) + '=' + encodeURIComponent(q[k]); });
    var url = '#' + path + (parts.length ? '?' + parts.join('&') : '');
    history.replaceState(null, '', url);
  }

  /* ---------- search ---------- */
  var index = null;
  function strip(html) { var d = document.createElement('div'); d.innerHTML = html; return (d.textContent || '').replace(/\s+/g, ' '); }
  function buildIndex() {
    index = [];
    var pages = [['Home', '#/home'], ['Lessons overview', '#/lessons'], ['Past Papers', '#/papers'], ['Practice', '#/practice'],
      ['Mock Exam', '#/mock'], ['Statistics', '#/stats'], ['Cheat Sheet', '#/cheatsheet'], ['Resources', '#/resources'], ['Study Plan', '#/plan']];
    pages.forEach(function (p) { index.push({ kind: 'page', title: p[0], text: p[0], href: p[1] }); });
    D.sections.forEach(function (s) {
      var body = (D.lessons[s.id] ? strip(D.lessons[s.id]) : '') + ' ' + (D.notes[s.id] ? strip(D.notes[s.id]) : '');
      index.push({ kind: 'lesson ' + s.id, title: s.id + ' ' + s.title, text: s.id + ' ' + s.title + ' ' + s.short + ' ' + body, href: lessonHref(s.id) });
    });
    D.papers.forEach(function (p) { index.push({ kind: 'paper', title: p.title, text: p.title + ' ' + (p.notes || ''), href: '#/paper/' + p.id }); });
    D.problems.forEach(function (p) {
      if (!listed(p)) return;
      index.push({ kind: (p.origin === 'generated' ? 'generated' : p.origin === 'homework' ? 'homework' : 'past paper') + ' · ' + p.section, title: problemLabel(p) + ' — ' + (p.topic || ''),
        text: [p.id, p.topic, p.section, strip(p.statement || ''), (p.tags || []).join(' ')].join(' '), href: '#/problem/' + encodeURIComponent(p.id) });
    });
    D.resources.forEach(function (r) { index.push({ kind: 'resource', title: r.title, text: r.title + ' ' + (r.note || ''), href: '#/resources' }); });
  }
  function problemLabel(p) {
    if (p.origin === 'generated') return 'Generated ' + p.id.replace(/^gen-/, '');
    if (p.origin === 'homework') return (paperById[p.paper] ? paperById[p.paper].short : 'HW') + ' · #' + p.number;
    var pa = paperById[p.paper];
    return (pa ? pa.short || pa.title : p.paper) + ' · #' + p.number;
  }
  function search(q) {
    if (!index) buildIndex();
    var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    var out = [];
    index.forEach(function (e) {
      var t = e.text.toLowerCase(), tt = e.title.toLowerCase(), score = 0;
      for (var i = 0; i < terms.length; i++) {
        if (t.indexOf(terms[i]) < 0) return;
        score += tt.indexOf(terms[i]) >= 0 ? 3 : 1;
      }
      if (e.kind === 'page' || e.kind.indexOf('lesson') === 0) score += 2;
      out.push({ e: e, score: score });
    });
    out.sort(function (a, b) { return b.score - a.score; });
    return out.slice(0, 25).map(function (x) { return x.e; });
  }
  function initSearch() {
    var input = qs('#searchInput'), box = qs('#searchResults'), active = -1;
    function show() {
      var res = search(input.value);
      active = -1;
      if (!input.value.trim()) { box.hidden = true; return; }
      box.innerHTML = res.length ? res.map(function (e) {
        return '<a href="' + e.href + '"><div class="sr-kind">' + esc(e.kind) + '</div>' + esc(e.title) + '</a>';
      }).join('') : '<div class="sr-empty">Nothing found</div>';
      box.hidden = false;
    }
    input.addEventListener('input', show);
    input.addEventListener('focus', show);
    input.addEventListener('keydown', function (ev) {
      var links = qsa('a', box);
      if (ev.key === 'ArrowDown' || ev.key === 'ArrowUp') {
        ev.preventDefault();
        active = Math.max(0, Math.min(links.length - 1, active + (ev.key === 'ArrowDown' ? 1 : -1)));
        links.forEach(function (a, i) { a.classList.toggle('active', i === active); });
      } else if (ev.key === 'Enter') {
        var a = links[active >= 0 ? active : 0]; if (a) { location.hash = a.getAttribute('href'); box.hidden = true; input.blur(); }
      } else if (ev.key === 'Escape') { box.hidden = true; input.blur(); }
    });
    document.addEventListener('click', function (ev) {
      if (!ev.target.closest('.search-wrap')) box.hidden = true;
      else if (ev.target.closest('.search-results a')) { box.hidden = true; input.value = ''; }
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') { ev.preventDefault(); input.focus(); }
    });
  }

  function fmtDuration(ms) {
    if (ms < 0) ms = 0;
    var s = Math.floor(ms / 1000), d = Math.floor(s / 86400), hh = Math.floor(s % 86400 / 3600), mm = Math.floor(s % 3600 / 60), ss = s % 60;
    return { d: d, h: hh, m: mm, s: ss };
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }

  window.App = {
    D: D, Store: Store, esc: esc, h: h, qs: qs, qsa: qsa, renderMath: renderMath,
    secById: secById, probById: probById, paperById: paperById, inScope: inScope, listed: listed,
    sectionProblems: sectionProblems, sectionProgress: sectionProgress, topics: topics, weakTopics: weakTopics,
    lessonHref: lessonHref, problemLabel: problemLabel,
    route: route, navigate: navigate, onLeave: onLeave, setQuery: setQuery, initSearch: initSearch,
    EXAM_START: EXAM_START, EXAM_END: EXAM_END, fmtDuration: fmtDuration, pad: pad
  };
})();

/* Full-screen slide viewer: arrows / keyboard / swipe, Esc or backdrop to close. */
(function () {
  'use strict';
  var A = window.App, box = null, list = [], idx = 0, title = '', onKey = null;
  function el(html) { var t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstElementChild; }
  function render() {
    var img = box.querySelector('.lb-img');
    img.src = list[idx];
    box.querySelector('.lb-count').textContent = title + ' · slide ' + (idx + 1) + ' / ' + list.length;
    box.querySelector('.lb-prev').disabled = idx === 0;
    box.querySelector('.lb-next').disabled = idx === list.length - 1;
    [idx - 1, idx + 1].forEach(function (j) { if (list[j]) { var p = new Image(); p.src = list[j]; } });
  }
  function go(d) { var n = idx + d; if (n >= 0 && n < list.length) { idx = n; render(); } }
  function close() {
    if (!box) return;
    document.removeEventListener('keydown', onKey);
    box.remove(); box = null;
    document.body.style.overflow = '';
  }
  A.lightbox = function (slides, start, ttl) {
    close();
    list = slides; idx = start || 0; title = ttl || '';
    box = el('<div class="lightbox" role="dialog" aria-modal="true">' +
      '<div class="lb-top"><span class="lb-count"></span><button class="lb-close" aria-label="Close">✕</button></div>' +
      '<div class="lb-stage"><button class="lb-nav lb-prev" aria-label="Previous slide">‹</button>' +
      '<img class="lb-img" alt="slide"><button class="lb-nav lb-next" aria-label="Next slide">›</button></div></div>');
    document.body.appendChild(box);
    document.body.style.overflow = 'hidden';
    box.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); go(-1); });
    box.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); go(1); });
    box.querySelector('.lb-close').addEventListener('click', close);
    box.addEventListener('click', function (e) { if (e.target === box || e.target.classList.contains('lb-stage')) close(); });
    var x0 = null;
    box.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    box.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) go(dx < 0 ? 1 : -1);
    });
    onKey = function (e) {
      if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); go(1); }
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); go(-1); }
      else if (e.key === 'Home') { idx = 0; render(); }
      else if (e.key === 'End') { idx = list.length - 1; render(); }
      else if (e.key === 'Escape') close();
    };
    document.addEventListener('keydown', onKey);
    render();
  };
  window.addEventListener('hashchange', close);
})();
