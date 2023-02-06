# 입출력 문제

# 문제 1 
num1 = int(input())
print(num1)

# 문제 2 
num1, num2 = map(int, input().split(' '))
print(num1, num2)

# 문제 3 
num1, num2, num3 = map(int, input().split(' '))
print(num1, num2, num3)

# 문제 4 
str1, str2, str3 = input().split(' ')
print(str1, str2, str3)

# 문제 5
numbers = map(int, input().split(' '))
print(*numbers)

# 문제 6 
numbers = map(int, input().split(' '))
print(*numbers)

# 문제 7 
alphabet_list = input().split(' ')
print(*alphabet_list)

# 문제 8
numbers = map(int, input().split(' '))
# 언패킹
print(*numbers)

# for문으로 출력
for number in numbers :
  print(number, end = ' ')

# 문제 9
numbers = map(int, input().split(' '))
# 언패킹
print(*numbers)

# for문으로 출력
for number in numbers :
  print(number, end = ' ')