# 비동기
- 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

# Ajax
- 비동기적인 웹 애플리케이션 개발을 위한 프로그래밍 기술명

## Ajax 사용 이유
- 사용자의 요청에 대한 즉각적인 반응을 제공하면서, 페이지 전체를 다시 로드하지 않고 필요한 부분만 업데이트 하는 것을 목표

## XMLHttpRequest
- JavaScript 객체로, 클라이언트와 서버 간에 데이터를 비동기적으로 주고받을 수 있도록 해주는 객체
- JavaScript 코드에서 서버에 요청을 보내고, 서버로부터 응답을 받을 수 있음

# Axios
- JavaScript에서 HTTP요청을 보내는 라이브러리
- 주로 프론트엔드 프레임워크에서 사용

## Axios 기본 문법

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  axios({
    method: 'HTTP 메서드',
    url: '요청 URL',
  })
    .then(성공하면 수행할 콜백함수)
    .catch(실패하면 수행할 콜백함수)
</script>
```
