from django.contrib import admin
from .models import Budget
# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
	list_display = ["budget_number","budget_name","budget_amount"]
	list_editable = ["budget_amount"]

	class Meta:
		model = Budget

admin.site.register(Budget, BudgetAdmin)