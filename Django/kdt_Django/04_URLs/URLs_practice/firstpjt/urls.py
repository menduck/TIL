"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# 앱에서 urls.py을 만들어 분산관리해줌
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles로 주소를 만나면 articles.urls로 연결시켜줌
    # 그럼 주소값이 articles/url_name이 됨
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
