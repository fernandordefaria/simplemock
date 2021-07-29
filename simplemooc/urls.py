from django.conf.urls import re_path, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = re_path('',
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
