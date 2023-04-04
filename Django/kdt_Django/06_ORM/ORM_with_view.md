👩‍💻 [실습파일](./ORM_practice)
# READ

##  전체 게시글 조회

- views 에서 data를 템플릿으로 넘겨줌.

 👩‍💻 [views 바로가기](./ORM_practice/articles/views.py)

```py
# 1. models파일에서 Article 클래스 import 하기
from .models import Article

# Create your views here.

# 2. 함수 작성
def index(request):
    # DB에 전체 게시글 조회를 요청하고 QuerySet을 응답받아 저장
    articles = Article.objects.all()
    # print(articles) <QuerySet [<Article: Article object (2)>, <Article: Article object (3)>]>
    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)
```

- 템플릿에서 출력함.

 👩‍💻 [템플릿으로 바로 가기](./ORM_practice/articles/templates/articles/index.html)

## 단일 게시글 조회

1. url에서 변수가 views로 넘어오게 한다.
    - http://127.0.0.1:8000/articles/해당 게시글 번호

👩‍💻 [urls 파일 바로가기](./ORM_practice/articles/urls.py)

```py
# articles/urls.py
urlpatterns = [
    path('',views.index, name ='index'),
    path('<int:pk>', views.detail, name = 'detail'),
]
```
2. views는 urls에서 받은 변수를 템플릿으로 넘겨줌
👩‍💻 [views 파일 바로가기](./ORM_practice/articles/views.py)

```py
def detail(request, pk):
    # 컬럼에서 pk = url에서 받은 pk
    article = Article.objects.get(pk=pk)
    # 확인하기
    # print(article)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)
```

3. 템플릿에서 출력

 👩‍💻 [메인 템플릿으로 바로 가기](./ORM_practice/articles/templates/articles/index.html) 
 👩‍💻 [상세 템플릿으로 바로 가기](./ORM_practice/articles/templates/articles/detail.html)

# CREATE

- CREATE 로직을 구현하기 위한 view 함수
    - 1. new
        - 사용자의 입력을 받는 페이지를 렌더링
    - 2. create
        - 사용자가 입력한 데이터를 받아 DB에 저장

1. urls
👩‍💻 [urls 파일 바로가기](./ORM_practice/articles/urls.py)

```py
# articles/urls.py
urlpatterns = [
    path('',views.index, name ='index'),
    path('<int:pk>', views.detail, name = 'detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
```
2. views
    👩‍💻 [views 파일 바로가기](./ORM_practice/articles/views.py)

```py
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. new에서 보낸 사용자 데이터를 받아 변수에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. 받은 데이터를 DB에 저장
        # 2-1. 특정 테이블에 새로운 행 추가하여 데이터 추가
    article = Article.objects.all()
    article.title = title
    article.content = content
    article.save()

        # 2-2. class 생성자 바로 넣는 방법
    article = Article(title = title, content = content)
        # 저장 전 유효성 검사
    article.save()

        # 2-3. create 메서드 사용
    Article.objects.create(title=title, content = content)
    

    # 3. 결과 페이지 반환
    return render(request, 'articles/create.html')
```

- 몇 번째 방법이 더 좋을까?
    - 저장 시점을 컨트롤 할 수 있는 class 생성자에 바로 넣는 방법을 더 권장한다.
    - 저장하기 전에 유효성 검사를 할 수 있다.

3. 템플릿
 👩‍💻 [new 템플릿으로 바로 가기](./ORM_practice/articles/templates/articles/new.html) 
 👩‍💻 [create 템플릿으로 바로 가기](./ORM_practice/articles/templates/articles/create.html)

```html
<!-- article/templates/articles/new.html -->
<!-- http://127.0.0.1:8000/articles/new/?title=제목&content=내용# 
/name=value로 url에 들어감-->
<body>
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="GET">
    <div>
      <!-- label의 for 값은 input의 id값을 넣어줌 -->
      <label for="title">제목: </label>
      <input type="text" name="title" id='title'>
    </div>
    <div>
      <label for="content">내용: </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>

    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
```

# redirect()

> redirect()

- 인자에 작성된 주소로 다시 요청을 보냄

👩‍💻 [views 바로가기](./ORM_practice/articles/views.py)

```py
# articles/views.py
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title = title, content = content)
    article.save()

    # 3. 결과 페이지 반환
    # return render(request, 'articles/create.html')

    # 이동 URL 반환
    # return redirect("articles:index")

    # 세부 페이지 URL로 이동 응답
    return redirect("articles:detail", article.pk)
```

- render는 템플릿을 불러오고, redirect는 URL로 이동함.
- redirect로 불러온 URL에 맞는 views가 다시 실행되고 여기서 다시 render를 할지, redirect를 할지 결정함.

# HTTP request methods

