from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request,pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request, 'articles/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
    
#     context = {
#         'article' : article,
#         'form' : form
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     article = Article.objects.get(pk=pk)
    
#     form = ArticleForm(request.POST, instance=article)

#     if form.is_valid():
#         form.save()
#         return redirect('articles:index')
#     context ={
#         'article' : article,
#         'form' : form
#     }
#     return render(request, 'articles/edit.html', context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
        
    context = {
        'article' : article,
        'form' : form
    }
    return render(request, 'articles/edit.html', context)       