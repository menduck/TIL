# 2576	홀수	
'''
https://www.acmicpc.net/problem/2576
'''

import sys
numbers = []
for _ in range(7):
  number = int(sys.stdin.readline().strip())
  # 받은 입력값이 홀수이면 list에 추가한다.
  if number% 2:
    numbers.append(number)

# 홀수 리스트에 길이가 있으면 합과 최소값을 출력하고 아니면 -1를 출력한다.
if len(numbers) :
  print(sum(numbers))
  print(min(numbers))
else:
  print(-1)
