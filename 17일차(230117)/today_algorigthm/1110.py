# 1110 더하기 사이클

import sys
N = sys.stdin.readline().strip() # '26'

# result에 N값을 할당한다. => 나중에 while문의 종료조건으로 값이 변한 N값과 비교하기 위함
result = N # 26
cnt = 0


while True:
  # N의 각 자리수를 담은 리스트
  N_list = list(map(int,N)) # [2,6] int

  # N의 각 자리수를 더한 값의 일의 자리 수
  N_sum_last = str(sum(N_list))[-1] # '8'
  
  # 새로운 수인 N = 그 전 사이클의 N의 일의 자리에 *10을 하고 각 자리수를 더한 값의 일의 자리수를 더해주면 됨
  N = str(N_list[-1]*10 + int(N_sum_last)) # '68'

  cnt += 1

  # 새로운 수가 된 N값과 맨 처음의 N값을 담았던 result값이 같으면 카운팅을 출력하고 whlie문을 빠져나감
  if N == result:
    print(cnt)
    break