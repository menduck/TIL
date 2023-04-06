# Login
- Session을 Create하는 과정
- 로그인은 데이터를 DB에 저장하지 않기때문에 form 활용
  - 데이터를 DB에 저장해야하는 것은 modelForm ex) 회원가입

## login을 위한 form

> AuthenticationForm()

- 로그인을 위한 built-in-form

## login 로직 순서

1. url

```py
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name = 'login'),
]
```

2. views

```py
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login # login 로직과 이름이 같으므로 login 모듈의 이름을 바꿔줌

# Create your views here.
def login(request):
    # 2. 로그인 실행 로직 (POST)
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 저장이 아니라 세션을 만들어야함.
            auth_login(request, form.get_user())
            return redirect('articles:index')
    # 1. 로그인 페이지 (GET)
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```
> login(request, user)

- 인증된 사용자를 로그인하는 함수

> .get_uer()

- AuthenticationForm의 인스턴스 메서드
- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환함.

3. template

```html
<!-- accounts/templates/accounts/index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>로그인</h1>
  <form action="{% url 'accounts:login' %}" method = "POST">
    {% csrf_token %}
    {{ form.as_p}}
    <input type="submit">
  </form>
{% endblock content %}
```

4. 세션데이터 쿠키로 확인.
+ 쿠키의 sessionid value랑 DB파일에서 django_session 테이블에서 session_key와 일치함.

# Logout
- Session을 Delete 하는 과정

## logout 로직 순서

1. url

```py
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    ...,
    path('logout/', views.logout, name = 'logout'),
]
```

2. views

```py
# accounts/views.py
...
from django.contrib.auth import logout as auth_logout # logout 로직과 이름이 같으므로 login 모듈의 이름을 바꿔줌

# Create your views here.
def logout(request):
    # session delete
    auth_logout(request)
    return redirect('articles:index')
```
> logout(request)

- 현재 요청에 대한 session data를 DB에서 삭제
- 클라이언트의 쿠키에서도 sessionid를 삭제

3. template

```html
<!-- articles/templates/articles/index.html -->

  <form action="{% url 'accounts:logout' %}" method = "POST">
    {% csrf_token %}
    <input type="submit" value = '로그아웃'>
  </form>

```

# Template with Authentication data
- 뎀플릿에서 인증 관련 데이터를 출력하는 방법
- 만약 index.html에서 user 이름을 받아 출력하려면?

```html
<!-- articles/templates/articles/index.html  -->
  <h3>안녕하세요 {{ user }}님</h3>
```

- 왜 {{user}}는 views에서 보내지 않았는데 쓰일 수 있을까? 
  - 장고에서 자주 쓰이는 것들은 미리 모듈을 시킴
- 로그인 되지 않은 상태라면 AnonymousUser

<br>

- context processors
  - 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
  - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
  - 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것.

```py
# settings.py
TEMPLATES = [
    {
        ...,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',

                # auth에 관한 모든 모듈이 이미 내장되어 있음 
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```