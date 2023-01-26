# 1453 피시방알바

'''
# solution - 전체 학생 수에 중복된 개수 빼기

```py
import sys
N = int(sys.stdin.readline().strip())
numbers = sys.stdin.readline().strip().split()

print(len(numbers) - len(set(numbers)))
```

# solution - 스택으로 풀기
'''
import sys
N = int(sys.stdin.readline().strip())
numbers = sys.stdin.readline().strip().split()

# 이미 차지한 컴퓨터 번호 리스트
seat = []
# 거절 당하는 사람의 수를 카운팅 함.
cnt = 0 

for num in numbers:
  if num not in seat: # 이미 차지한 컴퓨터 번호 리스트에 없으면
    seat.append(num) # 리스트에 컴퓨터 번호를 추가하고
  else: # 이미 누가 차지하여 번호가 있으면
    cnt += 1 # 카운팅을 증가함
print(cnt)
