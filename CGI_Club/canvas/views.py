from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
    return render(request, 'canvas/home.html')

def about(request):
    return render(request, 'canvas/about.html')

def gallery(request):
    return render(request, 'canvas/gallery.html')

def feed(request):
    context = {
            'posts': Post.objects.all()
    }
    return render(request, 'canvas/feed.html', context)