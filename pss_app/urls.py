# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # registration page
    path('register/', views.register, name ="register"),
    path('', include("django.contrib.auth.urls")),
    path('', views.index, name='home'),

    # view feed
    path('feed/', views.PostList.as_view(), name="feed"),
    # view user images only
    path('user_feed/', views.UserPostList.as_view(), name="user_feed"),
    
    # password reset

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name="password_reset_done"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name="password_reset_complete"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name="password_reset_confirm"),

]