from urllib import quote_plus
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.template import RequestContext


from .models import Notice

# Create your views here.

def view1(request):
	template_name = "notice.html"
	return notice(request, template_name)

def view2(request):
	template_name = "small_column.html"
	return notice(request, template_name)

def notice(request):
	notice = Notice.objects.all()
	notice_context = {
	"notice":notice,
	'range':range(0,10),
	}
	return render_to_response("notice.html", notice_context, RequestContext(request))

def notice_nep(request):
	notice = Notice.objects.all()
	notice_context = {
	"notice":notice,
	'range':range(0,10),
	}
	return render_to_response("notice_nep.html", notice_context, RequestContext(request))

def notice_base(request):
	notice_base = Notice.objects.all()
	notice_context_base = {
	"notice_base":notice_base,
	'range':range(0,10),
	}
	return render_to_response("base.html", notice_context_base, RequestContext(request))

def notice_detail_nep(request, id=None):
	#instance = Post.objects(id=5)
    instance = get_object_or_404(Notice, id=id)
    share_string = quote_plus(instance.title)
    context = {
	"title":instance.title,
	"instance":instance,
    "share_string":share_string
	}
    return render(request, "notice_detail_nep.html", context)#return HttpResponse("<h1>Detail<h1>")

def notice_detail(request, id=None):
	#instance = Post.objects(id=5)
    instance = get_object_or_404(Notice, id=id)
    share_string = quote_plus(instance.title)
    context = {
	"title":instance.title,
	"instance":instance,
    "share_string":share_string
	}
    return render(request, "notice_detail.html", context)#return HttpResponse("<h1>Detail<h1>")
