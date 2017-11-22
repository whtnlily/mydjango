#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return HttpResponse(u'欢迎来到Django世界！')

def add(request):
    a = request.GET['a']   # request.GET 类似于一个字典，更好的办法是用 request.GET.get('a', 0) 当没有传递 a 的时候默认 a 为 0
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse('%s' % c)

def home(request):
    return render(request,'home.html')

'''

'''
def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2',args=(a,b)))
