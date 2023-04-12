from django.db import models
# 직접 참조는 권장하지 않음
# from accounts.models import User

# 간접 참조 get_user_model은 models.py에선 사용하지 않음.
# django 내부 실행 원리로 인해 아직 User 객체를 생성하기 전에 models.py부터 실행되기 때문에
# from django.contrib.auth import get_user_model

# models.py에서 User를 참조할때만 다음과 같이 참조한다.
from django.conf import settings
# Create your models here.

class Article(models.Model):
    # settings.AUTH_USER_MODEL 문자열로 참조
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # 외래 키 필드
    # DB엔 article_id로 저장됨. 그렇기 때문에 명시적으로 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장함
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)