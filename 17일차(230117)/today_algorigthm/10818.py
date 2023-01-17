# 10818 최소 최대
import  sys
N = sys.stdin.readline().strip()
N_list = list(map(int, sys.stdin.readline().strip().split()))

print(min(N_list),max(N_list))