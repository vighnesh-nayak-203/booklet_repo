from django.forms import ModelForm
from django import forms
from .models import Booklet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookletForm(ModelForm):
    class Meta: 
        model = Booklet
        fields = ['title','file']

class Register(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']