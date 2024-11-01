from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='canvas-home'),
    path('about/', views.about, name='canvas-about'),
    path('gallery/', views.gallery, name='canvas-gallery'),
    path('feed/', views.feed, name='canvas-feed'),
    
]