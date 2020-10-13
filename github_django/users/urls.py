# /usr/bin/env python
# -*- coding: utf-8 -*-
# author:szc
# from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^users/index/$',views.index)
]
