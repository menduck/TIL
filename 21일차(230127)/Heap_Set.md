# 우선순위 큐 (Priority Queue)
- 우선순위(중요도, 크기 등 순서 이외의 기준)를 기준으로 가장 우선순위 높은 데이터가 먼저 나가는 방식

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/215101743-e329415f-4f75-4a73-82c9-cbc135a316f2.PNG'>
</p>

- 우선순위의 예
    1. 가중치가 있는 데이터
    2. 작업 스케줄링
    3. 네트워크

- 우선순위 큐를 구현하는 방법
    1. 배열
    2. 힙 (배열보다 더 빠름)

    <p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/215101751-a65ec895-b9a0-4d46-94ff-8f9e8cf25d7d.PNG'>
</p>

# Heap (힙)
- 우선순위 큐(Priority Queue)를 구현하는 방법 중 하나
- 최댓값 또는 최솟값을 빠르게 찾아내도록 만들어진 데이터 구조
- 완전 이진 트리 형태로 느슨한 정렬 상태를 지속적으로 유지(완벽하게 정렬된 상태가 아님)
- 중복허용

## Heap 활용
1. 데이터가 지속적으로 정렬되야 하는 경우
2. 데이터가 삽입/삭제가 빈번할 경우

## 파이썬과 Heap
- 파이썬엔 heapq모듈로 Heap을 구현함.
- Minheap(최소 힙)으로 구현됨
- 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠름

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/215100804-e94b2f50-e040-4bb3-8e1d-326d59d5c61a.PNG'>
</p>

# set

-   중복을 허용하지 않음.
-   순서가 없음
    -   순서가 없기 때문에 index로 접근X (list나 tuple에 담아서 index로 접근)

set()의 값 추가/ 여러 값 추가/ 제거

```py
a = set([1,2,3])

# 특정 값 추가
a.add(4)
print(a) # {1, 2, 3, 4}

# 여러 값 추가
a.update([5,6,7,8])
print(a) # {1, 2, 3, 4, 5, 6, 7, 8}

# 특정 값 제거
a.remove(1)
print(a) # {2, 3, 4, 5, 6, 7, 8}
```

## set()의 교집합/합집합/차집합

-   set()의 교집합
    1.  & 연산자 사용
    2.  .intersection() 사용

```py
a = set([1,2,3,4,5])
b = set([3,4,5,6,7,8,9])

print(a & b) # {3, 4, 5}
print(a.intersection(b)) # {3, 4, 5}
```

-   set()의 합집합
    1.  | 연산자 사용
    2.  .union() 사용

```py
a = set([1,2,3,4,5])
b = set([3,4,5,6,7,8,9])

print(a | b) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

-   set()의 차집합
    1.  \* 연산자 사용
    2.  .difference() 사용

```py
a = set([1,2,3,4,5])
b = set([3,4,5,6,7,8,9])

print(a - b) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a.difference(b)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

-   set()의 대칭 차집합
    - 각 집합에서 교집합을 제한 집합
    1.  ^ 연산자 사용
    
```py
a = set([1,2,3,4,5])
b = set([3,4,5,6,7,8,9])

print(a ^ b) # {1, 2, 6, 7, 8, 9}
```

## set의 시간복잡도
- 중복없는 리스트를 탐색할때, set으로 탐색하면 O(1), list으로 탐색하면 O(n)

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/215099399-f2fea38d-0f0b-4dcc-9317-b7d7eed2af07.PNG'>
</p>

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/215099405-9e4ae479-7a6d-4d69-ac2b-c281d84d40d1.PNG'>
</p>

