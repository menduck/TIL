# 11286 절대값 힙

'''
https://www.acmicpc.net/problem/11286
'''

import sys
import heapq
N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
  x = int(sys.stdin.readline().strip())
  if x:
    heapq.heappush(arr,(abs(x),x))
  else:
    if not arr: # arr가 비워져있으면 True
      print(0)
    else:
      print(heapq.heappop(arr)[1])
    
