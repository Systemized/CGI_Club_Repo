from django.shortcuts import render
# Create your views here.

posts = [
    {
    "author": "James Games",
    "title" : "Blog Post",
    "content":"Hello World",
    "date_posted":"11/10/2020"
    }, 
    {
    "author": "Corey James",
    "title" : "Blog Post 2",
    "content":"Hello Worlds",
    "date_posted":"11/11/2020"
    },
]

def home(request):
    context = {
            'posts': posts
    }
    return render(request, 'canvas/home.html', context)

def about(request):
    return render(request, 'canvas/about.html')

def gallery(request):
    return render(request, 'canvas/gallery.html')