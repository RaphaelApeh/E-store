import datetime

from django.views.generic import View, DetailView
from django.shortcuts import render

from .models import Product, Cart


class ProductView(View):

    def get(self, request, *args, **kwargs):

        products = Product.objects.filter(in_stock=True).order_by("-timestamp")

        context = {
            "products": products,
            'year': datetime.datetime.now().year
        }
        return render(request, "products/products.html", context)
    
product_list_view = ProductView.as_view()


class ProductDetailView(DetailView):
    template_name = "products/products-details.html"
    model = Product
    queryset = Product.objects.filter(in_stock=True)
    query_pk_and_slug = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.exclude(id=self.get_object().id)
        return context
    

product_detail_view = ProductDetailView.as_view()