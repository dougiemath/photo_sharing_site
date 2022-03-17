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
    UserPostList,
    UserImageDetails,
    AddCommentView,
    LikeView,
)

app_name = 'image'

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    
    path('', ImageFeedView.as_view(), name='list'),

    path('image/<int:pk>/', ImageDetailView.as_view(), name='detail'),

    path('tag/<slug:tag>/', ImageTagListView.as_view(), name='tag'),

    path('image/create/', ImageCreateView.as_view(), name='create'),

    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='update'),

    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='delete'),

    path('image/user_feed/', UserPostList.as_view(), name="user_feed"), 

    path('image/<int:pk>/user_image_details', UserImageDetails.as_view(), name='user_image_details'),

    path('photo/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment'),

    path('search_results', views.search_results, name='search_results'),

    path('like/<int:pk>', LikeView, name='like_post')
]
