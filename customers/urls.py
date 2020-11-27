from django.urls import path

from customers.views import CustomerAPIView, CustomerDetailView

urlpatterns = [
    path('customers/<int:pk>/', CustomerDetailView.as_view()),
    path('customers', CustomerAPIView.as_view()),
]
