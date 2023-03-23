from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['치킨', '삼겹살', '짜장면','김치 볶음밥', '초밥', '김치 찌개', '콩나물 국밥', '스파게티', '비빔밥', '짜장면', '칼국수', '삼계탕', '돈까스']
    context = {
        'foods': random.choice(foods)
    }
    return render(request,'articles/today_dinner.html',context)

def throw(request):
    return render(request,'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data':data,
    }
    return render(request, 'articles/catch.html', context)

def lotto_create(request):
    return render(request,'articles/lotto_create.html')

def lotto(request):
    lotto_quantity = int(request.GET.get("quantity"))
    lotto_list = [random.sample(range(1,46),6) for _ in range(lotto_quantity)]

    context = {
        'lotto_list' : lotto_list,
        'lotto_quantity' : lotto_quantity,
    }
    return render(request,'articles/lotto.html',context)