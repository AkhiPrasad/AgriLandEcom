from django.conf.urls.static import static
from django.urls import path

from AgrilandProject import settings
from cart import views

urlpatterns = [
         path('', views.cart_summary, name="cart_summary"),
         path('add/', views.cart_add, name="cart_add"),
         path('delete/', views.cart_delete, name="cart_delete"),
         path('update/', views.cart_update, name="cart_update"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)