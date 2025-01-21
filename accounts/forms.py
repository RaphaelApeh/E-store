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

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email__iexact=email).exists():
                self.add_error("email", "A user with is email exists.")
            return email

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "johndoe@email.com"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if not qs.exists():
            self.add_error("email", "No user with this %s exists." % self.cleaned_data.get("email"))
        return email
    
    def send_mail(self, url=None, message=None):
        if message is None:
            message = "An email as been sent to reset your password"
        email = self.cleaned_data["email"]
        qs = User.objects.filter(email__iexact=email)
        if not qs.exists():
            return
        user = qs.get()
        user.email_user("Forgot Password", "Link to change your password %s" % url)
        return message