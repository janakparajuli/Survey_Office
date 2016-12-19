from urllib import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone

from .models import Search

# Create your views here.

def search_items(request):
	search_items_list = Search.objects.all()
	search_items=request.GET.get("search")
	if search_items:
		search_items_list = search_items_list.filter(
			Q(name__icontains=search_items)|
			Q(link__icontains=search_items)
			).distinct()
	paginator = Paginator(search_items_list, 4)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		search_items = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		search_items = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		search_items = paginator.page(paginator.num_pages)

	search_items_context = {
	"object_list":search_items,
	"search_items":search_items,
	"page_request_var":page_request_var,
	}
	return render(request, 'search_items.html',search_items_context)