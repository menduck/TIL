
import sys

cnt = 0

for i in range(8):
    room = sys.stdin.readline().strip()
    for j in range(len(room)):
        # 라인 번호(i)가 가 짝수이고 그 라인 안에 인덱스(j)가 짝수일때 요소가 'F'이면 카운팅해줌
        if i%2 == 0 and j%2 == 0 and room[j] == 'F': 
          cnt += 1
        # 라인 번호(i)가 가 홀수이고 그 라인 안에 인덱스(j)가 홀수일때 요소가 'F'이면 카운팅해줌
        elif i%2 == 1 and j%2 == 1 and room[j] == 'F':
          cnt += 1      
print(cnt)
