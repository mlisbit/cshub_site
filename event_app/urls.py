from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'event_app.views.listings'), 

	url(r'^get/(?P<event_id>\d+)/$', 'event_app.views.listing'),

	url(r'^add_comment/(?P<event_id>\d+)/$', 'event_app.views.add_comment'), #adding a comment
	url(r'^going_to/(?P<event_id>\d+)/$', 'event_app.views.going_to'),

)