import stripe

from django.views import View
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404

from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutView(View):

    def get(self, request, *args, **kwargs):

        product_slug = kwargs["slug"]
        product = get_object_or_404(Product, slug=product_slug)
        stripe_price_id = product.stripe_price_id
        success_url = self.request.build_absolute_uri("/success/?session_id{CHECKOUT_SESSION_ID}")
        cancel_url = self.request.build_absolute_uri("/products/")
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price": stripe_price_id,
                "quantity": 1
            }],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url
        )
        return redirect(checkout_session.url)
        

checkout_view = CheckoutView.as_view()