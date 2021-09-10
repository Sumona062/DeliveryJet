from django.test import TestCase
from order.forms import *
from order.models import *

class TestOrderForm(TestCase):
	def test_order_form_valid_data(self):
		form = OrderForm(data={
			
			})
		self.assertTrue(form.is_valid())
