# Generated by Django 5.1.5 on 2025-01-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
