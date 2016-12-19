"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'website.views.index'),
    url(r'^index/$', 'website.views.index'),
    url(r'^index_nep/$', 'website.views.index_nep'),

    url(r'^introduction/$', 'website.views.introduction'),
    url(r'^introduction_nep/$', 'website.views.introduction_nep'),
    
    url(r'^organogram/$', 'website.views.organogram'),
    url(r'^organogram_nep/$', 'website.views.organogram_nep'),

    url(r'^major_activities/$', 'website.views.major_activities'),
    url(r'^major_activities_nep/$', 'website.views.major_activities_nep'),

    url(r'^future_plans/$', 'website.views.future_plans'),
    url(r'^future_plans_nep/$', 'website.views.future_plans_nep'),

    url(r'^products_and_services/$', 'website.views.products_and_services'),
    url(r'^products_and_services_nep/$', 'website.views.products_and_services_nep'),
    
    url(r'^citizen_charter/$', 'website.views.citizen_charter'),
    url(r'^citizen_charter_nep/$', 'website.views.citizen_charter_nep'),

    url(r'^field_demarcation_revenue/', include('field_demarcation_revenue.urls',namespace='field_demarcation_revenue')),

    url(r'^feedbacks/', include('feedbacks.urls', namespace='feedbacks')),
    url(r'^feedbacks_nep/', include('feedbacks.urls_nep', namespace='feedbacks_nep')),
    
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^contacts_nep/', include('contacts.urls_nep', namespace='contacts_nep')),
    
    url(r'^notice/', include('notice.urls', namespace='notice')),
    url(r'^notice_nep/', include('notice.urls_nep', namespace='notice_nep')),
    
    url(r'^budget/', include('budget.urls', namespace='budget')),
    url(r'^budget_nep/', include('budget.urls_nep', namespace='budget_nep')),

    url(r'^revenue/', include('revenue.urls', namespace='revenue')),
    url(r'^revenue_nep/', include('revenue.urls_nep', namespace='revenue_nep')),

    url(r'^news/$', 'website.views.news'),
    url(r'^news_nep/$', 'website.views.news_nep'),
    
    url(r'^photo_gallery/$', 'website.views.photo_gallery'),
    url(r'^photo_gallery_nep/$', 'website.views.photo_gallery_nep'),

    url(r'^search_items/', include('search_items.urls', namespace='search_items')),
]


if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
