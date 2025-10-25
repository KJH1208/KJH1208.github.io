---
title: "자격증"
type: page
summary: "최근 취득 및 준비 중인 자격증"
show_breadcrumb: true
---
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
  display: grid; grid-template-columns: 64px 1fr; align-items: start;
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
}

/* Body */
.kjh-certs .cert-body h3{ 
  margin: 2px 0 6px; font-size: 1.1rem; font-weight: 700; color: var(--ink);
}
.kjh-certs .cert-meta{ 
  display: flex; flex-wrap: wrap; gap: 8px 12px; margin: 0 0 8px; padding: 0; list-style: none;
}
.kjh-certs .cert-meta li{ color: var(--muted); font-size: .95rem; }
.kjh-certs .cert-desc{ color: #374151; line-height: 1.6; margin: 2px 0 0; }

/* Chips */
.kjh-certs .chip{ 
  display: inline-flex; align-items: center; gap: 6px; 
  font-size: .78rem; font-weight: 600; letter-spacing: .2px; 
  padding: 4px 8px; border-radius: 999px; border: 1px solid var(--line);
  background: var(--bg-alt); color: var(--navy);
}
.kjh-certs .chip.pending{ border-color: rgba(58,134,255,.35); color: var(--brand); background: rgba(58,134,255,.08); }
.kjh-certs .chip.done{ border-color: rgba(6,214,160,.45); color: var(--mint); background: rgba(6,214,160,.08); }

@media (max-width: 640px){
  .kjh-certs .cert-card{ grid-template-columns: 48px 1fr; padding: 12px 12px; }
  .kjh-certs .cert-icon{ width: 48px; height: 48px; font-size: 24px; }
}
</style>

<div class="kjh-certs">
  <h2 class="page-subtitle">🧾 자격증 목록</h2>

  <div class="cert-list">
    <article class="cert-card">
      <div class="cert-icon">🧠</div>
      <div class="cert-body">
        <h3>정보처리기사 <span class="chip pending">예정</span></h3>
        <ul class="cert-meta">
          <li>기관: 한국산업인력공단</li>
          <li>취득 예정: 2025년 상반기</li>
        </ul>
        <p class="cert-desc">필기 및 실기 준비 과정을 진행 중이며, 데이터베이스·운영체제·네트워크 중심으로 학습 중입니다.</p>
      </div>
    </article>

    <article class="cert-card">
      <div class="cert-icon">💻</div>
      <div class="cert-body">
        <h3>리눅스마스터 2급 <span class="chip pending">예정</span></h3>
        <ul class="cert-meta">
          <li>기관: 한국정보통신진흥협회</li>
          <li>취득(예정): 2025-02</li>
        </ul>
        <p class="cert-desc">사용자 관리, 파일 권한, 네트워크 기초 등 실무 중심의 리눅스 명령어 학습 포함.</p>
      </div>
    </article>

    <article class="cert-card">
      <div class="cert-icon">🌐</div>
      <div class="cert-body">
        <h3>네트워크관리사 2급</h3>
        <ul class="cert-meta">
          <li>기관: 한국정보통신자격협회</li>
          <li>취득(예정): 2024-12</li>
        </ul>
        <p class="cert-desc">TCP/IP, 라우팅, 스위칭 기초와 실제 네트워크 구성 실습 진행 중.</p>
      </div>
    </article>
  </div>
</div>