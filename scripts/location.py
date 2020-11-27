import requests

from customers.models import Customer


def run():
    customers = Customer.objects.all()
    for customer in customers:
        address = customer.city
        api_response = requests.get(
            'https://nominatim.openstreetmap.org/search.php?q={0}&polygon_geojson=1&format=jsonv2'.format(address))
        loaded_json = api_response.json()

        if api_response.status_code == 200:
            if len(loaded_json) > 0:
                updated = Customer.objects.filter(pk=customer.pk).update(longitude=loaded_json[0]['lon'],
                                                                         latitude=loaded_json[0]['lat'])
                print(updated)
