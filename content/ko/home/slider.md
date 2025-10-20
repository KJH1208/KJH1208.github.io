---
widget: blank
active: true
weight: 10

# `blank` 위젯은 모든 내용을 `content.text` 안에 넣습니다.
content:
  # 이 옵션은 내용물을 가운데 정렬합니다.
  # 0 = 왼쪽, 1 = 가운데, 2 = 오른쪽
  align: center
  text: |-
    <div style="
      background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/media/desk.jpg');
      background-size: cover;
      background-position: center;
      padding: 10rem 1rem;
      border-radius: 10px;
      color: white;
    ">
      <h1 class="display-3">KJH 포트폴리오</h1>
      <p class="lead">프로젝트와 도전을 통해 성장하는 과정을 기록합니다.</p>
      <a class="btn btn-lg btn-primary" href="/about/">소개 보기</a>
    </div>
  
# `blank` 위젯은 기본적으로 좌우에 여백이 있으므로,
# `advanced` 옵션으로 여백을 제거하여 꽉 찬 화면 효과를 냅니다.
advanced:
  css_style: "padding: 0;"
---