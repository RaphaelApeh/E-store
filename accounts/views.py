from django.views.generic import View, FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm, ForgotPasswordForm


class RegisterView(FormView):
    template_name = "accounts/account.html"
    form_class = RegisterForm
    success_url = "/products/"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect("/products/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            redirect("/accounts/register/")
        return super().form_valid(form)

register_view = RegisterView.as_view()


class LoginView(View):


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            return redirect("/products/")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "accounts/account.html", context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("products:products-list")
            else:
                messages.error(request, "user does not exists or or invalid data.")
                return redirect("accounts:login")
        else:
            messages.error(request, "Invalid data.")
            return redirect("accounts:login")

login_view = LoginView.as_view()

class LogoutView(View):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        
        logout(request)
        messages.success(request, "user logged out successfully.")
        return redirect("accounts:login")
    
logout_view = LogoutView.as_view()

class ForgotPasswordView(View):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect("/products/")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = ForgotPasswordForm()
        context = {
            "show_form": True,
            "form": form
        }
        return render(request, "accounts/forgot-password.html", context)
    
    def post(self, request, *args, **kwargs):
        form = ForgotPasswordForm(self.request.POST)
        if form.is_valid():
            message = form.send_mail(self.request.build_absolute_uri())
            context = {
                "show_form": True,
                "message": message
            }
            return render(request, "accounts/forgot-password.html", context)
        else:
            return redirect("accounts:forgot-password")

forgot_password_view = ForgotPasswordView.as_view()