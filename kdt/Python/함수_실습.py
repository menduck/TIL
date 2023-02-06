# 문제 1
'''
정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.

단, abs() 함수는 사용하지 마세요.
'''
num1 = int(input("정수를 입력하세요 > "))

def abs_min(number) :
  if number< 0 : 
    return number * -1
  return number 

print(abs_min(num1))

# 문제 2
'''
정수만 저장한 리스트가 주어집니다.

리스트 요소의 개수를 출력하세요.

단, len() 함수는 사용하지 마세요
'''
number_list = [1, 2, 3, 4, 5]
number_list2 = []


def len_min(number_list):
  cnt = 0
  for number in number_list :
    cnt += 1
  return cnt

print(len_min(number_list)) # 5
print(len_min(number_list2)) # 0

# 문제 3
''' 
정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수들의 합을 출력하세요.

단, sum() 함수는 사용하지 마세요.
'''
number_list = [1, 2, 3, 4, 5]
number_list2 = [-1, -2, -3, -4, -5]

def sum_min(number_list):
  sum = 0
  for number in number_list:
    sum += number
  return sum

print(sum_min(number_list)) # 15
print(sum_min(number_list2)) # -15

# 문제 4
'''
정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수들의 평균을 출력하세요.

단, len() / sum() 함수는 사용하지 마세요.
'''
number_list = [2, 4, 6]
number_list2 = [2, 3, 5, 7]

def mean_min(num_list):
  cnt, sum = 0, 0
  for number in num_list:
    cnt += 1
    sum += number
  return sum/cnt

print(mean_min(number_list)) # 4.0
print(mean_min(number_list2)) # 4.25

# 문제 5
''' 
정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수들의 곱을 출력하세요.
'''
number_list = [1, 2, 3, 4, 5]
number_list2 = [-1, -2, 3]

def total_multiply_min(num_list):
  total_multiply = 1
  for number in num_list:
    total_multiply *= number
  return total_multiply

print(total_multiply_min(number_list)) # 120
print(total_multiply_min(number_list2)) # 6
    
# 문제 6
'''
양의 정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수 중 가장 큰 값을 출력하세요.

단, max() 함수는 사용하지 마세요.
'''
number_list = [1, 2, 3, 4, 5]
number_list2 = [1, 1, 1]

def max_min(num_list):
  return sorted(num_list)[-1]

print(max_min(number_list)) # 5
print(max_min(number_list2)) # 1

# 문제 7
'''
양의 정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수 중 가장 작은 값을 출력하세요.

단, min() 함수는 사용하지 마세요.
'''
number_list = [1, 2, 3, 4, 5]
number_list2 = [5, 5, 5, 2]

def min_min(num_list):
  return sorted(num_list)[0]

print(min_min(number_list)) # 1
print(min_min(number_list2)) # 2

