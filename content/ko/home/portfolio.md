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
    - name: 전체
      tag: '*'
    - name: 보안
      tag: SEC
    - name: 네트워크
      tag: NET
    - name: 웹/앱
      tag: WEB
    - name: 데이터 파이프라인
      tag: DATA

design:
  columns: '1'
  view: compact
  flip_alt_rows: true
  background: {}
  spacing: {padding: [0, 0, 0, 0]}
---

<style>
/* Portfolio filter buttons: hover/active in point color */
.home-section .isotope-filters .btn:hover,
.home-section .isotope-filters .btn:focus,
.home-section .isotope-filters .btn.active {
  color: #fff !important;
  background-color: #3A86FF !important; /* point color */
  border-color: #3A86FF !important;
  box-shadow: 0 6px 14px rgba(58,134,255,0.28);
}

/* Dark mode contrast */
.dark .home-section .isotope-filters .btn:hover,
.dark .home-section .isotope-filters .btn:focus,
.dark .home-section .isotope-filters .btn.active {
  color: #0D1B2A !important;           /* navy text for contrast on bright chip */
  background-color: #3A86FF !important;
  border-color: #3A86FF !important;
}
</style>
