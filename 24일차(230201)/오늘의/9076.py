# 9076 점수 집계

import sys
N = int(sys.stdin.readline().strip())
for _ in range(N):
  score = list(map(int,sys.stdin.readline().strip().split()))
  # 점수르 오름차순으로 정렬 
  sort_socre = sorted(score)
  # 나머지 3명의 최고점과 최저점의 차이가 4점이상 나는 경우 
  if sort_socre[-2] - sort_socre[1] >= 4:
    print('KIN')
  # 그 외의 경우는 나머지 3명의 점수를 모두 더하고 출력해줌
  else:
    print(sum(sort_socre[1:-1]))