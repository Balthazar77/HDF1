from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from organizations import views
from organizations.views import Profile

urlpatterns = [
     # url('^login/$', Login, name='login'),
     # # url(r'^login/$', SigninView.as_view(), name='signup'),
     url(r'^account/profile', Profile.as_view(), name='profile'),
     # path('', SignoutView.as_view(), name='logout'),




]