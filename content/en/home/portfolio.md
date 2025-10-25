---
# A section created with the Portfolio widget.
# This section displays content from `content/project/`.
# See https://docs.hugoblox.com/widget/portfolio/
widget: portfolio

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 30

title: ''
subtitle: ''

content:
  # Page type to display. E.g. project.
  page_type: project

  # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  filter_default: 0

  # Filter toolbar (optional).
  # Add or remove as many filters (`filter_button` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove the toolbar, delete the entire `filter_button` block.
  filter_button:
    - name: All
      tag: '*'
    - name: Security
      tag: SEC
    - name: Web/App
      tag: WEB
    - name: AI
      tag: AI

design:
  columns: '1'
  view: masonry
  flip_alt_rows: true
  background: {}
  spacing: {padding: [0, 0, 0, 0]}
---
<br>
<div class="kjh-timeline-wrap">
  <div class="kjh-timeline">
    {{< kcard href="/goals/roadmap" title="활동 연혁" desc="2023~2025 주요 참여 기록" image="/media/timeline.jpg" badge="Timeline" variant="horizontal">}}
  </div>
  <div class="kjh-timeline">
    {{< kcard href="/goals/certs" title="자격증 현황" desc="취득 및 예정 자격증 정리" image="/media/certificate.jpg" badge="Certifications" variant="horizontal">}}
  </div>
</div>

<style>
.kjh-timeline-wrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.kjh-timeline {
  flex: 1 1 400px;
  max-width: 400px;
  min-height: 420px; /* consistent card height */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.kjh-timeline .kcard {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.kjh-timeline img {
  object-fit: cover;
  width: 100%;
  height: 200px; /* fixed uniform image height */
  border-radius: 12px 12px 0 0;
}

/* Portfolio filter chips use Bootstrap nav-pills (.nav-link). Force our point colors on hover/active. */
.home-section .isotope-filters .nav-pills .nav-link {
  border-radius: 12px;
  transition: all .25s ease-in-out;
}
/* Hover state */
.home-section .isotope-filters .nav-pills .nav-link:hover,
.home-section .isotope-filters .nav-pills .nav-link:focus {
  color: #fff !important;
  background: linear-gradient(90deg, #3A86FF 0%, #06D6A0 100%) !important;
  box-shadow: 0 8px 20px rgba(58,134,255,0.35);
  transform: translateY(-2px);
}

/* Active (selected) state */
.home-section .isotope-filters .nav-pills .nav-link.active,
.home-section .isotope-filters .nav-pills .show > .nav-link {
  color: #fff !important;
  background: linear-gradient(90deg, #3A86FF 0%, #06D6A0 100%) !important;
  box-shadow: 0 8px 20px rgba(58,134,255,0.35);
}

/* Keep supporting .btn markup just in case (some themes render buttons) */
.home-section .isotope-filters .btn:hover,
.home-section .isotope-filters .btn:focus,
.home-section .isotope-filters .btn.active {
  color: #fff !important;
  background: linear-gradient(90deg, #3A86FF 0%, #06D6A0 100%) !important;
  border-color: #3A86FF !important;
  box-shadow: 0 8px 20px rgba(58,134,255,0.35);
  transform: translateY(-2px);
}

/* Dark mode contrast */
.dark .home-section .isotope-filters .nav-pills .nav-link:hover,
.dark .home-section .isotope-filters .nav-pills .nav-link:focus,
.dark .home-section .isotope-filters .nav-pills .nav-link.active,
.dark .home-section .isotope-filters .btn:hover,
.dark .home-section .isotope-filters .btn:focus,
.dark .home-section .isotope-filters .btn.active {
  color: #ffffffff !important;
}

/* === Portfolio 필터 버튼 다크모드 보정 === */
.dark .isotope-filters button,
[data-theme="dark"] .isotope-filters button {
  color: #ffffff !important;                 /* 텍스트 흰색 */
  border-color: rgba(255, 255, 255, 1) !important;  /* 외곽선 은은한 흰색 */
  background: transparent !important;        /* 배경 투명하게 */
}

/* hover 시 */
.dark .isotope-filters button:hover,
[data-theme="dark"] .isotope-filters button:hover {
  color: #06D6A0 !important;                 /* 호버 시 포인트색 */
  border-color: #06D6A0 !important;
}

/* 선택된(active) 버튼 */
.dark .isotope-filters button.active,
[data-theme="dark"] .isotope-filters button.active {
  color: #ffffffff !important;                 /* 선택된 버튼 글자색 */
  background: linear-gradient(90deg, #06D6A0, #3A86FF) !important; /* 예쁜 그라데이션 */
  border: none !important;
}
</style>


<script>
/**
 * Hash-based portfolio filter
 * /project/#AI 처럼 들어오면 해당 필터 버튼을 자동 클릭
 */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    // 현재 페이지가 포트폴리오 섹션을 포함할 때만 동작
    var sec = document.querySelector('.home-section.wg-portfolio');
    if (!sec) return;

    // URL hash -> 'AI', 'NET' 등으로 정규화
    var raw = (location.hash || '').replace('#', '').trim();
    if (!raw) return;
    var hash = decodeURIComponent(raw).toUpperCase();

    // 1) data-filter 속성으로 먼저 찾기 (테마에 따라 ".AI" 또는 "AI")
    var btn =
      sec.querySelector('[data-filter="' + hash + '"]') ||
      sec.querySelector('[data-filter=".' + hash + '"]');

    // 2) 못 찾으면 라벨 텍스트로 탐색 (보안/네트워크/웹/앱/AI 등)
    if (!btn) {
      var candidates = sec.querySelectorAll(
        '.isotope-filters .nav-link, .isotope-filters .btn'
      );
      btn = Array.from(candidates).find(function (el) {
        return el.textContent.replace(/\s+/g, '').toUpperCase().includes(hash);
      });
    }

    // 3) 마지막으로 '전체'('*') 지원
    if (!btn && hash === '*' || hash === 'ALL') {
      btn =
        sec.querySelector('[data-filter="*"]') ||
        Array.from(
          sec.querySelectorAll('.isotope-filters .nav-link, .isotope-filters .btn')
        ).find(function (el) {
          return /전체|ALL/i.test(el.textContent);
        });
    }

    if (btn) {
      // 스크롤해서 섹션으로 가져오고 클릭
      sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
      // 버튼이 Isotope 필터인 경우 click이 가장 호환성이 좋음
      setTimeout(function () {
        btn.click();
      }, 50);
    }
  });
})();
</script>