from django.conf.urls import url
from django.contrib import admin

from feedbacks.views import (
	feedbacks_nep,
	)

urlpatterns = [
    url(r'^$', 'feedbacks.views.feedbacks_nep', name="feedbacks_nep"),
    url(r'^(?P<id>\d+)/$', 'feedbacks.views.feedbacks_detail_nep', name="detail_nep"),
]