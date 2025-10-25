---
widget: blank
headless: true
active: true
weight: 56
title: "Learning & Skills"
design:
  view: showcase
  columns: 3
---

<div class="kjh-skill-grid">
  <div class="skill-card">
    <div class="skill-icon">💻</div>
    <strong>네트워크 보안</strong><br>
    TCP/IP, 방화벽, 패킷 분석 등 네트워크 보안 기본기 학습<br>
    <em>Kali Linux · Wireshark · tcpdump</em>
  </div>

  <div class="skill-card">
    <div class="skill-icon">🧠</div>
    <strong>데이터베이스</strong><br>
    SQL 최적화와 트랜잭션 처리 중심으로 학습 중<br>
    <em>MariaDB · Oracle · ERD 설계</em>
  </div>

  <div class="skill-card">
    <div class="skill-icon">⚙️</div>
    <strong>DevOps 자동화</strong><br>
    CI/CD 파이프라인 구축 및 서버 관리 자동화<br>
    <em>GitHub Actions · Docker · Bash 스크립트</em>
  </div>
</div>

<style>
.kjh-skill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 1rem;
}
.skill-card {
  background: #fff;
  border-radius: 14px;
  padding: 2rem 1.5rem 1.5rem;
  box-shadow: 0 8px 20px rgba(0,0,0,0.12);
  line-height: 1.6;
  color: #222;
  text-align: center;
  transition: background 0.4s ease, box-shadow 0.4s ease, transform 0.3s ease, color 0.3s ease;
  cursor: default;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.skill-icon {
  font-size: 2.5rem;
  width: 64px;
  height: 64px;
  line-height: 64px;
  border-radius: 50%;
  background: #e0e7ff;
  color: #3A86FF;
  margin-bottom: 1rem;
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