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

