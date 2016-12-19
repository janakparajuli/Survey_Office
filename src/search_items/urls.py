from django.conf.urls import url
from django.contrib import admin

from search_items.views import (
	search_items,
	)

urlpatterns = [
    url(r'^$', 'search_items'),
]