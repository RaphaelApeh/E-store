from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, label="", required=True, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(max_length=20, label="", required=True, widget=forms.PasswordInput(attrs={'placeholder': "Password"}))


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "joedoe@example.com"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
        }