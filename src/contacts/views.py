from urllib import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone

from .models import Contacts

# Create your views here.

def contacts(request):
	staff_contacts_list = Contacts.objects.all()
	staff_contacts=request.GET.get("q")
	if staff_contacts:
		staff_contacts_list = staff_contacts_list.filter(
			Q(name__icontains=staff_contacts)|
			Q(post__icontains=staff_contacts)|
			Q(sheetroll_num__icontains=staff_contacts)|
			Q(address__icontains=staff_contacts)
			).distinct()
	paginator = Paginator(staff_contacts_list, 4)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		staff_contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		staff_contacts = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		staff_contacts = paginator.page(paginator.num_pages)

	contact_context = {
	"object_list":staff_contacts,
	"staff_contacts":staff_contacts,
	"page_request_var":page_request_var,
	}
	return render(request, 'contacts.html',contact_context)

def contacts_nep(request):
	staff_contacts_list = Contacts.objects.all()
	staff_contacts=request.GET.get("q")
	if staff_contacts:
		staff_contacts_list = staff_contacts_list.filter(
			Q(name__icontains=staff_contacts)|
			Q(post__icontains=staff_contacts)|
			Q(sheetroll_num__icontains=staff_contacts)|
			Q(address__icontains=staff_contacts)
			).distinct()
	paginator = Paginator(staff_contacts_list, 4)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		staff_contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		staff_contacts = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		staff_contacts = paginator.page(paginator.num_pages)

	contact_context = {
	"object_list":staff_contacts,
	"staff_contacts":staff_contacts,
	"page_request_var":page_request_var,
	}
	return render(request, 'contacts_nep.html',contact_context)