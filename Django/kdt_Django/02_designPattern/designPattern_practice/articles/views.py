from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view 함수를 만듦

# 모든 view 함수는 첫번째 인자로 요청 객체를 필수적으로 받음
# 메인페이지를 주로 index라고 명시함
def index(request):
    # return 메인 페이지로 응답
    # 경로는 templates 안에 있는게 기본 경로, 따로 templates/ 안해도 됨.
    return render(request,'index.html')