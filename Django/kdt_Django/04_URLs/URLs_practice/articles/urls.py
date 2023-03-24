from django.urls import path
# 명시적 상대경로(django 권장사항)
# 현재 위치에 있는 views를 import 하겠다를 명시적으로 정의함.
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index, name="index"),
    path('search/',views.search, name="search"),
    path('<int:num>/',views.detail, name="detail"),
    path('hello/<str:name>/',views.hello, name="hello"),
]
