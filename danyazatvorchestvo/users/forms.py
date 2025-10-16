from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SimpleRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш email'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте логин'
            }),
        }
        
        labels = {
            'username': 'Логин',
            'email': 'Email',
            'password1': 'Пароль',
            'password2': 'Повторите пароль'
        }

class SimpleLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш логин'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш пароль'
        })
    )