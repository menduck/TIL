'''
https://www.acmicpc.net/problem/10773
# 10773 제로

# 문제 풀이
- 입력값을 입력받는다
- 만약 입력값이 0이면 리스트에 넣은 가장 최신값을 pop()시켜 제거한다.
- 0이 아니면 리스트에 추가한다.
- 그 리스트 요소들의 합을 출력한다.

'''
import sys
K = int(sys.stdin.readline().strip())
result = []
for _ in range(K):
  number = int(sys.stdin.readline().strip())
  if number == 0: 
    result.pop()
  else:
    result.append(number)
print(sum(result))
