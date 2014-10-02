from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
	(r'^events/', include('event_app.urls')),
    (r'^accounts/', include('userprofile.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'cshub_site.views.home'), 

    #reset pass
    url(r'^resetpass/$', 'cshub_site.views.reset_password_view'),
    url(r'^resetpass/(?P<email_reset_email>[\w\-\@\.]+)/(?P<email_reset_id>\d+)$', 'cshub_site.views.reset_password_edit'),

    url(r'^graph/$', 'cshub_site.views.graph'), 
    url(r'^contact/$', 'cshub_site.views.view_contact'), 
    url(r'^contact/sendmail$', 'cshub_site.views.post_contact'), 
    url(r'^faq/$', 'cshub_site.views.faq_view'), 
    url(r'^about-site/$', 'cshub_site.views.about_site'), 
    #user authentication
    url(r'^accounts/login/$', 'cshub_site.views.login'),
    url(r'^accounts/auth/$', 'cshub_site.views.auth_view'), 
    url(r'^accounts/logout/$', 'cshub_site.views.logout'), 
    url(r'^accounts/loggedin/$', 'cshub_site.views.loggedin'), 
    url(r'^accounts/invalid/$', 'cshub_site.views.invalid_login'), 

    #user registration urls
    url(r'^accounts/register/$', 'cshub_site.views.register_user'), 
    url(r'^accounts/register_success/$', 'cshub_site.views.register_success'), 

    
)

