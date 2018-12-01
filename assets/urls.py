#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.urls import path,re_path
from assets import views

app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    re_path(r'^detail/(?P<asset_id>[0-9]+)/$', views.detail, name="detail"),
    path('', views.dashboard),
]


