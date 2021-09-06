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

    #def test_about_url_is_resolved(self):
    #    url = reverse('about')
    #    self.assertEqual(resolve(url).func, about)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_company_feed_url_is_resolved(self):
        url = reverse('company-feed', args = ['1'])
        self.assertEqual(resolve(url).func, company_feed)

    def test_buyer_feed_url_is_resolved(self):
        url = reverse('buyer-feed', args = ['1'])
        self.assertEqual(resolve(url).func, buyer_feed)

    def test_delivary_man_feed_url_is_resolved(self):
        url = reverse('deliveryMan-feed', args = ['1'])
        self.assertEqual(resolve(url).func, deliveryMan_feed)

    def test_company_feed_category_url_is_resolved(self):
        url = reverse('company-feed-category', args = ['1', 'Book Store'])
        self.assertEqual(resolve(url).func, company_feed_category)

    def test_company_edit_profile_url_is_resolved(self):
        url = reverse('company-edit-profile')
        self.assertEqual(resolve(url).func, company_edit_profile)

    def test_buyer_edit_profile_url_is_resolved(self):
        url = reverse('buyer-edit-profile')
        self.assertEqual(resolve(url).func, buyer_edit_profile)

    def test_delivery_man_edit_profile_url_is_resolved(self):
        url = reverse('deliveryMan-edit-profile')
        self.assertEqual(resolve(url).func, deliveryMan_edit_profile)

    def test_add_availability_url_is_resolved(self):
        url = reverse('add-availability')
        self.assertEqual(resolve(url).func, add_availability)

    def test_delete_availability_url_is_resolved(self):
        url = reverse('delete-availability', args = ['1'])
        self.assertEqual(resolve(url).func, delete_availability)

    def test_delete_preferred_area_url_is_resolved(self):
        url = reverse('delete-preferredArea', args = ['1'])
        self.assertEqual(resolve(url).func, delete_preferredArea)

    def test_post_product_url_is_resolved(self):
        url = reverse('post-product')
        self.assertEqual(resolve(url).func, post_product)

    def test_edit_product_url_is_resolved(self):
        url = reverse('edit-product', args = ['1'])
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_product_url_is_resolved(self):
        url = reverse('delete-product', args = ['1'])
        self.assertEqual(resolve(url).func, delete_product)

    def test_account_settings_url_is_resolved(self):
        url = reverse('account-settings', args = ['1'])
        self.assertEqual(resolve(url).func, account_settings)












