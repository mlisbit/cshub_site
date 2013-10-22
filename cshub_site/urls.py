from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()
#django social auth https://github.com/omab/django-social-auth#!

urlpatterns = patterns('',
	#(r'^signup/', include('registration_app.urls')), 
	(r'^events/', include('event_app.urls')),
	#userprofile 
    (r'^accounts/', include('userprofile.urls')),
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'cshub_site.views.home'), 
    
    #user authentication
    url(r'^accounts/login/$', 'cshub_site.views.login'),
    url(r'^accounts/auth/$', 'cshub_site.views.auth_view'), 
    url(r'^accounts/logout/$', 'cshub_site.views.logout'), 
    url(r'^accounts/loggedin/$', 'cshub_site.views.loggedin'), 
    url(r'^accounts/invalid/$', 'cshub_site.views.invalid_login'), 

    #user registration urls
    url(r'^accounts/register/$', 'cshub_site.views.register_user'), 
    url(r'^accounts/register_success/$', 'cshub_site.views.register_success'), 

    #password and email resets
    #source: http://garmoncheg.blogspot.com.au/2012/07/django-resetting-passwords-with.html
    url(r'^accounts/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/done/'},name="password_reset"),
    url(r'^accounts/reset/done/$','django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/done/'}),
    url(r'^accounts/done/$', 'django.contrib.auth.views.password_reset_complete'),
    

    #django-registration package
)

