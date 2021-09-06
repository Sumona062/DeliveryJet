from django.test import SimpleTestCase
from order.models import *
from django.db import models
from django.urls import reverse, resolve
from order.views import *

# URLS testing
class TestUrls(SimpleTestCase):
    def test_view_cart_url_is_resolved(self):
        url = reverse('view-cart', args = ['1'])
        self.assertEqual(resolve(url).func, view_cart)

    def test_view_pending_url_is_resolved(self):
        url = reverse('view-pending', args = ['1'])
        self.assertEqual(resolve(url).func, view_pending)
