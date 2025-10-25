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
    💻 <strong>네트워크 보안</strong><br>
    TCP/IP, 방화벽, 패킷 분석 등 네트워크 보안 기본기 학습<br>
    <em>Kali Linux · Wireshark · tcpdump</em>
  </div>

  <div class="skill-card">
    🧠 <strong>데이터베이스</strong><br>
    SQL 최적화와 트랜잭션 처리 중심으로 학습 중<br>
    <em>MariaDB · Oracle · ERD 설계</em>
  </div>

  <div class="skill-card">
    ⚙️ <strong>DevOps 자동화</strong><br>
    CI/CD 파이프라인 구축 및 서버 관리 자동화<br>
    <em>GitHub Actions · Docker · Bash 스크립트</em>
  </div>
</div>

<style>
.kjh-skill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}
.skill-card {
  background: #fff;
  border-radius: 14px;
  padding: 1.5rem;
  box-shadow: 0 6px 16px rgba(0,0,0,0.08);
  line-height: 1.6;
  transition: all .25s ease;
}
.skill-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 22px rgba(0,0,0,0.12);
}
.dark .skill-card {
  background: #1b2838;
  color: #fff;
}
</style>