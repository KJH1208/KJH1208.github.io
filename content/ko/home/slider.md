---
widget: markdown
headless: true
active: true
weight: 1
title: ""
css_class: fullwidth
design:
  spacing:
    padding: [0, 0, 0, 0]
---

<style>
/* full-bleed wrapper so the slider spans edge-to-edge */
.fullbleed{width:100vw;position:relative;left:50%;right:50%;margin-left:-50vw;margin-right:-50vw;max-width:100vw;overflow:hidden}

/* carousel visuals */
#homeCarousel .carousel-item{
  min-height:70vh;
  background-size:cover;
  background-position:center;
  color:#fff;
  text-align:center;
  display:flex;align-items:center;justify-content:center;
  padding:10rem 1rem;
}
#homeCarousel .carousel-caption{position:static;text-shadow:0 2px 12px rgba(0,0,0,.6)}
#homeCarousel .carousel-indicators{bottom:1.25rem;z-index:10}
#homeCarousel .carousel-indicators [data-bs-target]{background-color:#fff;opacity:.8}
#homeCarousel .carousel-indicators .active{opacity:1}
@media (max-width: 992px){
  #homeCarousel .carousel-item{min-height:55vh;padding:6rem 1rem}
}
</style>

<div class="fullbleed">
  <div id="homeCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>

    <div class="carousel-inner">
      <div class="carousel-item active" style="background-image:linear-gradient(rgba(0,0,0,.45), rgba(0,0,0,.45)), url('/media/desk.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">KJH 포트폴리오</h1>
          <p class="lead">프로젝트와 도전을 통해 성장하는 과정을 기록합니다.</p>
          <a class="btn btn-primary btn-lg" href="/about/">소개 보기</a>
        </div>
      </div>

      <div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.45), rgba(0,0,0,.45)), url('/media/field.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">취미</h1>
          <p class="lead">여러가지 취미를 가지며 지치지 않는 일상을 유지합니다.</p>
          <a class="btn btn-outline-light btn-lg" href="/post/">여행 기록</a>
        </div>
      </div>

      <div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.45), rgba(0,0,0,.45)), url('/media/contact.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">연락하기</h1>
          <p class="lead">협업과 피드백은 언제나 환영합니다.</p>
          <a class="btn btn-primary btn-lg" href="/contact/">Contact</a>
        </div>
      </div>
    </div>

    <button class="carousel-control-prev" type="button" data-bs-target="#homeCarousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">이전</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#homeCarousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">다음</span>
    </button>
  </div>
</div>
