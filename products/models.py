import stripe

from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager

stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()

class Cart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", blank=True)
    total_price = models.FloatField(default=10.1, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):

    product_name = models.CharField(max_length=50, db_index=True)
    product_description = models.TextField()
    product_image = models.ImageField()
    stripe_product_id = models.CharField(max_length=60, null=True, blank=True)
    stripe_price_id = models.CharField(max_length=60, null=True, blank=True)
    slug = models.SlugField(max_length=52, blank=True, null=True)
    tags = TaggableManager()
    price = models.FloatField(default=93.3)
    in_stock = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        if self.product_name:
            self.slug = slugify(self.product_name)
            if self.stripe_product_id is None:
                if self.stripe_product_id or self.stripe_price_id is None:
                    stripe_product_id = stripe.Product.create(name=self.product_name, description=self.product_description).id
                    stripe_price_id = stripe.Price.create(product=stripe_product_id, currency="usd", unit_amount=int(self.price) * 100).id
                    self.stripe_product_id = stripe_product_id
                    self.stripe_price_id = stripe_price_id
        super().save(*args, **kwargs)

    def get_absolute_url(self):

        return reverse('products:product-detail', kwargs={'slug': self.slug})
    

def sync_user_cart_price(instance, action, **kwargs):
    prices = [obj.price for obj in instance.products.all().distinct()]
    sumed_prices = sum(list(prices)) or 0.00
    instance.total_price = sumed_prices
    instance.save()

m2m_changed.connect(sync_user_cart_price, sender=Cart.products.through)

def create_user_cart(instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

post_save.connect(create_user_cart, sender=User)