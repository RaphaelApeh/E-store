# Generated by Django 5.1.5 on 2025-01-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_cart_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="total_price",
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
