from django.db.models import fields
from .models import Addresses, Gymnasts, University, Meets, University_Meet_Participation
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


class AddAddressForm(forms.ModelForm):
    class Meta:
        model=Addresses
        fields=['Address']


class AddUniversityForm(forms.ModelForm):
    class Meta:
        model=University
        fields=['University_Name', 'Other_Details']


class AddMeetForm(forms.ModelForm):
    class Meta:
        model=Meets
        fields=['Meet_Date', 'Meet_Location', 'Meet_Score', 'Other_Details']


class AddUniversityMeetForm(forms.ModelForm):
    class Meta:
        model=University_Meet_Participation
        fields=['University_ID', 'Meet_ID', 'Overall_University_Scores']


class UpdateGymnastForm(forms.ModelForm):
    class Meta:
        model=Gymnasts
        fields=['Gymnast_Name','Gymnast_Hometown', 'Gymnast_Address', 'Other_Gymnast_Details', 'University_ID']
