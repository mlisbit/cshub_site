from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'forum.views.forum_home'), 
	url(r'^view/(?P<forum_name>[\w\-\@\.]+)/thread/(?P<thread_name>[\w\-\@\.]+)/$', 'forum.views.view_thread'),
	url(r'^view/(?P<forum_name>[\w\-\@\.]+)/$', 'forum.views.view_threads'),

)