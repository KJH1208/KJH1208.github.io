---
# 위젯 타입을 'hero'로 변경합니다.
widget: hero
# 위젯의 순서를 정합니다.
weight: 10
# 슬라이드 쇼 기능을 활성화합니다.
active: true

# 슬라이드에 들어갈 내용들을 'items' 아래에 하나씩 정의합니다.
items:
  # --- 첫 번째 슬라이드 ---
  - title: KJH 포트폴리오
    content: 프로젝트와 도전을 통해 성장하는 과정을 기록합니다.
    # 버튼 설정
    buttons:
      - label: '소개 보기'
        url: '/about/'
    # 이미지 설정
    image:
      # 슬라이드 배경 이미지
      filename: desk.jpg
      # 이미지를 어둡게 만들어 글씨가 잘 보이게 합니다.
      filters:
        brightness: 0.6

  # --- 두 번째 슬라이드 ---
  - title: 취미
    content: 여러가지 취미를 가지며 지치지 않는 일상을 유지합니다.
    buttons:
      - label: '여행 기록'
        url: '/post/'
    image:
      filename: field.jpg
      filters:
        brightness: 0.6

  # --- 세 번째 슬라이드 ---
  - title: 연락하기
    content: 협업과 피드백은 언제나 환영합니다.
    buttons:
      - label: 'Contact'
        url: '/contact/'
    image:
      filename: contact.jpg
      filters:
        brightness: 0.6

# 위젯 디자인 설정
design:
  # 위젯의 너비를 화면에 꽉 차게 설정
  spacing:
    padding: ['0', '0', '0', '0']
  # 글씨 색상을 밝게 설정 (어두운 이미지 위에서 잘 보이도록)
  font_color: 'light'
---