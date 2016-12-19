from django.contrib import admin
from .models import Feedbacks
from django.forms import Textarea, ModelForm

from feedbacks.forms import FeedbacksForm
# Register your models here.

class FeedbacksAdmin(admin.ModelAdmin):
	list_display = ["name", "email", "subject", "date"]
	forms=FeedbacksForm

	class Meta:
		model= Feedbacks

admin.site.register(Feedbacks, FeedbacksAdmin)