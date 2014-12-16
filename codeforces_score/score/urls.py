from django.conf.urls import patterns, include, url
from django.contrib import admin
from score import views

urlpatterns = patterns('',
    url(r'^(?P<req_time>\d*-\d*-\d*)/$', views.score, name='score'),
)
