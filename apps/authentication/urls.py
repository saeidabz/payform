# from django.urls import path
# from .views import login_view, register_user

# urlpatterns = [
#     path('login/', login_view, name="login"),
#     path('register/', register_user, name="register"),
# ]

from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import login_view, register_user, insert_user

urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('register/', register_user, name='register'),
    # path('insert_user/', insert_user, name='insert_user'),
    # # path('/pdf_download/<str:username>/', download_pdf, name = 'download_pdf'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]


