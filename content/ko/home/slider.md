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
/* 전체 화면 가득 차도록 */
.fullbleed {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  max-width: 100vw;
  overflow: hidden;
}

/* 캐러셀 기본 스타일 */
#homeCarousel .carousel-item {
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  color: #fff;
  text-align: center;
  position: relative;
}

/* 가운데 텍스트 중앙 정렬 + 기본은 숨김(페이드/애니메이션용) */
#homeCarousel .carousel-caption{
  position:absolute;
  top:50%;
  left:50%;
  transform:translate(-50%,-42%);
  width:90%;
  max-width: 900px;
  text-shadow:0 2px 12px rgba(0,0,0,.6);
  opacity:0;                /* inactive 기본 숨김 */
  transition: opacity .5s ease, transform .6s ease;
}
/* 활성 슬라이드에서 캡션 보이기 */
#homeCarousel .carousel-item.active .carousel-caption{
  opacity:1;
  transform:translate(-50%,-50%);
  animation: none; /* base */
}
/* 캡션 자식 단계적 등장 */
#homeCarousel .carousel-item .carousel-caption h1,
#homeCarousel .carousel-item .carousel-caption p,
#homeCarousel .carousel-item .carousel-caption a{
  opacity:0; transform: translateY(14px);
}
#homeCarousel .carousel-item.active .carousel-caption h1{opacity:1; transform:none; transition: all .6s ease .05s;}
#homeCarousel .carousel-item.active .carousel-caption p{opacity:1; transform:none; transition: all .6s ease .18s;}
#homeCarousel .carousel-item.active .carousel-caption a{opacity:1; transform:none; transition: all .6s ease .30s;}

/* 부트스트랩 페이드 전환 강화 */
#homeCarousel.carousel-fade .carousel-item {opacity:0; transition-property: opacity;}
#homeCarousel.carousel-fade .carousel-item.active,
#homeCarousel.carousel-fade .carousel-item-next.carousel-item-start,
#homeCarousel.carousel-fade .carousel-item-prev.carousel-item-end {opacity:1;}
#homeCarousel.carousel-fade .active.carousel-item-start,
#homeCarousel.carousel-fade .active.carousel-item-end {opacity:0;}

/* 화살표 클릭 가능 보장 */
#homeCarousel .carousel-control-prev,
#homeCarousel .carousel-control-next { z-index: 15; width:10%; pointer-events:auto; }
#homeCarousel .carousel-control-prev-icon,
#homeCarousel .carousel-control-next-icon { filter: drop-shadow(0 2px 6px rgba(0,0,0,.6)); }

/* 인디케이터 */
#homeCarousel .carousel-indicators {
  bottom: 1.25rem;
  z-index: 10;
}
#homeCarousel .carousel-indicators [data-bs-target] {
  background-color: #fff;
  opacity: .8;
}
#homeCarousel .carousel-indicators .active {
  opacity: 1;
}

/* 좌우 화살표 */
#homeCarousel .carousel-control-prev,
#homeCarousel .carousel-control-next {
  z-index: 11;
  width: 8%;
}

/* 반응형 */
@media (max-width: 992px) {
  #homeCarousel .carousel-item {
    min-height: 60vh;
  }
  #homeCarousel .carousel-caption h1 {
    font-size: 2rem;
  }
}
/* === Fallback slide animation when Bootstrap JS is not present === */
#homeCarousel.no-bs .carousel-inner{ position: relative; overflow: hidden; }
#homeCarousel.no-bs .carousel-item{
  position: absolute; top:0; left:0; width:100%;
  opacity: 0; transform: translateX(100%);
  transition: transform .6s ease, opacity .6s ease;
}
#homeCarousel.no-bs .carousel-item.active{
  opacity: 1; transform: translateX(0);
  z-index: 2;
}
#homeCarousel.no-bs .carousel-item.out-left{
  transform: translateX(-100%); opacity: 0; z-index: 1;
}
#homeCarousel.no-bs .carousel-item.out-right{
  transform: translateX(100%); opacity: 0; z-index: 1;
}
</style>

