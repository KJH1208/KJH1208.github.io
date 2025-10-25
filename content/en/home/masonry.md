---
widget: blank
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
    <div class="kjh-hobby-card__inner">
      <h3>🎬 Watching Movies & Performances</h3>
      <p>I often gain energy and inspiration from visiting cinemas or live concerts.</p>
    </div>
  </div>
  <div class="kjh-hobby-card">
    <div class="kjh-hobby-card__inner">
      <h3>☕ Café Hopping</h3>
      <p>I enjoy visiting new cafés to appreciate the atmosphere, design, and aroma of each space.</p>
    </div>
  </div>
  <div class="kjh-hobby-card">
    <div class="kjh-hobby-card__inner">
      <h3>📖 Reading</h3>
      <p>I broaden my perspective by reading books on technology, self-reflection, and human relationships.</p>
    </div>
  </div>
</div>

<style>
.kjh-hobby-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:1.5rem; margin-top:1.5rem; }
.kjh-hobby-card { 
  background:#fff; border-radius:14px; box-shadow:0 4px 16px rgba(0,0,0,.08);
  padding:1.2rem 1.4rem; transition:transform .25s ease, box-shadow .25s ease;
  display:grid; align-content:center; min-height:140px;
}
.kjh-hobby-card__inner { width:100%; }
.kjh-hobby-card:hover { transform:translateY(-6px); box-shadow:0 10px 28px rgba(0,0,0,.12); }
.kjh-hobby-card h3 { font-size:1.1rem; margin:0 0 .5rem; color:#172a3e; }
.kjh-hobby-card p { margin:0; color:#374151; text-align:justify; text-justify: inter-word;line-height:1.55; }
.dark .kjh-hobby-card { background:#0D1B2A; color:#fff; box-shadow:0 4px 12px rgba(255,255,255,.08); }
.dark .kjh-hobby-card h3,
.dark .kjh-hobby-card p {
  color: #ffffff !important;
}
</style>