from django.db import models

from time import time
from datetime import datetime
import django.utils.timezone

#convert color names to bootflat name
COLOR_CHOICES = (
    ('danger', 'red'),
    ('warning', 'orange'),
    ('info', 'blue'),
    ('success', 'green'),
)

def get_upload_file_name(instance, filename):
	return "user_uploads/banner_images/%s_%s" % (str(time()).replace('.','_'), filename)

class Notification(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	color = models.CharField(max_length=200, choices=COLOR_CHOICES, default=1)

class OfficeHours(models.Model):
	monday = models.CharField(max_length=200, blank=True, null=True)
	tuesday = models.CharField(max_length=200, blank=True, null=True)
	wednesday = models.CharField(max_length=200, blank=True, null=True)
	thursday = models.CharField(max_length=200, blank=True, null=True)
	friday = models.CharField(max_length=200, blank=True, null=True)
	saturday = models.CharField(max_length=200, blank=True, null=True)
	sunday = models.CharField(max_length=200, blank=True, null=True)

class BannerImages(models.Model):
	banner_image = models.FileField(upload_to=get_upload_file_name)