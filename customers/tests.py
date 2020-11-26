from django.test import TestCase

# Create your tests here.
from customers.models import Customer


class ModelTestCase(TestCase):

    def setUp(self):
        self.customer_name = "Kou"
        self.customer = Customer(name=self.customer_name)

    def test_model_can_create_a_customer(self):
        old_count = Customer.objects.count()
        self.Customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)