from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     '''
#     # 필드가 많아질수록 아래 코드가 길어지게 된다.
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     '''
#     form = ArticleForm(request.POST)
#     # 유효성 검사
#     if form.is_valid(): # True 
#         # 저장
#         article = form.save() # 새로운 게시글 객체
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form' : form, # 통과하지 못한 form은 에러메시지가 담아져있음.
#     }
#     return render(request, 'articles/new.html', context)


# new+create 통합 로직
def create(request):
    # HTTP request method POST라면 => create 로직
    if request.method == "POST":
        form = ArticleForm(request.POST)
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


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     # 기존 데이터를 인자로 넣어줌
#     # .html에서 value값으로 해당 데이터 내용이 있는거와 동일함
#     form = ArticleForm(instance=article) 
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request,pk):
#     article = Article.objects.get(pk=pk)
#     # 두 번째 인자로 기존 데이터를 가져옴
#     form = ArticleForm(request.POST, instance=article)
#     # 유효성 검사
#     if form.is_valid(): # True 
#         # save()는 form이 두 번째 인자로 기존 데이터를 가져왔으므로 수정이라고 판단함.
#         # 만약 두 번째 인자가 없으면 생성이라고 판단함.
#         form.save() 
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article' : article,
#         'form' : form, # 통과하지 못한 form은 에러메시지가 담아져있음.
#     }
#     return render(request, 'articles/edit.html', context)


# edit+update 통합
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save() 
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form, 
    }
    return render(request, 'articles/edit.html', context)


    
