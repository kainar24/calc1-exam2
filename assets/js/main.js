(function () {
  'use strict';
  var A = window.App;
  A.qs('#themeBtn').addEventListener('click', function () {
    var cur = document.documentElement.getAttribute('data-theme');
    if (!cur) cur = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    var next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('c1e2.theme', next); } catch (e) {}
    if (window.Plots) window.Plots.init(A.qs('#app'));
  });
  A.qs('#menuBtn').addEventListener('click', function () { A.qs('#sidebar').classList.toggle('open'); });
  A.initSearch();
  window.addEventListener('hashchange', A.navigate);
  A.navigate();
})();
