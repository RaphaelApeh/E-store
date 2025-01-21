from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.home_page_view),
    path("products/", views.product_list_view, name="products-list"),
    path("products/<slug:slug>/", views.product_detail_view, name="product-detail"),
    path("cart/", views.cart_view, name="cart")
]