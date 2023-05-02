from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
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
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)


@login_required
def delete(request, pk):
    # 삭제를 요청하는 자 vs 게시글의 작성자를 비교
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    
    return redirect('articles:index')



@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 수정을 요청하는 자 vs 게시글의 작성자를 비교
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article' : article,
        'form' : form
    }
    return render(request, 'articles/edit.html', context)     


@login_required
def comment_create(request, pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        # commit을 False로 주면 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', pk)
    context = {
        'article' : article,
        # 에러메시지가 포함된 form
        'comment_form' : comment_form,
    }
    # 에러메시지가 출력됨
    return render(request, 'articles/detail.html', context)


@login_required
def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk = comment_pk)
    # 삭제를 요청하는 자 vs 댓글의 작성자를 비교
    if comment.user == request.user:
        # 댓글 삭제
        comment.delete()
    return redirect('articles:detail', article_pk)

@login_required
def likes(request, article_pk):
    # 1. 좋아요를 누르는 대상 게시글
    article = Article.objects.get(pk=article_pk)
    
    # 2. 좋아요 관계를 추가 or 삭제

    # 2-1. 유저가 게시글에 좋아요 누르는 유저들 안에 있는지 확인
    if request.user in article.like_users.all():
        # 있으면 좋아요 취소
        article.like_users.remove(request.user)
        # request.user.like_articles.remove(article) #역참조
    else:
        # 없으면 좋아요 추가
        article.like_users.add(request.user)
        # request.user.like_articles.add(article) #역참조
    return redirect('articles:index')