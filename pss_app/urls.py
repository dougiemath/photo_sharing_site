from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ="homepage"),
    path('register/', views.register, name ="register"),
    path('', include("django.contrib.auth.urls"))
]
