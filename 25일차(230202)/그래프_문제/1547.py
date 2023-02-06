# 1547 공

import sys
M = int(sys.stdin.readline().strip())
line = [1,2,3]

for _ in range(M):
    x,y = map(int,sys.stdin.readline().strip().split() )
    for cup_num in range(len(line)):
        # x와 같은 컵 번호는 y로 바꾼다.
        if  line[cup_num]== x: 
            line[cup_num] = y
        # y와 같은 컵 번호는 x로 바꾼다.
        elif line[cup_num]== y: 
            line[cup_num] = x
            
# 컵은 가장 왼쪽에 고정되어있기때문에 첫번째 요소 출력
print(line[0])