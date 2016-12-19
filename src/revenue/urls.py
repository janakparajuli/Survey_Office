from django.conf.urls import url
from django.contrib import admin
from revenue.views import (
    revenue_list,
    revenue_detail,
    )
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', revenue_list, name="list"),
    url(r'^(?P<id>[\w-]+)/$', revenue_detail, name="detail"),
]