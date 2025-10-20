---
# 위젯 타입을 markdown으로 지정합니다.
widget: markdown
active: true
weight: 10

# 위젯 자체의 상하좌우 여백을 제거합니다.
design:
  spacing:
    padding: [0, 0, 0, 0]
---

{{< md_to_html >}}
<div style="
  /* 이 부분이 화면을 꽉 채우는 역할을 합니다 */
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
">
  <div style="
    /* 이 부분은 이전과 동일한 배경 이미지와 텍스트 스타일입니다 */
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/media/desk.jpg');
    background-size: cover;
    background-position: center;
    padding: 10rem 1rem;
    color: white;
    text-align: center;
  ">
    <h1 class="display-3">KJH 포트폴리오</h1>
    <p class="lead">프로젝트와 도전을 통해 성장하는 과정을 기록합니다.</p>
    <a class="btn btn-lg btn-primary" href="/about/">소개 보기</a>
  </div>
</div>
{{< /md_to_html >}}