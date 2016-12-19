from urllib import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .tables import RevenueTable
from .models import Revenue

def revenue_list(request):
    today = timezone.now().date()
    revenueset_list = Revenue.objects.all()#filter(draft=False).filter(publish__lte=timezone.now())#.all()#.order_by("-timestamp")
    #queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())#.all()#.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        revenueset_list = Revenue.objects.all()

    revenue = request.GET.get("q")
    if revenue:
        revenueset_list = revenueset_list.filter(
            Q(month__icontains=revenue)|
            Q(total_print_map_num__icontains=revenue)|
            Q(total_trace_map_num__icontains=revenue)
            ).distinct()

    paginator = Paginator(revenueset_list, 4) # Show 4 contacts per page
    page_request_var='page'
    page = request.GET.get(page_request_var)
    try:
        revenueset = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        revenueset = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        revenueset = paginator.page(paginator.num_pages)
    
    revenueset.order_by="publish"
    context = {
    "object_list":revenueset,
    "title":"List",
    "page_request_var":page_request_var,
    "today":today,
    }
    return render(request, "revenue_list.html", context)

def revenue_detail(request, id=None):
    #instance = Post.objects(id=5)
    instance = get_object_or_404(Revenue, id=id)
    share_string = quote_plus(instance.month)
    context = {
    "month":instance.month,
    "instance":instance,
    "share_string":share_string
    }
    return render(request, "revenue_detail.html", context)#return HttpResponse("<h1>Detail<h1>")

def revenue_list_nep(request):
    today = timezone.now().date()
    revenueset_list = Revenue.objects.all()#filter(draft=False).filter(publish__lte=timezone.now())#.all()#.order_by("-timestamp")
    #queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())#.all()#.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        revenueset_list = Revenue.objects.all()

    revenue = request.GET.get("q")
    if revenue:
        revenueset_list = revenueset_list.filter(
            Q(month__icontains=revenue)|
            Q(total_print_map_num__icontains=revenue)|
            Q(total_trace_map_num__icontains=revenue)
            ).distinct()

    paginator = Paginator(revenueset_list, 4) # Show 4 contacts per page
    page_request_var='page'
    page = request.GET.get(page_request_var)
    try:
        revenueset = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        revenueset = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        revenueset = paginator.page(paginator.num_pages)
    
    revenueset.order_by="publish"
    context = {
	"object_list":revenueset,
	"title":"List",
    "page_request_var":page_request_var,
    "today":today,
	}
    return render(request, "revenue_list_nep.html", context)

def revenue_detail_nep(request, id=None):
	#instance = Post.objects(id=5)
    instance = get_object_or_404(Revenue, id=id)
    share_string = quote_plus(instance.month)
    context = {
	"month":instance.month,
	"instance":instance,
    "share_string":share_string
	}
    return render(request, "revenue_detail_nep.html", context)#return HttpResponse("<h1>Detail<h1>")
