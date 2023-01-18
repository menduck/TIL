# 나무조각
'''
https://www.acmicpc.net/problem/2947

# 문제 풀이
- bubble sort 구현을 의도한 문제이다.

'''
import sys
numbers = list(map(int,sys.stdin.readline().strip().split()))

while True:
  for i in range(0,len(numbers)-1):
    # 왼쪽 요소가 오른쪽 요소보다 크면
    if numbers[i] > numbers [i+1]:
      # 왼쪽 요소와 오른쪽 요소의 자리를 바꿔주고
      numbers[i], numbers [i+1] =  numbers [i+1],  numbers [i]
      # 출력한다.
      print(*numbers)

      # numbers가 오름차순으로 정렬이 되면 반복문을 종료한다.
  if numbers == [1,2,3,4,5]:
    break
    
