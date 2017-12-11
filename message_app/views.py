# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from .models import Message
# Create your views here.



class Home(ListView):
    model = Message

    template_name = 'message_app/index.html'