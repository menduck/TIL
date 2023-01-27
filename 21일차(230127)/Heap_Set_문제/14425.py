# 14425 문자열 집합

'''
https://www.acmicpc.net/problem/14425

# soltuion - 실패

```py
import sys
N, M = map(int, sys.stdin.readline().strip().split())
S = set([sys.stdin.readline().strip() for _ in range(N)])
check_str = set([sys.stdin.readline().strip() for _ in range(M)])

print(len(check_str & S))
```

- 반례
  input = [2, 2, a, b, a, a]일때 출력값이 2가 나와야되는데 1이 출력됨.
- 검사해야 할 문자열에 중복된 문자열이 있을 수도 있는데 set를 하면 그 경우의 수가 무시됨.

'''
# solution - list 탐색 O(n)
# import sys
# N, M = map(int, sys.stdin.readline().strip().split())
# S = [sys.stdin.readline().strip() for _ in range(N)]
# check_str = [sys.stdin.readline().strip() for _ in range(M)]
# cnt = 0
# for word in check_str:
#   if word in S: # O(n)
#     cnt +=1
# print(cnt)

# solution - set탐색 O(1)
import sys
N, M = map(int, sys.stdin.readline().strip().split())
S = set([sys.stdin.readline().strip() for _ in range(N)])
check_str = [sys.stdin.readline().strip() for _ in range(M)]
cnt = 0
for word in check_str:
  if word in S: # O(1)
    cnt +=1
print(cnt)
    