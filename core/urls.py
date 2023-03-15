from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static #add this
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("account/", include("apps.accounts.urls")),             # UI Kits Html files
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),             # UI Kits Html files
    path('', include("users.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
