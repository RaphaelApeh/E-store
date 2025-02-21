# Generated by Django 5.1.5 on 2025-01-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stripe_price_id",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="stripe_product_id",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
