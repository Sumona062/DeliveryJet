from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from users.forms import *
from users.models import *

class TestLoginForm(TestCase):
	@classmethod
	def setUp(self):
		self.user = User.objects.create(
			email="test@ewubd.edu",
			name="test"
		)
		self.user.set_password("Test123")
		self.user.save()
	
	def test_login_form_valid_data(self):
		form = LoginForm(data={
			'email': 'test@ewubd.edu',
			'password': 'Test123'
			})

		self.assertTrue(form.is_valid())

	def test_login_form_invalid_data(self):
		form = LoginForm(data={

			})
		self.assertFalse(form.is_valid())

	def test_user_email(self):
		test_email = "test@ewubd.edu"
		self.assertEqual(self.user.email, test_email)
	def test_user_password(self):
		test_password = self.user.password
		self.assertEqual(self.user.password, test_password)

class TestBuyerRegistrationForm(TestCase):
	@classmethod
	def setUp(self):
		self.buyer = User.objects.create(
			email="buyer@ewubd.edu",
			name="buyer"
		)
		self.buyer.set_password("Buyer123")
		self.buyer.is_buyer = True
		self.buyer.save()


	def test_buyer_registration_form_valid_data(self):
		form = BuyerRegistrationForm(data={
			'name': 'buyer123',
			'email': 'buyer123@ewubd.edu',
			'password1': 'asdf_ASDF123',
			'password2': 'asdf_ASDF123', 
			'is_buyer': True
			})
		self.assertTrue(form.is_valid())

	def test_buyer_registration_form_invalid_data(self):
		
		form = BuyerRegistrationForm(data={

			})
		self.assertFalse(form.is_valid())
	def test_buyer_email(self):
		test_email = "buyer@ewubd.edu"
		self.assertEqual(self.buyer.email, test_email)
	def test_buyer_name(self):
		test_name = "buyer"
		self.assertEqual(self.buyer.name, test_name)
	def test_buyer_password(self):
		test_password = self.buyer.password
		self.assertEqual(self.buyer.password, test_password)
	def test_is_buyer(self):
		test_is_buyer = True
		self.assertEqual(self.buyer.is_buyer, test_is_buyer)	

class TestCompanyRegistrationForm(TestCase):
	@classmethod
	def setUp(self):
		self.company = User.objects.create(
			email="company@ewubd.edu",
			name="company"
		)
		self.company.set_password("Company123")
		self.company.is_company = True
		self.company.save()


	def test_company_registration_form_valid_data(self):
		form = CompanyRegistrationForm(data={
			'name': 'company123',
			'email': 'company123@ewubd.edu',
			'password1': 'asdf_ASDF123',
			'password2': 'asdf_ASDF123', 
			'is_company': True
			})
		self.assertTrue(form.is_valid())

	def test_company_registration_form_invalid_data(self):
		
		form = CompanyRegistrationForm(data={

			})
		self.assertFalse(form.is_valid())
	def test_company_email(self):
		test_email = "company@ewubd.edu"
		self.assertEqual(self.company.email, test_email)
	def test_company_name(self):
		test_name = "company"
		self.assertEqual(self.company.name, test_name)
	def test_company_password(self):
		test_password = self.company.password
		self.assertEqual(self.company.password, test_password)
	def test_is_company(self):
		test_is_company = True
		self.assertEqual(self.company.is_company, test_is_company)	

class TestDeliveryManRegistrationForm(TestCase):
	@classmethod
	def setUp(self):
		self.deliveryMan = User.objects.create(
			email="deliveryMan@ewubd.edu",
			name="deliveryMan"
		)
		self.deliveryMan.set_password("deliveryMan123")
		self.deliveryMan.is_DeliveryMan = True
		self.deliveryMan.save()


	def test_deliveryMan_registration_form_valid_data(self):
		form = DeliveryManRegistrationForm(data={
			'name': 'deliveryMan123',
			'email': 'deliveryMan123@ewubd.edu',
			'password1': 'asdf_ASDF123',
			'password2': 'asdf_ASDF123', 
			'is_DeliveryMan': True
			})
		self.assertTrue(form.is_valid())

	def test_deliveryMan_registration_form_invalid_data(self):
		
		form = DeliveryManRegistrationForm(data={

			})
		self.assertFalse(form.is_valid())
	def test_deliveryMan_email(self):
		test_email = "deliveryMan@ewubd.edu"
		self.assertEqual(self.deliveryMan.email, test_email)
	def test_deliveryMan_name(self):
		test_name = "deliveryMan"
		self.assertEqual(self.deliveryMan.name, test_name)
	def test_deliveryMan_password(self):
		test_password = self.deliveryMan.password
		self.assertEqual(self.deliveryMan.password, test_password)
	def test_is_deliveryMany(self):
		test_is_deliveryMan = True
		self.assertEqual(self.deliveryMan.is_DeliveryMan, test_is_deliveryMan)	

