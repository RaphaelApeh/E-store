from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


class AuthenticationView(View):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("products:products-list")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        register_form = RegisterForm()
        login_form = LoginForm()
        password_fields = ['password1', 'password2']
        context = {
            "register_form": register_form,
            "login_form":login_form,
            "password_fields": password_fields
        }
        return render(request, "accounts/account.html", context)
    
    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(self.request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get("username")
            password = register_form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "User saved.")
                return redirect("products:products-list")
            messages.error(request, "Error occured")
            return redirect("accounts:auth")
    

account_view = AuthenticationView.as_view()


class LogoutView(View):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        
        logout(request)
        messages.success(request, "user logged out successfully.")
        return redirect("accounts:auth")
    
logout_view = LogoutView.as_view()