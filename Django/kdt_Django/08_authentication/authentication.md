# Django Authentication System
- 사용자 인증과 관련된 기능을 모아 놓는 시스템
- 인증과 권한 부여를 함께 제공 및 처리

# Custom User model

- django가 기본적으로 제공하는 User model은 내장된 auth모듈의 User 클래스를 사용
- 별도의 설정 없이 사용 가능
- 그러나 직접 수정할 수 없어서 Custom User model로 대체함.

## custom user model로 대체하는 순서
- 프로젝트 중간에 AUTH_USER_MODEL을 변경 할 수 없음
- 이미 진행할 경우 데이터베이스 초기화 후 진행
  - migrations에 설계도 파일(번호붙여진 파일) 지우기
  - db.splite3 지우기

1. 별도의 urls 만들기

```py
# curd/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ...,
    path('accounts/', include('accounts.urls')),
]

# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
 
]
```

2. custom user class 작성 
- AbstractUser를 상속받는 커스텀 User 클래스를 작성
- 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨.

```py
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  pass
```

3. settings 설정
- django 프로젝트가 사용하는 기본 User모델을 우리가 작성한 User모델로 지정
- 기본 값은 'auth.User'

```py
# crud/settings.py

# custom user로 지정
AUTH_USER_MODEL = 'accounts.User'
```

4. admin 등록
- 기본 User모델이 아니기 때문에 등록하지 않으면 admin.site에 출력되지 않음.

```py
# accounts/admin.py
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

5. migration

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## custom user을 꼭 사용해야될까?
- django는 새 프로젝트를 시작하는 경우 기본 User모델이 충분 하더라도 custom User 모델을 설정하는 것을 강력히 권장함.
- custom User 모델은 기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
- 단, User모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함.
