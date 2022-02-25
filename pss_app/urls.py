# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.index, name ="homepage"),
    path('register/', views.register, name ="register"),
    path('', include("django.contrib.auth.urls")),
    # path('feed/', views.feed, name ="feed"),
    path('', views.PostList.as_view(), name='home'),

    # password reset

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name="password_reset_done"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name="password_reset_complete"),
]
