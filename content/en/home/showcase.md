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
    <strong>Learning Focus</strong><br>
    Focusing on security and networking fields,<br>
    currently studying to acquire related skills and certifications.<br>
    <em>Information Security · Network Management · System Administration</em>
  </div>

  <div class="skill-card">
    <div class="skill-icon">🎯</div>
    <strong>Career Goal</strong><br>
    Aiming to work as an IT officer in a public institution,<br>
    efficiently and securely managing its information systems.<br>
    <em>Stability · Efficiency · Public Service</em>
  </div>

  <div class="skill-card">
    <div class="skill-icon">🚀</div>
    <strong>Future Plan</strong><br>
    Planning to enhance practical skills through<br>
    certifications, internships, and supporter activities while refining my portfolio.<br>
    <em>TOPCIT · Engineer Information Processing · NCS Competency Development</em>
  </div>
</div>

<style>
.kjh-skill-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(320px, 1fr));
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