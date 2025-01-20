from django.contrib import admin

from .models import Product, Cart

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("product_name",)}
    list_display = ['product_name', 'timestamp', 'in_stock']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    ...