from django.shortcuts import render, redirect

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

def detail(request, pk):
    # 컬럼에서 pk = url에서 받은 pk
    article = Article.objects.get(pk=pk)
    # 확인하기
    # print(article)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. new에서 보낸 사용자 데이터를 받아 변수에 저장
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    
    # POST
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. 받은 데이터를 DB에 저장
        # 2-1. 특정 테이블에 새로운 행 추가하여 데이터 추가
    # article = Article.objects.all()
    # article.title = title
    # article.content = content
    # article.save()

        # 2-2. class 생성자 바로 넣는 방법
    article = Article(title = title, content = content)
    article.save()

        # 2-3. create 메서드 사용
    # Article.objects.create(title=title, content = content)
    

    # 3. 결과 페이지 반환
    # return render(request, 'articles/create.html')

    # 이동 URL 반환
    # return redirect("articles:index")

    # 세부 페이지 URL로 이동 응답
    return redirect("articles:detail", article.pk)

def delete(request, pk):
    # 삭제할 데이터 조회
    article = Article.objects.get(pk=pk)

    # 조회할 데이터 삭제
    article.delete()

    # 메인 페이지로 이동
    return redirect("articles:index")

def edit(request,pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request,'articles/edit.html', context)

def update(request,pk):
    # 데이터 조회
    article = Article.objects.get(pk=pk)

    # 데이터 수정
    # 데이터가 입력한 form 데이터 저장
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 조회한 데이터의 필드 값 변경
    article.title = title
    article.content = content

    # 데이터 저장
    article.save()

    return redirect('articles:index')