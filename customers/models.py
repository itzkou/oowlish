from django.db import models


# Create your models here.


class Customer(models.Model):
    """This class defines our customer model."""

    first_name = models.TextField(max_length=100, default=None)
    last_name = models.TextField(max_length=100, default=None)
    email = models.TextField(max_length=100, default=None)
    gender = models.TextField(max_length=100, default=None)
    company = models.TextField(max_length=255, default=None)
    city = models.TextField(max_length=255, default=None)
    title = models.TextField(max_length=255, default=None)
    ''' GeoLocation'''
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')

    def __str__(self):
        return self.first_name
