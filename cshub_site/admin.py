from django.contrib import admin
from cshub_site.models import Notification, OfficeHours, BannerImages

from event_app.models import Event, Comment, Going
from django.contrib.auth.models import User

from userprofile.models import UserProfile, Positions

#describes how to display the widget within admin interface
class PositionsAdmin(admin.ModelAdmin):
	filter_horizontal = ('club_position', )


#custom app db registrations
#=======================================
admin.site.register(UserProfile, PositionsAdmin)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Going)
admin.site.register(OfficeHours)
admin.site.register(Positions)
admin.site.register(Notification)
admin.site.register(BannerImages)

