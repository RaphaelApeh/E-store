import stripe

from django.conf import settings
from django.core.management.base import BaseCommand

from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


class Command(BaseCommand):


    def handle(self, *args, **options):
        try:
            for product in Product.objects.all():
                if all([product.stripe_product_id, product.stripe_price_id]):
                    continue
                
                stripe_product_id = stripe.Product.create(name=product.product_name, description=product.product_description).id
                
                stripe_price_id = stripe.Price.create(product=stripe_product_id, currency="usd", unit_amount=int(product.price) * 100).id
                
                product.stripe_product_id = stripe_product_id
                product.stripe_price_id = stripe_price_id
                product.save()
        except:
            pass