---
# 슬라이드/캐러셀 섹션
widget: gallery
headless: true
active: true
weight: 1                # 화면에서 가장 위로 오게 (기존 hero/intro보다 작은 값)
title: ""                # 섹션 제목 숨김

design:
  columns: "1"        # 한 장씩(전체 폭)
  view: slider        # ← 캐러셀/슬라이더 모드
  interval: 5000      # 자동 전환(ms). 0이면 자동 전환 없음
  arrows: true        # 좌우 화살표
  indicators: true    # 하단 점(●●●)

content:
  items:
    - image: "media/desk.jpg"
      caption: |
        **KJH 포트폴리오**  
        프로젝트와 도전을 통해 성장하는 과정을 기록.
      link:
        text: "소개 보기"
        url: "/about/"

    - image: "media/field.jpg"
      caption: |
        **취미**  
        여러가지 취미를
      link:
        text: "여행 기록"
        url: "/post/"

    - image: "media/contact.jpg"
      caption: |
        **연락**  
        협업과 피드백은 언제나 환영합니다.
      link:
        text: "Contact"
        url: "/contact/"
---
