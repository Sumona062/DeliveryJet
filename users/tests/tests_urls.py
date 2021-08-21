from django.test import TestCase, Client, SimpleTestCase
from users.models import *
from django.db import models
from django.urls import reverse, resolve
from users.views import *

# URLS testing
class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_page)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_company_feed_url_is_resolved(self):
        url = reverse('company-feed', args = ['1'])
        self.assertEqual(resolve(url).func, company_feed)

    def test_company_feed_category_url_is_resolved(self):
        url = reverse('company-feed-category', args = ['1', 'Book Store'])
        self.assertEqual(resolve(url).func, company_feed_category)

    def test_company_edit_profile_url_is_resolved(self):
        url = reverse('company-edit-profile')
        self.assertEqual(resolve(url).func, company_edit_profile)




