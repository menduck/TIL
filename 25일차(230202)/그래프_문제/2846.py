# 오르막길

# solution - 시도/성공

# import sys
# N = int(sys.stdin.readline().strip())
# pi = list(map(int,sys.stdin.readline().strip().split()))

# # 오르막의 크기
# d =[pi[i+1] - pi[i] for i in range(len(pi)-1)]

# total_list = []
# total = 0
# for j in range(len(d)):
#     # 변화크기가 양수이면 total에 더해준다.
#     if d[j] > 0:
#         total += d[j]
#     # 변화크기가 음수이면 total에 더하는 것을 멈추고 list에 누적합을 담고 total을 초기화시켜준다.
#     else:
#         total_list.append(total)
#         total = 0
# # 마지막까지 음수가 나오지 않으면 젤 마지막 누적합을 리스트에 추가해준다.
# total_list.append(total)
# print(max(total_list))

# 보완안할 점
# - 변화크기를 따로 리스트에 담지 않고 변화크기를 계산해 바로 누적합한다.
  # - 불필요한 메모리를 낭비할 수 있다

# soltuion - 최종코드/성공
import sys
N = int(sys.stdin.readline().strip())
pi = list(map(int,sys.stdin.readline().strip().split()))

total_sum = 0
total_sum_list = []
for i in range(N-1):
    # 변화크기기가 양수이면 total_sum에 더해준다.
    if pi[i+1] - pi[i] > 0:
        total_sum += pi[i+1] - pi[i]
    else:
        total_sum_list.append(total_sum)
        total_sum = 0
total_sum_list.append(total_sum)
print(max(total_sum_list))