<div class="fullbleed">
  <div id="homeCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="0" class="active" aria-current="true"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="1"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="2"></button>
    </div>

<div class="carousel-inner">
      <div class="carousel-item active" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/media/desk.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">KJH 포트폴리오</h1>
          <p class="lead">프로젝트와 도전을 통해 성장하는 과정을 기록합니다.</p>
          <a class="btn btn-primary btn-lg" href="/about/">소개 보기</a>
        </div>
      </div>

<div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/media/field.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">취미</h1>
          <p class="lead">여러 가지 취미를 가지며 지치지 않는 일상을 유지합니다.</p>
          <a class="btn btn-outline-light btn-lg" href="/post/">여행 기록</a>
        </div>
      </div>

<div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/media/contact.jpg');">
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

<script>
(function(){
  var el = document.getElementById('homeCarousel');
  if(!el) return;

  // 방향에 따라 클래스를 부여해 슬라이드 애니메이션
  function initFallback(){
    el.classList.add('no-bs');

    var items = Array.from(el.querySelectorAll('.carousel-item'));
    var indicators = Array.from(el.querySelectorAll('.carousel-indicators [data-bs-slide-to]'));
    var prevBtn = el.querySelector('.carousel-control-prev');
    var nextBtn = el.querySelector('.carousel-control-next');

    // 최초 active 인덱스
    var idx = items.findIndex(function(i){return i.classList.contains('active');});
    if(idx < 0) idx = 0;

    // 초기 위치 정리
    items.forEach(function(it,i){
      it.classList.remove('out-left','out-right');
      if(i < idx){ it.style.transform = 'translateX(-100%)'; }
      else if(i > idx){ it.style.transform = 'translateX(100%)'; }
      else { it.classList.add('active'); it.style.transform = 'translateX(0)'; }
    });

    function show(next){
      if(next === idx) return;
      var dir = (next > idx || (idx === 0 && next === items.length-1) === false) ? 1 : -1; // 대략 방향
      // 현재/다음
      var cur = items[idx];
      var nxt = items[next];

      // out 방향 지정
      cur.classList.remove('out-left','out-right','active');
      nxt.classList.remove('out-left','out-right','active');

      if(dir > 0){ // 오른쪽으로 이동: 현재는 왼쪽으로 나가고, 다음이 오른쪽에서 들어옴
        cur.classList.add('out-left');
        nxt.style.transform = 'translateX(100%)';
      }else{
        cur.classList.add('out-right');
        nxt.style.transform = 'translateX(-100%)';
      }

      // 다음을 활성화
      requestAnimationFrame(function(){
        nxt.classList.add('active');
        nxt.style.transform = 'translateX(0)';
      });

      // 인디케이터 동기화
      indicators[idx] && indicators[idx].classList.remove('active');
      indicators[next] && indicators[next].classList.add('active');

      idx = next;
    }

    function nextIndex(){ return (idx + 1) % items.length; }
    function prevIndex(){ return (idx - 1 + items.length) % items.length; }

    prevBtn && prevBtn.addEventListener('click', function(e){ e.preventDefault(); show(prevIndex()); });
    nextBtn && nextBtn.addEventListener('click', function(e){ e.preventDefault(); show(nextIndex()); });
    indicators.forEach(function(btn){
      btn.addEventListener('click', function(){
        var i = parseInt(btn.getAttribute('data-bs-slide-to'), 10);
        if(!isNaN(i)) show(i);
      });
    });

    // 자동 전환
    setInterval(function(){ show(nextIndex()); }, 5000);
  }

  try {
    if (window.bootstrap && bootstrap.Carousel) {
      // 부트스트랩이 있으면 기본 전환 사용
      new bootstrap.Carousel(el, { interval: 5000, ride: 'carousel', touch: true, pause: false, wrap: true });
    } else {
      initFallback();
    }
  } catch (e) {
    console && console.warn && console.warn('Carousel init fallback:', e);
    initFallback();
  }
})();
</script>