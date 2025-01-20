from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=20, required=True)
