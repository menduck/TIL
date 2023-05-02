from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # user_id는 사용자에게 받는 것이 아니므로 출력에서 가림
        fields = ('title','content',)

class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('content',)