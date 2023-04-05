# HTTP requests 처리에 따른 view 함수 구조 변화

## new+create, edit+update 로직 통합

### new & create view 함수간 공통점과 차이점

- 공통점
  - 데이터 생성(C) 로직을 구현하기 위함

- 차이점
  - new는 GET method 요청만을, / 페이지 조회
  - create는 POST method 요청만을 처리

- new와 create 로직을 합친다.
  - method의 요청에 따라 분기문을 작성한다.
  - GET이면 new, POST는 create
- 관련 url 수정하기

```py
# articles/views.py

def new_create(request):
    # HTTP request method POST라면 => create 로직
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid(): 
            article = form.save() 
            return redirect('articles:detail', article.pk)
        # 중복제거
        # context = {
        #     'form' : form, 
        # }
        # return render(request, 'articles/new.html', context)
    

    # HTTP request method POST가 아니라면 (GET)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

### edit+update 로직

```py
# articles/views.py

# edit+update 통합
def update(request,pk):
    article = Article.objects.get(pk=pk)
    # update
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save() 
            return redirect('articles:detail', article.pk)
    # edit
    else:
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form, 
    }
    return render(request, 'articles/edit.html', context)
```