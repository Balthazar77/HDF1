"""HDF1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

app_name = 'shop'
app_name = 'cart'
app_name = 'orders'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('organizations.urls')),
    url(r'^contact/', include('contact.urls'))


]
