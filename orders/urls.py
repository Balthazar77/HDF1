from django.conf.urls import url
from . import views
from .views import Order

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', Order.as_view(), name='orders'),

]