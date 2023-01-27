# 1269 대칭 차집합

import sys
A_n, B_n = map(int, sys.stdin.readline().strip().split())
A = set(list(map(int, sys.stdin.readline().strip().split())))
B = set(list(map(int, sys.stdin.readline().strip().split())))

print(len(A ^ B))

