from django.conf.urls import url
from django.contrib import admin

from contacts.views import (
	contacts_nep,
	)

urlpatterns = [
    url(r'^$', 'contacts.views.contacts_nep'),
]