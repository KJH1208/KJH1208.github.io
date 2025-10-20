---
# 위젯 타입을 hero로 지정
widget: hero
# 활성화 상태
active: true
# 페이지 맨 위에 오도록 가중치를 10으로 설정
weight: 10

# 모든 복잡한 설정을 제거하고 슬라이드 딱 하나만 테스트합니다.
items:
  - title: 히어로 위젯 테스트
    content: 이 글이 보인다면 hero 위젯은 작동하는 것입니다.
    image:
      # 이 이미지가 assets/media/ 폴더에 있는지 확인해주세요.
      filename: desk.jpg 
      filters:
        brightness: 0.6

# 디자인 설정
design:
  spacing:
    padding: ['0', '0', '0', '0']
  font_color: 'light'
---