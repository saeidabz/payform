from django.urls import path
from .views import UserRegistration, GeneratePdf

urlpatterns = [
    path('yek/', UserRegistration.as_view(), name='register'),
    path('pdf/<int:pk>', GeneratePdf.as_view(), name='pdf'),
]
