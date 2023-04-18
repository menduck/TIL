from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'memos/index.html')


def throw(request):
    return render(request, 'memos/throw.html')


def catch(request):
    data = request.GET.get('word')
    print(request)
    context = {
        'data' : data,
    }
    return render(request, 'memos/catch.html',context)


def number_print(request, number):
    context = {
        'number' : number,
    }
    return render(request,'memos/number_print.html',context)


def calculate(request,num1,num2):
    context = {
        'num1' : num1,
        'num2' : num2,
        'mulitply' : num1*num2,
        'divide' : num1//num2,
        'sum' : num1+num2,
        'subtract' : num1-num2,
    }
    return render(request, 'memos/calculate.html',context)