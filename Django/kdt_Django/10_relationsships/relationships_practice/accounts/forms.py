from django.contrib.auth.forms  import UserCreationForm, UserChangeForm
'''
# django User 객체에 대한 직접 참조 권장하지 않음. 
from .models import User 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
      # 현재 우리가 사용하는 User class로 직접 재정의
      model = User
'''

# 간접 참조 권장
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
      # 현재 우리가 사용하는 User class를 호출해 재정의
      model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
      # 현재 우리가 사용하는 User class를 호출해 재정의
      model = get_user_model()
      # 모든 필드가 아니라 원하는 필드만 열어줌
      fields = ('email', 'first_name', 'last_name', )