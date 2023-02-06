# 입출력 문제

# 문제 1
import sys
sys.stdin = open('13일차(230111)/practice_txt/input1.txt','r')
numbers = map(int,input().split())
print(*numbers)

# 문제 2
# import sys 이미 2라인에서 import해줬기 때문에 아래 문제에서 생략합니다.
sys.stdin = open('13일차(230111)/practice_txt/input2.txt','r')
strings= input().split()
print(*strings)

# 문제 3
sys.stdin = open('13일차(230111)/practice_txt/input3.txt','r')
test_case = int(input())

for _ in range(test_case) :
  set_count = int(input())
  for _ in range(set_count) :
    print(int(input()))

# 문제 4
sys.stdin = open('13일차(230111)/practice_txt/input4.txt','r')
test_case = int(input())

for _ in range(test_case) :
  set_count = int(input())
  for _ in range(set_count) :
    print(*map(int,input().split()))

# 문제 5
sys.stdin = open('13일차(230111)/practice_txt/input5.txt','r')
test_case = int(input())
for _ in range(test_case):
  set_count = int(input())
  for _ in range(set_count) :
    print(*input().split())

# 문제 6
sys.stdin = open('13일차(230111)/practice_txt/input6.txt','r')
test_case = int(input())

for _ in range(test_case) :
  set_count = int(input())
  for _ in range(set_count) :
    print(*map(int,input().split()))
    
# 문제 7
sys.stdin = open('13일차(230111)/practice_txt/input7.txt','r')
test_case, input_case = map(int, input().split())
for _ in range(test_case):
  num = int(input())
  print(num)

# 문제 8
sys.stdin = open('13일차(230111)/practice_txt/input8.txt','r')
test_case, input_case = map(int, input().split())
for _ in range(test_case):
  for _ in range(input_case):
    num = list(map(int,input().split()))
    print(*num)

# 문제 9
sys.stdin = open('13일차(230111)/practice_txt/input9.txt','r')
test_case, input_case = map(int, input().split())
for _ in range(test_case):
  for _ in range(input_case):
    num = list(map(int,input().split()))
    print(*num)
