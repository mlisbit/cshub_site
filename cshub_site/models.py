from django.db import models

# Create your models here.

class Notification(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	color = models.CharField(max_length=200)

class OfficeHours(models.Model):
	monday = models.CharField(max_length=200)
	tuesday = models.CharField(max_length=200)
	wednesday = models.CharField(max_length=200)
	thursday = models.CharField(max_length=200)
	friday = models.CharField(max_length=200)
	saturday = models.CharField(max_length=200)
	sunday = models.CharField(max_length=200)