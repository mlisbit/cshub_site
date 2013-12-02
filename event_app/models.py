from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
	return "user_uploads/event_imgs/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	location = models.CharField(max_length=200)
	when = models.DateTimeField('Date Of', blank=True, null=True)
	date_posted = models.DateTimeField('Date Posted', blank=True, null=True)
	
	event_img = models.FileField(upload_to=get_upload_file_name)
	
	def __unicode__(self):
		return self.name

class Comment(models.Model):
	username = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')

	event = models.ForeignKey(Event)

class Going(models.Model):	
	username = models.CharField(max_length=200, blank=True, null=True)
	pub_date = models.DateTimeField('date published', blank=True, null=True)
	event = models.ForeignKey(Event, blank=True, null=True)

	def __unicode__(self): 
		return self.username