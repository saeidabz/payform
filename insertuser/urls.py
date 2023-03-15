from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import sample_view

urlpatterns = [
   path('sample/', sample_view, name="sample_view"),
]
