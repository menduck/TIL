# 예제 1
list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")
    
"""
3 4 5 6 7 8
"""

# 예제 1 - 풀이
list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop() # 6
print(list_variable) # [0, 1, 2, 3, 4, 5]
list_variable.append(7) 
print(list_variable) # [0, 1, 2, 3, 4, 5, 7]
list_variable.append(8) 
print(list_variable) # [0, 1, 2, 3, 4, 5, 7, 8]

for element in list_variable[2:]: # [2, 3, 4, 5, 7, 8]
    print(element, end=" ") # 2 3 4 5 7 8

# 예제 2
for element in range(-2, 10, 2): # -2 0 2 4 6 8
    print(element, end=" ")
    
"""
-2 0 2 4 6 8
"""

# 예제 3
a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n): # 0 1 2 3 4 5 6 7 8 9
    if number % 2 == 0: # 0 2 4 6 8 
        a = a + 1 # 5
        
    if number % 3 == 0: # 0 3 6 9
        b = b + 1 # 4
        
    if number % 4 == 0: # 0 4 8
        c = c + 1 # 3
        
    if number % 5 == 0: # 0 5
        d = d + 1 # 2

print(a, b, c, d) # 5 4 3 2

# 예제 4
i = 0
while i <= 10:
    print(i) # 0 1 2 3 4 5 6 7 8 9 10
    i = i + 1
"""
0
1
2
3
4
5
6
7
8
9
10
"""

# 예제 5
i = 0
while i <= 10:
    i = i + 1 # i = 0 + 1
    print(i) # 1 2 3 4 5 6 7 8 9 10 11
"""
1
2
3
4
5
6
7
8
9
10
11
"""

# 예제 6
i = 0
while i <= 10:
    i = i + 2 # i = 0 + 2
    print(i) # 2 4 6 8 10 12
"""
2
4
6
8
10
12
"""

# 예제 7
i = 0
while True:
    print(i) 
    i = i + 1
    if i > 10:
        break
"""
0
1
2
3
4
5
6
7
8
9
10
"""
# 예제 7 - 풀이
i = 0
while True:
    print(i)  # 0 1 2 3 4 5 6 7 8 9 10 
    i = i + 1 # 1 2 3 4 5 6 7 8 9 10 11
    if i > 10: # i가 11일때 true
        break # break 발생
  
# 예제 8
i = 0
while True:
    print(i) # 0 1 2 3 4 5 6 7 8 9 10 11
    if i > 10:
        break
    i = i + 1 # 1 2 3 4 5 6 7 8 9 10 11
    
"""
0
1
2
3
4
5
6
7
8
9
10
11
"""

# 예제 9
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable)) # 7

# 예제 10
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable)) # 21

# 예제 11
list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # -12