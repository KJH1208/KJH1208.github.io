---
widget: blank
headless: true
active: true
weight: 56
title: "Learning Roadmap"
design:
  view: showcase
  columns: 3
---

<div class="kjh-skill-grid">
  <div class="skill-card">
    <div class="skill-icon">📘</div>
    <strong>학습 방향</strong><br>
    보안과 네트워크 분야에 집중하며<br>
    관련 기술 및 자격증 취득을 위해 공부 중입니다.<br>
    <em>정보보안 · 네트워크 관리 · 시스템 운영</em>
  </div>

  <div class="skill-card">
    <div class="skill-icon">🎯</div>
    <strong>진로 목표</strong><br>
    공기업 전산직으로 진출하여 공공기관의 정보시스템을<br>
    효율적이고 안전하게 운영하고자 합니다.<br>
    <em>안정성 · 효율성 · 공공서비스</em>
  </div>

  <div class="skill-card">
    <div class="skill-icon">🚀</div>
    <strong>미래 계획</strong><br>
    자격증 취득 및 인턴·서포터즈 경험을 통해<br>
    실무 역량을 쌓고 포트폴리오를 고도화할 예정입니다.<br>
    <em>TOPCIT · 정보처리기사 · NCS 역량 강화</em>
  </div>
</div>

<style>
.kjh-skill-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  grid-auto-rows: 1fr;
  margin-top: 1rem;
  align-items: stretch;
}
@media (max-width: 900px) {
  .kjh-skill-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 600px) {
  .kjh-skill-grid {
    grid-template-columns: repeat(1, 1fr);
  }
}
.skill-card {
  background: #fff;
  border-radius: 14px;
  padding: 1.2rem 1.2rem 1rem;
  box-shadow: 0 8px 20px rgba(0,0,0,0.12);
  line-height: 1.6;
  color: #222;
  text-align: center;
  transition: background 0.4s ease, box-shadow 0.4s ease, transform 0.3s ease, color 0.3s ease;
  cursor: default;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 100%;
  box-sizing: border-box;
  overflow-wrap: anywhere;
  word-break: keep-all;
}
.skill-icon {
  font-size: 2rem;
  width: 52px;
  height: 52px;
  line-height: 52px;
  border-radius: 50%;
  background: #e0e7ff;
  color: #3A86FF;
  margin-bottom: 0.6rem;
  box-shadow: 0 4px 10px rgba(58, 134, 255, 0.3);
  user-select: none;
  display: flex;
  justify-content: center;
  align-items: center;
}
.skill-card strong {
  font-size: 1.2rem;
  margin-bottom: 0.4rem;
  display: block;
}
.skill-card em {
  font-style: normal;
  color: #666;
  font-size: 0.9rem;
  margin-top: 0.5rem;
  display: block;
}
.skill-card:hover {
  background: linear-gradient(135deg, #3A86FF, #06D6A0);
  color: #f0f0f0;
  transform: scale(1.03);
  box-shadow: 0 14px 30px rgba(58, 134, 255, 0.5);
}
.skill-card:hover .skill-icon {
  background: rgba(255, 255, 255, 0.3);
  color: #e0f7f5;
  box-shadow: 0 6px 16px rgba(255, 255, 255, 0.5);
}
.skill-card:hover em {
  color: #d0f0e8;
}
.dark .skill-card {
  background: #1b2838;
  color: #ddd;
  box-shadow: 0 8px 24px rgba(0,0,0,0.6);
}
.dark .skill-icon {
  background: #2a3b54;
  color: #3A86FF;
  box-shadow: 0 4px 10px rgba(58, 134, 255, 0.5);
}
.dark .skill-card:hover {
  background: linear-gradient(135deg, #3A86FF, #06D6A0);
  color: #f0f0f0;
  box-shadow: 0 14px 30px rgba(58, 134, 255, 0.7);
}
.dark .skill-card:hover .skill-icon {
  background: rgba(255, 255, 255, 0.2);
  color: #d0f0e8;
  box-shadow: 0 6px 16px rgba(255, 255, 255, 0.4);
}
.dark .skill-card:hover em {
  color: #b0e8d8;
}
</style>