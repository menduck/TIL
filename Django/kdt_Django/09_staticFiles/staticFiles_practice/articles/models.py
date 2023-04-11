from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  # MEDIA_ROOT 이후의 추가 경로를 설정 -> upload_to
  image = models.ImageField(blank=True, upload_to='images/')
  # image = models.ImageField(blank=True, upload_to='%y/%m/%d/') 날짜별 업로드 파일 분류
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# articles.Article.image: (fields.E210) Cannot use ImageField because Pillow is not installed.  
        # HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".