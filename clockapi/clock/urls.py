from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clocks/$', views.ClockList.as_view(), name='clock-list'),
    url(r'^clocks/(?P<pk>[0-9]+)/$', views.ClockDetail.as_view(), name='clock-detail')
]