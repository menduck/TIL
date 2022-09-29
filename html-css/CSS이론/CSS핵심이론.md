# CSS란?
- HTMl문서 내에 HTML 태그를 선택해 디자인하고 배치하는 역할.

# CSS 링크하기
  - 내부 CSS 구문 작성
    : html 파일의 <head>...</head> 사이에 <style>... </style>로 시작
  - 외부 CSS 파일로 링크 후 CSS 구문 작성
    : html 파일의 <head>...</head> 사이에 css 파일 링크

# CSS 기본문법

> selector{ <br>
  property : value ;
<br>}

## CSS 선택자
### 선택자 종류
1. 태그 선택자
2. 클래스 선택자 .center
3. 아이디 선택자 #center
4. 태그와 함께 쓰는 선택자 
  - p.center : p태그 중에서 center라는 클래스명을 가지고 있는 선택자.

### 그룹 선택자

1. 그룹 선택자
  - h1,p{color : red}
2. 하위 선택자
  - p_span{color : red} // p태그 안에 span태그
3. 전체 선택자
  - *{color : red}

### 태그 우선순위
1. !important Style
2. inline Style
3. ID Selector Style
4. Class Selector Style
5. Tag Selector Style

## CSS 서식관련 속성






