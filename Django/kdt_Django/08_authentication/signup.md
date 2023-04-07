# 회원가입
- User 객체를 Create하는 것

## 회원가입 등록 순서
1. urls

```py
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    ...,
    path('signup/', views.signup, name = 'signup'),
]
```

2. views

```py
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signup(request):
    # 2. 회원가입 생성 로직 (POST)
    if request.method == "POST":
        # model form은 첫 번째 인자로 데이터를 받음
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    # 1. 회원가입 페이지 (GET)
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```

> UserCreationForm
회원가입을 시켜주는 built-in model form class

3. template

```html
<!-- accounts/templates/accounts/signup.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method = "POST">
    {% csrf_token %}
    {{ form.as_p}}
    <input type="submit">
  </form>
{% endblock content %}
```

### BUT 에러 확인!
- 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문

#### 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 forms
1. UserCreationForm
2. UserChangeForm

- 두 forms 모두 class Meta :model = User가 등록된 form이기 때문
- 상속을 받아 재정의 해줘야함

- custom form 작성.

```py
# accounts/forms.py
from django.contrib.auth.forms  import UserCreationForm, UserChangeForm
'''
# django User 객체에 대한 직접 참조 권장하지 않음. 
from .models import User 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
      # 현재 우리가 사용하는 User class로 직접 재정의
      model = User
'''

# 간접 참조 권장
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
      # 현재 우리가 사용하는 User class를 호출해 재정의
      model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
      # 현재 우리가 사용하는 User class를 호출해 재정의
      model = get_user_model()
```

> get_user_model()

- 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 함수

- User모델을 직접 참조하지 않는 이유는?
  - user 모델이 바뀌더라도 자동으로 반환.
  - django는 User클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조
  
### 회원 가입 로직 수정

```py
# accounts/views.py 

from .forms import CustomUserCreationForm

def signup(request):
    # 2. 회원가입 생성 로직 (POST)
    if request.method == "POST":
        # model form은 첫 번째 인자로 데이터를 받음
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원가입 후 로그인까지 진행되려면
            # user = form.save()
            # auth_login(request, user)
            return redirect('articles:index')
    # 1. 회원가입 페이지 (GET)
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```

# 회원 탈되
- User 객체를 Delete 하는 것.

## 회원 탈퇴 순서
1. url

```py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    ...,
    path('delete/', views.delete, name = 'delete'),
]
```

2. views

```py
# accounts/views.py
def delete(request):
    # 게시글처럼 조회한 후에 삭제하는 것이 아니라
    # 나의 유저객체 삭제하는 것
    request.user.delete()

    # 유저의 세션 정보도 함께 지우고 싶은 경우
    # auth_logout(request)
    return redirect('articles:index')
```

- 탈퇴하면서 유저의 세션 정보도 함께 지우고 싶은 경우
  - 탈퇴 -> 로그아웃 / 순서 중요
  - 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 유저 정보가 없어짐.


# 회원정보 수정
- User 객체를 Update 하는 것

## 회원정보 수정 순서
1. urls

```py
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    ...,
    path('update/', views.update, name = 'update'),
  ]
```

2. view

```py
# accounts/views.py
from .forms import CustomUserChangeForm

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)
```

> UserChangeForm()

- 회원가입을 위한 built-in Model Form

- UserchangeForm 사용 시 문제점
  - 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정 가능
  - admin 인터페이스에서 사용되는 ModelForm 때문
  - 따라서 접근 가능한 필드를 조정해야 함.

```py
# accounts/forms.py
from django.contrib.auth.forms  import UserCreationForm, UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
      # 현재 우리가 사용하는 User class를 호출해 재정의
      model = get_user_model()
      # 모든 필드가 아니라 원하는 필드만 열어줌
      fields = ('email', 'first_name', 'last_name', )
```

3. template

