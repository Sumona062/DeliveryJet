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

class BuyerFeedTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.buyer = BuyerModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/buyer-feed/' + str(self.buyer.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'buyer-feed'
        response = self.client.get(reverse(url, kwargs = {'pk':self.buyer.id}))
        self.assertEqual(response.status_code, 302)

class DeliveryManFeedTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.deliveryMan = DeliveryManModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/deliveryMan-feed/' + str(self.deliveryMan.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'deliveryMan-feed'
        response = self.client.get(reverse(url, kwargs = {'pk':self.deliveryMan.id}))
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

class CompanyEditProfileTestCase(TestCase):

    def test_view_url_exists_at_desired_location_valid_form(self):
        client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        type = "Book Store"
        company = CompanyModel.objects.create(user=user,type=type)
        client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/company-feed/' + str(company.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'company-edit-profile'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 302)

class DeliveryManEditProfileTestCase(TestCase):

    def test_view_url_exists_at_desired_location_valid_form(self):
        client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        documentID = '8678900918'
        documentType = 'NID'
        deliveryMan = DeliveryManModel.objects.create(user=user,documentID=documentID, documentType=documentType)
        client.login(email="test@ewubd.edu", password="Test123")
        url = '/account/deliveryMan-feed/' + str(deliveryMan.id) + '/'
        response = client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'deliveryMan-edit-profile'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 302)

class BuyerEditProfileTestCase(TestCase):

    def test_view_url_exists_at_desired_location_valid_form(self):
        client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        gender = 'Male'
        buyer = BuyerModel.objects.create(user=user,gender=gender)
        client.login(email="test@ewubd.edu", password="Test123")
        url = '/customer/customer-edit-profile'
        response = client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'buyer-edit-profile'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 302)

class DeletePreferredAreaTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.preferredArea = PreferredAreaModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/delete-preferredArea/' + str(self.preferredArea.id) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'delete-preferredArea'
        response = self.client.get(reverse(url, kwargs = {'pk':self.preferredArea.id}))
        self.assertEqual(response.status_code, 302)

class DeleteAvailabilityTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.availability = AvailabilityModel.objects.create(buyer=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/customer/delete-address/' + str(self.availability.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'delete-availability'
        response = self.client.get(reverse(url, kwargs = {'pk':self.availability.id}))
        self.assertEqual(response.status_code, 302)

class AddAvailabilityTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.availability = AvailabilityModel.objects.create(buyer=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/customer/add-address'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'add-availability'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 302)

class AccountSettingsTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.buyer = BuyerModel.objects.create(user=user)
        self.company = CompanyModel.objects.create(user=user)
        self.deliveryMan = DeliveryManModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location_for_buyer(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account-settings/' + str(self.buyer.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name_for_buyer(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'account-settings'
        response = self.client.get(reverse(url, kwargs = {'pk':self.buyer.id}))
        self.assertEqual(response.status_code, 302)

    def test_view_url_exists_at_desired_location_for_company(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account-settings/' + str(self.company.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name_for_company(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'account-settings'
        response = self.client.get(reverse(url, kwargs = {'pk':self.company.id}))
        self.assertEqual(response.status_code, 302)

    def test_view_url_exists_at_desired_location_for_delieveryMan(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/account-settings/' + str(self.deliveryMan.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name_for_deliveryMan(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'account-settings'
        response = self.client.get(reverse(url, kwargs = {'pk':self.deliveryMan.id}))
        self.assertEqual(response.status_code, 302)

class EditProductTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.company = CompanyModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/edit-product/' + str(self.company.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'edit-product'
        response = self.client.get(reverse(url, kwargs = {'pk':self.company.id}))
        self.assertEqual(response.status_code, 302)

class DeleteProductTestCase (TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        user = authenticate(email="test@ewubd.edu", password="Test123")
        self.company = CompanyModel.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = '/delete-product/' + str(self.company.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

    def test_view_url_accessible_by_name(self):
        self.client.login(email="test@ewubd.edu", password="Test123")
        url = 'delete-product'
        response = self.client.get(reverse(url, kwargs = {'pk':self.company.id}))
        self.assertEqual(response.status_code, 302)

class PostProductTestCase (TestCase):
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
        url = 'post-product'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 302)

