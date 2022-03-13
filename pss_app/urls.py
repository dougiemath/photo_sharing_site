# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import(
    ImageFeedView,
    ImageDetailView,
    ImageTagListView,
    ImageCreateView,
    ImageUpdateView,
    ImageDeleteView,
    CustomLoginView,
    UserPostList,
    UserImageDetails,
)

app_name = 'image'

urlpatterns = [
    # registration page
    path('register/', views.register, name ="register"),
    path('', include("django.contrib.auth.urls")),
    
    # login
    path('login/', CustomLoginView.as_view(), name='login'),

    # password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name="password_reset_done"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name="password_reset_complete"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name="password_reset_confirm"),

    path('', ImageFeedView.as_view(), name='list'),

    path('image/<int:pk>/', ImageDetailView.as_view(), name='detail'),

    path('tag/<slug:tag>/', ImageTagListView.as_view(), name='tag'),

    path('image/create/', ImageCreateView.as_view(), name='create'),

    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='update'),

    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='delete'),

    path('image/user_feed/', UserPostList.as_view(), name="user_feed"), 

    path('image/<int:pk>/user_image_details', UserImageDetails.as_view(), name='user_image_details'),


]
