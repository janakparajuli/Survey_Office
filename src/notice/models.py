from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.

class Notice(models.Model):
	title = models.CharField(max_length=120)
	notice_content = models.TextField()
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("notice:detail",kwargs={"id":self.id})

	def get_nep_url(self):
		return reverse("notice_nep:detail_nep",kwargs={"id":self.id})
