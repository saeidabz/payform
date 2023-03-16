from django.urls import path

from . import views

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
    path('insert_profile/', views.insert_profile, name='insert_profile'),
    path('success/<int:user_id>/', views.success_view, name='success'),

]