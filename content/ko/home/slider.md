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
/* Auto-hide navbar (local fallback to ensure specificity) */
.navbar { 
  position: fixed !important; top:0; left:0; right:0; z-index:10000; 
  will-change: transform, opacity; 
  transition: transform .38s cubic-bezier(.22,.61,.36,1), opacity .24s ease-out; 
}
.navbar.kjh-hide { transform: translateY(-110%); opacity: 0; }
#kjh-nav-hover { position: fixed; top:0; left:0; right:0; height:16px; z-index:10001; }

@media (prefers-reduced-motion: reduce){
  .navbar{ transition:none; }
}
/* ===== FAB Speed Dial (scoped by existence of .fab-dock in Home) ===== */
.fab-dock{
  position: fixed; right: 20px; bottom: 24px;
  width: 56px; height: 56px; z-index: 2147483647; /* MAX: stay above everything */
  display: grid; place-items: center;
  pointer-events: auto;
}

.fab-main{
  width: 56px; height:56px; border-radius:50%;
  border: none; cursor:pointer;
  background: #172a3eff; color:#fff; font-size: 28px; line-height: 1;
  box-shadow: 0 8px 24px rgba(0,0,0,.18);
  transition: transform .25s ease, box-shadow .25s ease, background-color .25s ease;
}
.fab-main:hover{ box-shadow: 0 12px 28px rgba(0,0,0,.22); }
.fab-dock.open .fab-main{ transform: rotate(45deg); }

.fab-mini{
  position: absolute; right: 8px; bottom: 8px; /* 시작점 */
  width: 44px; height: 44px; border-radius: 50%;
  background: #fff; color:#222; display: grid; place-items:center;
  text-decoration: none; font-size: 20px;
  box-shadow: 0 6px 18px rgba(0,0,0,.18);
  transform: translateY(0) scale(.6); opacity: 0; pointer-events: none;
  transition: transform .28s cubic-bezier(.22,.61,.36,1), opacity .2s ease;
}

/* 펼쳐졌을 때 위로 차곡차곡 */
.fab-dock.open .fab-mini{ opacity: 1; pointer-events: auto; }
.fab-dock.open .fab-mini:nth-of-type(2){ transform: translateY(-60px)  scale(1); }
.fab-dock.open .fab-mini:nth-of-type(3){ transform: translateY(-115px) scale(1); }
.fab-dock.open .fab-mini:nth-of-type(4){ transform: translateY(-170px) scale(1); }
.fab-dock.open .fab-mini:nth-of-type(5){ transform: translateY(-225px) scale(1); }
.fab-dock.open .fab-mini:nth-of-type(6){ transform: translateY(-280px) scale(1); }
.fab-dock.open .fab-mini:nth-of-type(7){ transform: translateY(-335px) scale(1); }

@media (prefers-reduced-motion: reduce){
  .fab-mini, .fab-main{ transition: none; }
}
.dark .fab-mini{ background:#2a2f3a; color:#fff; }

/* ===== Slider button theming (only affects buttons inside the carousel) ===== */
#homeCarousel .carousel-caption .btn {
  border-radius: 12px;
  padding: .85rem 1.4rem;
  font-weight: 600;
  transition: all .22s ease-in-out;
}

/* Primary button — transparent glass-like */
#homeCarousel .carousel-caption .btn.btn-primary {
  color: #ffffff;
  background-color: transparent;      /* 투명 배경 */
  border: 1.5px solid rgba(255,255,255,0.9);
  border-radius: 14px;
  padding: 0.85rem 1.6rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  box-shadow: none;
  transition: background-color .2s ease, border-color .2s ease, color .2s ease, transform .15s ease, box-shadow .15s ease;
}

#homeCarousel .carousel-caption .btn.btn-primary:hover,
#homeCarousel .carousel-caption .btn.btn-primary:focus {
  color: #ffffff;
  background-color: rgba(255,255,255,0.16); /* hover 시 은은한 백색 틴트 */
  border-color: rgba(255,255,255,1);
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.18);
}

/* 접근성: 키보드 포커스 링 */
#homeCarousel .carousel-caption .btn.btn-primary:focus-visible{
  outline: none;
  box-shadow: 0 0 0 3px rgba(255,255,255,0.35);
}

/* Outline light button — transparent unify */
#homeCarousel .carousel-caption .btn.btn-outline-light{
  color: #ffffff;
  background-color: transparent;
  border: 1.5px solid rgba(255,255,255,0.9);
}
#homeCarousel .carousel-caption .btn.btn-outline-light:hover,
#homeCarousel .carousel-caption .btn.btn-outline-light:focus{
  color: #ffffff;
  background-color: rgba(255,255,255,0.16);
  border-color: rgba(255,255,255,1);
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.18);
}
#homeCarousel .carousel-caption .btn.btn-outline-light:focus-visible{
  outline: none;
  box-shadow: 0 0 0 3px rgba(255,255,255,0.35);
}
</style>

<!-- Bootstrap Icons 불러오기 (반드시 style 태그 바깥) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">

<div class="fullbleed">
  <div id="homeCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="0" class="active" aria-current="true"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="1"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="2"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="3"></button>
    </div>

<div class="carousel-inner">
      <div class="carousel-item active" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/media/desk.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold" style="color: #fff;">강주현의 포트폴리오</h1>
          <p class="lead">네트워크와 보안을 공부하며, 성장중인 전북대학교 컴퓨터공학부 학생입니다.</p>
          <a class="btn btn-primary btn-lg" href="/about/">소개 보기</a>
        </div>
      </div>

<div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/media/labtab.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold"  style="color: #fff;">프로젝트</h1>
          <p class="lead">진행했던 프로젝트를 기록합니다.</p>
          <a class="btn btn-primary btn-lg" href="/project/">프로젝트</a>
        </div>
      </div>


<div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/media/path.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold"  style="color: #fff;">활동</h1>
          <p class="lead">활동 및 미래 계획과 목표를 기록합니다.</p>
          <a class="btn btn-primary btn-lg" href="/goals/">활동 확인하기</a>
        </div>
      </div>

<div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/media/contact.jpg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold" style="color: #fff;">연락</h1>
          <p class="lead">언제든 연락을 환영합니다.</p>
          <a class="btn btn-primary btn-lg" href="/contact/">연락처</a>
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

<!-- FAB speed dial (Home only) -->
<div class="fab-dock" aria-label="Quick actions">
  <button class="fab-main" aria-label="Toggle quick actions" type="button">
    <i class="bi bi-plus-lg"></i>
  </button>
  <a class="fab-mini" href="#top" aria-label="맨 위로"><i class="bi bi-arrow-up"></i></a>
  <a class="fab-mini" href="/about/" aria-label="자기소개"><i class="bi bi-person"></i></a>
  <a class="fab-mini" href="/project/" aria-label="프로젝트"><i class="bi bi-briefcase"></i></a>
  <a class="fab-mini" href="/contact/" aria-label="연락"><i class="bi bi-envelope"></i></a>
  <a class="fab-mini" href="/goals/roadmap/" aria-label="활동기록"><i class="bi bi-journal-text"></i></a>
  <a class="fab-mini" href="/goals/certs/" aria-label="자격증"><i class="bi bi-folder2-open"></i></a>
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
  var topLimit = 64;  // 상단 64px 이내에서는 항상 메뉴 표시

  // 마우스 hover 상태 추적
  var hoverOver = false;      // strip 또는 nav 위에 마우스가 있는지
  var hideTimer = null;       // 마우스가 떠났을 때 지연 숨김 타이머
  var HIDE_DELAY = 380;       // ms

  function clearHideTimer(){ if(hideTimer){ clearTimeout(hideTimer); hideTimer=null; } }

  function show(){
    clearHideTimer();
    if(hidden){
      nav.classList.remove('kjh-hide');
      nav.style.transform = '';
      hidden = false;
    }
  }

  function hide(){
    clearHideTimer();
    if(!hidden){
      nav.classList.add('kjh-hide');
      nav.style.transform = 'translateY(-110%)';
      hidden = true;
    }
  }

  function scheduleHide(){
    // 상단 영역에 있거나(고정 표시), 마우스가 올라와 있으면 숨김 예약하지 않음
    if ((window.pageYOffset || document.documentElement.scrollTop) <= topLimit) return;
    if (hoverOver) return;
    clearHideTimer();
    hideTimer = setTimeout(function(){ if(!hoverOver) hide(); }, HIDE_DELAY);
  }

  // 스크롤 방향에 따라 메뉴 숨기기/보이기 (requestAnimationFrame으로 부드럽게)
  var ticking = false;
  window.addEventListener('scroll', function(){
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function(){
      var y = window.pageYOffset || document.documentElement.scrollTop;
      var dy = y - lastY; lastY = y;
      if (y < topLimit) { show(); ticking=false; return; }
      if (Math.abs(dy) < threshold) { ticking=false; return; }
      if (dy > 0) { if (!hoverOver) hide(); } else { show(); }
      ticking = false;
    });
  }, { passive: true });

  // --- Hover 동작 ---
  function onEnter(){ hoverOver = true; show(); }
  function onLeave(){ hoverOver = false; scheduleHide(); }

  strip.addEventListener('mouseenter', onEnter);
  strip.addEventListener('mouseleave', onLeave);
  nav.addEventListener('mouseenter', onEnter);
  nav.addEventListener('mouseleave', onLeave);

  // 접근성: 키보드 포커스가 네비로 들어오면 표시, 포커스가 빠지면 숨김 예약
  nav.addEventListener('focusin', function(){ hoverOver = true; show(); });
  nav.addEventListener('focusout', function(){ hoverOver = false; scheduleHide(); });
})();
})();
</script>

<script>
(function(){
  var dock = document.querySelector('.fab-dock');
  // Ensure dock is attached directly to <body> to avoid clipping by ancestor overflow/transform
  if (dock && dock.parentNode !== document.body) {
    document.body.appendChild(dock);
  }
  if(!dock) return;
  var main = dock.querySelector('.fab-main');

  function closeDock(){ dock.classList.remove('open'); }
  function toggleDock(){ dock.classList.toggle('open'); }

  main.addEventListener('click', function(e){
    e.preventDefault(); e.stopPropagation();
    toggleDock();
  });

  // Dock 바깥 클릭 시 닫기
  document.addEventListener('click', function(){ closeDock(); });
  // ESC로 닫기
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeDock(); });

  // 맨 위로 이동 버튼 보정
  var topAnchor = dock.querySelector('a[href="#top"]');
  if(topAnchor){
    topAnchor.addEventListener('click', function(){
      closeDock();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
})();
</script>