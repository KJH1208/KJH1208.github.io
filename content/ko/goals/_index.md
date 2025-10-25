---
title: "Goals"
summary: "미래의 계획과 목표, 달성을 기록합니다."
sort_by: date
sort_ascending: false
image:
  filename: /media/achieve.jpg
  preview_only: false
cascade:
  show_breadcrumb: true
---

<style>
/* ====== Goals page: hero & layout ====== */
.kjh-hero{ position: relative; min-height: 42vh; display: grid; place-items: center; overflow: hidden; border-radius: 16px; }
.kjh-hero::before{
  content: ""; position:absolute; inset:0;
  background-image: var(--hero-img, url('/media/achieve.jpg'));
  background-size: cover; background-position: center; filter: brightness(.55);
}
.kjh-hero::after{ /* 위-아래 그라데이션으로 가독성 보강 */
  content:""; position:absolute; inset:0;
  background: linear-gradient(to bottom, rgba(0,0,0,.30), rgba(0,0,0,.15) 40%, rgba(0,0,0,.45));
}
.kjh-hero__inner{ position: relative; z-index: 1; text-align: center; padding: 3rem 1rem; color:#fff; }
.kjh-hero__inner h1{ font-size: clamp(2rem, 3.6vw, 3rem); font-weight: 800; margin: 0 0 .4rem; }
.kjh-hero__inner p{ font-size: clamp(1rem, 1.6vw, 1.2rem); opacity:.95; margin:0; }
.dark .kjh-hero::before{ filter: brightness(.6); }

/* 구분선 */
.kjh-sep { position: relative; width: min(900px, 92%); margin: 2.5rem auto 1.75rem; text-align: center; }
.kjh-sep::before { content: ""; display: block; height: 1px; background: linear-gradient(90deg, transparent, rgba(23,42,62,0.45), transparent); }
.kjh-sep span { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: #fff; color: #172a3e; font-weight: 600; font-size: .95rem; padding: 0 .75rem; }
.dark .kjh-sep::before { background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 1), transparent); }
.dark .kjh-sep span { background: #0D1B2A; color: #fff; }

/* 본문 2열 레이아웃 */
.goals-wrap{ width:min(1100px, 96%); margin:0 auto 3rem; display:grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
@media (max-width: 900px){ .goals-wrap{ grid-template-columns: 1fr; } }
.goals-col{ background:#fff; border:1px solid rgba(13,27,42,.08); border-radius:14px; padding:1.25rem 1.25rem 1.1rem; box-shadow: 0 6px 20px rgba(0,0,0,.06); }
.dark .goals-col{ background:#0D1B2A; border-color: rgba(255,255,255,.12); }
.goals-col h2{ font-size:1.15rem; margin:.1rem 0 1rem; color:#172a3e; font-weight:800; letter-spacing:.02em; }
.dark .goals-col h2{ color:#fff; }

/* 타임라인 스타일 (활동 내역) */
.timeline{ list-style:none; margin:0; padding:0; }
.timeline li{ position:relative; padding-left:1.1rem; margin:.65rem 0; }
.timeline li::before{ content:""; position:absolute; left:0; top:.55rem; width:.42rem; height:.42rem; border-radius:50%; background:#172a3e; }
.dark .timeline li::before{ background:#fff; }
.timeline time{ font-weight:700; color:#172a3e; margin-right:.35rem; }
.dark .timeline time{ color:#fff; }

/* 체크리스트 (미래 계획) */
.checklist{ list-style:none; margin:0; padding:0; }
.checklist li{ position:relative; padding-left:1.6rem; margin:.5rem 0; }
.checklist li::before{ content:"✓"; position:absolute; left:.15rem; top:0; color:#2c65c0; font-weight:800; }
.dark .checklist li::before{ color:#06D6A0; }

/* CTA 버튼 */
.kjh-cta{ display:flex; gap:.5rem; flex-wrap:wrap; margin-top:.75rem; }
.kjh-btn{ display:inline-flex; align-items:center; gap:.4rem; padding:.52rem .8rem; border-radius:10px; font-weight:700; border:1px solid rgba(23,42,62,.18); color:#172a3e; background:#fff; text-decoration:none; }
.kjh-btn:hover{ background:#f5f6f7; border-color:rgba(23,42,62,.28); }
.dark .kjh-btn{ background:#162332; color:#fff; border-color:rgba(255,255,255,.18); }
.dark .kjh-btn:hover{ background:#1b2b40; border-color:rgba(255,255,255,.28); }
</style>

<section class="kjh-hero" style="--hero-img:url('/media/achieve.jpg')">
  <div class="kjh-hero__inner">
    <h1>Goals</h1>
    <p>미래의 계획과 목표, 달성을 기록합니다.</p>
  </div>
</section>

<div class="kjh-sep"><span>OVERVIEW</span></div>