from django.conf.urls.static import static
from django.urls import path

from AgrilandProject import settings
from payment import views

urlpatterns = [
         path('payment_success', views.payment_success, name="payment_success"),
         path('checkout', views.checkout, name="checkout"),
         path('bill', views.billing_info, name="billing_info"),
         path('order', views.process_order, name="process_order"),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)