from django.shortcuts import render, render_to_response
from django.template import RequestContext


def index(request):
	return render_to_response('index.html',RequestContext(request))

def index_nep(request):
	return render_to_response('index_nep.html',RequestContext(request))

def introduction(request):
	return render_to_response('introduction.html',{},RequestContext(request))

def introduction_nep(request):
	return render_to_response('introduction_nep.html',{},RequestContext(request))

def organogram(request):
	return render_to_response('organogram.html',RequestContext(request))

def organogram_nep(request):
	return render_to_response('organogram_nep.html',RequestContext(request))

def major_activities(request):
	return render_to_response('major_activities.html',{},RequestContext(request))

def major_activities_nep(request):
	return render_to_response('major_activities_nep.html',{},RequestContext(request))

def future_plans(request):
	return render_to_response('future_plans.html',{},RequestContext(request))

def future_plans_nep(request):
	return render_to_response('future_plans_nep.html',{},RequestContext(request))

def products_and_services(request):
	return render_to_response('products_and_services.html',RequestContext(request))

def products_and_services_nep(request):
	return render_to_response('products_and_services_nep.html',RequestContext(request))

def citizen_charter(request):
	return render_to_response('citizen_charter.html',RequestContext(request))

def citizen_charter_nep(request):
	return render_to_response('citizen_charter_nep.html',RequestContext(request))

def news(request):
	return render_to_response('news.html',RequestContext(request))

def news_nep(request):
	return render_to_response('news_nep.html',RequestContext(request))

def photo_gallery(request):
	return render_to_response('photo_gallery.html',RequestContext(request))

def photo_gallery_nep(request):
	return render_to_response('photo_gallery_nep.html',RequestContext(request))

