/* Interactive figures. A lesson places <div class="plot" data-plot="name" data-args='{...}'></div>;
   Plots.init() finds them after each page render and builds the JSXGraph board. */
(function () {
  'use strict';
  var registry = {};
  var boards = [];
  function dark() {
    var t = document.documentElement.getAttribute('data-theme');
    if (t) return t === 'dark';
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function colors() {
    return dark()
      ? { axis: '#9aa3b5', curve: '#7aa2ff', fill: '#7aa2ff', fill2: '#ff9f7a', accent: '#ffb84d', text: '#e6e9f0', good: '#4cc47f', bad: '#ff7a6b' }
      : { axis: '#5d6679', curve: '#2f5bd3', fill: '#2f5bd3', fill2: '#e0663a', accent: '#c77700', text: '#1b2130', good: '#1f8a4c', bad: '#c0392b' };
  }
  var uid = 0;
  function board(el, bbox, extra) {
    var id = el.id || ('jxg' + (++uid));
    el.id = id;
    el.classList.add('jxg');
    var c = colors();
    JXG.Options.text.color = c.text;
    var b = JXG.JSXGraph.initBoard(id, Object.assign({
      boundingbox: bbox, axis: true, showCopyright: false, showNavigation: false,
      pan: { enabled: false }, zoom: { enabled: false },
      defaultAxes: { x: { strokeColor: c.axis, ticks: { strokeColor: c.axis, label: { color: c.axis } } },
                     y: { strokeColor: c.axis, ticks: { strokeColor: c.axis, label: { color: c.axis } } } }
    }, extra || {}));
    boards.push(b);
    return b;
  }
  function init(root) {
    if (!window.JXG) return;
    boards.splice(0).forEach(function (b) { try { JXG.JSXGraph.freeBoard(b); } catch (e) {} });
    Array.prototype.forEach.call((root || document).querySelectorAll('[data-plot]'), function (wrap) {
      var name = wrap.getAttribute('data-plot'), fn = registry[name];
      if (!fn) { wrap.textContent = '[missing figure: ' + name + ']'; return; }
      var args = {};
      try { args = JSON.parse(wrap.getAttribute('data-args') || '{}'); } catch (e) {}
      try { fn(wrap, args, { board: board, colors: colors() }); } catch (e) { console.error('plot ' + name, e); }
    });
  }
  window.Plots = { register: function (n, f) { registry[n] = f; }, init: init, board: board, colors: colors };
})();

/* ---------------- figure library ---------------- */
(function () {
  'use strict';
  var R = window.Plots.register;
  function fn(expr) {
    return new Function('x', 'var sin=Math.sin,cos=Math.cos,tan=Math.tan,exp=Math.exp,log=Math.log,sqrt=Math.sqrt,abs=Math.abs,atan=Math.atan,PI=Math.PI,pow=Math.pow,cbrt=Math.cbrt; return ' + expr + ';');
  }
  function holder(wrap, controlsHtml, caption) {
    wrap.classList.add('plot-wrap');
    wrap.innerHTML = '<div class="jxg"></div>' + (controlsHtml ? '<div class="plot-controls">' + controlsHtml + '</div>' : '') +
      (caption ? '<div class="plot-caption">' + caption + '</div>' : '');
    return wrap.querySelector('.jxg');
  }
  function simpson(f, a, b) { var n = 400, h = (b - a) / n, s = f(a) + f(b); for (var i = 1; i < n; i++) s += f(a + i * h) * (i % 2 ? 4 : 2); return s * h / 3; }
  function fmt(v) { return (Math.abs(v) < 1e-10 ? 0 : v).toFixed(4); }

  /* Riemann sums: args {f, a, b, n, bbox, label} */
  R('riemann', function (wrap, a, ctx) {
    var f = fn(a.f), A = a.a, B = a.b;
    var el = holder(wrap, 'n = <input type="range" min="1" max="60" value="' + (a.n || 4) + '" class="rn"> <b class="rv"></b>' +
      ' <select class="rm"><option value="r">right endpoints</option><option value="l">left endpoints</option><option value="m">midpoints</option></select>',
      '<span class="rs"></span>');
    var c = ctx.colors, b = ctx.board(el, a.bbox || [A - 0.5, 1.5, B + 0.5, -0.5]);
    b.create('functiongraph', [f, A - 0.5, B + 0.5], { strokeColor: c.curve, strokeWidth: 2.5 });
    var rects = [];
    var nIn = wrap.querySelector('.rn'), mIn = wrap.querySelector('.rm');
    var exact = simpson(f, A, B);
    function draw() {
      b.suspendUpdate();
      rects.forEach(function (r) { b.removeObject(r); }); rects = [];
      var n = +nIn.value, dx = (B - A) / n, s = 0, m = mIn.value;
      for (var k = 0; k < n; k++) {
        var x0 = A + k * dx, xs = m === 'l' ? x0 : m === 'r' ? x0 + dx : x0 + dx / 2, h = f(xs);
        s += h * dx;
        rects.push(b.create('polygon', [[x0, 0], [x0 + dx, 0], [x0 + dx, h], [x0, h]], {
          fillColor: c.fill2, fillOpacity: 0.25, borders: { strokeColor: c.fill2, strokeWidth: 1 }, vertices: { visible: false }, fixed: true, highlight: false }));
      }
      b.unsuspendUpdate();
      wrap.querySelector('.rv').textContent = n;
      wrap.querySelector('.rs').innerHTML = 'Riemann sum ≈ ' + fmt(s) + ' &nbsp;·&nbsp; exact integral ≈ ' + fmt(exact) + ' &nbsp;·&nbsp; error ' + fmt(s - exact);
    }
    nIn.addEventListener('input', draw); mIn.addEventListener('change', draw); draw();
  });

  /* Mean Value Theorem: args {f, df, a, b, cs:[c...], bbox} */
  R('mvt', function (wrap, a, ctx) {
    var f = fn(a.f), A = a.a, B = a.b, c = ctx.colors;
    var el = holder(wrap, 'Drag the point on the curve; it turns green when the tangent is parallel to the secant.', '');
    var b = ctx.board(el, a.bbox);
    b.create('functiongraph', [f, A - 1, B + 1], { strokeColor: c.curve, strokeWidth: 2.5 });
    var pA = b.create('point', [A, f(A)], { fixed: true, name: 'a', size: 3, color: c.axis }), pB = b.create('point', [B, f(B)], { fixed: true, name: 'b', size: 3, color: c.axis });
    b.create('line', [pA, pB], { strokeColor: c.fill2, dash: 2, strokeWidth: 2 });
    var gl = b.create('glider', [(A + B) / 2, f((A + B) / 2), b.create('functiongraph', [f, A, B], { visible: false })], { name: 'c', size: 4, color: c.accent });
    var tan = b.create('tangent', [gl], { strokeColor: c.accent, strokeWidth: 2 });
    var slope = (f(B) - f(A)) / (B - A);
    b.on('update', function () {
      var h = 1e-5, d = (f(gl.X() + h) - f(gl.X() - h)) / (2 * h), ok = Math.abs(d - slope) < 0.04;
      gl.setAttribute({ color: ok ? c.good : c.accent }); tan.setAttribute({ strokeColor: ok ? c.good : c.accent });
    });
    b.update();
  });

  /* Graph of f with f' and f'' and sign info: args {f, df, d2f, bbox, show:['f','df','d2f']} */
  R('derivs', function (wrap, a, ctx) {
    var c = ctx.colors, el = holder(wrap,
      '<label><input type="checkbox" class="s0" checked> f</label> <label><input type="checkbox" class="s1"> f′</label> <label><input type="checkbox" class="s2"> f″</label>',
      a.caption || 'Where f′ &gt; 0 the graph rises; where f″ &gt; 0 it bends up.');
    var b = ctx.board(el, a.bbox);
    var g = [b.create('functiongraph', [fn(a.f)], { strokeColor: c.curve, strokeWidth: 3 }),
      b.create('functiongraph', [fn(a.df)], { strokeColor: c.fill2, strokeWidth: 2, dash: 1, visible: false }),
      b.create('functiongraph', [fn(a.d2f)], { strokeColor: c.good, strokeWidth: 2, dash: 3, visible: false })];
    [0, 1, 2].forEach(function (i) {
      var box = wrap.querySelector('.s' + i);
      if (a.show && a.show.indexOf(i) >= 0) { box.checked = true; g[i].setAttribute({ visible: true }); }
      box.addEventListener('change', function () { g[i].setAttribute({ visible: box.checked }); });
    });
  });

  /* Absolute extrema on [a,b] with sliders for the endpoints: args {f, a, b, bbox} */
  R('absext', function (wrap, a, ctx) {
    var f = fn(a.f), c = ctx.colors, el = holder(wrap, 'Drag the endpoints a and b along the x-axis.', '<span class="out"></span>');
    var b = ctx.board(el, a.bbox);
    b.create('functiongraph', [f], { strokeColor: c.axis, strokeWidth: 1, dash: 2 });
    var ax = b.create('glider', [a.a, 0, b.defaultAxes.x], { name: 'a', size: 4, color: c.fill2 });
    var bx = b.create('glider', [a.b, 0, b.defaultAxes.x], { name: 'b', size: 4, color: c.fill2 });
    b.create('functiongraph', [f, function () { return Math.min(ax.X(), bx.X()); }, function () { return Math.max(ax.X(), bx.X()); }], { strokeColor: c.curve, strokeWidth: 3 });
    var pmax = b.create('point', [0, 0], { name: 'max', fixed: true, color: c.good, size: 4 }), pmin = b.create('point', [0, 0], { name: 'min', fixed: true, color: c.bad, size: 4 });
    function upd() {
      var lo = Math.min(ax.X(), bx.X()), hi = Math.max(ax.X(), bx.X()), N = 600, best = [lo, f(lo)], worst = [lo, f(lo)];
      for (var i = 0; i <= N; i++) { var x = lo + (hi - lo) * i / N, y = f(x); if (y > best[1]) best = [x, y]; if (y < worst[1]) worst = [x, y]; }
      pmax.setPosition(JXG.COORDS_BY_USER, best); pmin.setPosition(JXG.COORDS_BY_USER, worst);
      wrap.querySelector('.out').textContent = 'On [' + lo.toFixed(2) + ', ' + hi.toFixed(2) + ']: max ≈ ' + best[1].toFixed(3) + ' at x ≈ ' + best[0].toFixed(2) + ', min ≈ ' + worst[1].toFixed(3) + ' at x ≈ ' + worst[0].toFixed(2);
    }
    b.on('update', upd); upd(); b.update();
  });

  /* Area function A(x)=∫_a^x f(t)dt : args {f, a, bbox} */
  R('ftc', function (wrap, a, ctx) {
    var f = fn(a.f), c = ctx.colors, A0 = a.a, el = holder(wrap, 'Drag x. Blue: y = f(t). Orange: the area function A(x) = ∫ from a to x of f(t) dt. Its slope at x equals f(x).', '<span class="out"></span>');
    var b = ctx.board(el, a.bbox);
    b.create('functiongraph', [f], { strokeColor: c.curve, strokeWidth: 2.5 });
    var X = b.create('glider', [A0 + 1.5, 0, b.defaultAxes.x], { name: 'x', size: 4, color: c.accent });
    b.create('integral', [[A0, function () { return X.X(); }], b.create('functiongraph', [f], { visible: false })], { fillColor: c.fill, fillOpacity: 0.2, label: { visible: false }, curveLeft: { visible: false }, curveRight: { visible: false } });
    var Af = function (x) { return simpson(f, A0, x); };
    b.create('functiongraph', [Af], { strokeColor: c.fill2, strokeWidth: 2.5 });
    var P = b.create('point', [function () { return X.X(); }, function () { return Af(X.X()); }], { name: 'A(x)', size: 3, color: c.fill2 });
    b.create('line', [P, [function () { return X.X() + 1; }, function () { return Af(X.X()) + f(X.X()); }]], { strokeColor: c.fill2, dash: 2, straightFirst: true, straightLast: true });
    function upd() { wrap.querySelector('.out').textContent = 'x = ' + X.X().toFixed(2) + ':  A(x) ≈ ' + Af(X.X()).toFixed(3) + ',  slope of A = f(x) ≈ ' + f(X.X()).toFixed(3); }
    b.on('update', upd); upd();
  });

  /* Velocity: displacement vs distance: args {v, a, b, bbox} */
  R('motion', function (wrap, a, ctx) {
    var v = fn(a.v), c = ctx.colors, el = holder(wrap, '', '<span class="out"></span>');
    var b = ctx.board(el, a.bbox);
    var g = b.create('functiongraph', [v, a.a, a.b], { strokeColor: c.curve, strokeWidth: 2.5 });
    b.create('integral', [[a.a, a.b], g], { fillColor: c.fill, fillOpacity: 0.25, label: { visible: false }, curveLeft: { visible: false }, curveRight: { visible: false } });
    var disp = simpson(v, a.a, a.b), dist = simpson(function (t) { return Math.abs(v(t)); }, a.a, a.b);
    wrap.querySelector('.out').innerHTML = 'displacement = ∫v dt ≈ <b>' + fmt(disp) + '</b> &nbsp;·&nbsp; distance = ∫|v| dt ≈ <b>' + fmt(dist) + '</b> (area below the axis counts as negative in the first, positive in the second)';
  });

  /* Average value rectangle: args {f, a, b, bbox} */
  R('avg', function (wrap, a, ctx) {
    var f = fn(a.f), c = ctx.colors, el = holder(wrap, '', '<span class="out"></span>');
    var b = ctx.board(el, a.bbox);
    var g = b.create('functiongraph', [f, a.a, a.b], { strokeColor: c.curve, strokeWidth: 2.5 });
    b.create('integral', [[a.a, a.b], g], { fillColor: c.fill, fillOpacity: 0.18, label: { visible: false }, curveLeft: { visible: false }, curveRight: { visible: false } });
    var av = simpson(f, a.a, a.b) / (a.b - a.a);
    b.create('polygon', [[a.a, 0], [a.b, 0], [a.b, av], [a.a, av]], { fillColor: c.fill2, fillOpacity: 0.15, borders: { strokeColor: c.fill2, dash: 2 }, vertices: { visible: false }, fixed: true });
    wrap.querySelector('.out').innerHTML = 'f<sub>ave</sub> ≈ ' + fmt(av) + ': the orange rectangle of height f<sub>ave</sub> has the same area as the region under the curve.';
  });

  /* Signed area: args {f, a, b, bbox} */
  R('netarea', function (wrap, a, ctx) {
    var f = fn(a.f), c = ctx.colors, el = holder(wrap, '', '<span class="out"></span>');
    var b = ctx.board(el, a.bbox);
    var g = b.create('functiongraph', [f, a.a, a.b], { strokeColor: c.curve, strokeWidth: 2.5 });
    b.create('integral', [[a.a, a.b], g], { fillColor: c.fill, fillOpacity: 0.25, label: { visible: false }, curveLeft: { visible: false }, curveRight: { visible: false } });
    wrap.querySelector('.out').innerHTML = '∫ f dx ≈ ' + fmt(simpson(f, a.a, a.b)) + ' (net signed area) · total area ∫|f| dx ≈ ' + fmt(simpson(function (x) { return Math.abs(f(x)); }, a.a, a.b));
  });

  /* Optimization: function of one variable with draggable point: args {f, a, b, bbox, xlabel, ylabel} */
  R('optim', function (wrap, a, ctx) {
    var f = fn(a.f), c = ctx.colors, el = holder(wrap, 'Drag the point to see how the quantity changes.', '<span class="out"></span>');
    var b = ctx.board(el, a.bbox);
    var g = b.create('functiongraph', [f, a.a, a.b], { strokeColor: c.curve, strokeWidth: 2.5 });
    var P = b.create('glider', [(a.a + a.b) / 2, f((a.a + a.b) / 2), g], { name: '', size: 4, color: c.accent });
    function upd() { wrap.querySelector('.out').textContent = (a.xlabel || 'x') + ' = ' + P.X().toFixed(3) + ' → ' + (a.ylabel || 'f') + ' = ' + P.Y().toFixed(3); }
    b.on('update', upd); upd();
  });
})();
