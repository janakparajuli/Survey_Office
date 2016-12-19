from django.contrib import admin
from .models import Contacts
# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
	list_display = ["name", "post", "sheetroll_num", "mobile_num", "address"]
	search_fields = ["name", "post", "sheetroll_num", "mobile_num", "address"]

	class Meta:
		model = Contacts

admin.site.register(Contacts, ContactsAdmin)