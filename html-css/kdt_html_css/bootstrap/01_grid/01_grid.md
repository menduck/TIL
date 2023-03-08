# Bootstrap Grid system
: 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템

- 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 테스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움.

- 왜 12개의 칼럼?
  - 적당히 큰 수이면서 약수가 많은 수
  - 다양한 레이아웃을 조정할 수 있음

## Grid system 핵심 클래스
👩‍💻 [grid 실습파일](../01_grid/%EC%8B%A4%EC%8A%B5/01_grid.html)

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/223460990-0489e650-4695-436e-850f-ede33e57a6ac.PNG'>
</p>

- 1개 row안에 12칸의 column 영역이 구성
- 각 요소가 12칸 중 몇 칸을 차지할 것인지 지정함.
- 중첩이 가능
- offset?
  - 그리드를 일정 크기만큼 간격을 둘 수 있는 기능

## gutters
👩‍💻 [gutters 실습파일](../01_grid/%EC%8B%A4%EC%8A%B5/02_gutters.html)

: Grid system에서 column 사이에 padding 영역

- 키워드 이해하기
  - gx-number : 수평
  - gy-number : 수직
  - g-number : 수평수직