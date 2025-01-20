from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.account_view, name="auth"),
    path("logout/", views.logout_view, name="logout")
]