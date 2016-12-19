from django.contrib import admin
from .models import Notice
# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
	list_display = ["title", "publish", "updated", "timestamp"]

	class Meta:
		model = Notice

admin.site.register(Notice, NoticeAdmin)