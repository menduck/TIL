# https://www.acmicpc.net/problem/2506

import sys

t = int(sys.stdin.readline().strip())
score_list = list(map(int, sys.stdin.readline().strip().split()))

sum = 0
totalScore = 0
for score in score_list:
  if score == 1:
    sum += 1
  else:
    sum = 0
  totalScore += sum
print(totalScore)