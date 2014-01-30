from django.db import models
from django.contrib.auth.models import User
from time import time
from datetime import datetime
import django.utils.timezone

#signals stuff:
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives 

def get_upload_file_name(instance, filename):
	return "user_uploads/event_imgs/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	location = models.CharField(max_length=200)
	when = models.DateTimeField('Date Of', blank=True, null=True)
	date_posted = models.DateTimeField('Date Posted', blank=True, null=True)
	
	event_img = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
	
	def __unicode__(self):
		return self.name
	@property
	def is_over(self):
		#if false show the event
		if (datetime.now() < self.when.replace(tzinfo=None)):
			return False
		else:
			return True

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

#send an email on creation of event. 
@receiver(post_save, sender=Event)
def send_email_on_event_creation(sender, **kwargs):
	event_id 	= ''
	event_name 	= ''
	try:
		event_id = Event.objects.get(name=kwargs.get('instance')).id
		event_name = Event.objects.get(name=kwargs.get('instance')).name
	except:
		print 'Error, most likely due to duplicate Event name'

	emails = list(User.objects.values_list('email', flat=True))
	html_content="<b>York University Computing Students Hub</b><br>"+ event_name +": <a href='http://www.cshub.ca/events/get/"+str(event_id)+"'>Check it out</a>"
	msg = EmailMultiAlternatives("New Event Posted on CSHUB", '', '', [emails])
	msg.attach_alternative(html_content, "text/html")
	msg.send()