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

/* ---- Fallback slide+fade motion for arrow clicks ---- */
#homeCarousel .carousel-item { transition: opacity .6s ease; }
@keyframes kjh-slide-out-left { from { transform: translateX(0); opacity: 1;} to { transform: translateX(-12%); opacity: 0;} }
@keyframes kjh-slide-out-right{ from { transform: translateX(0); opacity: 1;} to { transform: translateX(12%);  opacity: 0;} }
@keyframes kjh-slide-in-left  { from { transform: translateX(-12%); opacity: 0;} to { transform: translateX(0);  opacity: 1;} }
@keyframes kjh-slide-in-right { from { transform: translateX(12%);  opacity: 0;} to { transform: translateX(0);  opacity: 1;} }
#homeCarousel .carousel-item.kjh-anim-out-left  { animation: kjh-slide-out-left  .6s ease both; }
#homeCarousel .carousel-item.kjh-anim-out-right { animation: kjh-slide-out-right .6s ease both; }
#homeCarousel .carousel-item.kjh-anim-in-left   { animation: kjh-slide-in-left   .6s ease both; }
#homeCarousel .carousel-item.kjh-anim-in-right  { animation: kjh-slide-in-right  .6s ease both; }

/* 화살표 클릭 가능 보장 */
#homeCarousel .carousel-control-prev,
#homeCarousel .carousel-control-next { z-index: 15; width:10%; pointer-events:auto; }
#homeCarousel .carousel-control-prev-icon,
#homeCarousel .carousel-control-next-icon { filter: drop-shadow(0 2px 6px rgba(0,0,0,.6)); }

/* 인디케이터 알약 스타일 */
#homeCarousel .carousel-indicators {
  bottom: 2rem;
  gap: 10px;                 /* 버튼 간 간격 */
}

#homeCarousel .carousel-indicators [data-bs-target]{
  width: 36px;               /* 기본 너비 */
  height: 6px;               /* 두께 */
  border: 0;
  border-radius: 999px;      /* 알약 모양 */
  background: rgba(255,255,255,.45);
  opacity: 1;                /* Bootstrap 기본 opacity 무효화 */
  box-shadow: 0 2px 10px rgba(0,0,0,.25) inset, 0 1px 3px rgba(0,0,0,.2);
  transition: width .28s ease, background .28s ease, transform .28s ease, box-shadow .28s ease;
  position: relative;
  overflow: hidden;          /* 내부 진행바 잘림 처리 */
}

/* 활성(slide 현재 위치) */
#homeCarousel .carousel-indicators .active{
  width: 56px;               /* 살짝 더 길게 */
  background: rgba(255,255,255,.85);
  transform: translateY(-1px);
  box-shadow: 0 4px 16px rgba(0,0,0,.35) inset, 0 4px 14px rgba(0,0,0,.3);
}

/* 마우스 오버 시 살짝 강조 */
#homeCarousel .carousel-indicators [data-bs-target]:hover{
  transform: translateY(-1px);
  background: rgba(255,255,255,.7);
}

/* 유리(blur) 느낌 추가 - 지원 브라우저에서만 */
#homeCarousel .carousel-indicators [data-bs-target]{
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
}

/* 진행 애니메이션 바(활성 버튼 내부에서 좌->우 채워짐) */
#homeCarousel .carousel-indicators [data-bs-target]::after{
  content:"";
  position:absolute; left:0; top:0; bottom:0;
  width:0%;
  background: #70A3C9;            /* 테마 포인트 컬러 */
  opacity:.9;
  border-radius: inherit;
}

/* .is-animating 클래스가 붙은 활성 버튼에 진행 애니메이션 실행 */
@keyframes kjh-fill {
  from { width: 0%; }
  to   { width: 100%; }
}
#homeCarousel .carousel-indicators .active.is-animating::after{
  animation: kjh-fill 5s linear forwards; /* interval과 동일하게 */
}

/* 좌우 화살표 */
#homeCarousel .carousel-control-prev,
#homeCarousel .carousel-control-next {
  z-index: 9999;           /* 항상 최상단 */
  width: 12%;              /* 클릭 영역 확대 */
  pointer-events: auto;     /* 클릭 통과 방지 */
}
#homeCarousel .carousel-caption { z-index: 5; } /* 캡션은 화살표보다 아래 */

/* 반응형 */
@media (max-width: 992px) {
  #homeCarousel .carousel-item {
    min-height: 60vh;
  }
  #homeCarousel .carousel-caption h1 {
    font-size: 2rem;
  }
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
      <span class="visually-hidden"></span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#homeCarousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden"></span>
    </button>
  </div>
</div>

