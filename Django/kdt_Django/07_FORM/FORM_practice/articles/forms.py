from django import forms
from .models import Article

''' 
# Form
# 모든 컬럼들을 다 나열해야됨. => 중복 발생
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
'''

# ModelForm
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목 => ',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-titile',
                'placeholder' : '제목을 입력해주세요',
            }
        )
    )
    
    class Meta:
        model = Article
        fields = '__all__'