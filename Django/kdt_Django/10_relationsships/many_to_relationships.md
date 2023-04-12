- 이전까지 실습한 article 모델과 accounts모델을 서로 이어져 있지 않았다.
- 그렇기 때문에 어떤 유저가 어떤 게시글을 쓰는지 알 수 없었다.
- 이를 알기 위해선 N:1 relationship 설정을 해야 한다.

- Foreign key
  - 테이블의 필드(컬럼) 중 다른 테이블의 레코드(행)를 식별할 수 있는 키
  - 각 레코드에서 서로 다른 테이블 간의 '관계'를 만드는 데 사용

# 게시글과 댓글 구현하기

## 모델 관계 설정
- Many to one relationships (1:N or N:1)  
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
    - 주문 테이블, 고객 테이블을 예로 들자면
    - 주문 테이블이 1개의 레코드가 있으면 고객 테이블은 1개의 레코드가 있다! 하지만 반대로 고객 테이블이 1개의 레코드가 있다고 해서 주문 테이블이 1개의 레코드를 가지는 것은 아니다.(고객이 주문을 안 할 수도 있다.)

> Comment(N) - Article(1)

- 댓글 테이블의 0개 이상의 레코드가 게시글 레코드 한 개와 관련된 관계 
  - 게시글이 있다고 해서 댓글이 반드시 있는 것은 아님
---

***Comment 테이블이 Article 테이블을 참조***
***Article 테이블이 Comment 테이블을 역참조***

### Comment 모델 정의

```py
# articles/models.py
class Comment(models.Model):
    # 외래 키 필드
    # DB엔 article_id로 저장됨. 그렇기 때문에 명시적으로 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장함
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

> ForeignKey(to, on_delete)

- django에서 N:1 관계 설정 모델 필드
- ForeignKey() 클래스의 인스턴스 이름을 참조하는 모델 클래스 이름의 단수형(소문자)을 작성하는 것을 권장함
- ForeignKey 클래스를 작성하는 위치와 관계없이 필드 마지막에 생성됨

- to : 참조하는 모델 class 이름
- on_delete : 참조하는 모델 class가 삭제 될 때 연결된 하위 객체의 동작을 결정
  - 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
    - 예를 들어, 댓글이 여러 개가 있는 게시글을 삭제할때, 댓글과 게시글을 모두 삭제할 것인지/ 댓글이 있으면 게시글을 삭제 못하게 할 것인지/ 게시글을 삭제하고 댓글의 외래키를 null값으로 남겨둘 것인지 등을 정함.
  - on_delete=models.CASCADE
    - 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제한다.

### shell_plus로 댓글 생성 연습하기

```bash
$ python manage.py shell_plus 

# Comment 클래스의 인스턴스 comment 생성
In [1]: comment = Comment()     

# 인스턴스 변수 저장
In [2]: comment.content = '댓글 

# DB에 댓글 저장
In [3]: comment.save()
--------------------------------IntegrityErrorTraceback (most recent call last)
# article_comment 테이블의 ForeignKeyField, article_id 값이 저장 시 누락됐기 때문

# 게시글 조회
In [5]: article = Article.objects.get(pk=1)

# 외래 키 데이터 입력
In [6]: comment.article = article
# 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래 키 컬럽에 넣어 줄 수도 있지만 권장하지 않음

# DB에 댓글 저장 및 확인
In [7]: comment.save()

In [8]: comment.content
Out[8]: '댓글'

# 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음.
In [9]: comment.article
Out[9]: <Article: Article object (1)>

In [10]: comment.article.title
Out[10]: 'ㄹㅇ'

# 두번째 댓글 작성
In [12]: comment = Comment(content='second comment', article = article)

In [13]: comment.save()

In [14]: comment.pk
Out[14]: 2

In [15]: comment
Out[15]: <Comment: Comment object (2)>

In [16]: comment.article.pk
Out[16]: 1

```

## 관계모델 참조

- 역참조
  - 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것.
  - N:1 관계에선 1이 N을 참조하는 상황

- Article에는 Comment를 참조할 어떠한 필드도 없다!
- 어떻게 해야 될까?

> 모델 인스턴스.related manager.QuerySetAPI

- related manager
  - N:1 혹은 M:N관계에서 역참조 시에 사용하는 manager
  (Objects 라는 매니저를 통해 quertsetAPI를 사용했던 것처럼 related manager를 통해 querysetAPI를 사용할 수 있게 됨.)
  - 사용하는 이유
    - article.comment 형식으로 댓글 객체를 참조 할 수 없음
    - 왜냐면 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않기 때문
    - 대신 Django가 역참조 할 수 있는 comment_set manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음.
    - N:1 관계에서는 생성되는 Related manager의 이름은 참조하는 ***모델명_set** 이름 규칙으로 만들어짐.

```bash
In [15]: comment
Out[15]: <Comment: Comment object (2)>

In [16]: comment.article.pk
Out[16]: 1

