from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from customers.models import Customer
from .serializers import CustomerSerializer


@swagger_auto_schema(operation_summary="Retrieve a list of customers", query_serializer=CustomerSerializer)
class CustomerAPIView(generics.ListAPIView):
    """Retrieve a list of customers."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@swagger_auto_schema(operation_summary="Retrieve a customer", query_serializer=CustomerSerializer)
class CustomerDetailView(generics.RetrieveAPIView):
    """Retrieve a customer."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
