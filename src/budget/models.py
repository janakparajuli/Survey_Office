from __future__ import unicode_literals
from django.conf import settings

from django.db import models

# Create your models here.
class Budget(models.Model):
	budget_number = models.CharField(default="N/A",verbose_name="Budget Number",max_length=120)
	budget_name = models.CharField(verbose_name="Budget Name",max_length=120)
	budget_amount = models.CharField(verbose_name="Budget Amount",max_length=120)

	def __unicode__(self):
		return self.budget_name

	def __str__(self):
		return self.budget_name
