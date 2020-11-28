from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from customers.views import CustomerAPIView, CustomerDetailView

""" This is swagger's configuration ."""
schema_view = get_schema_view(
    openapi.Info(
        title="Oowlish API Challenge",
        default_version='v1',
        description="This API is dedicated to oowlish in corporation with Aiesec Brazil",
        contact=openapi.Contact(email="koutheir.elbehi@etudiant-isi.utm.tn"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

""" Here we define urls of our endpoints"""
urlpatterns = [
    path('customers/<int:pk>/', CustomerDetailView.as_view()),
    path('customers/', CustomerAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
