from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
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
    
    path('gallery/', views.gallery, name='canvas-gallery'),
    # Images for Gallery Page (Create, delete Images)
    

    
]