'''
https://www.acmicpc.net/problem/3009

# 3009 네 번째 점

# 문제 풀이
- 세 점을 리스트에 담는다.
- x와 y의 서로 교차하는 경우의 수를 계산하고 세 점을 담은 리스트에 비교하고 없느 경우의 수를 출력함.
'''
import sys

# 세 점을 x_y_list에 담음.
x_y_list = []
for _ in range(3):
  point = list(map(int, sys.stdin.readline().strip().split()))
  x_y_list.append(point)


for [x,_] in x_y_list:
  for [_,y] in x_y_list:
    # [x,y]의 모든 경우의 수가 세 점을 담은 리스트 안에 없을 경우
    if [x,y] not in x_y_list:
      # 그 경우의 수를 출력함.
      print(x,y)

