---
# 슬라이드/캐러셀 섹션
widget: slider
headless: true
active: true
weight: 1                # 화면에서 가장 위로 오게 (기존 hero/intro보다 작은 값)
title: ""                # 섹션 제목 숨김

design:
  height: "70vh"         # 슬라이드 높이 (px, vh 모두 가능)
  interval: 5000         # 자동 전환 간격(ms) - 0이면 자동전환 없음
  loop: true             # 마지막 다음에 첫 슬라이드로 순환
  indicators: true       # 하단 ●●● 인디케이터
  arrows: true           # 양옆 화살표 노출
  effect: slide          # slide | fade

content:
  slides:
    - title: "KJH 포트폴리오"
      subtitle: "프로젝트와 도전을 통해 성장하는 과정을 기록합니다."
      align: center
      cta:
        - label: "소개 보기"
          url: "/about/"
          style: primary
        - label: "프로젝트"
          url: "/project/"
          style: outline
      background:
        image: "media/desk.jpg"   # static/ 에 두는 이미지 경로
        position: "center"
        filters:
          brightness: 0.65                # 어둡게(텍스트 가독성)
    # - title: "취미"
    #   subtitle: "여러가지 취미"
    #   align: center
    #   cta:
    #     - label: "여행 기록"
    #       url: "/post/"
    #       style: primary
    #   background:
    #     image: "media/slider/field.jpg"
    #     position: "center"
    #     filters:
    #       brightness: 0.55
    - title: "연락하기"
      subtitle: "협업과 피드백은 언제나 환영합니다."
      align: center
      cta:
        - label: "Contact"
          url: "/contact/"
          style: primary
      background:
        image: "media/contact.jpg"
        position: "center"
        filters:
          brightness: 0.55