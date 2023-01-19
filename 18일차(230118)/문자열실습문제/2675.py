# 2675 문자열반복
'''
https://www.acmicpc.net/problem/2675
'''
import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
  R,str = sys.stdin.readline().strip().split()
  result = ''
  for s in str:
    result += s*int(R)
  print(result)