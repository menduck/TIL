# M:N 모델 관계 특징
- M:N 관계로 맺어진 두 테이블은 변화가 없음
- ManyToManyField는 중개 테이블을 자동으로 생성함
- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
- 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

# ManyToManyField

> ManyToManyField(to, **options)

- Many-to-Many 관계 설정 시 사용하는 모델 필드
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성
  - add(), remove(), create(), clear() ....

> add()

- 지정한 객체를 관련 객체 집합에 추가
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음 -> 아무런 결과가 없음

> remove()

- 관련 객체 집합에서 지정된 모델 개체를 제거

## ManyToManyField Arguments

1. related_name
- 역참조시 사용하는 manager name을 변경함.

```py
# models.py
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor, related_name = 'patients')
  ...

# 조회할때
doctor.patient_set.all() # 역참조로 조회
doctor.patients.all() # related_name 활용 (외래키가 많아지거나 모델이 복잡해지면 manager name이 겹치는게 있을 수도 있으므로)
```

2. through
- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용, 중개 테이블을 나타내는 Django 모델을 지정
- 일반적으로 중개 테이블에 추가 테이터를 사용하는 다대다 관계와 연결하는 경우에 사용됨.


3. symmetrical
- ManyToManyField가 동일한 모델을 가리키는 정의에만 사용
- 다대다 관계를 자신과 맺을때
  - 인스타 팔로우(user클래스는 하나인데 user끼리 친구인가 아닌가)
- 기본값: True
  - 대칭임. => 내가 A에게 팔로우를 신청해 수락되면 자동으로 서로 맞팔로우(친구)가 된다.

```py
class Person(models.Model):
  friends = models.ManyToManyField('self') # self일때만 사용
  # friends = models.ManyToManyField('self', symmetrical=False)
```

# 예시 - 좋아요 구현

## Article & User

- Article(M) - User(N)
  - 0개 이상의 게시글은 0명 이상의 회원과 관련된다.
  - 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고
  - 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.

### model 관계 설정

```py
# articles/models.py

class Article(models.Model):
    # user모델 참조는 settings.AUTH_USER_MODEL 문자열로 참조
    # article(N)-user(1) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    # article(N)-users(N) 
    # article 테이블에 필드가 추가되는 것이 아니라 중개 테이블일 만들어짐
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

- ERROR 발생
  - Reverse accessor for 'articles.Article.users' clashes with reverse accessor for 'articles.Article.user'.
- ERROR 원인
  - user가 작성한 글들(user.article_set)과 user가 좋아요 누른 글들(user.article_set) manager name을 구분할 수 없음
- ERROR 해결
  - related_name을 작성해 구분 짓음

```py
# articles/models.py
# 좀 더 명시적인 변수명을 위해 like를 붙임.


class Article(models.Model):
    # user모델 참조는 settings.AUTH_USER_MODEL 문자열로 참조
    # article(N)-user(1) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    # article(N)-users(N) 
    # article 테이블에 필드가 추가되는 것이 아니라 중개 테이블일 만들어짐
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

---

##  User-Article 사용 가능한 related manager 정리

- article.user
  - 게시글을 작성한 유저 - N:1
- user.article_set
  - 유저가 작성한 게시글(역참조) - N:1
- article.like_users
  - 게시글을 좋아요한 유저들 - M:N
- user.like_articles
  - 유저가 좋아요한 게시글들(역참조) - M:N


### 좋아요 구현
1. url

```py
# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    ...,
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

2. view

```py
# articles/views.py

@login_required
def likes(request, article_pk):
    # 1. 좋아요를 누르는 대상 게시글
    article = Article.objects.get(pk=article_pk)
    
    # 2. 좋아요 관계를 추가 or 삭제

    # 2-1. 유저가 게시글에 좋아요 누르는 유저들 안에 있는지 확인
    if request.user in article.like_users.all():
        # 있으면 좋아요 취소
        article.like_users.remove(request.user)
        # request.user.like_articles.remove(article) #역참조
    else:
        # 없으면 좋아요 추가
        article.like_users.add(request.user)
        # request.user.like_articles.add(article) #역참조
    return redirect('articles:index')
```
- if request.user in article.like_users.all():
  -  article.like_users.all() 데이터의 양이 커지면 in 연산자는 처음부터 찾기 때문에 상대적으로 속도가 느려짐
  - ***article.like_users.filter(pk=request.user.pk).exists()***
  - 해당 게시글의 좋아요를 누른 유저에서 현재 요청하는 유저의 존재를 조회하기 때문에 상대적으로 속도가 빠름
3. templates

```html
<!-- articles/templates/articles/index.html -->
<form action="{% url 'articles:likes' article.pk%}" method="POST">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
      <p><input type="submit" value='♥'> - {{article.like_users.all.count}} </p>
      {% else %}
      <p><input type="submit" value='♡'> - {{article.like_users.all.count}} </p>
      {% endif %}
    </form>
```

# 예시 - 팔로우 & 팔로워

