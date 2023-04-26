from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUerCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html',context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


def signup(request):
    if request.method == "POST":
        form = CustomUerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUerCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html',context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')


def update(request):
    if request.method=="POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html',context)


def update_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update_password.html', context)
