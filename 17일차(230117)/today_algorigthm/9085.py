'''
https://www.acmicpc.net/problem/9085

# 9085 더하기

'''

import sys
# 테스트 케이스의 개수 입력 받음
T = int(sys.stdin.readline().strip())

# 테스트 케이스 개수만큼 반복하여 입력을 받음.
for _ in range(T):
  N = int(sys.stdin.readline().strip())
  # N개의 자연수를 공백을 구분하여 numbers에 할당함
  numbers = map(int,sys.stdin.readline().strip().split())
  # numbers 객체의 요소를 다 더해 출력함.
  print(sum(numbers))