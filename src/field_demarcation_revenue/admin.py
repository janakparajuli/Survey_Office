from django.contrib import admin
from .models import FieldDemarcationRevenue
# Register your models here.
class FieldDemarcationRevenueAdmin(admin.ModelAdmin):
	list_display = ["distance","vdc","revenue","remarks"]
	list_editable = ["revenue"]
	ordering = ["distance"]

	class Meta:
		model = FieldDemarcationRevenue

admin.site.register(FieldDemarcationRevenue, FieldDemarcationRevenueAdmin)