# 2754	학점계산	
'''
https://www.acmicpc.net/problem/2754
'''                                                        
score_dict = {}
grade_str = 'ABCDF'
grade = list(grade_str[::-1])
grade_point_str = ['-','0','+']
grade_point_int = [-0.3,0,+0.3]

grade_dict = {} # {'F': 0, 'D': 1, 'C': 2, 'B': 3, 'A': 4}
for i,g in enumerate(grade):
  grade_dict[g] = i

grade_point_dict = dict(zip(grade_point_str,grade_point_int))

import sys

user_grade = sys.stdin.readline().strip()
if user_grade == 'F':
  print(f'{grade_dict[user_grade]:.1f}')
else :
  score = grade_dict[user_grade[0]] + grade_point_dict[user_grade[1]]
  print(f'{score :.1f}')
