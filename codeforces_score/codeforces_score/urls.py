from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeforces_score.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^score/', include('score.urls')),
)
