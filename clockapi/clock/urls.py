from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clocks/$', views.ClockList.as_view(), name='clock-list'),
    url(r'^clock/(?P<pk>[0-9]+)/detail/$', views.ClockDetail.as_view(), name='clock-detail'),
    url(r'^clock/(?P<pk>[0-9]+)/update/$', views.ClockDetail.as_view(), name='clock-update'),
    url(r'^clock/(?P<pk>[0-9]+)/delete/$', views.ClockDetail.as_view(), name='clock-delete')
]