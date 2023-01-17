import sys

number_list = [int(sys.stdin.readline().strip()) for _ in range(9)]
max_num = max(number_list)
print(max_num)
print(number_list.index(max_num)+1) # 인덱스 값은 0부터 시작이므로 인덱스 값에 +1를 해주어 몇 번째 수인지를 출력함