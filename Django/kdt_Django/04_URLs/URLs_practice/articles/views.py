from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'articles/index.html')


def search(request):
    return render(request,'articles/search.html')

# path('articles/<int:num>/',views.detail) URL에서 넘어온 변수명과 일치해야 함 
def detail(request,num):
    context = {
        'num':num
    }
    return render(request,'articles/detail.html',context)


# 함수와 함수사이는 두줄씩 띄어주기
def hello(request,name):
    context = {
        'name':name
    }
    return render(request,'articles/hello.html',context)