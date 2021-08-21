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
    def setUpTestData(self):
        user = authenticate(email="test@ewubd.edu", password="Test123")
        name = "Test Product"
        self.product = ProductModel.objects.create(user=user, name=name )

    def test_productmodel_creation(self):
        self.assertTrue(isinstance(self.product, ProductModel))
        self.assertEqual(self.product.getProductName(), self.product.name)
        self.assertEqual(self.product.getCompany(), self.product.user)
