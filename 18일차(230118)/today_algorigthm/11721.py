# 11721 열개씩 끊어 출력하기
'''
https://www.acmicpc.net/problem/11721

# 문제 풀이
- 10개씩 끊어 출력하기 위해서 문자열 slicing을 이용함
- 0에서 문장 길이 끝까지 10씩 건너뛰며 range를 돌려 문자열에서 10개씩 출력함.
- 문자열 slicing의 두번째 요소인 마지막 인덱스는 마지막 인덱스보다 더 큰 값을 넣으면 끝까지 출력하기 때문에 10개가 안되더라도 출력함.
'''
import sys

sentense = sys.stdin.readline().strip()

for i in range(0,len(sentense),10) :
  print(sentense[i:i+10])