from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from user.views import register,login


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',login),
    url(r'^login/$',login),
    url(r'^register/$', register),
]
