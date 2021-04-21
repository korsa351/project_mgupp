from .models import Addresses, Gymnasts, University
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'password')


class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')


class AddGymnastForm(forms.ModelForm):
    class Meta:
        model=Gymnasts
        fields=['Gymnast_Name','Gymnast_Hometown', 'Gymnast_Address', 'Gymnast_Photo', 'Other_Gymnast_Details', 'University_ID']


class UpdateGymnastForm(forms.ModelForm):
    class Meta:
        model=Gymnasts
        fields=['Gymnast_Name','Gymnast_Hometown', 'Gymnast_Address', 'Other_Gymnast_Details', 'University_ID']
