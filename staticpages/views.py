# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    msg = "afljl"

    return HttpResponse(msg)


def home_page_view(request):

    return render(request, 'staticpages/index.html')

def about_page_view(request):

    return render(request, 'staticpages/about.html')

class HomeView(TemplateView):
    template_name = 'staticpages/index.html'


class AboutView(TemplateView):
    template_name = 'staticpages/about.html'
