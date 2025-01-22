import time
import random

from django.db import transaction
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.views.generic import View, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Cart


class ProductView(View):

    def get(self, request, *args, **kwargs):
        
        qs = Product.objects.filter(in_stock=True).order_by("-timestamp").only("product_image", "product_name", "price")
        paginator = Paginator(qs, 3)
        try:
            pages = int(self.request.GET.get("pages", 1))
        except:
            pages = 1
        products = paginator.get_page(pages)

        context = {
            "products": products
        }
        return render(request, "products/products.html", context)
    
product_list_view = ProductView.as_view()


class ProductDetailView(DetailView):
    template_name = "products/products-details.html"
    model = Product
    queryset = Product.objects.filter(in_stock=True)
    query_pk_and_slug = True

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            if self.request.method in ["POST", "DELETE", "PUT"]:
                return redirect("accounts:login")
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset = ...):

        queryset = queryset if queryset is None else self.get_queryset()

        return get_object_or_404(queryset, slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_queryset().filter(tags__name__in=self.get_object().tags.names()).distinct().exclude(id=self.get_object().id)[:3]
        return context
    
    def get_queryset(self):
        return self.model.objects.prefetch_related("tags").filter(in_stock=True)
    

product_detail_view = ProductDetailView.as_view()


class HomePageView(TemplateView):
    template_name = "index.html"


home_page_view = HomePageView.as_view()


class CartView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        random_numbers = list(range(100, 500))
        try:
            qs = Cart.objects.prefetch_related("products").filter(user=self.request.user).order_by("-products__timestamp").get()
        except (Cart.DoesNotExist, Cart.MultipleObjectsReturned):
            raise Http404
        context = {
            "qs": qs,
            "tax": random.choice(random_numbers),
            "sub_total": random.choice(random_numbers)
        }

        return render(request, "products/cart.html", context)
    

cart_view = CartView.as_view()


class AddToCartView(LoginRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        product_slug = kwargs["slug"]
        user = self.request.user
        with transaction.atomic():
            cart = Cart.objects.get(user=user)
            product = get_object_or_404(Product, slug=product_slug)
            if cart.products.contains(product):
                time.sleep(2)
                cart.products.remove(product)
                return JsonResponse({"added": False})
            time.sleep(2)
            cart.products.add(product)
        return JsonResponse({"added": True})
    
add_to_cart_view = AddToCartView.as_view()