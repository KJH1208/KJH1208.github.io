---
title: "📄 자격증"
type: page
summary: "최근 취득 및 준비 중인 자격증"
image:
  filename: /media/book.jpg
  preview_only: false
show_breadcrumb: true
share: false
---
<section class="kjh-hero" style="position:relative; overflow:hidden; border-radius:16px; margin-bottom:2rem;">
  <img src="/media/book.jpg" 
       alt="자격증 대표 이미지" 
       style="width:100%; height:280px; object-fit:cover; filter:brightness(0.75); border-radius:16px;">
  <div style="position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center; align-items:center; color:#fff;">
    <h1 style="font-size:2.2rem; font-weight:800; margin:0;">자격증</h1>
    <p style="font-size:1.1rem; opacity:0.9;">최근 취득 및 준비 중인 자격증</p>
  </div>
</section>
<style>
/* ====== KJH Certs Page (scoped) ====== */
.kjh-certs{ 
  --navy:#0D1B2A; --ink:#1B263B; --muted:#6B7280; 
  --bg:#FFFFFF; --bg-alt:#F5F6F7; --line:#E5E7EB; 
  --brand:#3A86FF; --mint:#06D6A0;
  max-width: 920px; margin: 0 auto; padding: 0 1rem 2rem; 
}
.kjh-certs .page-subtitle{ 
  font-size: 1.6rem; font-weight: 700; color: var(--navy); 
  margin: 1.2rem 0 1rem; letter-spacing: .2px;
}

/* Card list */
.kjh-certs .cert-list{ display: grid; gap: 14px; }
.kjh-certs .cert-card{
  display: grid; grid-template-columns: 64px 1fr; align-items: center;
  background: var(--bg); border: 1px solid var(--line); border-radius: 14px;
  padding: 14px 16px; box-shadow: 0 2px 10px rgba(13,27,42,.04);
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.kjh-certs .cert-card:hover{ 
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(13,27,42,.08);
  border-color: rgba(58,134,255,.35);
}

/* Icon */
.kjh-certs .cert-icon{ 
  width: 56px; height: 56px; border-radius: 12px; 
  display: grid; place-items: center; font-size: 28px; 
  background: linear-gradient(135deg, rgba(58,134,255,.18), rgba(6,214,160,.18));
  color: var(--navy);
  align-self: center;
}

/* Body */
.kjh-certs .cert-body h3{
  margin: 2px 0 6px;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--ink);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.kjh-certs .cert-meta{ 
  display: flex; flex-wrap: wrap; gap: 8px 12px; margin: 0 0 8px; padding: 0; list-style: none;
}
.kjh-certs .cert-meta li{ color: var(--muted); font-size: .95rem; line-height: 1.4; }
.kjh-certs .cert-desc{ color: #374151; line-height: 1.6; margin: 2px 0 0; }

/* Chips */
.kjh-certs .chip{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: .76rem;
  font-weight: 600;
  line-height: 1;
  letter-spacing: .2px;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: #fff;
  color: var(--navy);
}
/* 예정 */
.kjh-certs .chip.pending{
  background: rgba(58,134,255,.08); /* ← 투명도 조절(0.05~0.15 추천) */
  border-color: rgba(58,134,255,.35);
}

/* 취득 */
.kjh-certs .chip.done{
  background: rgba(6,214,160,.08);  /* ← 투명도 조절 */
  border-color: rgba(6,214,160,.35);
}
@media (max-width: 640px){
  .kjh-certs .cert-card{ grid-template-columns: 48px 1fr; padding: 12px 12px; }
  .kjh-certs .cert-icon{ width: 48px; height: 48px; font-size: 24px; }
}
</style>

<div class="kjh-certs">
  <h2 class="page-subtitle"> 자격증 목록</h2>

  <div class="cert-list">
    <article class="cert-card">
      <div class="cert-icon">💡</div>
      <div class="cert-body">
        <h3><a href="https://www.q-net.or.kr/" target="_blank">정보처리기사</a> <span class="chip pending">예정</span></h3>
        <ul class="cert-meta">
          <li>기관: 한국산업인력공단</li>
          <li>취득 예정: 2026년 상반기</li>
        </ul>
        <p class="cert-desc">필기 및 실기 준비 과정을 진행 중이며, 데이터베이스·운영체제·네트워크 중심으로 학습 중입니다.</p>
      </div>
    </article>

<article class="cert-card">
      <div class="cert-icon">💡</div>
      <div class="cert-body">
        <h3><a href="https://www.topcit.or.kr/" target="_blank">TOPCIT 수준 2</a> <span class="chip done">취득</span></h3>
        <ul class="cert-meta">
          <li>기관: 정보통신산업진흥원(NIPA)</li>
          <li>취득일: 2023년 상반기</li>
        </ul>
        <p class="cert-desc">소프트웨어 개발, 데이터 관리, ICT 문제해결 역량 평가에서 수준 2를 달성했습니다.</p>
      </div>
    </article>

<article class="cert-card">
      <div class="cert-icon">💡</div>
      <div class="cert-body">
        <h3><a href="https://www.historyexam.go.kr/" target="_blank">한국사능력검정시험</a> <span class="chip pending">예정</span></h3>
        <ul class="cert-meta">
          <li>기관: 국사편찬위원회</li>
          <li>응시 예정: 2026-02</li>
        </ul>
        <p class="cert-desc">한국사의 주요 시대 구분, 정치·문화사 및 근현대사 중심으로 학습 중입니다.</p>
      </div>
    </article>

<article class="cert-card">
      <div class="cert-icon">💡</div>
      <div class="cert-body">
        <h3><a href="https://license.korcham.net/" target="_blank">컴퓨터활용능력 1급</a> <span class="chip pending">예정</span></h3>
        <ul class="cert-meta">
          <li>기관: 대한상공회의소</li>
          <li>응시 예정: 2025-12</li>
        </ul>
        <p class="cert-desc">엑셀과 액세스를 활용한 데이터 분석, 업무자동화 및 함수 활용 중심 학습 진행 중.</p>
      </div>
    </article>

<article class="cert-card">
      <div class="cert-icon">💡</div>
      <div class="cert-body">
        <h3><a href="https://www.dataq.or.kr/" target="_blank">SQLD (SQL 개발자)</a> <span class="chip pending">예정</span></h3>
        <ul class="cert-meta">
          <li>기관: 한국데이터산업진흥원</li>
          <li>응시 예정: 2026-06</li>
        </ul>
        <p class="cert-desc">데이터 모델링, SQL 최적화, 인덱스 관리 및 성능 개선에 대한 실무 학습을 진행 중입니다.</p>
      </div>
    </article>
  </div>
</div>