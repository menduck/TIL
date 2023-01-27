# 1927 최소 힙

import sys
import heapq
N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
  x = int(sys.stdin.readline().strip())
  if x:
    heapq.heappush(arr,x)
  else:
    if not arr: # arr가 비워져있으면 True
      print(0)
    else:
      print(heapq.heappop(arr))