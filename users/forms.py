from django import forms
from django.forms import TextInput, PasswordInput


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин',
                               widget=TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               widget=PasswordInput(attrs={'class': 'form-input'}))

