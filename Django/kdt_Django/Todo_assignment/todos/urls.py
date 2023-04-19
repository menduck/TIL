from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:todo_pk>/', views.detail, name = 'detail'),
    path('new/', views.new, name = 'new'),
    path('<int:todo_pk>/delete/', views.delete, name = 'delete'),
    path('<int:todo_pk>/update/', views.update, name='update'),
    path('<int:todo_pk>/completed/', views.completed, name='completed'),
]
