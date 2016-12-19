from django.conf.urls import url
from django.contrib import admin

from notice.views import (
	notice_nep,
	notice_detail_nep,
	)

urlpatterns = [
    url(r'^$', 'notice.views.notice_nep'),
    url(r'^(?P<id>[\w-]+)/$', notice_detail_nep, name="detail_nep"),

]