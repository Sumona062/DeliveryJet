from django.test import TestCase, Client
from order.models import *
from django.db import models
from django.urls import reverse, resolve
from order.views import *


class ViewCartTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.buyer = BuyerModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/buyer-feed/' + str(self.buyer.id) + '/view_cart'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'view-cart'
        response = self.client.get(reverse(url, kwargs = {'pk':self.buyer.id}))
        self.assertEqual(response.status_code, 302)

class ViewPendingTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.buyer = BuyerModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/buyer-feed/' + str(self.buyer.id) + '/view_pending'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'view-pending'
        response = self.client.get(reverse(url, kwargs = {'pk':self.buyer.id}))
        self.assertEqual(response.status_code, 302)

class OrderDetailsTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
			email="test@ewubd.edu",
			name="test"
		)
        self.user.set_password("Test123")
        self.order = OrderModel.objects.create(buyer=self.user)
        self.orderSchedule = OrderScheduleModel.objects.create(order=self.order)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/order-details/' + str(self.orderSchedule)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'order-details'
        response = self.client.get(reverse(url, kwargs = {'pk':self.orderSchedule.id}))
        self.assertEqual(response.status_code, 302)

class OrderDeliveredTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
			email="test@ewubd.edu",
			name="test"
		)
        self.user.set_password("Test123")
        self.order = OrderModel.objects.create(buyer=self.user)
        self.orderSchedule = OrderScheduleModel.objects.create(order=self.order)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/order-delivered-form/' + str(self.orderSchedule)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'order-delivered'
        response = self.client.get(reverse(url, kwargs = {'pk':self.orderSchedule.id}))
        self.assertEqual(response.status_code, 302)

class ViewOrderTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
			email="test@ewubd.edu",
			name="test"
		)
        self.user.set_password("Test123")
        self.order = OrderModel.objects.create(buyer=self.user)
        self.orderSchedule = OrderScheduleModel.objects.create(order=self.order)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/company-feed/' + str(self.user.id) + '/view_order'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'view-order'
        response = self.client.get(reverse(url, kwargs = {'pk':self.user.id}))
        self.assertEqual(response.status_code, 302)