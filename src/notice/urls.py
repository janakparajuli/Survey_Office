from django.conf.urls import url
from django.contrib import admin

from notice.views import (
	notice,
	notice_detail,
	)

urlpatterns = [
    url(r'^$', 'notice.views.notice'),
    url(r'^(?P<id>[\w-]+)/$', notice_detail, name="detail"),

]