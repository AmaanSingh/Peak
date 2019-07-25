from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .import models

class UserRegisterForm(forms.ModelForm):
    class Meta():
        model = models.User
        fields = ['email']

def clean_email(self):
    email = self.cleaned_data['email']
    email_qs = User.objects.filter(email = email)
    if email_qs.exists():
        raise forms.ValdiationError(
            "This email already exists. Please try another one."
        )
    return email