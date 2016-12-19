from django.conf.urls import url
from django.contrib import admin

from contacts.views import (
	contacts,
	)

urlpatterns = [
    url(r'^$', 'contacts.views.contacts',name='staff_detail'),
]