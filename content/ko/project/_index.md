---
title: "프로젝트"
type: widget_page
summary: "개발 및 실습 프로젝트 모음"
image:
  filename: /media/labtab.jpg
  preview_only: false
---
<style>
/* ===== KJH — Project page custom hero (list page용) ===== */
.kjh-hero{ position: relative; min-height: 42vh; display: grid; place-items: center; overflow: hidden; border-radius: 16px; }
.kjh-hero::before{
  content: ""; position:absolute; inset:0;
  background-image: var(--hero-img, url('/media/labtab.jpg'));
  background-size: cover; background-position: center; filter: brightness(.55);
}
.kjh-hero::after{ /* 위-아래 그라데이션으로 가독성 보강 */
  content:""; position:absolute; inset:0;
  background: linear-gradient(to bottom, rgba(0,0,0,.30), rgba(0,0,0,.15) 40%, rgba(0,0,0,.45));
}
.kjh-hero__inner{ position: relative; z-index: 1; text-align: center; padding: 3rem 1rem; color:#fff; }
.kjh-hero__inner h1{ font-size: clamp(2rem, 3.6vw, 3rem); font-weight: 800; margin: 0 0 .4rem; }
.kjh-hero__inner p{ font-size: clamp(1rem, 1.6vw, 1.2rem); opacity:.95; margin:0; }

/* ===== Hero와 리스트 사이 구분선 ===== */
.kjh-sep {
  position: relative;
  width: min(900px, 92%);
  margin: 2.5rem auto 1.5rem;
  text-align: center;
}
.kjh-sep::before {
  content: "";
  display: block;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(23,42,62,0.45), transparent);
}
.kjh-sep span {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #fff;
  color: #172a3e;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0 0.75rem;
}
.dark .kjh-sep::before {
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.35), transparent);
}
.dark .kjh-sep span {
  background: #0D1B2A;
  color: #fff;
}
.dark .kjh-sep::before{ background: linear-gradient(90deg, transparent, rgba(255,255,255,.35), transparent); }
.dark .kjh-sep span{ background:#0D1B2A; color:#fff; }
</style>

/* ===== 양쪽 정렬 적용 ===== */
.home-section.wg-portfolio p,
.home-section.wg-portfolio li,
.home-section.wg-portfolio .article-style {
  text-align: justify;
}

<section class="kjh-hero" style="--hero-img:url('/media/labtab.jpg')">
  <div class="kjh-hero__inner">
    <h1>프로젝트</h1>
    <p>개발 및 실습 프로젝트 모음</p>
  </div>
</section>
<div class="kjh-sep"><span>PROJECT LIST</span></div>