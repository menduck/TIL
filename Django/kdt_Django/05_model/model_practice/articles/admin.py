from django.contrib import admin
# 명시적 상대 경로
# 현재 있는 models에서 Article 클래스를 가져온다.
from .models import Article 

# Register your models here.
# admin.site.register(우리가 만든 Article 클래스를 등록)
admin.site.register(Article)