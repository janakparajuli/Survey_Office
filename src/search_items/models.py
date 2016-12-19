from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# Create your models here.

class Search(models.Model):
	name = models.CharField(max_length=120)
	link = models.CharField(max_length=120)
	
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
