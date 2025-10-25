---
# An instance of the Contact widget.
# Documentation: https://docs.hugoblox.com/getting-started/page-builder/
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 50

title: Get in touch
subtitle:

content:
  # Automatically link email and phone or display as text?
  autolink: true

  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false

design:
  columns: '1'
---

<div style="text-align:center; margin: 1.5rem 0 0;">
  <a href="/contact/" role="button" class="kjh-transparent-btn">
    연락
  </a>
</div>

<style>
.kjh-transparent-btn {
  display: inline-block;
  padding: 0.8rem 1.6rem;
  font-size: 1.05rem;
  font-weight: 600;
  color: #172a3e;
  background-color: transparent;
  border: 2px solid #172a3e;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.25s ease;
}
.kjh-transparent-btn:hover {
  color: #fff;
  background-color: #172a3e;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}
</style>
