# django Form
## 배경
- HTML form
: 사용자로부터 form 요소를 통해 데이터를 받고 있으나 비정상적 혹은 악의적인 요청을 확인하지 않고 모두 수용중

- HTML form은 모두 수용하기 때문에 데이터가 형식에 맞는지 유효성 검증이 필요함.
- 유효성 검증엔 부가적인 많은 것들을 고려해야 하기 때문에 과정과 기능을 제공해주는 도구가 필요

## Django Form
- 사용자 입력 데이터를 수집, 처리 및 유효성 검증을 수행하기 위한 도구
- 유효성 검증을 단순화, 자동화 할 수 있는 기능 제공

1. Form Class 선언
  - 앱 파일 안에 forms 파일 생성

```py
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

```html
<!--
  articles/templates/new.html 
-->
    <div>
      <label for="title">제목: </label>
      <input type="text" id= title name='title'>
    </div>
    <div>
      <label for="content">내용: </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
```
-  html에서 form 태그 안에 있는거와 form 클래스와 내용이 같음.
- 아래 코드는 form 클래스 적용한 템플릿 코드

```html
<!-- articles/templates/new.html  -->

 <form action="{% url 'articles:create' %}" method = POST>
    {% csrf_token %}
    
    <!-- {{ form }} 에 .as_p 속성값을 넣으면 input 태그들이 p태그로 묶임. -->
    {{ form.as_p }}
    <input type="submit" value ="작성완료">
  </form>
```
2. Form class를 적용한 new 로직

```py
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

---

- form클래스를 쓰면 input type은 각각 어떻게 지정할까?
  - Widgets 활용

### Widgets
: HTML input elements의 표현을 담당

```py
# articles/forms.py

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

## ModelForm

- Form : 사용자 입력 데이터를 DB에 저장하지 않을 떄 ex) 로그인
- ModelForm : 사용자 입력데이터를 DB에 저장해야 할 때 ex) 회원가입

  - (게시판 구현을 실습과제로 하고 있으므로, 새로운 게시글 작성하여 DB에 저장해야되므로 ModelForm)

### ModelForm class 선언
- app 폴더 안에 forms 파일 만들기

```py
# articles/forms.py
from django import forms
from .models import Article

''' 
# Form
# 모든 컬럼들을 다 나열해야됨. => 중복 발생
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
'''

# ModelForm
class ArticleForm(forms.ModelForm):
    # inner class와 관련 없고 구조가 이렇게 설계되었음.
    class Meta: # form에 대한 추가 정보
        model = Article
        fields = '__all__' # 전체 출력

# meta data : 데이터에 대한 데이터 / 사진에 대한 데이터 ex) 화소, 밝기 등
```

### fields 및 exclude 속성
- fields : 사용자에게 출력되는 렌더링을 on 할 수 있음.

```py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',) # title만 출력되고 content는 보이지 않음.
```

- exclude : 사용자에게 출력되는 렌더링을 off 할 수 있음

```py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',) # content만 출력되고 title은 보이지 않음.
```

### 유효성 검사

> is_valid()

- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

### create와 edit 로직 modelForm과 유효성 적용해보기

#### create

- 해당 템플릿에 form으로 대체함
- form class를 create 로직에 적용시킴

```py
# articles/templates/articles/new.html
{% extends 'base.html' %}

{% block content %}
  <form action="{% url 'articles:create' %}" method = POST>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value ="작성완료">
  </form>

  <a href="{% url 'articles:index' %}">뒤로가기</a>
{% endblock content %}


# articles/views.py

def create(request):
    '''
    # 필드가 많아질수록 아래 코드가 길어지게 된다.
    title = request.POST.get('title')
    content = request.POST.get('content')
    '''
    form = ArticleForm(request.POST)
    # 유효성 검사
    if form.is_valid(): # True 
        # 저장
        article = form.save() # 새로운 게시글 객체
        return redirect('articles:detail', article.pk)
    context = {
        'form' : form, # 통과하지 못한 form은 에러메시지가 담아져있음.
    }
    return render(request, 'articles/new.html', context)
```

#### edit

```py
# articles/templates/articles/edit.html
{% extends 'base.html' %}

{% block content %}
  <form action="{% url 'articles:update' article.pk %}" method = POST>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value ="작성완료">
  </form>
{% endblock content %}


# articles/views.py
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    # 기존 데이터를 인자로 넣어줌
    # .html에서 value값으로 해당 데이터 내용이 있는거와 동일함
    form = ArticleForm(instance=article) 
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)


def update(request,pk):
    article = Article.objects.get(pk=pk)
    # 두 번째 인자로 기존 데이터를 가져옴
    form = ArticleForm(request.POST, instance=article)
    # 유효성 검사
    if form.is_valid(): # True 
        # save()는 form이 두 번째 인자로 기존 데이터를 가져왔으므로 수정이라고 판단함.
        # 만약 두 번째 인자가 없으면 생성이라고 판단함.
        form.save() 
        return redirect('articles:detail', article.pk)
    context = {
        'article' : article, # 템플릿에 variable routing으로 쓰이기 때문에 넘겨줌
        'form' : form, # 통과하지 못한 form은 에러메시지가 담아져있음.
    }
    return render(request, 'articles/edit.html', context)
```

- save()
  - 데이터베이스 객체를 만들어 저장
  - 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정함.

---

- 왜 ModelForm 키워드 인자 instance를 써야될까?

```py
class BaseModelForm(BaseForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, instance=None, use_required_attribute=None,
                 renderer=None):
```

- ArticleForm(data = request.POST, instance=article) 
- data는 위치인자로 키워드를 기입하지 않아도 data로 인식
- instance는 키워드 기입하지 않으면 files로 인식하기 때문에 키워드를 입력해야 한다.

### ModelForm 스타일 주는법

- widget 활용하기

```py
# articles/forms.py
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목 => ',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-titile',
                'placeholder' : '제목을 입력해주세요',
            }
        )
    )
    
    class Meta:
        model = Article
        fields = '__all__'
```

```html
<!-- 개발자 도구에서 title 요소 확인 -->
<p><label for="id_title">제목 =&gt; :</label> <input type="text" name="title" class="my-titile" placeholder="제목을 입력해주세요" required="" id="id_title"></p>
```