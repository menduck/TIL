# 20001 고무오리 디버깅

import sys
start_str = sys.stdin.readline().strip()
problem = []
while True:
  word = sys.stdin.readline().strip()
  if word == '문제':
    problem.append(0)
  if word == '고무오리':
    if not problem:
      problem.append(0)
      problem.append(0)
    else:
      problem.pop()
  if word == '고무오리 디버깅 끝':
    break
if not problem:
  print('고무오리야 사랑해')
else:
  print('힝구')