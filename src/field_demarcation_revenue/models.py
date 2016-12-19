from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# Create your models here.
class FieldDemarcationRevenue(models.Model):
	#sn = models.CharField(default="1",verbose_name="SN",max_length=120)
	distance = models.CharField(verbose_name="Distance(Miles)",max_length=120)
	vdc = models.CharField(verbose_name="VDC Name",max_length=120)
	revenue = models.CharField(verbose_name="Revenue(NRs)",max_length=120)
	remarks = models.CharField(default="N/A", verbose_name="Remarks",max_length=120)

	def __unicode__(self):
		return self.distance

	def __str__(self):
		return self.distance
