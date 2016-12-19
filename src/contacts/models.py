from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# Create your models here.
def upload_location(instance, filename):
	# filebase, extension=filename.split(".")
	# return "%s/%s.%s" %(instance.id, instance.id, extension)
	return "%s/%s" %(instance.id, filename)
	
class Contacts(models.Model):
	name = models.CharField(max_length=120)
	post = models.CharField(max_length=120)
	sheetroll_num = models.CharField(max_length=120)
	mobile_num = models.CharField(max_length=120)
	address = models.CharField(max_length=120)
	image = models.ImageField(upload_to=upload_location, 
		null=True, 
		blank=True, 
		height_field="height_field", 
		width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/contacts/%s" %(self.id)
