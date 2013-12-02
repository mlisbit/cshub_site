from django.contrib import admin
from cshub_site.models import Notification, OfficeHours

from event_app.models import Event, Comment, Going
from django.contrib.auth.models import User

from userprofile.models import UserProfile, Positions

'''
from django.contrib.auth.admin import UserAdmin
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.ModelAdmin):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

# Define a new User admin
class UserProfile(UserAdmin):
    inlines = (UserProfileInline, )

#re-register user admin
admin.site.unregister(User)
admin.site.register(User, UserProfile)
'''

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

