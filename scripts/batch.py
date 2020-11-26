import csv  

from customers.models import Customer


def run():
    fhand = open('customers/customers.csv')
    reader = csv.reader(fhand)
    next(reader)  

    Customer.objects.all().delete()
    

    

    for row in reader:
        print(row)

        p, created = Customer.objects.get_or_create(first_name=row[1],last_name=row[2],email=row[3],gender=row[4],company=row[5],city=row[6],title=row[7])
