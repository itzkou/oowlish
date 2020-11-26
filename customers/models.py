from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.TextField(max_length=100,default=None)
    last_name = models.TextField(max_length=100,default=None)
    email = models.TextField(max_length=100,default=None)
    gender = models.TextField(max_length=100,default=None)
    company = models.TextField(max_length=255,default=None)
    city = models.TextField(max_length=255,default=None)
    title = models.TextField(max_length=255,default=None)


    def __str__(self):
        return self.first_name
