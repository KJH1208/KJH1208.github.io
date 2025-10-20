---
# 위젯 타입을 markdown으로 지정합니다.
widget: markdown
active: true
weight: 10

# 위젯 자체의 상하좌우 여백을 제거하여 꽉 찬 화면 효과를 줍니다.
design:
  spacing:
    padding: [0, 0, 0, 0]
---

{{%/* md_to_html */%}}
<div style="
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/media/desk.jpg');
  background-size: cover;
  background-position: center;
  padding: 10rem 1rem;
  border-radius: 10px;
  color: white;
  text-align: center; /* 텍스트 가운데 정렬 */
">
  <h1 class="display-3">KJH 포트폴리오</h1>
  <p class="lead">프로젝트와 도전을 통해 성장하는 과정을 기록합니다.</p>
  <a class="btn btn-lg btn-primary" href="/about/">소개 보기</a>
</div>
{{%/* /md_to_html */%}}