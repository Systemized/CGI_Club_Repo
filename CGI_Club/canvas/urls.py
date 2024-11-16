from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    
    ImageListView,
    ImageDetailView,
    ImageCreateView,
    ImageDeleteView,
)
from . import views


urlpatterns = [
    path('', views.home, name='canvas-home'),
    path('about/', views.about, name='canvas-about'),
    path('feed/', PostListView.as_view(), name='canvas-feed'),
    # Posts for Feed Page (Create, update, delete Posts)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    # End Post for Feed Page
    
    path('gallery/', ImageListView.as_view(), name='canvas-gallery'),
    # Images for Gallery Page (Create, delete Images)
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('image/new/', ImageCreateView.as_view(), name='image-create'),
    path('image/<int:pk>/delete', ImageDeleteView.as_view(), name='image-delete'),


    
]