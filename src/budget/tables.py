import django_tables2 as tables
from .models import Budget

class BudgetTable(tables.Table):
	#budget_number=tables.Column(attrs={"th": {"id": "foo"}})
	# budget_name=tables.Column()
	# budget_amount=tables.Column()
	class Meta:
		model = Budget
		#add class = "paleblue" to <table> tag
		attrs = {"class":"paleblue"}