# 10798 세로 읽기
'''
# 문제 풀이
- 이차원리스트(행렬 형태)로 받아 열 기준으로 출력한다.
'''
import sys

data = [list(sys.stdin.readline().strip()) for _ in range(5)]

for i in range(15): # 한 줄에 최대 15자 글자가 들어간다.
    for j in range(5):
        if len(data[j]) > i : # 한 라인의 길이가 i보다 클때만 출력한다.
            print(data[j][i], end ='')


