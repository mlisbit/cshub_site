from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'forum.views.forum_home'), 
	url(r'^view/(?P<forum_name>[\w\-\@\.]+)/thread/(?P<thread_name>[\w\-\@\.]+)/$', 'forum.views.view_thread'),
	url(r'^view/(?P<forum_name>[\w\-\@\.]+)/$', 'forum.views.view_threads'),
	url(r'^reply_to_thread$', 'forum.views.reply_to_thread'),
	url(r'^create_thread$', 'forum.views.create_thread'),
)