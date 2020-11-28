from django.test import TestCase

# Create your tests here.
from customers.models import Customer


class ModelTestCase(TestCase):
    @classmethod
    def setUp(self):
        # Create a customer
        testuser1 = Customer.objects.create(
            first_name='Kou',
            last_name='Elbehi',
            email='koutheir@gmail.com',
            gender='male',
            company='SeekMake',
            city='RafRaf',
            title='Software Engineer',
        )
        testuser1.save()

