from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^user/(?P<username>.+)/$', 'userprofile.views.view_member'),
	url(r'^profile/$', 'userprofile.views.user_profile'),
	url(r'^list/$', 'userprofile.views.view_members'),
	
)