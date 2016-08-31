from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tredo/', include('tredo.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^static/(?P<path>.*)',
         'serve',
         {'document_root': settings.STATIC_ROOT}), )
