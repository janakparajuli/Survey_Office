from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone

# Create your models here.
class Revenue(models.Model):
	month = models.CharField(default=0, max_length=120)

	total_print_map_num = models.CharField(max_length=120)
	print_map_rate = models.CharField(max_length=120, default=100)
	print_map_revenue = models.CharField(max_length=120)
	
	total_trace_map_num = models.CharField(max_length=120)
	trace_map_rate = models.CharField(max_length=120,default=100)
	trace_map_revenue = models.CharField(max_length=120)
	
	field_visit_revenue = models.CharField(max_length=120)
	
	publish = models.DateField(auto_now=False, auto_now_add=False)

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	total_revenue = models.IntegerField(default=0)



	def __unicode__(self):
		return self.month

	def __str__(self):
		return self.month

	def get_absolute_url(self):
		return reverse("revenue:detail",kwargs={"id":self.id})

	def get_nep_url(self):
		return reverse("revenue_nep:detail_nep",kwargs={"id":self.id})

	
	#Order the queryset
	class Meta:
		ordering = ["-timestamp", "-updated"]