## HTTP
- 네트워크 상에서 데이터를 주고 받기위한 약속
- 사용자가 서버에게 요청하고 서버가 사용자에게 응답받기 위한 약속

## HTTP request methods
- 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것.
- GET & POST

> GET Method

- 특정 리소스를 조회하는 요청
- GET으로 데이터를 전달하면 Query String 형식으로 보내짐
- ***데이터를 조회할 때만 사용해야함!***
- 입력 길이 제한 있음 (255)
- http://127.0.0.1:8000/articles/new/?title=제목&content=내용
    - key=value

> POST Method

- 특정 리소스에 변경사항을 만드는 요청
- POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐.
- 길이 제한 없음

## CSFR
- Cross-Site-Request-Forgery
- 사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

### Security Token (CSRF Token)
- 대표적인 CSRF 방어 방법

1. 서버는 사용자 입력 데이터에 임의의 난수 값(Token)을 부여
2. 매 요청마다 해당 Token을 포함시켜 전송 시키도록 함
3. 이후 서버에서 요청을 받을 때마다 전달된 Token이 유효한지 검증함.

```py
# ./articles/new.html
 <form action="{% url 'articles:create' %}" method="POST">
    # form태그 안에 명시해두면 됨.
    {% csrf_token %}
```

- 개발자 도구에서 확인하기
    - DTL(Django Template Engine)의 csrf_token 태그를 사용해 사용자에게 토큰 값을 부여
    - 요청 시 토큰 값도 함께 서버로 전송됨.
    - 토큰값은 계속 바뀜.

```html
<form action="/articles/create/" method="POST">
    <input type="hidden" name="csrfmiddlewaretoken" value="nTOuql3n9D72bg86ZgommLZPoVGd3fysa4apkyv2M2bZvdBIux2cnd7G8O0W6O1f">
  </form>
```
<br>

- 게시글 생성 후 Form Data가 전송되는 모습 확인

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/229661420-9a40f21e-5c4b-45f3-be81-d78a844323ab.PNG'>
</p>


***POST Method는 DB에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것***

# Delete

1. url

 👩‍💻 [url 바로 가기](./ORM_practice/articles/urls.py) 

```py
# ./articles/urls.py
app_name='articles'
urlpatterns = [
    ...
    path('<int:pk>/delete', views.delete,name='delete'),
]
```
2. views
👩‍💻 [url 바로 가기](./ORM_practice/articles/views.py) 

```py
# ./articles/views.py
def delete(request, pk):
    # 삭제할 데이터 조회
    article = Article.objects.get(pk=pk)

    # 조회할 데이터 삭제
    article.delete()

    # 메인 페이지로 이동
    return redirect("articles:index")
```
3. template
👩‍💻 [템플릿 바로 가기](./ORM_practice/articles/templates/articles/detail.html) 
- 삭제 페이지는 별도로 필요하지 않다고 판단
- 상세 페이지에 버튼 만들기

```html
<!-- ./articles/templates/articles/detail.html -->
  <!--
   - DB에 접근해 삭제해야 하기 때문에 POST
   - a태그는 GET이 default method이기 때문에 method가 post일땐 a태그를 쓰지 않는다.
   - 만약 하이퍼링크처럼 표현하고 싶으면 style 변경하면 됨.
   -->
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
```

# UPDATE

- UPDATE 로직을 구현하기 위한 view 함수
    - 1. edit
        - 사용자의 입력을 받는 페이지를 렌더링
    - 2. update
        - 사용자가 입력한 데이터를 받아 DB에 저장 -> 페이지 필요 없음

1. url
👩‍💻 [url 바로 가기](./ORM_practice/articles/urls.py) 

```py
# ./articles/urls.py
app_name='articles'
urlpatterns = [
    ...
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
]
```

2. views
👩‍💻 [url 바로 가기](./ORM_practice/articles/views.py) 

```py
# ./articles/views.py
def update(request,pk):
    # 데이터 조회
    article = Article.objects.get(pk=pk)

    # 데이터 수정
    # 데이터가 입력한 form 데이터 저장
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 조회한 데이터의 필드 값 변경
    article.title = title
    article.content = content

    # 데이터 저장
    article.save()

    return redirect('articles:index')
```

3. templates
👩‍💻 [템플릿 바로 가기](./ORM_practice/articles/templates/articles/edit.html)

```html

<body>
  <h1>EDIT</h1>
  <!-- 제출하기 버튼을 누르면 url로 연결 -->
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    <div>
      <label for="title">제목: </label>
      <input type="text" name="title" id='title' value='{{article.title}}'>
    </div>
    <div>
      <label for="content">내용: </label>
      <textarea name="content" id="content" cols="30" rows="10" >{{article.content}}</textarea>
    </div>

    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
</body>

```