from django.contrib import admin
from .models import ShippingAddress, OrderItem, Order

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

