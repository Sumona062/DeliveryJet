from django.test import TestCase, Client, SimpleTestCase
from users.models import *
from django.db import models
from django.urls import reverse, resolve
from users.views import *

# Create your tests here.

class BuyerModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.buyer = BuyerModel.objects.create(user=user)

    def test_buyermodel_creation(self):
        self.assertTrue(isinstance(self.buyer, BuyerModel))
        self.assertEqual(self.buyer.getBuyer(), self.buyer.user)

class DeliveryManModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.deliveryMan = DeliveryManModel.objects.create(user=user)

    def test_buyermodel_creation(self):
        self.assertTrue(isinstance(self.deliveryMan, DeliveryManModel))
        self.assertEqual(self.deliveryMan.getDeliveryMan(), self.deliveryMan.user)

class CompanyModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.company = CompanyModel.objects.create(user=user)

    def test_companymodel_creation(self):
        self.assertTrue(isinstance(self.company, CompanyModel))
        self.assertEqual(self.company.getCompany(), self.company.user)

class ProductModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        name = "Test Product"
        self.product = ProductModel.objects.create(user=user, name=name )

    def test_productmodel_creation(self):
        self.assertTrue(isinstance(self.product, ProductModel))
        self.assertEqual(self.product.getProductName(), self.product.name)
        self.assertEqual(self.product.getCompany(), self.product.user)

class AvailabilityModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        buyer = authenticate(email="test@ewubd.edu", password="Test123")
        address = "Rampura,Dhaka"
        phone = "01711567890"
        self.availability = AvailabilityModel.objects.create(buyer=buyer, address=address, phone = phone )

    def test_availabilitymodel_creation(self):
        self.assertTrue(isinstance(self.availability, AvailabilityModel))
        self.assertEqual(self.availability.getBuyer(), self.availability.buyer)
        self.assertEqual(self.availability.getAddress(), self.availability.address)
        self.assertEqual(self.availability.getPhone(), self.availability.phone)

class PreferredAreaModelTestCase (TestCase):
    @classmethod
    def setUp(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        area = "Rampura,Dhaka"
        time = "9am-3pm"
        self.preferredArea = PreferredAreaModel.objects.create(user=user, area=area, time = time )

    def test_preferredAreamodel_creation(self):
        self.assertTrue(isinstance(self.preferredArea, PreferredAreaModel))
        self.assertEqual(self.preferredArea.getUser(), self.preferredArea.user)
        self.assertEqual(self.preferredArea.getArea(), self.preferredArea.area)
        self.assertEqual(self.preferredArea.getTime(), self.preferredArea.time)

