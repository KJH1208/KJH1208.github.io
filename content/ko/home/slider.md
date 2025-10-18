---
widget: markdown
headless: true
active: true
weight: 1
title: ""
css_class: fullwidth 
design:
  spacing:
    padding: [0,0,0,0]   # 위아래 여백 제거
---

<div id="homeCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
  <!-- 인디케이터 -->
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="0" class="active" aria-current="true"></button>
    <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="1"></button>
    <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="2"></button>
  </div>

  <!-- 슬라이드들 -->
  <div class="carousel-inner">
    <!-- 1 -->
    <div class="carousel-item active">
      <img src="/media/desk.jpg" class="d-block w-100" alt="desk" />
      <div class="carousel-caption">
        <h2 class="display-5 fw-semibold">KJH 포트폴리오</h2>
        <p>프로젝트와 도전을 통해 성장하는 과정을 기록합니다.</p>
        <a class="btn btn-primary btn-lg" href="/about/">소개 보기</a>
      </div>
    </div>
    <!-- 2 -->
    <div class="carousel-item">
      <img src="/media/field.jpg" class="d-block w-100" alt="field" />
      <div class="carousel-caption">
        <h2 class="display-5 fw-semibold">취미</h2>
        <p>여러가지 취미를 가지며 지치지 않는 일상을 유지합니다.</p>
        <a class="btn btn-outline-light btn-lg" href="/post/">여행 기록</a>
      </div>
    </div>
    <!-- 3 -->
    <div class="carousel-item">
      <img src="/media/contact.jpg" class="d-block w-100" alt="contact" />
      <div class="carousel-caption">
        <h2 class="display-5 fw-semibold">연락하기</h2>
        <p>협업과 피드백은 언제나 환영합니다.</p>
        <a class="btn btn-primary btn-lg" href="/contact/">Contact</a>
      </div>
    </div>
  </div>

  <!-- 좌우 화살표 -->
  <button class="carousel-control-prev" type="button" data-bs-target="#homeCarousel" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">이전</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#homeCarousel" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">다음</span>
  </button>
</div>