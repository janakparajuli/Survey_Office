import django_tables2 as tables
from .models import Revenue

class RevenueTable(tables.Table):

	class Meta:
		model = Revenue
		#add class = "paleblue" to <table> tag
		attrs = {"class":"paleblue"}