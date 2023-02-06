# 문제 1
# 숫자를 입력 받고, 10을 더해서 출력하세요.
number_input = int(input('숫자를 입력해주세요 > '))
print(number_input + 10)

# 문제2
# 좋아하는 음식을 입력 받고, 출력하세요.
menu_input = input('좋아하는 음식을 입력해주세요 > ')
print('좋아하는 음식 :',menu_input)

# 문제3
# 이름과 태어난 년도를 입력 받고, 출력하세요.(단, 태어난 년도를 나이로 변환해서 출력하세요.)
name_input = input('이름을 입력해주세요 > ')
birthday_input = int(input('태어난 년도를 입력해주세요 > '))
print(f'저의 이름은 {name_input}이고, 올해 나이는 {2023 - birthday_input + 1}세 입니다.')

# 문제4
# 문장 두 개를 입력 받고, 두 문장을 연결해서 출력하세요.
str1_input = input('첫 번째 문장을 입력해주세요 > ')
str2_input = input('두 번째 문장을 입력해주세요 > ')
print(f'{str1_input}{str2_input}')

# 문제5
# 숫자 한 개를 입력 받고, 숫자의 부호를 바꿔서 출력하세요.
num_input = int(input('숫자를 입력해주세요 > '))
print(-1 * num_input )

# 문제6
# 숫자 두 개를 입력 받고, 두 숫자에 대한 아래 산술 연산 결과를 출력하세요.
num1_input = int(input("첫 번째 숫자를 입력해주세요 > "))
num2_input = int(input("두 번째 숫자를 입력해주세요 > "))
print('더하기 연산 :', num1_input+num2_input)
print('빼기 연산 :', num1_input-num2_input)
print('곱하기 연산 :', num1_input*num2_input)
print('몫 연산 :', num1_input//num2_input)
print('나머지 연산 :', num1_input%num2_input)

# 문제7
# 숫자 세 개를 입력 받고, 세 숫자의 평균을 출력하세요.
number1_input = int(input('첫 번째 숫자를 입력해주세요 > '))
number2_input = int(input('두 번째 숫자를 입력해주세요 > '))
number3_input = int(input('세 번째 숫자를 입력해주세요 > '))
print((number1_input + number2_input + number3_input) / 3)

# 문제8
# 숫자 다섯 개를 입력 받고, 다섯 개의 숫자를 리스트 객체에 저장해서 출력하세요.
number4_input = int(input('첫 번째 숫자를 입력해주세요 > '))
number5_input = int(input('두 번째 숫자를 입력해주세요 > '))
number6_input = int(input('세 번째 숫자를 입력해주세요 > '))
number7_input = int(input('네 번째 숫자를 입력해주세요 > '))
number8_input = int(input('다섯 번째 숫자를 입력해주세요 > '))
number_list = []
number_list.append(number4_input)
number_list.append(number5_input)
number_list.append(number6_input)
number_list.append(number7_input)
number_list.append(number8_input)
print(number_list)

# 문제9
# 문자열 하나와 숫자 한 개를 입력 받고, 문자열을 숫자만큼 반복해서 출력하세요.
repeat_str_input = input('문자열을 입력해주세요 > ')
repeat_num_input = int(input('숫자를 입력해주세요'))
print(repeat_str_input * repeat_num_input)

# 문제10
# 숫자 다섯 개를 입력 받고, 입력할 때 마다 입력한 숫자들의 합을 출력하세요.
sum_num1_input = int(input('첫 번째 숫자를 입력해주세요 > '))
print(sum_num1_input)
sum_num2_input = int(input('두 번째 숫자를 입력해주세요 > '))
print(sum_num1_input + sum_num2_input)
sum_num3_input = int(input('세 번째 숫자를 입력해주세요 > '))
print(sum_num1_input + sum_num2_input + sum_num3_input)
sum_num4_input = int(input('네 번째 숫자를 입력해주세요 > '))
print(sum_num1_input + sum_num2_input + sum_num3_input + sum_num4_input)
sum_num5_input = int(input('다섯 번째 숫자를 입력해주세요 > '))
print(sum_num1_input + sum_num2_input + sum_num3_input + sum_num4_input + sum_num5_input)
