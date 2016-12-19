from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.

class Feedbacks(models.Model):
	name = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	message = models.TextField()
	date = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse("feedbacks:feedbacks",kwargs={"id":self.id})
		return "/feedbacks/%s" %(self.id)

	def get_nep_url(self):
		return reverse("feedbacks_nep:detail_nep",kwargs={"id":self.id})
		#return "/feedbacks/%s" %(self.id)

	#Order the queryset
	class Meta:
		ordering = ["-timestamp", "-updated"]

