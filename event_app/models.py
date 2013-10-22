from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	date_posted = models.DateTimeField('Date Posted', blank=True, null=True)
	date_of = models.DateTimeField('Date Of', blank=True, null=True)

	pub_date = models.DateTimeField('Date Published')

	attending = models.TextField(blank=True, null=True)
	maybe_attending = models.TextField(blank=True, null=True)
	
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