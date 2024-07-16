
from django.urls import path

from AgrilandApp import views


urlpatterns = [
    path('login/', views.login_user, name='lg1'),
    path('signup/', views.signup, name='sg1'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('ship_info/', views.shipping_info, name='shipping_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('logout/', views.logout_user, name='logout'),
    path('product/<int:pk>', views.Product, name='product'),
    path('category/<str:cat>', views.category, name='category'),


]

