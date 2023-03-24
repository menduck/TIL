from django.shortcuts import render

# Create your views here.

def index(request):
  context = {
    'name': 'Harry',
  }
  return render(request, 'articles/index.html',context)


def dinner(request):
  foods = ['떡볶이', '닭발', '닭볶음탕', '쌀국수']
  context = {
    'foods':foods
  }
  return render(request, 'articles/dinner.html', context)

def dinner2(request):
  foods = ['떡볶이', '닭발', '닭볶음탕', '쌀국수']
  context = {
    'foods':foods
  }
  return render(request, 'articles/dinner_inheritance.html', context)

def search(request):
  return render(request,'articles/search.html')

def throw(request):
  return render(request, 'articles/throw.html')

def catch(request):
  data = request.GET.get('message')
  context = {
    'data' : data,
  }
  return render(request, 'articles/catch.html',context)