from django.contrib import admin
from django.urls import path, include
from pss_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pss_app.urls')),
    path("accounts/", include("allauth.urls")),
    ]
