from django.contrib import admin
from .models import Revenue
# Register your models here.
class RevenueAdmin(admin.ModelAdmin):
	list_display = ["month", "total_print_map_num", "print_map_rate", "print_map_revenue",
	 "total_trace_map_num", "trace_map_rate", "trace_map_revenue","field_visit_revenue",
	 "total_revenue"]
	#list_editable = ["cost"]

	class Meta:
		model = Revenue

admin.site.register(Revenue, RevenueAdmin)