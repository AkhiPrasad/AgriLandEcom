"""
URL configuration for AgrilandProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import AgrilandApp
from AgrilandApp import views
from AgrilandProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpgfn, name='h1'),
    path('mrkt', views.market, name='m1'),
    path('si', include('AgrilandApp.Loginurl')),
    path('payment/', include('payment.urls')),
    path('cart/', include('cart.urls')),
    path('abt/', views.aboutpg, name='abt1'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
