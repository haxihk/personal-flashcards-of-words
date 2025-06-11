from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from .models import Word


# فرم ثبت‌نام کاربر
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

# فرم ورود کاربر
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'definition', 'language']
        labels = {
            'word': 'کلمه',
            'definition': 'معنی',
            'language': 'زبان',
        }
        widgets = {
            'word': forms.TextInput(attrs={'placeholder': 'کلمه مورد نظر را وارد کنید'}),
            'definition': forms.TextInput(attrs={'placeholder': 'معنی کلمه را وارد کنید'}),
        }
