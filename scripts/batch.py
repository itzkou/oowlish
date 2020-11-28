import csv

from customers.models import Customer

""" This script is linked to RunScript and executed using manage.py , it allows us to load data from a CSV file into the database"""


def run():
    fhand = open('customers/customers.csv') # Opening CSV file
    reader = csv.reader(fhand) # Defining a reader
    next(reader)

    Customer.objects.all().delete() # Clearing the database before adding data

    for row in reader: # Looping through CSV file and creating customer object in Database
        customer, created = Customer.objects.get_or_create(first_name=row[1], last_name=row[2], email=row[3],
                                                           gender=row[4],
                                                           company=row[5], city=row[6], title=row[7])
        print(customer, created) # 'created' is Boolean check to see if the operation is successful
