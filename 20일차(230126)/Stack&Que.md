# Stack
- LIFO(Last-in First-out, 후입선출)방식
- 데이터를 한쪽에서만 넣고 빼는 자료 구조

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/214800627-f5b63c04-28a5-4a5b-8628-bc67bf9de784.jpg'>
</p>

- 예시
  - 브라우저 히스토리, ctrl + Z
  : 이전 링크로 돌아갈때, 가장 최신 링크를 제거해 이전 링크로 돌아감.
  - 단어 뒤집기

- stack 자료구조 활용 유형
: 괄호 매칭, 함수 호출(재귀 호출), 백트래킹, DFS(깊이 우선 탐색)

- 파이썬의 list로 간편하게 사용하는 법

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/214800720-0f9d2d6d-2b54-45d0-81a4-c4124abe47b6.PNG'>
</p>

- append로 가장 최신의 데이터를 추가하고 pop()으로 제거함

# Que
- FIFO(First-in First-out, 선입선출)방식
- 한 쪽 끝에서 데이터를 넣고, 한 쪽 끝에서만 데이터를 뺄 수 있는 자료 구조

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/214800821-593a1c27-8c2e-4fb5-acd5-a498281a19d8.PNG'>
</p>


- 예시
  - 순서와 대기
    - 프로세스 관리(데이터 버퍼: 메모리가 여유가 없으면, 가장 먼저 들어온 데이터를 올려놨다가 버퍼에서 받아서 처리함 ex) 여러 파일을 인쇄할때)
    - 클라이언트/서버 (Message Queue)
      - 접속 대기열    

<br>

- que 자료구조 활용 유형
  - BFS(너비 우선 탐색)
  - 다익스트라 - 우선순위 큐

## 파이썬의 list
- que는 파이썬의 list로 간편하게 사용할 수 있음

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/214800854-c35bf32d-c17d-44ab-9e0f-38246440033d.PNG'>
</p>

최신 데이터 넣는거 append. 가장 오래된 데이터 빼는거 pop(0)

- 단점

  - 데이터를 뺄 때 큐 안에 있는 데이터가 많을 경우 비효율적임.
    - 맨 앞 데이터가 빠질때, 리스트 인덱스가 하나씩 당겨지기 때문
    - pop()은 시간 복잡도가 O(1)이지만 pop(index)는 O(n)임.

# Deque(Double-Ended Queqe, 덱)
- 양방향으로 삽입과 삭제가 자유로운 큐
- que로 파이썬 list의 단점을 보완해줌
- 양방향 삽입, 추출 모두 큐보다 훨씬 빠르기 때문에 데이터가 많을 경우 시간을 크게 단축시킬 수 있음.
  - popleft()가 O(1)임 (que를 사용시 O(n)임.)

## Deque와 que 비교

- Deque / 시간 복잡도 O(1)

```py
from collections import deque

a = [1, 2, 3, 4, 5]
deque_a = deque(a)
deque_a.popleft()

print(list(deque_a)) # [2, 3, 4, 5]
```

- que / 시간 복잡도 O(n)

```py
a = [1, 2, 3, 4, 5]
a.pop(0)

print(a) # [2, 3, 4, 5]
```
- 리스트에 첫 번째 요소를 삭제할때 pop(0)을 쓰면 O(n)연산을 수행하지만 deque는 leftpop()으로 O(1) 연산을 수행하기 때문에
- 시간이 훨씬 단축된다
- 또한 데이터의 양이 많아질수록 시간을 크게 단축시킬 수 있음.
