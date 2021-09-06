from django.test import TestCase
from order.models import *
from django.db import models
from django.urls import reverse, resolve
from order.views import *

# Create your tests here.

class OrderModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.order = OrderModel.objects.create(buyer=user)

    def test_ordermodel_creation(self):
        self.assertTrue(isinstance(self.order, OrderModel))
        self.assertEqual(self.order.getBuyer(), self.order.buyer)

class OrderScheduleModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.order = OrderModel.objects.create(buyer=user)
        self.orderSchedule = OrderScheduleModel.objects.create(order=self.order)

    def test_ordermodel_creation(self):
        self.assertTrue(isinstance(self.orderSchedule, OrderScheduleModel))
        self.assertEqual(self.orderSchedule.getOrder(), self.orderSchedule.order)

