from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone

# Create your views here.

from .forms import FeedbacksForm
from .models import Feedbacks

def feedbacks(request):
	form = FeedbacksForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		print form.cleaned_data.get("title")
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	feedbacks_context = {
		"form":form
	}
	return render(request, "feedbacks.html", feedbacks_context)

def feedbacks_detail(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		return HttpResponse("You need to be admin to view this page. Please Log in to continue...")
	feedbacks = get_object_or_404(Feedbacks, id=id)

	feedbacks_context = {
	"subject":feedbacks.subject,
	"feedbacks":feedbacks,
	}
	return render(request,"feedbacks_detail.html",feedbacks_context)

def feedbacks_nep(request):
	form = FeedbacksForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		print form.cleaned_data.get("title")
		instance.save()
		messages.success(request, "Successfully Completed")
		return HttpResponseRedirect(instance.get_nep_url())

	feedbacks_context = {
		"form":form
	}
	return render(request, "feedbacks_nep.html", feedbacks_context)

def feedbacks_detail_nep(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		return HttpResponse("Unauthorised Access Denied...")
	feedbacks = get_object_or_404(Feedbacks, id=id)

	feedbacks_context = {
	"subject":feedbacks.subject,
	"feedbacks":feedbacks,
	}
	return render(request,"feedbacks_detail_nep.html",feedbacks_context)