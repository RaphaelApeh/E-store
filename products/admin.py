from django.contrib import admin

from .models import Product, Cart

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    ...