class TestCompanyEditProfileForm(TestCase):
	def test_company_edit_profile_form_valid_data(self):
		form = CompanyEditProfileForm(data={
			'location' : 'Malibag,Dhaka,Bangladesh',
			'website' : 'www.company.com',
			'type': 'Book Store',
			'phone': '01711123456',
			})
		self.assertTrue(form.is_valid())

	def test_company_edit_profile_form_invalid_data(self):
		form = CompanyEditProfileForm(data={

			})
		self.assertFalse(form.is_valid())

class TestBuyerEditProfileForm(TestCase):
	def test_buyer_edit_profile_form_valid_data(self):
		form = BuyerEditProfileForm(data={
			'gender': 'Male'
			})
		self.assertTrue(form.is_valid())

	def test_buyer_edit_profile_form_invalid_data(self):
		form = BuyerEditProfileForm(data={

			})
		self.assertFalse(form.is_valid())

class TestDeliveryManEditProfileForm(TestCase):
	def test_delivery_man_edit_profile_form_valid_data(self):
		form = DeliveryManEditProfileForm(data={
			'phone' : '01775698564',
			'documentID': '8678900918',
			'documentType': 'NID'
			})
		self.assertTrue(form.is_valid())

	def test_delivery_man_edit_profile_form_invalid_data(self):
		form = DeliveryManEditProfileForm(data={

			})
		self.assertFalse(form.is_valid())

class TestAccountInformationForm(TestCase):
	@classmethod
	def setUp(self):
		self.user = User.objects.create(
			email="test1@ewubd.edu",
			name="test1"
		)
		self.user.set_password("Test123")
		self.user.save()
	def test_account_information_form_valid_data(self):
		form = AccountInformationForm(data={
			'email': 'test2@ewubd.edu',
			'name': 'test2'
			})
		self.assertTrue(form.is_valid())	
	def test_account_information_form_invalid_data(self):
		form = AccountInformationForm(data={

			})
		self.assertFalse(form.is_valid())

	def test_account_email(self):
		test_email = "test1@ewubd.edu"
		self.assertEqual(self.user.email, test_email)
	def test_account_name(self):
		test_name = "test1"
		self.assertEqual(self.user.name, test_name)

class TestPostProductForm(TestCase):
	def test_post_product_form_valid_data(self):
		form = PostProductForm(data={
			'category': 'food',		
			'name' : 'Burger',
			'price' : 100,
			'availQuantity' : 50
			})
		self.assertTrue(form.is_valid())

	def test_post_product_form_invalid_data(self):
		form = PostProductForm(data={

			})
		self.assertFalse(form.is_valid())

class TestAvailabilityForm(TestCase):
	def test_availability_form_valid_data(self):
		form = AvailabilityForm(data={
			'time': '9am-3pm',
			'Days' :'Monday-Friday',
			'address': 'Rampura,Dhaka',
			'phone': '01811123456'
			})
		self.assertTrue(form.is_valid())

	def test_availability_form_invalid_data(self):
		form = AvailabilityForm(data={

			})
		self.assertFalse(form.is_valid())

class TestPreferredAreaForm(TestCase):
	def test_preferred_area_form_valid_data(self):
		form = PreferredAreaForm(data={
			'time' : '9am-3pm',
			'area': 'Rampura,Dhaka'
			})
		self.assertTrue(form.is_valid())

	def test_preferred_area_form_invalid_data(self):
		form = PreferredAreaForm(data={

			})
		self.assertFalse(form.is_valid())