# 본인을 참조하는 외래키의 모델_set
In [17]: article.comment_set.all()
Out[17]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>
In [19]: Comment.objects.filter(article_id=1)
Out[19]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>
# 주체가 댓글, 참조의 개념은 가능하지만 역참조의 개념은 불가능
```

## 댓글 기능 구현

1. form

```py
# articles/forms.py
class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            # fields = '__all__'

            # 내용만 보여줌
            fields = ('content',)
```

- 모든 필드를 출력하면 Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문에 select 박스로 form이 출력된다.
- 하지만, 외래 키 필드는 사용자에게 입력 받는 것이 아니라, view 함수 내에서 별도로 처리되어 저장해야 한다.
=> 내가 어떤 게시글에(1) 무슨 댓글(2)을 쓸지가 아니라 어떤 게시글에 들어가면(view로 별도 처리) 무슨 댓글을 쓰면 됨.

2. url

```py
# articles/urls.py
urlpatterns = [
    ...,
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/comments/', views.comment_create, name = 'comment_create'),
]
```

- detail url을 살펴보면 url에 해당 게시글의 pk값이 사용되고 있음.
- 댓글의 외래 키 데이터에 필요한 정보가 게시글의 pk값임으로 이를 이용한다.

3. view & template

- detail 페이지에서 CommentForm 출력

```py
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form' : comment_form,
    }

    return render(request, 'articles/detail.html', context)


