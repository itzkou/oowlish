import requests

from customers.models import Customer

""" This script is linked to RunScript and executed using manage.py , it allows us to load data from a CSV file into the database"""


def run():
    customers = Customer.objects.all()  # Retrieveing customers
    for customer in customers:  # Looping through the data
        address = customer.city  # For each customer we read his city/address
        api_response = requests.get(
            'https://nominatim.openstreetmap.org/search.php?q={0}&polygon_geojson=1&format=jsonv2'.format(
                address))  # API call using Openstreetmap to convert address into lat/lon
        loaded_json = api_response.json()  # Converting the api response into a Json

        if api_response.status_code == 200:  # Safety check
            if len(loaded_json) > 0:  # IndexOutOfBound Protection
                updated = Customer.objects.filter(pk=customer.pk).update(longitude=loaded_json[0]['lon'],
                                                                         latitude=loaded_json[0][
                                                                             'lat'])  # Updating each row with proper longitude and latitude
                print(
                    updated)  # 'updated' is a Boolean indicator , if update ==1 an update operation worked else an update operation failed
