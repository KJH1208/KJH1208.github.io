// ---- Headroom-lite: Auto-hide navbar on scroll ----
(function(){
  var nav = document.querySelector('.navbar');
  if (!nav) return;

  var lastY = window.pageYOffset || 0;
  var hidden = false;
  var minDelta = 8;   // 민감도 (픽셀)
  var topLock = 48;   // 상단 48px 이내는 항상 표시

  function pin(){
    if(hidden){
      hidden = false;
      nav.classList.remove('kjh-hide');
      nav.style.transform = '';
    }
  }
  function unpin(){
    if(!hidden){
      hidden = true;
      nav.classList.add('kjh-hide');
      nav.style.transform = 'translateY(-110%)';
    }
  }

  window.addEventListener('scroll', function(){
    var y = window.pageYOffset || 0;
    var dy = y - lastY;
    lastY = y;

    if (y <= topLock) { pin(); return; }
    if (Math.abs(dy) < minDelta) return; // 미세한 스크롤 무시

    if (dy > 0) unpin();  // 아래로 스크롤 → 숨김
    else pin();           // 위로 스크롤 → 표시
  }, { passive: true });
})();