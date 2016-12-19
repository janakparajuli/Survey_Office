from django.conf.urls import url
from django.contrib import admin

from feedbacks.views import (
	feedbacks,
	)

urlpatterns = [
    url(r'^$', 'feedbacks.views.feedbacks', name="feedbacks"),
    url(r'^(?P<id>\d+)/$', 'feedbacks.views.feedbacks_detail', name="detail"),
]