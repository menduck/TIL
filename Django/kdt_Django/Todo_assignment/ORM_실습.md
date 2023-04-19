"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""
In [1]: todo = Todo(content='실습 제출', priority = 5, completed = False, deadline = '2023-04-19')

In [2]: todo.save()
"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
In [4]: todo1 = Todo(content = '데일리 설문(오후) 제출', deadline = '2023-04-19')     

In [5]: todo1.save()

"""
3. 임의의 할 일 5개 생성
"""
In [8]: todo = Todo(content='내용1', priority = 5, completed = Fal 
   ...: se, deadline = '2023-04-19')

In [9]: todo2 = Todo(content='내용2', priority = 4, completed = Fa 
   ...: lse, deadline = '2023-04-19')

In [10]: todo.save()

In [11]: todo2.save()

In [12]: todo2 = Todo(content='내용3', priority = 3, completed = F 
    ...: alse, deadline = '2023-04-19')

In [13]: todo2.save()


In [15]: todo = Todo(content='내용4', priority = 2, completed = Fa 
    ...: lse, deadline = '2023-04-19')


In [17]: todo = Todo(content='내용5', priority = 1, completed = Fa
    ...: lse, deadline = '2023-04-19')

In [18]: todo.save()

In [19]: Todo.objects.all()
Out[19]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""
In [26]: todo_pk = Todo.objects.all().order_by('pk')

In [27]: todo_pk
Out[27]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>  
"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
In [28]: todo_priority = Todo.objects.all().order_by('-priority')  

In [29]: todo_priority
Out[29]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (2)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>  

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""

In [32]: todo_1 = Todo.objects.get(pk=1)

In [33]: todo_1
Out[33]: <Todo: Todo object (1)>
Out[34]: 1

In [35]: todo_1.content
Out[35]: '실습 제출'

In [37]: todo_1.priority
Out[37]: 5

In [38]: todo_1.deadline
Out[38]: datetime.date(2023, 4, 19)

In [39]: todo_1.created_at
Out[39]: datetime.datetime(2023, 4, 19, 2, 43, 30, 936686, tzinfo=<UTC>)

---

"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""
In [2]: newspaper_1 = Newspaper.objects.get(pk=1)

In [3]: newspaper_1
Out[3]: <Newspaper: Newspaper object (1)>

In [5]: newspaper_1.journalist
Out[5]: 'Laney Mccullough'
"""

2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""
In [6]: newspaper_2 = Newspaper.objects.filter(journalist = 'Laney Mccullough') 
   ...: .count()

In [7]: newspaper_2
Out[7]: 858

"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""

In [9]: newspaper_3
Out[9]: <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, <Newspaper: Newspaper object (9998)>, <Newspaper: Newspaper object (9997)>, <Newspaper: Newspaper object (9996)>, <Newspaper: Newspaper object (9995)>, <Newspaper: Newspaper object (9994)>, <Newspaper: Newspaper object (9993)>, <Newspaper: Newspaper object (9992)>, <Newspaper: Newspaper object (9991)>, <Newspaper: Newspaper object (9990)>, <Newspaper: Newspaper object (9989)>, <Newspaper: Newspaper object (9988)>, <Newspaper: Newspaper object (9987)>, <Newspaper: Newspaper object (9986)>, <Newspaper: Newspaper object (9985)>, <Newspaper: Newspaper object (9984)>, <Newspaper: Newspaper object (9983)>, <Newspaper: Newspaper object (9982)>, <Newspaper: Newspaper object (9981)>, '...(remaining elements truncated)...']>

"""
4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""
In [12]: newspaper_4 = Newspaper.objects.all().order_by('-created_at')

In [13]: newspaper_4
Out[13]: <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, <Newspaper: Newspaper object (5500)>, <Newspaper: Newspaper object (4918)>, <Newspaper: Newspaper object (5753)>, <Newspaper: Newspaper object (3706)>, <Newspaper: Newspaper object (4012)>, <Newspaper: Newspaper object (452)>, <Newspaper: Newspaper object (6865)>, <Newspaper: Newspaper object (3265)>, <Newspaper: Newspaper object (2643)>, <Newspaper: Newspaper object (7022)>, <Newspaper: Newspaper object (3700)>, <Newspaper: Newspaper object (3236)>, <Newspaper: Newspaper object (9607)>, <Newspaper: Newspaper object (4461)>, <Newspaper: Newspaper object (419)>, <Newspaper: Newspaper object (251)>, <Newspaper: Newspaper object (8613)>, <Newspaper: Newspaper object (1670)>, '...(remaining elements truncated)...']>

"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""

In [21]: newspaper_5 = Newspaper.objects.filter(journalist__contains = 'Britney').count()

In [22]: newspaper_5
Out[22]: 799

"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""

In [27]: newspaper_6 = Newspaper.objects.filter(journalist__in = list).count()

In [28]: newspaper_6
Out[28]: 2469

"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""
In [31]: newspaper_7 = Newspaper.obje 
    ...: cts.filter(created_at__year_ 
    ...: _gte = 2000).count()

In [32]: newspaper_7
Out[32]: 4355

"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""

In [39]: print(f"title : {newspaper_7.title}")
    ...: print(f"content : {newspaper_7.content}")
    ...: print(f"journalist : {newspaper_7.journalist}")
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough

