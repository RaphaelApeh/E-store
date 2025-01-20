from django.core.paginator import Paginator
from django.views.generic import View, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product, Cart


class ProductView(View):

    def get(self, request, *args, **kwargs):
        
        qs = Product.objects.filter(in_stock=True).order_by("-timestamp")
        paginator = Paginator(qs, 6)
        pages = int(self.request.GET.get("pages", 1))
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
    query_pk_and_slug = "slug"

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