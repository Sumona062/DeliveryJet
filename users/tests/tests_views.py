from django.test import TestCase, Client, SimpleTestCase
from users.models import *
from django.db import models
from django.urls import reverse, resolve
from users.views import *


class CompanyFeedTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.company = CompanyModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/company-feed/' + str(self.company.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'company-feed'
        response = self.client.get(reverse(url, kwargs = {'pk':self.company.id}))
        self.assertEqual(response.status_code, 302)

class CompanyFeedCategoryTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        type = "Book Store"
        self.company = CompanyModel.objects.create(user=user,type=type)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/company-feed-category/' + str(self.company.id) + '/' + str(self.company.type) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'company-feed-category'
        response = self.client.get(reverse(url, kwargs = {'pk':self.company.id,'cat':self.company.type}))
        self.assertEqual(response.status_code, 302)

