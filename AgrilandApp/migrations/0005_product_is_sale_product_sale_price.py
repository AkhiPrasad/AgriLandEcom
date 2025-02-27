# Generated by Django 5.0.4 on 2024-06-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgrilandApp', '0004_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
