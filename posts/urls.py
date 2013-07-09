from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\S+)/$', views.details, name='details')
    url(r'^(?P<id>\S+)/upvote$', views.upvote, name='upvote')
    url(r'^(?P<id>\S+)/downvote$', views.downvote, name='downvote')
)