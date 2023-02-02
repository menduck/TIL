# 2669 직사각형 네개의 합집합의 면적 구하기
'''

# solution - 시도 / 성공
```py
import sys
import itertools
area = 0
common_area = 0
x_range= []
y_range = []
for _ in range(4):
  x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
  area += (x2 - x1) * (y2 - y1)
  x_range.append(set(range(x1,x2+1)))
  y_range.append(set(range(y1,y2+1)))


a = list(itertools.combinations([0,1,2,3],2))
for i,j in a:
  common_x_range = len(x_range[i] & x_range[j]) -1
  common_y_range = len(y_range[i] & y_range[j]) -1
  if common_x_range > 0  and common_y_range > 0:
    common_area += (common_x_range) * (common_y_range)


b = list(itertools.combinations([0,1,2,3],3))
for i,j,w in b:
  common_x_range = len(x_range[i] & x_range[j]& x_range[w]) -1
  common_y_range = len(y_range[i] & y_range[j]& y_range[w]) -1
  if common_x_range > 0  and common_y_range > 0:
    common_area -= (common_x_range) * (common_y_range)


c = list(itertools.combinations([0,1,2,3],4))
for i,j,w,z in c:
  common_x_range = len(x_range[i] & x_range[j]& x_range[w]& x_range[z]) -1
  common_y_range = len(y_range[i] & y_range[j]& y_range[w]& y_range[z]) -1
  if common_x_range > 0  and common_y_range > 0:
    common_area += (common_x_range) * (common_y_range)

print(area - common_area)
```
'''
# solution

import sys
total_area_point = set() # 중복방지를 위해 set으로 설정
for _ in range(4):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().strip().split())
    for x in range(x1, x2):
        for y in range(y1,y2):
            total_area_point.add((x,y)) # x,y 좌표를 set에 추가한다.
print(len(total_area_point)) # 중복이 제거된 좌표 개수를 출력한다.

'''
# 문제 풀이
- 한 칸은 4개의 좌표로 이뤄져 있다.
- 계산을 용이하기 위해 한 칸의 4개의 좌표 중 하나의 좌표를 기준점으로 잡고 개수를 셌다. 
  - 나의 기준 좌표(x,y)는 왼쪽 아래 좌표이다.

  - 만약 입력값이 1 2 4 4 일때 

  - x1 = 1, y1 = 2, x2 = 4, y2 = 4 이다.

  - 기준 좌표는
    (1,2) (2,2) (3,2)
    (1,3) (2,3) (3,3)
    
    넓이는 이 좌표들의 개수인 6이다.

  - x의 범위는 1 2 3
    y의 범위는 2 3

  - 이를 일반화 했을때 
    x의 범위는 range(x1, x2)
    y의 범위는 range(y1, y2)

- 이렇게 네개의 직사각형 좌표들을 받고, set을 (x,y)을 넣어 중복되는 좌표값을 제거한다.

- 중복되지 않는 좌표값이 들어있는 set 집합 요소의 길이를 출력한다. 

'''