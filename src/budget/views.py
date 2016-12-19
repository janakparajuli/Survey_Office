from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Budget
from .tables import BudgetTable
# Create your views here.

def budget(request):
	budget_table = BudgetTable(Budget.objects.all())
	budget_table.order_by="budget_number"
	RequestConfig(request, paginate={"per_page":25}).configure(budget_table)
	context = {
	"budget_table": budget_table
	}
	return render(request,"budget.html",context)

def budget_nep(request):
	budget_table = BudgetTable(Budget.objects.all())
	budget_table.order_by="budget_number"
	RequestConfig(request, paginate={"per_page":25}).configure(budget_table)
	context = {
	"budget_table": budget_table
	}
	return render(request,"budget_nep.html",context)