from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager

User = get_user_model()

class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", blank=True)
    total_price = models.FloatField(default=99.89)

    def __str__(self):
        return self.user.username

class Product(models.Model):

    product_name = models.CharField(max_length=50, db_index=True)
    product_description = models.TextField()
    product_image = models.ImageField()
    slug = models.SlugField()
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