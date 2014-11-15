from django.db import models
from django.contrib.auth.models import User

def get_upload_file_name(instance, filename):
	return "user_uploads/user_uploads/%s_%s" % (str(time()).replace('.','_'), filename)

class Catagory(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(blank=True, null=True)
	ordering = models.PositiveIntegerField(default=1)

	def __unicode__(self):
		return self.name

class Forum(models.Model):
	catagory = models.ForeignKey(Catagory)
	name = models.CharField(max_length=200, blank=True, null=True)
	description = models.CharField(max_length=200, blank=True, null=True)
	ordering = models.PositiveIntegerField(default=1)
	is_special = models.NullBooleanField(blank=True, default=False)
	suscribed = models.ManyToManyField(User, blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(blank=True, null=True)
	num_threads = models.IntegerField(default=0)
	num_posts = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Thread(models.Model):
	forum = models.ForeignKey(Forum)
	name = models.CharField(max_length=200, blank=True, null=True)
	attachment = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
	message = models.TextField(blank=True, null=True, default='')
	is_sticky = models.NullBooleanField(blank=True, default=False)
	suscribed = models.ManyToManyField(User, blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(blank=True, null=True)
	num_replies = models.PositiveIntegerField(default=0)
	closed = models.BooleanField(default=False)
	post = models.ForeignKey('Post',related_name='threads_', blank=True, null=True)
	created_by = models.ForeignKey(User, related_name='users_')

	def __unicode__(self):
		return self.name

class Post(models.Model):
	topic = models.ForeignKey(Thread, related_name='posts')
	posted_by = models.ForeignKey(User)
	poster_ip = models.IPAddressField()
	message = models.TextField()


	def __unicode__(self):
		return self.message

