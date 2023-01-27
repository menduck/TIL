# 10817 세 수

import sys
import heapq
numbers = list(map(int, sys.stdin.readline().strip().split()))

print(heapq.nlargest(2,numbers)[-1])