# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # registration page
    path('register/', views.register, name ="register"),
    path('', include("django.contrib.auth.urls")),

    # view feed
    path('feed/', views.PostList.as_view(), name="feed"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='image_details'),
    # view user images only
    path('user_feed/', views.UserPostList.as_view(), name="user_feed"),
    
    # password reset

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name="password_reset_done"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name="password_reset_complete"),

]
