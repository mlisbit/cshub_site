from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^user/(?P<username>.+)/$', 'userprofile.views.view_profile'),
	url(r'^profile/$', 'userprofile.views.edit_profile'), #edit the profile
	url(r'^list/$', 'userprofile.views.view_members'),
	url(r'^list/(?P<year_id>\d+)/$', 'userprofile.views.view_members'),
)