---
title: "Goals"
summary: "미래의 계획과 목표, 달성을 기록합니다."
sort_by: date
sort_ascending: false
image:
  filename: /media/path.jpg
  preview_only: false
cascade:
  show_breadcrumb: true
---

<style>
/* ====== Goals page: hero & layout ====== */
.kjh-hero{ position: relative; min-height: 42vh; display: grid; place-items: center; overflow: hidden; border-radius: 16px; }
.kjh-hero::before{
  content: ""; position:absolute; inset:0;
  background-image: var(--hero-img, url('/media/goals-hero.jpg'));
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
.dark .kjh-sep::before { background: linear-gradient(90deg, transparent, rgba(255,255,255,.35), transparent); }
.dark .kjh-sep span { background: #0D1B2A; color: #fff; }

/* 본문 2열 레이아웃 (새 디자인) */
.goals-grid{ width:min(1100px,96%); margin:0 auto 3rem; display:grid; grid-template-columns: 1fr 1fr; gap:1.4rem; }
@media (max-width: 900px){ .goals-grid{ grid-template-columns: 1fr; } }

.goal-card{ position:relative; border-radius:16px; overflow:hidden; background:#fff; border:1px solid rgba(23,42,62,.08); box-shadow:0 10px 30px rgba(0,0,0,.06); }
.dark .goal-card{ background:#0D1B2A; border-color: rgba(255,255,255,.12); }

.goal-head{ display:flex; align-items:center; gap:.6rem; padding:.85rem 1rem; background:linear-gradient(90deg,#172a3e 0%, #1f3550 100%); color:#fff; }
.goal-head .emoji{ font-size:1.2rem; }
.goal-head h2{ font-size:1.05rem; font-weight:800; letter-spacing:.02em; margin:0; }

.goal-body{ padding:1rem 1.15rem 1.1rem; }

/* 활동 내역 - 세로 타임라인 */
.timeline{ position:relative; list-style:none; margin:0; padding-left:1.25rem; }
.timeline::before{ content:""; position:absolute; left:.5rem; top:.2rem; bottom:.2rem; width:2px; background:rgba(23,42,62,.25); }
.dark .timeline::before{ background:rgba(255,255,255,.25); }
.timeline li{ position:relative; margin:.6rem 0; }
.timeline li::before{ content:""; position:absolute; left:-.1rem; top:.42rem; width:.55rem; height:.55rem; border-radius:50%; background:#172a3e; box-shadow:0 0 0 3px rgba(23,42,62,.15); }
.dark .timeline li::before{ background:#fff; box-shadow:0 0 0 3px rgba(255,255,255,.18); }
.timeline time{ display:inline-block; min-width:7.4rem; font-weight:800; font-size:.92rem; color:#172a3e; }
.dark .timeline time{ color:#fff; }

/* 미래 계획 - 체크칩 스타일 */
.plan-list{ list-style:none; margin:0; padding:0; display:grid; gap:.55rem; }
.plan-list li{ display:flex; align-items:center; gap:.6rem; padding:.55rem .7rem; border-radius:12px; background:#f5f6f7; border:1px solid rgba(23,42,62,.08); }
.plan-list .badge{ display:inline-grid; place-items:center; width:1.35rem; height:1.35rem; border-radius:50%; font-size:.8rem; font-weight:900; color:#fff; background:#2c65c0; }
.dark .plan-list li{ background:#162332; border-color:rgba(255,255,255,.14); }
.dark .plan-list .badge{ background:#06D6A0; color:#0D1B2A; }
.plan-list .soon{ background:#ffb703; color:#172a3e; }

/* CTA 버튼 - 우측 정렬 */
.card-cta{ display:flex; gap:.5rem; flex-wrap:wrap; margin-top:.8rem; }
.card-cta .kjh-btn{ display:inline-flex; align-items:center; gap:.4rem; padding:.52rem .8rem; border-radius:10px; font-weight:700; border:1px solid rgba(23,42,62,.18); color:#172a3e; background:#fff; text-decoration:none; }
.card-cta .kjh-btn:hover{ background:#f5f6f7; border-color:rgba(23,42,62,.28); }
.dark .card-cta .kjh-btn{ background:#162332; color:#fff; border-color:rgba(255,255,255,.18); }
.dark .card-cta .kjh-btn:hover{ background:#1b2b40; border-color:rgba(255,255,255,.28); }
</style>

<section class="kjh-hero" style="--hero-img:url('/media/goals-hero.jpg')">
  <div class="kjh-hero__inner">
    <h1>Goals</h1>
    <p>미래의 계획과 목표, 달성을 기록합니다.</p>
  </div>
</section>

<div class="kjh-sep"><span>OVERVIEW</span></div>

<section class="goals-grid">
  <article class="goal-card">
    <div class="goal-head"><span class="emoji">📅</span><h2>활동 내역</h2></div>
    <div class="goal-body">
      <ul class="timeline">
        <li><time>2023-05-20</time> TOPCIT 응시 — 수준 2</li>
        <li><time>2023-06-24</time> 전주 ICT · AI 코딩 대회</li>
        <li><time>2023-2학기</time> 진로캠프</li>
        <li><time>2024-1학기</time> 취업 트렌드 특강 · 해외취업 특강</li>
        <li><time>2025-09-27~28</time> WHO 동아리 · SW사업단 대회 운영</li>
        <li><time>2025-2학기</time> AI JOB@JBNU 시범운영단 활동</li>
      </ul>
      <div class="card-cta">
        <a class="kjh-btn" href="/goals/roadmap/">로드맵 보기</a>
        <a class="kjh-btn" href="/goals/certs/">자격증 보기</a>
      </div>
    </div>
  </article>

  <article class="goal-card">
    <div class="goal-head"><span class="emoji">🎯</span><h2>미래 계획</h2></div>
    <div class="goal-body">
      <ul class="plan-list">
        <li><span class="badge">✓</span> 프론트엔드 부트캠프 수료 <em class="soon" style="margin-left:.35rem; padding:.08rem .4rem; border-radius:.5rem; font-style:normal; font-size:.82rem;">예정</em></li>
        <li><span class="badge">✓</span> 알고리즘·네트워크 스터디 정례화</li>
        <li><span class="badge">✓</span> 보안 실습 프로젝트 고도화 및 정리</li>
        <li><span class="badge">✓</span> 오픈소스 기여 2건 이상</li>
      </ul>
      <div class="card-cta">
        <a class="kjh-btn" href="/project/">프로젝트 보기</a>
        <a class="kjh-btn" href="/contact/">연락하기</a>
      </div>
    </div>
  </article>
</section>