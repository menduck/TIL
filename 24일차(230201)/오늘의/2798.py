# 2798 블랙잭
import sys
import itertools
N,M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
# 내림차순을 정렬
sort_cards = sorted(cards, reverse=True)

# 고를 수 있는 카드 세가지의 경우의 수 (중복X)
three_card = list(itertools.combinations(sort_cards,3))
# [(9, 8, 7), (9, 8, 6), (9, 8, 5), (9, 7, 6), (9, 7, 5), (9, 6, 5), (8, 7, 6), (8, 7, 5), (8, 6, 5), (7, 6, 5)]  

# 카드 3가지의 합
three_sum_conbination = list(map(sum,three_card))

# M보다 작은 수만 추출하고 그 중 가장 작은 값만 출력
under_M_list = list(filter(lambda x:x <=M, three_sum_conbination))
print(max(under_M_list))


