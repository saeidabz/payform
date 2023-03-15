from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.hello_world, name='home'),
    # add more URLs here as needed
]
