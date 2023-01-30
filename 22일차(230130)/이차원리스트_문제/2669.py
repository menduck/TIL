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
import sys

area = [[0] * 100 for _ in range(101)]
for _ in range(4):
  x1,y1,x2,y2 = map(int, sys.stdin.readline().split())

  for i in range(x1,x2):
    for j in range(y1,y2):
        area[i][j] = 1

result = sum(area,[])
print(sum(result))