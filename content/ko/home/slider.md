---
# 위젯 타입을 slider로 지정
widget: slider
# 활성화 상태
active: true
# 페이지 맨 위에 오도록 가중치를 10으로 설정
weight: 1

# `content` 블록 안에 `slides` 목록을 정의합니다. (items -> content.slides 로 변경)
content:
  slides:
    # --- 첫 번째 슬라이드 ---
    - title: KJH 포트폴리오
      content: 프로젝트와 도전을 통해 성장하는 과정을 기록합니다.
      buttons:
        - name: '소개 보기'
          url: '/about/'
      image:
        filename: desk.jpg
        filters:
          brightness: 0.6
    # --- 두 번째 슬라이드 ---
    - title: 취미
      content: 여러가지 취미를 가지며 지치지 않는 일상을 유지합니다.
      buttons:
        - name: '여행 기록'
          url: '/post/'
      image:
        filename: field.jpg
        filters:
          brightness: 0.6
    # --- 세 번째 슬라이드 ---
    - title: 연락하기
      content: 협업과 피드백은 언제나 환영합니다.
      buttons:
        - name: 'Contact'
          url: '/contact/'
      image:
        filename: contact.jpg
        filters:
          brightness: 0.6

# 디자인 설정
design:
  # 전체 너비 슬라이더를 위해 `view: 3` 추가
  view: 3
  # 글씨 색상을 밝게 설정
  font_color: 'light'
---