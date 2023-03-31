from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.
def index(request):
    articles = AccountBook.objects.order_by('-amount')
    context = {
        'articles': articles,
    }
    return render(request, 'accountbooks/index.html', context)


def detail(request, pk):
    article = AccountBook.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    try:
        note = request.POST.get('note')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        description = request.POST.get('description')
        article = AccountBook(note=note, category=category, amount=amount, date=date, description=description)
        article.save()
        return redirect('accountbooks:index')
    except:
        return redirect('accountbooks:index')
        

def edit(request, pk):
    article = AccountBook.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, pk):
    article = AccountBook.objects.get(pk=pk)
    article.note = request.POST.get('note')
    article.amount = request.POST.get('amount')
    article.category = request.POST.get('category')
    article.description = request.POST.get('description')
    article.date = request.POST.get('date')
    article.save()
    return redirect('accountbooks:detail', pk)


def delete(request, pk):
    article = AccountBook.objects.get(pk=pk)
    article.delete()
    return redirect('accountbooks:index')


def copy(request, pk):
    article = AccountBook.objects.get(pk=pk)
    article.pk = None
    article.save()
    return redirect('accountbooks:index')