from django.conf.urls import patterns, url
from tredo import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )