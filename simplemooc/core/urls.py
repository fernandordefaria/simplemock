from django.conf.urls import re_path, include, url

urlpatterns = re_path('simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)