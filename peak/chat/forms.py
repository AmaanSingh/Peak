from django import forms
from .models import *
from django.contrib.auth.models import User


class userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter username'}
    ), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Enter email address'}
    ), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter first name'}
    ), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter last name'}
    ), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Enter password'}
    ), required=True, max_length=50)

class Meta():
    model = User
    fields = ['username','email','first_ name', 'last_name','password']