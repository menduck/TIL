# 2750 수 정렬하기
'''
https://www.acmicpc.net/problem/2750
'''

import sys
N = int(sys.stdin.readline().strip())

# N개의 줄에 주어진 수를 리스트에 할당함.
number_list = []
for _ in range(N):
  num = int(sys.stdin.readline().strip())
  number_list.append(num)

# sorted로 오름차순을 해주고, 언패킹으로 list를 풀어주고 개행으로 구분해주어 출력함.
print(*sorted(number_list), sep = '\n')