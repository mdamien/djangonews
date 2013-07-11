from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	(r'^comments/', include('django.contrib.comments.urls')),
	#url(r'', include('social_auth.urls')),
)

urlpatterns += patterns('',
	url(r'^', include('posts.urls')),
)