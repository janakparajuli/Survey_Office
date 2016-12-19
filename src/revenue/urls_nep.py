from django.conf.urls import url
from django.contrib import admin
from revenue.views import (
    revenue_list,
    revenue_list_nep,
    revenue_detail,
    revenue_detail_nep,
    )
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', revenue_list_nep, name="list_nep"),
    url(r'^(?P<id>[\w-]+)/$', revenue_detail_nep, name="detail_nep"),
]