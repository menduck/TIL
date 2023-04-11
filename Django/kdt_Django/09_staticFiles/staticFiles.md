# Static Files
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일

## 웹 서버와 정적 파일
- 웹 서버의 기본 동작
  - 특정 위치 (URL)에 있는 자원을 요청(HTTP request) 받아서
  - 응답 (HTTP response)을 처리하고 제공을 하는 것.
- 자원제 접근 가능한 주소가 있다.는 의미
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함.
- ***정적 파일을 제공하기 위한 경로(URL)이 필요함***

## Staric files 제공하기

1. 기본 경로
  - app/static/

```html
 <!-- 
  articles/templates/articles/index.html

  내장된 태그를 가져오는 load / 파이썬의 import
  -->

{% load static %} 
<img src="{% static 'articles/sample-1.png' %}" alt="1번 그림">
<link rel="stylesheet" href=" {% static 'articles/style.css' %}">
```
  - STATIC_URL
    - 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
    - 실제 파일이나 디렉토리가 아니며, URL로만 존재
    - 비어 있지 않은 값으로 설정 시 반드시 /로 끝나야 함.  

```py
# settings.py

# 정적파일이 웹사이트에 사용되는 주소
STATIC_URL = '/static/'
```

> URL + STATIC_URL + 정적파일 경로
= http://127.0.0.1:8000/static/articles/sample-1.png


2. 추가 경로
  - STATICFILES_DIRS
    - 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

```py
# settings
# 추가 경로 statix file 
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

```html
  <!-- articles/templates/articles/index.html -->
 {% load static %} 
 <img src="{% static 'sample-2.png' %}" alt="2번 그림">
```


## Media Files
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
- 사용자가 업로드 하는 파일도 static file
- static file안에 media file


### 미디어 파일을 제공하기 전 준비
1. settings.py에 MEDIA_ROOT, MEDIA URL 설정

> MEDIA_ROOT

- 미디어 파일들이 위치하는 디렉토리의 절대 경로
- static은 내장되어 있지만 media는 설정 해줘야 함

> MEDIA URL

- MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성
- STATIC_URL과 동일한 역할
- static은 내장되어 있지만 media는 설정 해줘야 함

```py
# 사용자가 업로드한 사진이 어디에 저장될 것인지
MEDIA_ROOT = BASE_DIR / 'media'

# 사용자가 업로드한 사진이 화면에 보기 위해 URL이 필요하기 때문
MEDIA_URL = '/media/'
```

2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정
- 사용자가 URL을 요청했을때 응답할 path를 하나 추가하는 것

```py
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# static(url, 물리적위치)
```

- 업로드 된 파일의 URL == settings.MEDIA_URL
- 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT

### 이미지 업로드 및 제공하기
1. model
- 이미지가 없어도 저장될 수 있도록 blank=True속성을 사용해 빈 문자열도 허용

```py
# articles/models.py

from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()

  # 이미지를 업로드 하지 않아도 허용
  image = models.ImageField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# 기존 필드 사이에 작성해도 실제 테이블 생성시 가장 우측(뒤)에 추가됨
# 왜냐면 그 전에 만든 DB가 있으니깐
```


> ImageField()

- 이미지 업로드에 사용하는 모델 필드
- 이미지 객체가 직접 저장되는 것이 아닌
- ***이미지 파일의 경로 문자열*** 이 DB에 저장

- 에러 발생
  - articles.Article.image: (fields.E210) Cannot use ImageField because Pillow is not installed. 
  
  HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
- ImageField는  pillow 라이브러리를 설치해야 사용가능
- 라이브러리 설치 후 requirements 업데이트 하기
  - $ pip freeze> requirements

2. migration 진행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

3. template

- form 요소의 enctype 속성 추가

> <form enctype="속성값">

  - form data가 서버로 제출될때 해당 데이터가 인코딩되는 방법을 명시함.
    - multipart/form-data
    - 모든 문자를 인코딩하지 않음을 명시함.
    - 이 방식은 <form> 요소가 파일이나 이미지를 서버로 전송할 때 주로 사용함.
  - method = "POST"인 경우에만 사용 가능 

```html
<!-- articles/templates/artices/new.html -->
 <form action="{% url 'articles:create' %}" method = "POST" enctype = "multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value ="작성완료">
  </form>
```

4. view

```py
# articles/views.py
def create(request):
    # HTTP request method POST라면 => create 로직
    # 두 번째 인자로 file를 입력받음
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid(): 
            article = form.save() 
            return redirect('articles:detail', article.pk)
    
    # HTTP request method POST가 아니라면 (GET)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

5. 결과

- DB엔 이미지 파일 자체가 아닌 경로가 저장됨.
- 여러 사용자가 같은 이름의 파일을 올려도 django가 동일한 이름뒤에 hash값을 붙여 구별한다.

### media file 추가 경로 설정

```py
# articles/models.py

class Article(models.Model):
  # MEDIA_ROOT 이후의 추가 경로를 설정 -> upload_to
  # MEDIA_ROOT는 media라고 설정했음

  # 1. media/image 디렉토리 안에 저장하기
  image = models.ImageField(blank=True, upload_to='images/')

  # 2. media/날짜별로 저장하기 ex) media/2023/04/11/01.png
  image = models.ImageField(blank=True, upload_to='%y/%m/%d/')

  # 3. media/유저 네임별로 저장하기
  def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'
  image = models.ImageField(blank=True, upload_to=articles_image_path)
```
