from django import forms
from .models import Account

from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['user_name', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user_name', 'email', 'image', 'about']

