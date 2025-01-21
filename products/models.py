# import stripe

from django.db import models
from django.db.models.signals import m2m_changed
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager

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
        super().save(*args, **kwargs)

    def get_absolute_url(self):

        return reverse('products:product-detail', kwargs={'slug': self.slug})
    

def sync_user_cart_price(instance, action, **kwargs):
    prices = [obj.price for obj in instance.products.all()]
    sumed_prices = sum(list(set(prices))) 
    instance.total_price = sumed_prices
    instance.save()

m2m_changed.connect(sync_user_cart_price, sender=Cart.products.through)