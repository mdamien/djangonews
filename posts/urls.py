from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^submit/$', views.submit),
    url(r'^(?P<id>\d+)/$', views.details),
    url(r'^(?P<id>\d+)/upvote$', views.upvote),
    url(r'^(?P<id>\d+)/downvote$', views.downvote),
    url(r'^(?P<post_id>\d+)/comments/(?P<node_id>\d+)/upvote$', views.comment_upvote),
    url(r'^(?P<post_id>\d+)/comments/(?P<node_id>\d+)/downvote$', views.comment_downvote),
    url(r'^(?P<post_id>\d+)/comments/reply/(?P<parent_id>\d+)$', views.comment_reply),
)