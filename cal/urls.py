#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('cal.views',
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", "month", name='month'),
    url(r"^month/(\d+)/(\d+)/$", "month", name='month'),
    url(r"^month$", "month", name='month'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", "day", name='day'),
    url(r"^settings/$", "settings", name='settings'),
    url(r"^(\d+)/$", "main", name='main'),
    url(r"", "main", name='main'),
)
