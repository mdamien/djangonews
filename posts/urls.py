from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\S+)/$', views.post, name='post')
)