from django import forms
from django.forms import ModelForm, Textarea

from .models import Feedbacks
class FeedbacksForm(forms.ModelForm):
	class Meta:
 		model = Feedbacks
 		fields = [
 			"name",
 			"email",
 			"subject",
 			"message",
 			"date"
 		]
 		widgets={"message":Textarea(attrs={'cols':70,'rows':5}),}