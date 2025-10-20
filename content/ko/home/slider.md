---
widget: markdown
active: true
weight: 10
design:
  spacing:
    padding: [0, 0, 0, 0]
---

<div style="
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
">

  <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
    
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>

    <div class="carousel-inner">
      
      <div class="carousel-item active" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/media/desk.jpg'); background-size: cover; background-position: center; padding: 10rem 1rem; color: white; text-align: center;">
        <h1 class="display-3">KJH 포트폴리오</h1>
        <p class="lead">프로젝트와 도전을 통해 성장하는 과정을 기록합니다.</p>
        <a class="btn btn-primary btn-lg" href="/about/">소개 보기</a>
      </div>

      <div class="carousel-item" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/media/field.jpg'); background-size: cover; background-position: center; padding: 10rem 1rem; color: white; text-align: center;">
        <h1 class="display-3">취미</h1>
        <p class="lead">여러가지 취미를 가지며 지치지 않는 일상을 유지합니다.</p>
        <a class="btn btn-primary btn-lg" href="/post/">여행 기록</a>
      </div>

      <div class="carousel-item" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/media/contact.jpg'); background-size: cover; background-position: center; padding: 10rem 1rem; color: white; text-align: center;">
        <h1 class="display-3">연락하기</h1>
        <p class="lead">협업과 피드백은 언제나 환영합니다.</p>
        <a class="btn btn-primary btn-lg" href="/contact/">Contact</a>
      </div>

    </div>

    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  </div>