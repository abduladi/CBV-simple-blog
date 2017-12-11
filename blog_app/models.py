# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title  = models.CharField(max_length=200)
    text   = models.TextField()


    def get_absolute_url(self):
        return reverse('post-list')


    def __str__(self):
        return self.title

# print models.Model.get_absolute_url()