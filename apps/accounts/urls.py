from django.urls import path

from .views import submit_form, insert_profile

urlpatterns = [
    path('submit/', submit_form, name='submit_form'),
    path('insert_profile/', insert_profile, name='insert_profile'),
    # path('generate_pdf/<int:user_id>/', generate_pdf, name='generate_pdf'),
    # path('insert_profile/pdf/', generate_pdf, name="pdf" ),
]