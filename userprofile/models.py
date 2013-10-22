from django.db import models
from django.contrib.auth.models import User
from time import time
# Create your models here.
# models.BooleanField() is a checkbox 

def get_upload_file_name(instance, filename):
	
	return "user_avatars/%s_%s" % (str(time()).replace('.','_'), filename)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone_number = models.CharField(max_length=200, blank=True, null=True)
	
	major = models.CharField(max_length=200, blank=True, null=True)
	user_description = models.TextField(blank=True, null=True)
	notes = models.TextField(blank=True, null=True)

	events_attended = models.IntegerField(blank=True, null=True)
	twitter_link = models.CharField(max_length=200, blank=True, null=True)
	linkedin_link = models.CharField(max_length=200, blank=True, null=True)
	github_link = models.CharField(max_length=200, blank=True, null=True)

	school = models.CharField(max_length=200, blank=True, null=True)
	student_number = models.CharField(max_length=200, blank=True, null=True)
	
	user_avatar = models.FileField(upload_to=get_upload_file_name)

	def __unicode__(self):
		user = str(self.user)
		return user

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])