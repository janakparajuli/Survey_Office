from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'field_demarcation_revenue.views.fieldDemarcationRevenue'),
]