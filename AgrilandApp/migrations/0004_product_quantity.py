# Generated by Django 5.0.4 on 2024-06-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgrilandApp', '0003_category_customer_orders_product_delete_agrilandmain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
