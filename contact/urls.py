from django.conf.urls import url

from contact.views import AboutUsView
from organizations.views import Profile

urlpatterns = [
     url(r'^contact-us', AboutUsView.as_view(), name='about'),





]