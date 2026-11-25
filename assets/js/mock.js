/* Mock exam: 8 open problems, 90 minutes, section weights from past-paper statistics. */
(function () {
  'use strict';
  var A = window.App, D = A.D, esc = A.esc, Store = A.Store;
  var N = 8, MINUTES = 90;

  function chapterOf(sec) { return sec.split('.')[0]; }

  /* how many problems per chapter, by largest remainder of the past-paper shares */
  function chapterQuota() {
    var bySec = (D.stats && D.stats.by_section) || {}, ch = { 4: 0, 5: 0, 7: 0 }, tot = 0;
    Object.keys(bySec).forEach(function (s) { ch[chapterOf(s)] = (ch[chapterOf(s)] || 0) + bySec[s]; tot += bySec[s]; });
    if (!tot) return { 4: 3, 5: 4, 7: 1 };
    var q = {}, rem = [], used = 0;
    Object.keys(ch).forEach(function (c) { var v = N * ch[c] / tot; q[c] = Math.floor(v); used += q[c]; rem.push([v - q[c], c]); });
    rem.sort(function (a, b) { return b[0] - a[0]; });
    for (var i = 0; used < N; i++, used++) q[rem[i % rem.length][1]]++;
    if (!q[7]) { q[7] = 1; q[5]--; }            // Exam 2 always has a Ch. 7 problem (§7.2/7.3 are named in the syllabus)
    return q;
  }

  function weightedPick(items, wfn) {
    var tot = items.reduce(function (a, it) { return a + wfn(it); }, 0), r = Math.random() * tot;
    for (var i = 0; i < items.length; i++) { r -= wfn(items[i]); if (r <= 0) return items[i]; }
    return items[items.length - 1];
  }

  function pool() {
    return D.problems.filter(function (p) {
      return A.listed(p) && (p.steps || []).length && p.answer && (p.tags || []).indexOf('originally multiple choice') < 0 && p.difficulty !== 'easy';
    });
  }

  function buildExam() {
    var q = chapterQuota(), P = pool(), topicW = (D.stats && D.stats.by_topic) || {}, chosen = [], usedTopics = {};
    var easyPool = D.problems.filter(function (p) { return A.listed(p) && (p.steps || []).length && p.answer; });
    Object.keys(q).forEach(function (c) {
      for (var i = 0; i < q[c]; i++) {
        var cand = P.filter(function (p) { return chapterOf(p.section) === c && !usedTopics[p.topic] && chosen.indexOf(p) < 0; });
        if (!cand.length) cand = P.filter(function (p) { return chapterOf(p.section) === c && chosen.indexOf(p) < 0; });
        if (!cand.length) cand = easyPool.filter(function (p) { return chapterOf(p.section) === c && chosen.indexOf(p) < 0; });
        if (!cand.length) continue;
        // weight: topic frequency, a bonus for generated problems (fresh), and for our instructor's sources
        var p = weightedPick(cand, function (x) {
          var w = (topicW[x.topic] || 1);
          if (x.origin === 'generated') w *= 1.3;
          if (/^(rev-|f25t)/.test(x.id)) w *= 1.5;
          return w;
        });
        chosen.push(p); usedTopics[p.topic] = 1;
      }
    });
    chosen.sort(function (a, b) { return parseFloat(a.section) - parseFloat(b.section); });
    return { ids: chosen.map(function (p) { return p.id; }), start: Date.now(), end: Date.now() + MINUTES * 60000, finished: false, results: {} };
  }

  A.route(/^\/mock$/, function (app) {
    var cur = Store.get('mockCurrent', null);
    if (cur && !cur.finished) return running(app, cur);
    if (cur && cur.finished) return review(app, cur);
    intro(app);
  });

  function intro(app) {
    var q = chapterQuota(), hist = Store.get('mockHistory', []) || [];
    app.innerHTML = '<h1>Mock exam</h1>' +
      '<div class="card"><p>8 open-ended problems · 90 minutes · no hints. Write full solutions on paper, as in the real exam.</p>' +
      '<p class="small muted">Problems per chapter follow the past-paper statistics: Ch. 4 × ' + q[4] + ', Ch. 5 × ' + q[5] + ', Ch. 7 × ' + q[7] +
      '. Inside a chapter the problem types are drawn by how often they appear, at most one problem per type. Real past problems and generated ones are mixed. ' +
      'Multiple-choice originals and “easy” warm-ups are left out.</p>' +
      '<p class="small muted">The timer keeps running if you reload or close the page.</p>' +
      '<button class="btn primary" id="go">Start the 90-minute mock</button></div>' +
      (hist.length ? '<h2>Previous attempts</h2><div class="card table-wrap"><table><thead><tr><th>Date</th><th>Score (self-graded)</th><th>Weak topics</th></tr></thead><tbody>' +
        hist.slice().reverse().map(function (h) {
          return '<tr><td>' + new Date(h.date).toLocaleString() + '</td><td>' + h.score + ' / ' + h.max + '</td><td class="small">' + (h.weak || []).map(esc).join(', ') + '</td></tr>';
        }).join('') + '</tbody></table></div>' : '');
    A.qs('#go', app).addEventListener('click', function () {
      Store.set('mockCurrent', buildExam()); A.navigate();
    });
  }

  function running(app, cur) {
    app.innerHTML = '<h1>Mock exam</h1>' +
      '<div class="timer-bar"><span class="clock" id="clock"></span><span class="small muted">8 problems · write full solutions on paper</span>' +
      '<button class="btn primary small" id="fin" style="margin-left:auto">Finish &amp; see solutions</button>' +
      '<button class="btn small" id="quit">Abandon</button></div><div id="list"></div>';
    var list = A.qs('#list', app);
    cur.ids.forEach(function (id, i) {
      var p = A.probById[id]; if (!p) return;
      list.appendChild(A.h('<article class="card problem"><div class="problem-head"><span class="pid">Problem ' + (i + 1) + '</span></div>' +
        '<div class="problem-statement">' + p.statement + '</div>' + (p.figure ? '<div class="figure"><img src="' + esc(p.figure) + '" alt="figure"></div>' : '') + '</article>'));
    });
    A.renderMath(list);
    var clock = A.qs('#clock', app);
    function tick() {
      var left = cur.end - Date.now(), f = A.fmtDuration(left);
      clock.textContent = (f.h * 60 + f.m) + ':' + A.pad(f.s);
      clock.classList.toggle('low', left < 10 * 60000);
      if (left <= 0) finish();
    }
    function finish() { clearInterval(iv); cur.finished = true; cur.finishedAt = Date.now(); Store.set('mockCurrent', cur); A.navigate(); }
    var iv = setInterval(tick, 1000); tick();
    A.onLeave(function () { clearInterval(iv); });
    A.qs('#fin', app).addEventListener('click', finish);
    A.qs('#quit', app).addEventListener('click', function () { clearInterval(iv); Store.set('mockCurrent', null); A.navigate(); });
  }

  var MARKS = { right: 1, partial: 0.5, wrong: 0 };
  function review(app, cur) {
    var used = Math.round(((cur.finishedAt || Date.now()) - cur.start) / 60000);
    app.innerHTML = '<h1>Mock exam — solutions</h1><p class="muted">Time used: ' + Math.min(used, MINUTES) + ' min. Grade yourself on each problem against the full solution, then press “Save result”.</p><div id="list"></div>' +
      '<div class="card" id="sum"></div>';
    var list = A.qs('#list', app);
    cur.ids.forEach(function (id, i) {
      var p = A.probById[id]; if (!p) return;
      var card = A.problemCard(p, { label: 'Problem ' + (i + 1), noStatus: true });
      var g = A.h('<div class="btn-row" style="margin-top:10px"><span class="small muted">My result:</span>' +
        ['right', 'partial', 'wrong'].map(function (m) { return '<button class="btn small' + (cur.results[id] === m ? ' primary' : '') + '" data-m="' + m + '">' + m + '</button>'; }).join('') + '</div>');
      g.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-m]'); if (!b) return;
        cur.results[id] = b.dataset.m; Store.set('mockCurrent', cur);
        A.qsa('button', g).forEach(function (x) { x.classList.toggle('primary', x === b); }); summary();
      });
      card.appendChild(g);
      list.appendChild(card);
    });
    A.renderMath(list);
    function summary() {
      var byTopic = {}, score = 0, graded = 0;
      cur.ids.forEach(function (id) {
        var p = A.probById[id], r = cur.results[id]; if (!p) return;
        byTopic[p.topic] = byTopic[p.topic] || { n: 0, s: 0, sec: p.section };
        byTopic[p.topic].n++;
        if (r) { graded++; score += MARKS[r]; byTopic[p.topic].s += MARKS[r]; }
      });
      var weak = Object.keys(byTopic).filter(function (t) { return cur.ids.some(function (id) { var p = A.probById[id]; return p && p.topic === t && cur.results[id] && cur.results[id] !== 'right'; }); });
      A.qs('#sum', app).innerHTML = '<h2 style="margin-top:0">Breakdown by topic</h2>' +
        '<div class="table-wrap"><table><thead><tr><th>Topic</th><th>Section</th><th>Result</th></tr></thead><tbody>' +
        Object.keys(byTopic).map(function (t) {
          var b = byTopic[t];
          return '<tr><td>' + esc(t) + '</td><td><a href="' + A.lessonHref(b.sec) + '">§' + b.sec + '</a></td><td>' + b.s + ' / ' + b.n + '</td></tr>';
        }).join('') + '</tbody></table></div>' +
        '<p><b>Score: ' + score + ' / ' + cur.ids.length + '</b> <span class="muted small">(' + graded + ' of ' + cur.ids.length + ' graded)</span></p>' +
        (weak.length ? '<p><b>Weak topics:</b> ' + weak.map(function (t) { return '<a class="tag warn" href="#/practice?topic=' + encodeURIComponent(t) + '">' + esc(t) + '</a>'; }).join(' ') + '</p>' : '') +
        '<div class="btn-row"><button class="btn primary" id="save"' + (graded < cur.ids.length ? ' disabled title="Grade every problem first"' : '') + '>Save result &amp; new mock</button>' +
        '<button class="btn" id="discard">Discard</button></div>';
      var save = A.qs('#save', app);
      save.addEventListener('click', function () {
        var hist = Store.get('mockHistory', []) || [];
        hist.push({ date: Date.now(), score: score, max: cur.ids.length, weak: weak,
          results: cur.ids.map(function (id) { return { id: id, self: cur.results[id] }; }) });
        Store.set('mockHistory', hist); Store.set('mockCurrent', null); A.navigate();
      });
      A.qs('#discard', app).addEventListener('click', function () { Store.set('mockCurrent', null); A.navigate(); });
    }
    summary();
  }
})();
