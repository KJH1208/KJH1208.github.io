---
title: "📄 Certificates"
type: page
summary: "Recently acquired and currently preparing certificates"
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
.kjh-certs .cert-desc {
  color: #374151;
  line-height: 1.6;
  margin: 2px 0 0;
  text-align: justify; /* ← 양쪽 정렬 추가 */
}
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
.kjh-certs .chip.pending{
  border-color: rgba(58,134,255,.35);
  color: #3A86FF;
  background: rgba(58,134,255,.08);
}
.kjh-certs .chip.done{
  border-color: rgba(6,214,160,.35);
  color: #06D6A0;
  background: rgba(6,214,160,.08);
}
@media (max-width: 640px){
  .kjh-certs .cert-card{ grid-template-columns: 48px 1fr; padding: 12px 12px; }
  .kjh-certs .cert-icon{ width: 48px; height: 48px; font-size: 24px; }
}
/* ===== Dark Mode Styling (enhanced for visibility) ===== */
.dark .kjh-certs {
  background-color: #0d1117; /* 어두운 배경 */
  color: #e6edf3; /* 기본 텍스트 밝게 */
}
.dark .kjh-certs .page-subtitle {
  color: #ffffff !important;
}
.dark .kjh-certs .cert-card {
  background: #161b22; /* 카드 배경 */
  border-color: #30363d;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}
.dark .kjh-certs .cert-card:hover {
  border-color: #58a6ff;
  box-shadow: 0 8px 20px rgba(56, 139, 253, 0.25);
}
.dark .kjh-certs .cert-body h3,
.dark .kjh-certs .cert-body h3 a {
  color: #ffffff !important;
}
.dark .kjh-certs .cert-desc,
.dark .kjh-certs .cert-meta li {
  color: #c9d1d9 !important;
}
.dark .kjh-certs .cert-icon {
  background: linear-gradient(135deg, rgba(56, 139, 253, 0.25), rgba(6, 214, 160, 0.25));
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.dark .kjh-certs .chip {
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.3);
}
.dark .kjh-certs .chip.pending {
  background: rgba(56, 139, 253, 0.18);
  border-color: rgba(56, 139, 253, 0.4);
  color: #58a6ff;
}
.dark .kjh-certs .chip.done {
  background: rgba(6, 214, 160, 0.2);
  border-color: rgba(6, 214, 160, 0.45);
  color: #39d353;
}
</style>

<div class="kjh-certs">
  <h2 class="page-subtitle"> List of Certificates</h2>

  <div class="cert-list">
    <article class="cert-card">
      <div class="cert-icon">💡</div>
      <div class="cert-body">
        <h3><a href="https://www.q-net.or.kr/" target="_blank">Engineer Information Processing</a> <span class="chip pending">예정</span></h3>
        <ul class="cert-meta">
          <li>Organization: Human Resources Development Service of Korea (HRD Korea)</li>
          <li>Expected Acquisition: First half of 2026</li>
        </ul>
        <p class="cert-desc">필Currently preparing for both written and practical exams, focusing on databases, operating systems, and networking.</p>
      </div>
    </article>

<article class="cert-card">
    <div class="cert-icon">💡</div>
    <div class="cert-body">
      <h3><a href="https://www.historyexam.go.kr/" target="_blank">Korean History Proficiency Test</a> <span class="chip pending">Planned</span></h3>
      <ul class="cert-meta">
        <li>Organization: National Institute of Korean History</li>
        <li>Planned Exam Date: February 2026</li>
      </ul>
      <p class="cert-desc">Studying major historical periods of Korea, with a focus on political, cultural, and modern/contemporary history.</p>
    </div>
  </article>

  <article class="cert-card">
    <div class="cert-icon">💡</div>
    <div class="cert-body">
      <h3><a href="https://license.korcham.net/" target="_blank">Computer Specialist in Spreadsheet & Database Level 1</a> <span class="chip pending">Planned</span></h3>
      <ul class="cert-meta">
        <li>Organization: Korea Chamber of Commerce and Industry (KCCI)</li>
        <li>Planned Exam Date: December 2025</li>
      </ul>
      <p class="cert-desc">Focusing on data analysis, business automation, and function utilization using Excel and Access.</p>
    </div>
  </article>

  <article class="cert-card">
    <div class="cert-icon">💡</div>
    <div class="cert-body">
      <h3><a href="https://www.dataq.or.kr/" target="_blank">SQLD (SQL Developer)</a> <span class="chip pending">Planned</span></h3>
      <ul class="cert-meta">
        <li>Organization: Korea Data Agency (K-DATA)</li>
        <li>Planned Exam Date: June 2026</li>
      </ul>
      <p class="cert-desc">Currently studying data modeling, SQL optimization, index management, and performance improvement in practical contexts.</p>
    </div>
  </article>
</div>