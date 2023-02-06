# 2592 대표값

import sys
from collections import Counter

numbers = [int(sys.stdin.readline().strip()) for _ in range(10)]

#가장 개수가 많은 1개의 데이터 [()]
# 최빈값이 둘 이상일 경우 그 중 하나만 출력하기 때문에 최빈값이 여러 개일때를 고려하지 않음
common_number = Counter(numbers).most_common(1) 
average = sum(numbers) // 10

print(average, common_number[0][0], sep = '\n')

# 최빈값 구하는 방법2
print(max(numbers , key = numbers.count))
