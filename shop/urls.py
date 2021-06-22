from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include

from . import views
from .views import ProductListView

app_name = 'shop'
app_name = 'orders'

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product'),
    url(r'^product_lists$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    url(r'^orders/', include('orders.urls', namespace='orders')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)