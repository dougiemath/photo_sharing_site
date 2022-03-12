# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import(
    ImageFeedView,
)

app_name = 'image'

urlpatterns = [
    # registration page
    path('register/', views.register, name ="register"),
    path('', include("django.contrib.auth.urls")),
    
    # password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name="password_reset_done"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name="password_reset_complete"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name="password_reset_confirm"),

    path('', ImageFeedView.as_view(), name='list'),
]
