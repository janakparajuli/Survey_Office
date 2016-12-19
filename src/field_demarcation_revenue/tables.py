import django_tables2 as tables
from .models import FieldDemarcationRevenue

class FieldDemarcationRevenueTable(tables.Table):
	#budget_number=tables.Column(attrs={"th": {"id": "foo"}})
	# budget_name=tables.Column()
	# budget_amount=tables.Column()
	class Meta:
		model = FieldDemarcationRevenue
		#add class = "paleblue" to <table> tag
		attrs = {"class":"paleblue"}