---
widget: portfolio
headless: true
active: true
weight: 55
title: "Hobby & Daily"
design:
  view: masonry
  columns: 3
---


<div class="kjh-hobby-grid">
  <div class="kjh-hobby-card">
    <h3>🎬 영화/공연 감상</h3>
    <p>주말엔 주로 영화관이나 콘서트 현장에서 영감을 얻어요.</p>
  </div>
  <div class="kjh-hobby-card">
    <h3>☕ 카페 탐방</h3>
    <p>새로운 카페를 방문해 공간과 향을 기록하는 걸 좋아합니다.</p>
  </div>
  <div class="kjh-hobby-card">
    <h3>💬 소통</h3>
    <p>블로그와 GitHub를 통해 개발과 일상 이야기를 나누고 있습니다.</p>
  </div>
</div>

<style>
.kjh-hobby-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:1.5rem; margin-top:1.5rem; }
.kjh-hobby-card { background:#fff; border-radius:14px; box-shadow:0 4px 16px rgba(0,0,0,.08); padding:1.2rem 1.4rem; transition:transform .25s ease, box-shadow .25s ease; }
.kjh-hobby-card:hover { transform:translateY(-6px); box-shadow:0 10px 28px rgba(0,0,0,.12); }
.kjh-hobby-card h3 { font-size:1.1rem; margin-bottom:.5rem; color:#172a3e; }
.kjh-hobby-card p { color:#374151; text-align:justify; line-height:1.55; }
.dark .kjh-hobby-card { background:#0D1B2A; color:#fff; box-shadow:0 4px 12px rgba(255,255,255,.08); }
</style>