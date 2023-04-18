from django.urls import path
from . import views

app_name = 'memos'
urlpatterns = [
    path('',views.index, name='index'),
    path('throw/',views.throw, name='throw'),
    path('catch/',views.catch, name='catch'),
    path('number-print/<int:number>/', views.number_print, name='number_print'),
    path('calculate/<int:num1>/<int:num2>/', views.calculate, name='calculate'),
]










