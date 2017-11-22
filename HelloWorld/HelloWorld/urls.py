#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import view
from learn import views as learn_views
urlpatterns = [
    url(r'^index$',view.index),
    url(r'^husnily$', view.hello),
    url(r'^learn$',learn_views.index),
    url(r'^add/$',learn_views.add,name='add'),   # name 可以用于在 templates, models, views ……中得到对应的网址，相当于“给网址取了个名字”，只要这个名字不变，网址变了也能通过名字获取到。
    url(r'^add/(\d+)/(\d+)/$',learn_views.old_add2_redirect),
    url(r'^add3/(\d+)/(\d+)/$',learn_views.add2,name='add2'),
    url(r'^hsnicy$',learn_views.home,name='home'),
]




















