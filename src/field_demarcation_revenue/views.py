from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import FieldDemarcationRevenue
from .tables import FieldDemarcationRevenueTable
# Create your views here.

def fieldDemarcationRevenue(request):
	fieldDemarcationRevenue_Table = FieldDemarcationRevenueTable(FieldDemarcationRevenue.objects.all())
	fieldDemarcationRevenue_Table.order_by="vdc"
	RequestConfig(request, paginate={"per_page":30}).configure(fieldDemarcationRevenue_Table)
	context = {
	"fieldDemarcationRevenue_Table": fieldDemarcationRevenue_Table
	}
	return render(request,"field_demarcation_revenue.html",context)

def budget_nep(request):
	budget_table = BudgetTable(Budget.objects.all())
	budget_table.order_by="budget_number"
	RequestConfig(request, paginate={"per_page":25}).configure(budget_table)
	context = {
	"budget_table": budget_table
	}
	return render(request,"budget_nep.html",context)