<script>
(function(){
  var el = document.getElementById('homeCarousel');
  var clickLock = false; // 연속 클릭 방지 락
  if(!el) return;
  function initFallback(){
    var items = Array.from(el.querySelectorAll('.carousel-item'));
    var indicators = Array.from(el.querySelectorAll('.carousel-indicators [data-bs-slide-to]'));
    var prevBtn = el.querySelector('.carousel-control-prev');
    var nextBtn = el.querySelector('.carousel-control-next');
    var idx = items.findIndex(function(i){return i.classList.contains('active');});
    if(idx < 0) idx = 0;

    function clearAnims(node){
      node.classList.remove('kjh-anim-out-left','kjh-anim-out-right','kjh-anim-in-left','kjh-anim-in-right');
    }

    function activate(i){
      items[i].classList.add('active');
      indicators[i] && indicators[i].classList.add('active');
    }
    function deactivate(i){
      items[i].classList.remove('active');
      indicators[i] && indicators[i].classList.remove('active');
    }

    function show(nextIndex, dir){
      if(nextIndex === idx) return;
      if (clickLock) return; clickLock = true;
      nextIndex = (nextIndex + items.length) % items.length;
      var cur = items[idx];
      var nxt = items[nextIndex];

      // Prepare next slide for entry
      activate(nextIndex);
      clearAnims(cur); clearAnims(nxt);

      // Choose directions
      var outClass = dir === 'prev' ? 'kjh-anim-out-right' : 'kjh-anim-out-left';
      var inClass  = dir === 'prev' ? 'kjh-anim-in-left'   : 'kjh-anim-in-right';

      // Start animations
      cur.classList.add(outClass);
      nxt.classList.add(inClass);

      // When the outgoing animation ends, finalize state
      var done = false;
      function finish(){
        if(done) return; done = true;
        clearAnims(cur); clearAnims(nxt);
        deactivate(idx);
        idx = nextIndex;
        clickLock = false;
      }
      cur.addEventListener('animationend', finish, { once: true });
      // Fallback safety in case animationend doesn't fire
      setTimeout(finish, 700);
    }

    prevBtn && prevBtn.addEventListener('click', function(e){ e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation && e.stopImmediatePropagation(); show(idx-1, 'prev'); });
    nextBtn && nextBtn.addEventListener('click', function(e){ e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation && e.stopImmediatePropagation(); show(idx+1, 'next'); });
    indicators.forEach(function(btn){
      btn.addEventListener('click', function(event){
        event && (event.preventDefault(), event.stopPropagation());
        var target = parseInt(btn.getAttribute('data-bs-slide-to'),10) || 0;
        var dir = (target < idx) ? 'prev' : 'next';
        show(target, dir);
      });
    });
    setInterval(function(){ show(idx+1, 'next'); }, 5000);
  }
  try {
    if (window.bootstrap && bootstrap.Carousel) {
      new bootstrap.Carousel(el, { interval: 5000, ride: 'carousel', touch: true, pause: false, wrap: true });
      // Bootstrap 사용 시에도 연타 방지 + 이벤트 차단
      var prevBtnBS = el.querySelector('.carousel-control-prev');
      var nextBtnBS = el.querySelector('.carousel-control-next');
      function guardHandler(dir){
        return function(e){
          e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation && e.stopImmediatePropagation();
          if (clickLock) return;
          clickLock = true;
          setTimeout(function(){ clickLock = false; }, 650);
        };
      }
      prevBtnBS && prevBtnBS.addEventListener('click', guardHandler('prev'), true);
      nextBtnBS && nextBtnBS.addEventListener('click', guardHandler('next'), true);
    } else {
      initFallback();
    }
  } catch (e) {
    console && console.warn && console.warn('Carousel init fallback:', e);
    initFallback();
  }
  // ---- Auto-hide navbar on scroll + reveal on hover ----
(function navbarAutoHide(){
  var nav = document.querySelector('.navbar');
  if(!nav) return;

  // 상단 hover 감지용 얇은 투명 영역 만들기
  var strip = document.getElementById('kjh-nav-hover');
  if(!strip){
    strip = document.createElement('div');
    strip.id = 'kjh-nav-hover';
    document.body.appendChild(strip);
  }

  var lastY = window.pageYOffset || document.documentElement.scrollTop;
  var hidden = false;
  var threshold = 10; // 민감도
  var topLimit = 50;  // 상단 50px 이내에서는 항상 메뉴 표시

  function show(){
    if(hidden){
      nav.classList.remove('kjh-hide');
      hidden = false;
    }
  }

  function hide(){
    if(!hidden){
      nav.classList.add('kjh-hide');
      hidden = true;
    }
  }

  // 스크롤 방향에 따라 메뉴 숨기기/보이기
  window.addEventListener('scroll', function(){
    var y = window.pageYOffset || document.documentElement.scrollTop;
    var dy = y - lastY;
    lastY = y;
    if (y < topLimit) { show(); return; }
    if (Math.abs(dy) < threshold) return; // 미세한 움직임은 무시
    if (dy > 0) hide();  // 아래로 스크롤 → 숨김
    else show();         // 위로 스크롤 → 표시
  }, { passive: true });

  // 마우스를 화면 맨 위로 올리면 다시 표시
  strip.addEventListener('mouseenter', show);
})();
</script>