def comment_create(request, pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        # commit을 flase로 주면 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', pk)
    context = {
        'article' : article,
        # 에러메시지가 포함된 form
        'comment_form' : comment_form,
    }
    # 에러메시지가 출력됨
    return render(request, 'articles/detail.html', context)

```

> save(commit=False)

- 'Create, but don't save the new instance'
- DB에 저장하지 않고 인스턴스만 반환함.

```html
<!-- articles/templates/articles/detail.html -->

  <form action="{% url 'articles:comment_create' article.pk %}" method = "POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

## 게시글별 댓글 출력

1. view

```py
# articles/views.py
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }

    return render(request, 'articles/detail.html', context)
```

2. templates

```html
<!-- articles/templates/articles/detail.html -->

<h3>댓글조회</h3>
  <ul>
    {% for comment in comments  %}
      <li>
        {{ comment.content }}
      </li>
    {% endfor %}
  </ul>
```

## 댓글 삭제

1. url

```py
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name = 'comment_delete'),
]
```

2. views

```py
# articles/views.py

def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk = comment_pk)
    # 댓글 삭제
    comment.delete()
    return redirect('articles:detail', article_pk)
```

3. templates

```html
<!-- articles/templates/articles/detail.html -->

<h3>댓글조회</h3>
  <ul>
    {% for comment in comments  %}
      <li>
        {{ comment.content }}
        <form action=" {% url 'articles:comment_delete' article.pk comment.pk %}" method = "POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% endfor %}
  </ul>
```

## 댓글 개수 출력하기

- DTL filter -length 사용

```html
{{ comment | length }}
{{ article.comment_set.all | length }}
```

- QuerysetAPI - count() 사용

```html
{{ article.comment_set.count }}
```

## 댓글이 없는 경우 대체 컨텐츠 출력
- DTL tag - for empty 사용

```html
<!-- articles/templates/articles/detail.html -->

<h3>댓글조회</h3>
  <ul>
    {% for comment in comments  %}
      <li>
        {{ comment.content }}
        <form action=" {% url 'articles:comment_delete' article.pk comment.pk %}" method = "POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>

    <!-- for 반복문에 comments가 없다면 empty 아래 코드가 실행 -->
    {% empty %} 
      <p> 무블 방지 </p>
    {% endfor %}
  </ul>
```

# Article과 User
## 모델 관계 설정
- Article(N) - User(1)
  - 0개 이상의 게시글은 1개의 회원에 의해 작성 될 수 있음.

1. User 외래 키 정의

```py
# articles/models.py
from django.db import models

# models.py에서 User를 참조할때만 다음과 같이 참조한다.
from django.conf import settings

class Article(models.Model):
    # settings.AUTH_USER_MODEL 문자열로 참조
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # title, content 등등
```
- User 모델을 참조하는 방법
  - 직접 참조는 권장하지 않음
    - from accounts.models import User
  - 간접 참조 get_user_model은 models.py에선 사용하지 않음. (ex from django.contrib.auth import get_user_model)
    - 반환 값 : 'User Object' 객체
    - django 내부 실행 원리로 인해 아직 User 객체를 생성하기 전에 models.py부터 실행되기 때문에
  - settings.AUTH_USER_MODEL
    - 반환 값: 'accounts.User' 문자열
    - modles.py의 모델 필드에서 참조할 때 사용

1-1. migration
- 기본적으로 모든 컬럼은 NOT NULL 제약 조건이 있기 때문, 데이터가 없이 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
- 이전에 이미 DB가 있기 때문
- 그래서 기본값을 어떻게 작성할 건인지 선택해야 함.

## CRUD 구현
### 1. 게시글 작성자 나타내기

1. ArticleForm 출력 필드 수정

```py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # user_id는 사용자에게 받는 것이 아니므로 출력에서 가림
        fields = ('title','content',)
```

- 여기까지 작성하고 게시글을 작성하면 ***IntegrityError*** 가 발생한다.
- 게시글 작성 시 user_id필드를 누락했기 때문이다.
- view에서 게시글 작성 시 작성자 정보도 함꼐 저장해야 한다.

2. view

```py
# articles/views.py
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
          # commit을 False로 저장하면 DB에 레코드를 작성하지 않도록 함. 인스턴스로 반환은 가능
          # 저장하기 전에 잠시 보류 해놓고 article.user에 작성자를 저장한 다음 DB에 저장해야 한다.
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

3. templates

- 메인페이지에 작성자와 제목 내용 표시하기

```html
<!-- articles/templates/articles/index.html -->

  {% for article in articles  %}
    <p>
      작성자 : {{ article.user.username }}
    </p>
    <p>
      제목 : <a href="{% url 'articles:detail' article.pk%}">{{ article.title }}</a>
    </p>
    <p>
      내용 : {{ article.content }}
    </p>
  {% endfor %}
```
- article.user.username 값과 article.user값이 같다.
  - 왜? article.user은 객체가 아닌가? 맞다 하지만
  - AbstractUser가 아래 코드가 작성되었기 때문에 user객체까지만 호출해도 username이 반환된다.

```py
# accounts/models.py
class User(AbstractUser):
  pass

  # AbstractUser가 아래 코드가 작성되어있음
  def __str(self):
    return self.username
```

### 2. 게시글 작성한 사람만 게시글 수정/삭제 하기

1. view

```py
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 수정을 요청하는 자 vs 게시글의 작성자를 비교
    # 같으면 그 아래 수정 코드 실행
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = ArticleForm(instance=article)
    # 수정을 요청하는 자가 게시글 작성자와 같지 않다면 index 페이지로 감.
    else:
        return redirect('articles:index')
    context = {
        'article' : article,
        'form' : form
    }
    return render(request, 'articles/edit.html', context)


@login_required
def delete(request, pk):
    # 삭제를 요청하는 자 vs 게시글의 작성자를 비교
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    
    return redirect('articles:index')
```     

2. template

- 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 함.

```html
<!-- articles/templates/articles/detail.html -->
{% if request.user == article.user  %}
    <form action="{% url 'articles:delete' article.pk %}" method='POST'>
      {% csrf_token %}
      <input type="submit" value ='삭제'>
    </form>
    <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  {% endif %}
```

# Comment와 User

## 모델 관계 설정
- Comment(N) - User(1)
  - 0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음.

1. User 외래 키 정의

```py
# articles/models.py
# models.py에서 User를 참조할때만 다음과 같이 참조한다.
from django.conf import settings

class Comment(models.Model):
    # 외래 키 필드
    # DB엔 article_id로 저장됨. 그렇기 때문에 명시적으로 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장함
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # 나머지 필드 생략
```

2. Migration 진행

- 이전에 Article 와 User 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새로운 칼럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요
- 기본값 설정해줘야 함.

## CRUD 구현

### 1. 로그인한 user가 댓글 남길때 user도 같이 저장하고, 출력하기

- 댓글 작성 시 user_id 필트 데이터가 누락되어 에러 발생

1. view

```py
# articles/views.py
@login_required  # 인증된 사용자만 댓글 작성 가능
def comment_create(request, pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        # commit을 False로 주면 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', pk)
    context = {
        'article' : article,
        # 에러메시지가 포함된 form
        'comment_form' : comment_form,
    }
    # 에러메시지가 출력됨
    return render(request, 'articles/detail.html', context)
```

2. templates
- 세부 페이지에 댓글 작성자 출력

```html
<!-- articles/templates/articles/detail.html -->

  <h3>댓글조회</h3>
  <ul>
    {% for comment in comments  %}
      <li>
        {{ comment.user }}: {{ comment.content }}
      </li>
    {% endfor %}
  </ul>
```

### 3. 댓글 작성한 유저가 댓글 삭제하기

1. view

- 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인 댓글만 삭제할 수 있도록 함.

```py
# articles/views.py
@login_required # 인증된 사용자만 댓글 삭제 가능
def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk = comment_pk)
    # 삭제를 요청하는 자 vs 댓글의 작성자를 비교
    if comment.user == request.user:
        # 댓글 삭제
        comment.delete()
    return redirect('articles:detail', article_pk)
```

2. templates
-  해당 댓글의 작성자가 아니면, 댓글 삭제 버튼을 출력하지 않도록 함.

```html
<!-- articles/templates/articles/detail.html -->

    <h3>댓글조회</h3>
  <ul>
    {% for comment in comments  %}
      <li>
        {{ comment.user }}: {{ comment.content }}
        {% if comment.user == request.user  %}
          <form action=" {% url 'articles:comment_delete' article.pk comment.pk %}" method = "POST">
            {% csrf_token %}
            <input type="submit" value="삭제">
          </form>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
```
