# 5576 콘테스트

import sys
w_score = [int(sys.stdin.readline().strip()) for _ in range(10)]
k_score = [int(sys.stdin.readline().strip()) for _ in range(10)]

# 내림차순으로 정렬
sort_w_score = sorted(w_score, reverse=True)
sort_k_score = sorted(k_score, reverse=True)

# 첫번째 요소부터 세번째 요소까지 더한 값을 각각 출력
print(sum(sort_w_score[0:3]), sum(sort_k_score[0:3]))