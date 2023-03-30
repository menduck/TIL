# Django ORM
- Object Relational Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
- django의 python Object를 ORM을 통해 SQL로 번역하고 그 반대도 번역한다.

# QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구(API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리)

> Model class.Manager.QuerySet API

```py
# 예
Article.objects.all() # Articles 모델 테이블 전체 조회
# SQL에선
SELECT * FROM articles
# shell에서 SQL 번역확인
print(Article.objects.all().query)
```

## Query

- DB에서 특정한 데이터를 보여 달라는 요청
- '쿼리문을 작성한다.' -> 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성함.
- 이때, 파이썬 코드가 ORM에 의해 SQL로 변환되어 DB에 전달되며, DB의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 전달함 

### QuerySet
- DB에서 전달 받은 객체 목록
  - 순회 가능한 데이터, 1개 이상의 데이터를 불러와 사용할 수 있음.
- Django ORM을 통해 만들어진 자료형
- DB가 단일한 객체를 반환 할 떄는 QuerySet이 아닌 Class의 인스턴스로 반환함.

# ORM CREATE

## Django shell
- django 환경 안에서 실행되는 python shell
- 입력하는 QuerySet API 구문이 django 프로젝트에 영향을 미침

- python shell : 실행문이 하나씩 실행 및 종료되기 때문에 결과를 바로 확인할 수 있음.

## 데이터 객체를 생성하는 3가지 방법

1. 특정 테이블에 새로운 행을 추가하여 데이터 추가

```shell
# Article 클래스의 인스턴스 생성
In [2]: article
Out[2]: <Article: Article object (None)>   

# article 인스터스에 title과 content 인스터스 변수에 값을 저장
In [4]: article.title = 'title'

In [5]: article.content = 'Django!!'

# 전체 조회
In [7]: Article.objects.all()
Out[7]: <QuerySet []>
# QuerySet이 빈 객체인 이유
# 아직 작성만 하고 저장하지 않은 상태이기 때문

# 테이블에 레코드 하나 생성을 위해 저장(인스턴스 메서드 save 호출)
In [8]: article.save()
# 전체 조회
In [9]: Article.objects.all()
Out[9]: <QuerySet [<Article: Article object (1)>]>
```

2. class 생성자 바로 넣는 방법

```shell
In [10]: article
    ...: = Articl
    ...: e(title=
    ...: 'second'
    ...: ,content
    ...: ='second
    ...:  django'
    ...: )

# 작성만 하고 저장되지 않음.
In [11]: article
Out[11]: <Article: Article object (None)>

#  save 호출하여 저장함.
In [12]: article.save()

# 저장된 article 확인
In [13]: article
Out[13]: <Article: Article object (2)>   

# 전체 조회
In [15]: Article.objects.all()
Out[15]: <QuerySet [<Article: Article object 
(1)>, <Article: Article object (2)>]>

# 값 확인
In [16]: article.pk
Out[16]: 2

In [17]: article.title
Out[17]: 'second'

In [18]: article.content
Out[18]: 'second django'

#  QuerySet 순회
In [23]: articles = Article.objects.all()    

In [24]: for article in articles:
    ...:     print(article) 
    # artcle를 템플릿에 넘겨주면 메인 페이지에서 모든 게시글을 출력할 수 있음.
    ...: 
Article object (1)
Article object (2)
Article object (3)

In [26]: for article in articles:
    ...:     print(article.id)
    ...:     print(article.title)
    ...:     print(article.content)
    ...:     print(article.created_at)       
    ...: 
1
title
Django!!
2023-03-30 02:36:42.809636+00:00
2
second
second django
2023-03-30 03:18:25.712848+00:00
3
third
 third django!
2023-03-30 03:23:17.331582+00:00
```

- article.pk와 article.id는 같은 값을 가진다.
- 만약 저장되기 전에 article.pk는 조회되지 않는다.
  - 왜냐면 값이 DB에 저장되기 전이기 때문이다.

3. QuerySet API인 create 메서드 사용

- save() 호출하지 않아도 저장됨
```shell
In [19]: Article.objects.create(title='third 
    ...: ', content=' third django!')        
Out[19]: <Article: Article object (3)>
# 바로 객체를 반환함.

# 확인
In [27]: Article.objects.all()
Out[27]: <QuerySet [<Article: Article object 
(1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

# ORM READ
## 전체 데이터 조회

```shell
>>> modleclass.obects.all()
```

## 단일 데이터 조회
- get()
  - pk와 같이 유일한 값을 조회해야 함.
  - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시킴.
  - 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

- 그렇기 때문에 pk는 get()으로 데이터를 조회를 하고 pk 이외의 데이터는 filter()로 조회함.

```shell
>>> modleclass.obects.get(컬럼값=값)

# 예시
In [28]: article = Article.objects.get(id=1) 
    ...: 

In [29]: article
Out[29]: <Article: Article object (1)>
In [31]: article.title
Out[31]: 'title'

# 만약 존재하지 않은 데이터를 조회하면?
In [33]: article = Article.objects.get(id=5) 
# ...생략
DoesNotExist: Article matching query does not exist.

# 만약 중복된 데이터를 조회하면?
# 에러 발생
multipleobjectsreturned: get() returned more than one 생략
```

## 특정 데이터 조회
- filter()
  - 특정 조건 데이터 조회

```shell
# filter를 활용해서 데이터 조회를 해야 함.
  # 현재 Article에 중복된 값이 없어서 그냥 결과값만 보기.
In[가짜]: Article.objects.filter(content='django')
Out[가짜]: <QuerySet [<Article: Article object 
(1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

  # filter로 존재하지 않은 데이터를 조회하면 빈 QuerySet을 반환함
In [35]: Article.objects.filter(title='notin 
    ...: g')
Out[35]: <QuerySet []>
```

- 세부 조건 데이터 조회

```shell
# Dj로 시작하는 content 찾기
In [36]: Article.objects.filter(content__sta 
    ...: rtswith='Dj')
Out[36]: <QuerySet [<Article: Article object 
(1)>]>
```
---

- 더 추가적인 API는 아래 문서 확인
[ORM API 공식문서 바로가기](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)

# QRM UPDATE

```shell
# title 수정하기
In [1]: article = Article.objects.get(pk=1)  

In [2]: article
Out[2]: <Article: Article object (1)>

In [3]: article.title
Out[3]: 'title'

In [5]: article.title='수정된 제목'

In [6]: article.title
Out[6]: '수정된 제목'
# 하지만 아직 DB에 반영 안됨 저장을 해야 함.

In [7]: article.save()
```

# ORM DELETE

```shell
In [8]: article.delete()
Out[8]: (1, {'articles.Article': 1})

In [9]: Article.objects.get(pk=1)
-----------------------------------
DoesNotExist: Article matching query does not exist.
```

# QuerySet API 활용시 외부 라이브러리 설치 및 과정

- django-extensions
  - ORM을 작성할때 필요한 것들을 미리 import를 해줌

1. 외부 라이브러리 설치

```
$ pip install ipython
$ pip install django-extensions
 <!-- $ pip install ipython django-extensions 로 한번에도 가능 -->
```

2. 외부 라이브러리 등록 - settings 설정

```py
# Application definition

INSTALLED_APPS = [
    'articles',
    'django_extensions'
```

3. requirements.txt 업데이트

```
$ pip freeze > requirements.txt
```

4. 실행

```
$ python manage.py shell_plus
```

