// ---- Auto-hide navbar on scroll + reveal on hover (global) ----
(function navbarAutoHide(){
  var nav = document.querySelector('.navbar');
  if(!nav) return;

  // 화면 맨 위 hover 감지용 얇은 스트립(한 번만 생성)
  var strip = document.getElementById('kjh-nav-hover');
  if(!strip){
    strip = document.createElement('div');
    strip.id = 'kjh-nav-hover';
    document.body.appendChild(strip);
  }

  // 네비 높이 계산 → CSS 변수에 기록 (타 페이지 상단 패딩 등에 활용)
  function applyNavHeight(){
    var h = nav.offsetHeight || 0;
    document.documentElement.style.setProperty('--kjh-nav-h', h + 'px');
  }
  window.addEventListener('load', applyNavHeight);
  window.addEventListener('resize', applyNavHeight);
  applyNavHeight();

  var lastY = window.pageYOffset || document.documentElement.scrollTop;
  var hidden = false;
  var threshold = 10; // 민감도: 스크롤 미세 움직임 무시
  var topLimit = 50;  // 상단 50px 이내는 항상 표시

  function show(){
    if(hidden){
      nav.classList.remove('kjh-hide');
      nav.style.transform = '';
      hidden = false;
    }
  }
  function hide(){
    if(!hidden){
      nav.classList.add('kjh-hide');
      // 혹시 다른 CSS가 덮어씌워도 확실히 숨기도록 인라인 지정
      nav.style.transform = 'translateY(-110%)';
      hidden = true;
    }
  }

  // 스크롤 방향 감지로 자동 숨김/표시
  window.addEventListener('scroll', function(){
    var y = window.pageYOffset || document.documentElement.scrollTop;
    var dy = y - lastY;
    lastY = y;
    if (y < topLimit) { show(); return; }
    if (Math.abs(dy) < threshold) return; // 미세한 움직임 무시
    if (dy > 0) hide();  // 아래로 스크롤 → 숨김
    else show();         // 위로 스크롤 → 표시
  }, { passive: true });

  // 화면 맨 위에 마우스를 올리면 즉시 표시
  strip.addEventListener('mouseenter', show);

  // 접근성: 키보드 포커스가 네비로 들어오면 표시
  nav.addEventListener('focusin', show);
})();