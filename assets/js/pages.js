/* Page renderers. */
(function () {
  'use strict';
  var A = window.App, D = A.D, esc = A.esc, Store = A.Store;

  var DIFF = { easy: 'easy', exam: 'exam-level', hard: 'hard' };

  /* ======================= problem card ======================= */
  function occurrences(p) { return 1 + (p.also_in ? p.also_in.length : 0); }

  function problemCard(p, opts) {
    opts = opts || {};
    var st = Store.status(p.id);
    var tags = [];
    var pp = A.paperById[p.paper];
    tags.push(p.origin === 'generated' ? '<span class="tag gen">generated</span>' : p.origin === 'homework' ? '<span class="tag hw">homework</span>' : (pp && pp.kind === 'review' ? '<span class="tag past">instructor review</span>' : pp && pp.kind === 'deck' ? '<span class="tag past">prep deck</span>' : '<span class="tag past">past paper</span>'));
    if (p.section) tags.push('<a class="tag" href="' + A.lessonHref(p.section) + '">§' + esc(p.section) + '</a>');
    if (p.topic) tags.push('<span class="tag" title="' + esc(p.subtopic || '') + '">' + esc(p.topic) + '</span>');
    if (p.difficulty) tags.push('<span class="tag">' + esc(DIFF[p.difficulty] || p.difficulty) + '</span>');
    if (p.points) tags.push('<span class="tag">' + esc(p.points) + ' pts</span>');
    if (!opts.hideMeta) {
      if (p.solution_source === 'official') tags.push('<span class="tag good" title="Solution taken from the source material">official solution</span>');
      if (p.verified) tags.push('<span class="tag good" title="Answer checked with SymPy">SymPy ✓</span>');
      if (p.verified === false || p.unverified) tags.push('<span class="tag warn" title="' + esc(p.unverified_note || 'Not fully verified') + '">unverified</span>');
      if (p.also_in && p.also_in.length) tags.push('<span class="tag" title="Same problem appears in other papers">×' + occurrences(p) + ' papers</span>');
      if (p.out_of_scope) tags.push('<span class="tag bad" title="Not on Exam 2">out of scope §' + esc(p.section) + '</span>');
      if (p.verified == null && p.solution_source === 'own' && (p.steps || []).length && !p.unverified_note) tags.push('<span class="tag" title="A proof or reasoning question: nothing numeric to check">reasoning</span>');
      (p.tags || []).forEach(function (tg) { tags.push('<span class="tag">' + esc(tg) + '</span>'); });
    }
    var label = opts.label || A.problemLabel(p);
    var el = A.h(
      '<article class="card problem" data-pid="' + esc(p.id) + '">' +
        '<div class="problem-head"><span class="pid">' + esc(label) + '</span>' + tags.join(' ') +
          (opts.noStatus ? '' : '<span class="status-btns">' +
            ['solved', 'unsure', 'unsolved'].map(function (s) {
              return '<button data-s="' + s + '" class="' + (st === s ? 'on' : '') + '">' + s + '</button>';
            }).join('') + '</span>') +
        '</div>' +
        '<div class="problem-statement">' + (p.statement || '') + '</div>' +
        (p.note ? '<div class="small muted" style="margin-top:6px">Note: ' + p.note + '</div>' : '') +
        (p.figure ? '<div class="figure"><img src="' + esc(p.figure) + '" alt="figure" loading="lazy"></div>' : '') +
        (p.source_image && opts.showSource ? '<details class="small"><summary>' + (p.paper === 'deck-nu' ? 'Original slide' : 'Original scan') + '</summary><div class="figure"><img src="' + esc(p.source_image) + '" alt="original" loading="lazy"></div></details>' : '') +
        (opts.noSolution ? '' :
          '<div class="btn-row sol-controls" style="margin-top:12px">' +
            '<button class="btn small" data-act="step">Show next step</button>' +
            '<button class="btn small" data-act="all">Show full solution</button>' +
            '<button class="btn small" data-act="hide" hidden>Hide</button>' +
            (opts.noLessonLink || !p.section ? '' : '<a class="btn small" href="' + A.lessonHref(p.section) + '">Lesson §' + esc(p.section) + '</a>') +
            (opts.permalink ? '<a class="btn small" href="#/problem/' + encodeURIComponent(p.id) + '">Open</a>' : '') +
          '</div><div class="steps"></div>') +
      '</article>');

    var steps = (p.steps || []).slice();
    var shown = 0, box = el.querySelector('.steps');
    function renderSteps() {
      box.innerHTML = '';
      for (var i = 0; i < shown && i < steps.length; i++) {
        var s = A.h('<div class="step"><div class="step-n">Step ' + (i + 1) + '</div><div>' + steps[i] + '</div></div>');
        box.appendChild(s);
      }
      if (shown > steps.length || (shown === steps.length && steps.length)) {
        if (p.answer) box.appendChild(A.h('<div class="answer"><b>Answer.</b> ' + p.answer + '</div>'));
      }
      if (shown && !steps.length && p.answer) box.appendChild(A.h('<div class="answer"><b>Answer.</b> ' + p.answer + '</div>'));
      if (shown && !steps.length && !p.answer) box.appendChild(A.h('<div class="note">No solution recorded yet.</div>'));
      if (shown && p.solution_note) box.appendChild(A.h('<div class="note info small">' + p.solution_note + '</div>'));
      A.renderMath(box);
      var hide = el.querySelector('[data-act=hide]'), stepBtn = el.querySelector('[data-act=step]');
      if (hide) hide.hidden = !shown;
      if (stepBtn) stepBtn.disabled = shown >= Math.max(steps.length, 1);
    }
    el.addEventListener('click', function (ev) {
      var b = ev.target.closest('button'); if (!b) return;
      if (b.dataset.s) {
        var ns = Store.setStatus(p.id, b.dataset.s);
        A.qsa('.status-btns button', el).forEach(function (x) { x.classList.toggle('on', x.dataset.s === ns); });
        if (opts.onStatus) opts.onStatus();
        return;
      }
      if (b.dataset.act === 'step') { shown = Math.min(shown + 1, Math.max(steps.length, 1)); renderSteps(); }
      if (b.dataset.act === 'all') { shown = Math.max(steps.length, 1); renderSteps(); }
      if (b.dataset.act === 'hide') { shown = 0; renderSteps(); }
    });
    return el;
  }
  A.problemCard = problemCard;

  /* ======================= home ======================= */
  A.route(/^\/home$/, function (app) {
    var past = D.problems.filter(function (p) { return p.origin === 'past' && A.listed(p); });
    var gen = D.problems.filter(function (p) { return p.origin === 'generated'; });
    var hw = D.problems.filter(function (p) { return p.origin === 'homework' && A.listed(p); });
    var freq = {};
    past.forEach(function (p) { freq[p.section] = (freq[p.section] || 0) + occurrences(p); });

    app.innerHTML =
      '<div class="hero">' +
        '<div class="card"><div class="muted small">Calculus 1 · Exam 2 · Saturday, 28 November 2026, 12:00–13:30 (Astana)</div>' +
          '<div class="countdown" id="cd"></div>' +
          '<div class="muted small" id="cdNote"></div>' +
          '<div class="small" style="margin-top:8px">≈8 open-ended problems · 90 minutes · full solutions with steps.<br>Scope: Ch. 4 (except 4.3, 4.7), Ch. 5, §7.2, §7.3.</div>' +
        '</div>' +
        '<div class="card"><b>Quick links</b>' +
          '<div class="btn-row" style="margin-top:10px">' +
            '<a class="btn primary" href="#/mock">Start mock exam</a>' +
            '<a class="btn" href="#/practice">Practice</a>' +
            '<a class="btn" href="#/papers">Past papers</a>' +
            '<a class="btn" href="#/cheatsheet">Cheat sheet</a>' +
            '<a class="btn" href="#/plan">Study plan</a>' +
            '<button class="btn" id="weakBtn">Weak topics</button>' +
          '</div>' +
          '<div class="count-line">' + D.papers.filter(function (x) { return x.kind !== 'homework'; }).length + ' past papers · ' + past.length + ' past problems · ' + hw.length + ' homework · ' + gen.length + ' generated</div>' +
          '<div id="weakOut" class="small" style="margin-top:8px"></div>' +
        '</div>' +
      '</div>' +
      '<div class="card"><b>Closest format to expect: Achenef\'s Fall 2025 tests</b>' +
        '<p class="small" style="margin:6px 0">This year\'s Exam 1 was very close to Fall 2025 Midterm 1, and the Exam 2 Review on Moodle is Achenef\'s too, so expect Exam 2 to look like his Fall 2025 tests. ' +
        'Last year our topics were split between Test 2 (the Ch. 4 problems) and Test 3 (the Ch. 5 problems). Each was 6 multiple-choice × 5 pts + 4 open problems × 12–13 pts = 80 pts. ' +
        '§7.2–7.3 were not on those tests: practise them from the Exam 2 Review and Fall 2024 Midterm 3.</p>' +
        '<div class="btn-row">' +
          '<a class="btn primary" href="#/mock">Fall 2025-format mock</a>' +
          '<a class="btn" href="#/paper/f25-t2a">F25 Test 2 · A</a><a class="btn" href="#/paper/f25-t2b">F25 Test 2 · B</a>' +
          '<a class="btn" href="#/paper/f25-t3a">F25 Test 3 · A</a><a class="btn" href="#/paper/f25-t3b">F25 Test 3 · B</a>' +
          '<a class="btn" href="#/paper/rev-f26">Exam 2 Review</a><a class="btn" href="#/paper/f24-m3">F24 Midterm 3 (Ch. 7)</a>' +
        '</div></div>' +
      '<h2>Sections</h2><p class="muted small">Bar = your marks in Practice (green solved, amber unsure, red unsolved). “seen ×N” = how often the section appears in past papers.</p>' +
      '<div id="secmap"></div>';

    var map = A.qs('#secmap', app);
    [4, 5, 7].forEach(function (ch) {
      map.appendChild(A.h('<div class="chapter-label">Chapter ' + ch + '</div>'));
      var g = A.h('<div class="grid"></div>');
      D.sections.filter(function (s) { return s.chapter === ch; }).forEach(function (s) {
        var pr = A.sectionProgress(s.id), t = Math.max(pr.total, 1);
        g.appendChild(A.h(
          '<a class="card sec-tile" href="' + A.lessonHref(s.id) + '">' +
            '<span class="sec-id">§' + s.id + '</span> ' + esc(s.title) +
            '<div class="freq">' + (freq[s.id] ? 'seen ×' + freq[s.id] + ' in past papers · ' : '') + pr.total + ' problems' +
              (D.lessons[s.id] ? '' : ' · lesson coming') + '</div>' +
            '<div class="bar"><i class="b-good" style="width:' + (100 * pr.solved / t) + '%"></i><i class="b-warn" style="width:' + (100 * pr.unsure / t) + '%"></i><i class="b-bad" style="width:' + (100 * pr.unsolved / t) + '%"></i></div>' +
          '</a>'));
      });
      map.appendChild(g);
    });

    var cd = A.qs('#cd', app), note = A.qs('#cdNote', app);
    function tick() {
      var now = Date.now(), ms = A.EXAM_START - now;
      var f = A.fmtDuration(ms);
      cd.innerHTML = '<div><b>' + f.d + '</b><span>days</span></div><div><b>' + A.pad(f.h) + '</b><span>hours</span></div>' +
        '<div><b>' + A.pad(f.m) + '</b><span>min</span></div><div><b>' + A.pad(f.s) + '</b><span>sec</span></div>';
      note.textContent = ms > 0 ? '' : (now < A.EXAM_END ? 'The exam is happening now. Good luck!' : 'The exam is over.');
    }
    tick();
    var iv = setInterval(tick, 1000);
    A.onLeave(function () { clearInterval(iv); });

    A.qs('#weakBtn', app).addEventListener('click', function () {
      var w = A.weakTopics();
      var out = A.qs('#weakOut', app);
      if (!w.length) {
        out.innerHTML = 'No weak topics yet. Mark problems in <a href="#/practice">Practice</a> as unsure/unsolved or finish a <a href="#/mock">mock exam</a>, and they will show up here.';
        return;
      }
      out.innerHTML = '<b>Weak topics:</b> ' + w.map(function (t) {
        return '<a class="tag warn" href="#/practice?topic=' + encodeURIComponent(t) + '">' + esc(t) + '</a>';
      }).join(' ') + ' <a href="#/practice?weak=1">practice all of them →</a>';
    });
  });

  /* ======================= lessons ======================= */
  A.route(/^\/lessons$/, function (app) {
    var html = '<h1>Lecture lessons</h1><p class="muted">Each section has three tabs: <b>Full lecture notes</b> (everything from Achenef Tesfahun\'s slides, in order: definitions, theorems with proofs, every lecture example solved step by step), <b>Exam summary</b> (short version with past-paper examples, common mistakes, tips) and <b>Lecture slides</b> (the original slides).</p>';
    [4, 5, 7].forEach(function (ch) {
      html += '<div class="chapter-label">Chapter ' + ch + '</div><div class="grid">';
      D.sections.filter(function (s) { return s.chapter === ch; }).forEach(function (s) {
        html += '<a class="card sec-tile" href="' + A.lessonHref(s.id) + '"><span class="sec-id">§' + s.id + '</span> ' + esc(s.title) +
          '<div class="freq">full notes · ' + ((D.slides[s.id] || []).length) + ' slides · ' + A.sectionProblems(s.id).length + ' problems</div></a>';
      });
      html += '</div>';
    });
    app.innerHTML = html;
  });

  A.route(/^\/lesson\/([\d.]+)$/, function (app, m, q) {
    var id = m[0], s = A.secById[id];
    if (!s) { app.innerHTML = '<div class="empty">Unknown section.</div>'; return; }
    var i = D.sections.indexOf(s), prev = D.sections[i - 1], next = D.sections[i + 1];
    var slides = D.slides[id] || [];
    var tabs = [['notes', 'Full lecture notes'], ['summary', 'Exam summary'], ['slides', 'Lecture slides (' + slides.length + ')']];
    var tab = q.tab || Store.get('lessonTab', 'notes');
    if (!D.notes[id] && tab === 'notes') tab = 'summary';
    app.innerHTML =
      '<div class="muted small"><a href="#/lessons">Lessons</a> › Chapter ' + s.chapter + '</div>' +
      '<h1>§' + s.id + ' ' + esc(s.title) + '</h1>' +
      '<div class="tabs no-print">' + tabs.map(function (t) { return '<button class="tab' + (t[0] === tab ? ' on' : '') + '" data-tab="' + t[0] + '">' + t[1] + '</button>'; }).join('') + '</div>' +
      '<div class="lesson" id="lessonBody"></div>' +
      '<div class="card"><b>Practice this section</b><div class="btn-row" style="margin-top:8px">' +
        '<a class="btn primary" href="#/practice?section=' + id + '">All §' + id + ' problems (' + A.sectionProblems(id).length + ')</a>' +
        '<a class="btn" href="#/practice?section=' + id + '&origin=past">Past paper only</a>' +
      '</div></div>' +
      '<div class="lesson-nav">' +
        (prev ? '<a class="btn" href="' + A.lessonHref(prev.id) + '">← §' + prev.id + ' ' + esc(prev.short) + '</a>' : '<span></span>') +
        (next ? '<a class="btn" href="' + A.lessonHref(next.id) + '">§' + next.id + ' ' + esc(next.short) + ' →</a>' : '<span></span>') +
      '</div>';
    var body = A.qs('#lessonBody', app);
    function show(t) {
      tab = t; Store.set('lessonTab', t);
      A.qsa('.tab', app).forEach(function (b) { b.classList.toggle('on', b.dataset.tab === t); });
      if (t === 'notes') { body.innerHTML = D.notes[id] || '<div class="empty">No notes.</div>'; A.qsa('details', body).forEach(function (d) { d.open = true; }); }
      else if (t === 'summary') body.innerHTML = D.lessons[id] || '<div class="empty">This lesson is not written yet.</div>';
      else body.innerHTML = slides.length ? '<p class="muted small">Slides of Achenef Tesfahun\'s lecture for this section, rendered from the Moodle .pptx files. Click a slide to view it full screen; use ← / → (or swipe) to move between slides, Esc to close.</p><div class="slide-grid">' +
        slides.map(function (p, k) { return '<button class="slide-thumb" data-k="' + k + '" aria-label="Open slide ' + (k + 1) + '"><img loading="lazy" src="' + esc(p) + '" alt="slide ' + (k + 1) + '"><span>' + (k + 1) + '</span></button>'; }).join('') + '</div>' : '<div class="empty">No slides.</div>';
      if (t === 'slides') A.qsa('.slide-thumb', body).forEach(function (b) {
        b.addEventListener('click', function () { A.lightbox(slides, +b.dataset.k, '§' + id + ' ' + s.short); });
      });
      A.renderMath(body);
      if (window.Plots) window.Plots.init(body);
    }
    A.qsa('.tab', app).forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.tab); }); });
    show(tab);
  });

  /* ======================= past papers ======================= */
  A.route(/^\/papers$/, function (app) {
    var html = '<h1>Past papers</h1>';
    if (!D.papers.length) {
      html += '<div class="empty">No past papers collected yet.</div>';
    } else {
      html += '<p class="muted">Each original file plus its problems split out. “Solve on time” hides solutions until you stop the timer. Papers are sorted by relevance: our instructor\'s review and tests first.</p>' +
        '<div class="table-wrap card"><table><thead><tr><th>Paper</th><th>Type</th><th>Problems</th><th>Solutions</th><th></th></tr></thead><tbody>';
      D.papers.forEach(function (p) {
        var inScopeN = (p.problems || []).filter(function (id) { return A.probById[id] && A.inScope(A.probById[id]); }).length;
        var likely = ['f25-t2a', 'f25-t2b', 'f25-t3a', 'f25-t3b'].indexOf(p.id) >= 0;
        html += '<tr><td><a href="#/paper/' + esc(p.id) + '"><b>' + esc(p.title) + '</b></a>' + (likely ? ' <span class="tag good" title="Same instructor and format as this year">closest format</span>' : '') + (p.notes ? '<div class="small muted">' + esc(p.notes) + '</div>' : '') + '</td>' +
          '<td>' + esc(p.kind || '') + '</td><td>' + (p.split === false ? '<span class="muted small">not split (Exam 1 topics)</span>' : inScopeN + ' in scope' + ((p.problems || []).length > inScopeN ? ' <span class="muted small">(+' + ((p.problems || []).length - inScopeN) + ' out of scope)</span>' : '')) + '</td>' +
          '<td>' + (p.has_solutions ? '<span class="tag good">yes</span>' : '<span class="tag">own</span>') + '</td>' +
          '<td><a class="btn small" href="#/paper/' + esc(p.id) + '">Open</a></td></tr>';
      });
      html += '</tbody></table></div>';
    }
    app.innerHTML = html;
  });

  A.route(/^\/paper\/(.+)$/, function (app, m) {
    var p = A.paperById[decodeURIComponent(m[0])];
    if (!p) { app.innerHTML = '<div class="empty">Unknown paper.</div>'; return; }
    var showOut = false;
    app.innerHTML =
      '<div class="muted small"><a href="#/papers">Past papers</a></div>' +
      '<h1>' + esc(p.title) + '</h1>' +
      '<div class="btn-row">' + (p.files || []).map(function (f) {
        return '<a class="btn small" href="' + esc(f.path) + '" target="_blank">Original: ' + esc(f.label || f.path.split('/').pop()) + '</a>';
      }).join('') + '<label class="small muted"><input type="checkbox" id="showOut"> show out-of-scope problems</label></div>' +
      (p.notes ? '<p class="muted small">' + esc(p.notes) + '</p>' : '') +
      '<div class="timer-bar no-print"><span class="clock" id="clock">' + (p.duration_min || 90) + ':00</span>' +
        '<button class="btn primary small" id="tStart">Solve on time (' + (p.duration_min || 90) + ' min)</button>' +
        '<button class="btn small" id="tStop" hidden>Stop &amp; show solutions</button>' +
        '<span class="small muted" id="tNote">Solutions stay hidden until you press a button.</span></div>' +
      '<div id="plist"></div>';
    var list = A.qs('#plist', app), timed = false;
    function draw() {
      list.innerHTML = '';
      (p.problems || []).forEach(function (id) {
        var q = A.probById[id]; if (!q) return;
        if (q.out_of_scope && !showOut) return;
        list.appendChild(problemCard(q, { label: '#' + q.number, noSolution: timed, showSource: true }));
      });
      A.renderMath(list);
    }
    draw();
    A.qs('#showOut', app).addEventListener('change', function (e) { showOut = e.target.checked; draw(); });
    var iv = null, end = 0, clock = A.qs('#clock', app);
    function tick() {
      var left = end - Date.now(), f = A.fmtDuration(left);
      clock.textContent = (f.h * 60 + f.m) + ':' + A.pad(f.s);
      clock.classList.toggle('low', left < 10 * 60 * 1000);
      if (left <= 0) stop();
    }
    function stop() { clearInterval(iv); iv = null; timed = false; A.qs('#tStart', app).hidden = false; A.qs('#tStop', app).hidden = true; A.qs('#tNote', app).textContent = 'Time stopped. Solutions are available below.'; draw(); }
    A.qs('#tStart', app).addEventListener('click', function () {
      timed = true; end = Date.now() + (p.duration_min || 90) * 60000; draw(); tick(); iv = setInterval(tick, 1000);
      A.qs('#tStart', app).hidden = true; A.qs('#tStop', app).hidden = false; A.qs('#tNote', app).textContent = 'Write full solutions on paper.';
    });
    A.qs('#tStop', app).addEventListener('click', stop);
    A.onLeave(function () { clearInterval(iv); });
  });

  /* ======================= practice ======================= */
  A.route(/^\/practice$/, function (app, m, q) {
    var secs = D.sections, tps = A.topics();
    var weak = q.weak ? A.weakTopics() : null;
    app.innerHTML =
      '<h1>Practice</h1>' +
      '<div class="filters no-print">' +
        '<select id="fSec"><option value="">All sections</option>' + secs.map(function (s) { return '<option value="' + s.id + '">§' + s.id + ' ' + esc(s.short) + '</option>'; }).join('') + '</select>' +
        '<select id="fTop"><option value="">All topics</option>' + tps.map(function (t) { return '<option>' + esc(t) + '</option>'; }).join('') + '</select>' +
        '<select id="fDiff"><option value="">Any difficulty</option><option value="easy">easy</option><option value="exam">exam-level</option><option value="hard">hard</option></select>' +
        '<select id="fOrig"><option value="">All sources</option><option value="past">Past paper</option><option value="homework">Homework (WeBWorK)</option><option value="generated">Generated</option></select>' +
        '<select id="fStat"><option value="">Any status</option><option value="none">Not marked</option><option value="solved">Solved</option><option value="unsure">Unsure</option><option value="unsolved">Unsolved</option></select>' +
        '<select id="fPaper"><option value="">All papers / sets</option>' + D.papers.map(function (p) { return '<option value="' + esc(p.id) + '">' + esc(p.short || p.title) + '</option>'; }).join('') + '</select>' +
        '<button class="btn small" id="fShuffle">Shuffle</button>' +
      '</div>' +
      (weak ? '<div class="note info">Showing weak topics: ' + (weak.length ? weak.map(esc).join(', ') : 'none yet') + ' · <a href="#/practice">clear</a></div>' : '') +
      '<div class="count-line" id="cnt"></div><div id="list"></div>';
    var f = { section: q.section || '', topic: q.topic || '', difficulty: q.difficulty || '', origin: q.origin || '', status: q.status || '', paper: q.paper || '' };
    var map = { section: 'fSec', topic: 'fTop', difficulty: 'fDiff', origin: 'fOrig', status: 'fStat', paper: 'fPaper' };
    Object.keys(map).forEach(function (k) { A.qs('#' + map[k], app).value = f[k]; });
    var order = null;
    function draw() {
      var ps = D.problems.filter(function (p) {
        if (!A.listed(p)) return false;
        if (weak && weak.indexOf(p.topic) < 0) return false;
        if (f.section && p.section !== f.section) return false;
        if (f.topic && p.topic !== f.topic) return false;
        if (f.difficulty && p.difficulty !== f.difficulty) return false;
        if (f.origin && p.origin !== f.origin) return false;
        if (f.paper && p.paper !== f.paper && (p.also_in || []).indexOf(f.paper) < 0) return false;
        var s = Store.status(p.id);
        if (f.status === 'none' && s) return false;
        if (f.status && f.status !== 'none' && s !== f.status) return false;
        return true;
      });
      if (order) ps.sort(function (a, b) { return (order[a.id] || 0) - (order[b.id] || 0); });
      A.qs('#cnt', app).textContent = ps.length + ' problems' + (ps.length > 60 ? ' (showing first 60 — narrow the filters)' : '');
      var list = A.qs('#list', app); list.innerHTML = '';
      if (!ps.length) list.innerHTML = '<div class="empty">No problems match these filters yet.</div>';
      ps.slice(0, 60).forEach(function (p) { list.appendChild(problemCard(p, { permalink: true })); });
      A.renderMath(list);
    }
    Object.keys(map).forEach(function (k) {
      A.qs('#' + map[k], app).addEventListener('change', function (e) {
        f[k] = e.target.value; var qq = {}; Object.keys(f).forEach(function (x) { qq[x] = f[x]; }); if (q.weak) qq.weak = 1;
        A.setQuery('/practice', qq); draw();
      });
    });
    A.qs('#fShuffle', app).addEventListener('click', function () {
      order = {}; D.problems.forEach(function (p) { order[p.id] = Math.random(); }); draw();
    });
    draw();
  });

  A.route(/^\/problem\/(.+)$/, function (app, m) {
    var p = A.probById[decodeURIComponent(m[0])];
    if (!p) { app.innerHTML = '<div class="empty">Unknown problem.</div>'; return; }
    var pa = A.paperById[p.paper];
    app.innerHTML = '<div class="muted small"><a href="#/practice">Practice</a>' + (pa ? ' · from <a href="#/paper/' + esc(pa.id) + '">' + esc(pa.title) + '</a>' : '') + '</div>';
    app.appendChild(problemCard(p, { showSource: true }));
    if (p.also_in && p.also_in.length) {
      app.appendChild(A.h('<p class="small muted">Also appears in: ' + p.also_in.map(function (id) {
        var x = A.paperById[id]; return x ? '<a href="#/paper/' + esc(id) + '">' + esc(x.title) + '</a>' : esc(id);
      }).join(', ') + '</p>'));
    }
  });

  /* ======================= statistics ======================= */
  A.route(/^\/stats$/, function (app) {
    var st = D.stats || {}, bySec = st.by_section || {}, byTop = st.by_topic || {}, ach = st.by_section_achenef || {};
    var past = D.problems.filter(function (p) { return p.origin === 'past'; });
    var total = Object.keys(bySec).reduce(function (a, k) { return a + bySec[k]; }, 0) || 1;
    function bars(obj, labelFn, linkFn, extra) {
      var keys = Object.keys(obj).sort(function (a, b) { return obj[b] - obj[a]; });
      var max = obj[keys[0]] || 1;
      return '<div class="table-wrap"><table><tbody>' + keys.map(function (k) {
        return '<tr><td style="width:42%"><a href="' + linkFn(k) + '">' + labelFn(k) + '</a></td><td style="width:38%"><div class="bar" style="margin:6px 0"><i style="width:' + (100 * obj[k] / max) + '%;background:var(--accent)"></i></div></td>' +
          '<td style="text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap">' + obj[k] + ' <span class="muted small">(' + Math.round(100 * obj[k] / total) + '%)</span></td>' +
          (extra ? '<td style="text-align:right;white-space:nowrap" class="small muted">' + extra(k) + '</td>' : '') + '</tr>';
      }).join('') + '</tbody></table></div>';
    }
    if (!total || !past.length) { app.innerHTML = '<h1>Statistics</h1><div class="empty">No past-paper problems yet.</div>'; return; }
    var splitPapers = D.papers.filter(function (p) { return p.split !== false; }).length;
    app.innerHTML = '<h1>Statistics of past papers</h1>' +
      '<p class="muted">' + splitPapers + ' papers split into ' + past.length + ' problems; ' + total + ' in-scope problem occurrences (duplicates merged and counted once per paper). ' +
      'This drives the mock-exam weights and the lesson order.</p>' +
      '<div class="card"><h2 style="margin-top:0">By section</h2><p class="small muted">Last column: how many of them come from our instructor (Achenef: Fall 2025 tests + this year\'s review).</p>' +
        bars(bySec, function (k) { var s = A.secById[k]; return '§' + k + ' ' + (s ? esc(s.short) : ''); }, function (k) { return '#/practice?section=' + k + '&origin=past'; }, function (k) { return ach[k] ? 'Achenef ×' + ach[k] : ''; }) + '</div>' +
      '<div class="card"><h2 style="margin-top:0">By problem type</h2>' +
        bars(byTop, function (k) { return esc(k) + ' <span class="muted small">§' + ((st.topic_sections || {})[k] || []).join(', §') + '</span>'; }, function (k) { return '#/practice?topic=' + encodeURIComponent(k); }) + '</div>' +
      '<div class="card"><h2 style="margin-top:0">Sections with no past problems</h2><p class="small">' +
        D.sections.filter(function (s) { return !bySec[s.id]; }).map(function (s) { return '<a class="tag warn" href="' + A.lessonHref(s.id) + '">§' + s.id + ' ' + esc(s.short) + '</a>'; }).join(' ') +
        '</p><p class="small muted">Covered only by lessons and generated problems.</p></div>' +
      '<div class="card"><h2 style="margin-top:0">Out-of-scope problems found (hidden)</h2><p class="small muted">' +
        Object.keys(st.out_of_scope_by_section || {}).map(function (k) { return '§' + k + ' ×' + st.out_of_scope_by_section[k]; }).join(' · ') + '</p></div>';
  });

  /* ======================= cheat sheet ======================= */
  A.route(/^\/cheatsheet$/, function (app) {
    app.innerHTML = '<div class="btn-row no-print" style="margin-bottom:12px"><h1 style="margin:0">Cheat sheet</h1><button class="btn" onclick="window.print()">Print (A4)</button></div>' +
      (D.cheatsheet ? '<div class="cheatsheet">' + D.cheatsheet + '</div>' : '<div class="empty">The cheat sheet is not ready yet.</div>');
  });

  /* ======================= resources ======================= */
  A.route(/^\/resources$/, function (app) {
    var html = '<h1>Resources</h1><p class="muted">Notes, cheat sheets and solutions found in Telegram and Moodle. Only files that were actually opened are described.</p>';
    if (!D.resources.length) html += '<div class="empty">No resources collected yet.</div>';
    D.resources.forEach(function (r) {
      html += '<div class="card"><div class="problem-head"><b>' + esc(r.title) + '</b>' +
        (r.sections || []).map(function (s) { return '<a class="tag" href="' + A.lessonHref(s) + '">§' + esc(s) + '</a>'; }).join(' ') +
        '<span class="tag">' + esc(r.source || '') + '</span></div>' +
        '<div class="small">' + (r.note || '') + '</div>' +
        '<div class="btn-row" style="margin-top:8px">' + (r.files || []).map(function (f) {
          var local = /^(localhost|127\.0\.0\.1|\d+\.\d+\.\d+\.\d+)$/.test(location.hostname);
          if (!local && f.indexOf('materials/textbook/') === 0) return '<span class="small muted">The textbook PDF is not on the online site: take it from the MATH 161 Telegram group.</span>';
          return '<a class="btn small" target="_blank" href="' + esc(f) + '">' + esc(f.split('/').pop()) + '</a>';
        }).join('') + '</div></div>';
    });
    app.innerHTML = html;
  });

  /* ======================= study plan ======================= */
  A.route(/^\/plan$/, function (app) {
    var done = Store.get('planDone', {}) || {};
    var html = '<h1>Study plan</h1><p class="muted">Until Saturday 28 November, 12:00. Tick tasks as you go (saved in this browser).</p>';
    if (!D.plan.length) html += '<div class="empty">The plan is not ready yet.</div>';
    D.plan.forEach(function (day, di) {
      html += '<div class="card"><h2 style="margin-top:0">' + esc(day.day) + '</h2>' + (day.focus ? '<div class="muted small">' + esc(day.focus) + '</div>' : '') + '<ul style="list-style:none;padding:0;margin:8px 0 0">';
      (day.tasks || []).forEach(function (t, ti) {
        var k = di + '.' + ti;
        html += '<li style="margin:6px 0"><label><input type="checkbox" data-k="' + k + '"' + (done[k] ? ' checked' : '') + '> ' + t.text + '</label>' +
          (t.href ? ' <a href="' + esc(t.href) + '">open →</a>' : '') + (t.min ? ' <span class="muted small">~' + t.min + ' min</span>' : '') + '</li>';
      });
      html += '</ul></div>';
    });
    app.innerHTML = html;
    app.addEventListener('change', function (e) {
      var k = e.target.dataset && e.target.dataset.k; if (!k) return;
      var d = Store.get('planDone', {}) || {}; if (e.target.checked) d[k] = 1; else delete d[k]; Store.set('planDone', d);
    });
  });
})();
