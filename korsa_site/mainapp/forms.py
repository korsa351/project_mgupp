from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.http import request

class LoginUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'password')


class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')
