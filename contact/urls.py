from django.conf.urls import url

from contact.views import get
from organizations.views import Profile

urlpatterns = [
     url(r'^contact-us', get, name='about'),





]