```html
 <!-- accounts/templates/accounts/update.html -->
{% extends 'base.html' %}

{% block content  %}
  <h2>회원정보수정</h2>
  <form action="{% url 'accounts:update' %}" method ="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value ='등록'>
  </form>
{% endblock content %}
```

# 비밀번호 변경
- django는 비밀번호 변경 페이지를 회원정보 수정 form에서 별도 주소(./accounts/password)로 안내
- 그렇기때문에 처음에 계정 앱 이름을 accounts로 하면 더 용이함.

## 비밀번호 변경 순서
1. urls

```py
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    ...,
    path('password/', views.change_password, name = 'change_password'),
]
```

2. views

```py
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
rom django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            
            # 비밀번호 변경 시 세션 무효화 방지
            # 세션의 값을 업데이트 => 비밀번호가 업데이트 되니깐 그에 맞춰 세션 값도 없데이트를 해줘야 한다. => 비밀번호를 바꾸고 다시 로그인을 안해도 된다.
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)
```

> PasswordChangeForm()

- 비밀번호 변경을 위한 built-in form

<br>

- 암호 변경 시 세션 무효화
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못함.
  - 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

> update_session_auth_hash(request, user)

- 암호 변경 시 세션 무효화 방지
- 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 기존 session을 업데이트

# 로그인 사용자에 대한 접근 제한
- 로그인 사용자에 대한 접근을 제한하는 2가지 방법
1. is_authenticated 
- 사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성
- 모든 User인스턴스에 대해 항상 True인 읽기 전용 속성
- AnonymousUser에 대해서는 항상 False
- 반환값이 T/F이니깐 조건문으로 활용하여 로그인/비로그인일때 링크 다르게 설정
- 권한과는 관련없음, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지 확인하지 않음

```html
<!-- articles/index.html -->

<!-- 로그인 사용자만 로그아웃, 회원정보 수정을 볼 수 있음. -->
{% if request.user.is_authenticated %}
  <h3>안녕하세요 {{ user }}님</h3> 
  <form action="{% url 'accounts:logout' %}" method = "POST">
    {% csrf_token %}
    <input type="submit" value = '로그아웃'>
  </form>
  
  <form action="{% url 'accounts:delete' %}" method = "POST">
    {% csrf_token %}
    <input type="submit" value ="계정탈퇴">
  </form>
  <a href="{% url 'accounts:update' %}">회원정보수정</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">로그인</a>
    <a href="{% url 'accounts:signup' %}">회원가입</a>
  {% endif %}
```

- template만 고치면 단순히 출력하는 것만 보지 못하게 하는거임.
- 로그인하지 않은 유저가 주소를 알면 다 접근 가능 
- view 로직을 수행할 수 없도록 처리해줘야함.

```py
# accounts/views.py
def login(request):
    # 로그인된 인증자는 login 뷰 함수를 호출할 권리가 없다.
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...


def signup(request):
    # 로그인 된 사용자는 회원가입할 권한이 없다.
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...
```


2. login_required 
- 로그인이 되지 않으면 거절
- 인증된 사용자에 대해서만 view함수를 실행시키는 데코레이터
- 로그인 하지 않은 사용자의 경우 /accounts/login/ 주소로 자동으로 redirect 시킴
- 아래 코드와 같은 동작
```py
if not request.user.is_authenticated:
        return redirect('accounts:login')
```

- 실습파일에 적용시킨 코드
  - 인증된 사용자만 게시글을 작성/삭제/수정할 수 있고 계정을 로그아웃/탈퇴/비밀번호 변경 할 수 있음

```py
# articles/views.py

from django.contrib.auth.decorators import login_required

@login_required
def create(request):
  pass

  
@login_required
def delete(request):
  pass


@login_required
def update(request):
  pass

# accounts/views.py

@login_required
def logout(request):
  pass

  
@login_required
def delete(request):
  pass


@login_required
def update(request):
  pass


@login_required
def change_password(request):
  pass
```