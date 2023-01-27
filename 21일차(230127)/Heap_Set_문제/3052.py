# 3052 나머지
import sys

number_list = [int(sys.stdin.readline().strip()) for _ in range(10)]

remainder_list = list(map(lambda x: x%42, number_list))
unique_remainder_list = set(remainder_list)

print(len(unique_remainder_list))