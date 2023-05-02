from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login # login 로직과 이름이 같으므로 login 모듈의 이름을 바꿔줌
from django.contrib.auth import logout as auth_logout # logout 로직과 이름이 같으므로 login 모듈의 이름을 바꿔줌
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.
def login(request):
    # 로그인된 인증자는 login 뷰 함수를 호출할 권리가 없다.
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 2. 로그인 실행 로직 (POST)
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 저장이 아니라 세션을 만들어야함.
            auth_login(request, form.get_user())
            return redirect('articles:index')
    # 1. 로그인 페이지 (GET)
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    # session delete
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    # 로그인 된 사용자는 회원가입할 권한이 없다.
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 2. 회원가입 생성 로직 (POST)
    if request.method == "POST":
        # model form은 첫 번째 인자로 데이터를 받음
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원가입 후 로그인까지 진행되려면
            # user = form.save()
            # auth_login(request, user)
            return redirect('articles:index')
    # 1. 회원가입 페이지 (GET)
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    # 게시글처럼 조회한 후에 삭제하는 것이 아니라
    # 나의 유저객체 삭제하는 것
    request.user.delete()
    return redirect('articles:index')


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            
            # 비밀번호 변경 시 세션 무효화 방지
            # 세션의 값을 업데이트 => 비밀번호가 업데이트 되니깐 그에 맞춰 세션 값도 없데이트를 해줘야 한다. => 비밀번호를 바꾸고 다시 로그인을 안해도 된다.
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username = username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user

    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        context = {
            'is_followed': is_followed,
            'followings_count': you.followings.count(),
            'followers_count': you.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)