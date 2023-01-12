'''
#클래스 이름
Calculator

#인스턴스 변수
number1 : 정수 타입
number2 : 정수 타입

#생성자
두 개의 정수를 인자로 받아서 number1, number2 에 저장합니다.

#메소드
plus
number1 + number2를 반환(return)합니다.

minus
number1 - number2를 반환(return)합니다.

multiply
number1 * number2를 반환(return)합니다.

division
number1 // number2를 반환(return)합니다.

print
인스턴스 변수와 모든 사칙연산 결과를 출력(print)합니다.
'''

class Calculator:
  def __init__(self, number1, number2) -> int:
    self.number1 = number1
    self.number2 = number2
  
  def plus(self) :
    return self.number1 + self.number2
  
  def minus(self) :
    return self.number1 - self.number2

  def multiply(self) :
    return self.number1 * self.number2
  
  def division(self) :
    return self.number1 // self.number2
  
  def print(self) -> str:
    result = f'합 : {self.number1 + self.number2}\n빼기 : {self.number1 - self.number2}\n곱 : {self.number1 * self.number2}\n몫 : {self.number1 // self.number2}'
    return print(result)
  
# 출력

# plus
calculator = Calculator(10, 5)
print(calculator.plus()) # 15

calculator.number1 = -2
calculator.number2 = 2
print(calculator.plus()) # 0

# minus
calculator = Calculator(10, 5)
print(calculator.minus()) # 5

calculator.number1 = -2
calculator.number2 = 2
print(calculator.minus()) # -4

# multiply
calculator = Calculator(10, 5)
print(calculator.multiply()) # 50

calculator.number1 = -2
calculator.number2 = 2
print(calculator.multiply()) # -4

# division
calculator = Calculator(10, 5)
print(calculator.division()) # 2

calculator.number1 = -2
calculator.number2 = 2
print(calculator.division()) # -1

# print
calculator = Calculator(10, 5)
calculator.print()
'''
합 : 15
빼기 : 5
곱 : 50
몫 : 2
'''

calculator.number1 = -2
calculator.number2 = 2
calculator.print()
'''
합 : 0
빼기 : -4
곱 : -4
몫 : -1
'''