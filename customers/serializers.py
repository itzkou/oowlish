from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model customer into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the customer fields."""
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email','gender','company','title','longitude','latitude')
