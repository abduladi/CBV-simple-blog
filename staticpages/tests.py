# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):

    def test_home_page(self):
        response = self.client.get('/staticpages/home/')
        self.assertEquals(response.status_code, 200)


    def test_about_page(self):
        response = self.client.get('/staticpages/about/')
        self.assertEquals(response.status_code, 200)
