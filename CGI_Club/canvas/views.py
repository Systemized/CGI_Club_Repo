from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Image
# Create your views here.


def home(request):
    return render(request, 'canvas/home.html')

def about(request):
    return render(request, 'canvas/about.html')


# ------------------------------    FEED/POSTS    ------------------------------

def feed(request):
    context = {
            'posts': Post.objects.all()
    }
    return render(request, 'canvas/feed.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'canvas/feed.html' # <app>/<model>_<viewtype>.html (in this case, it will be (canvas/Post_list) originally)
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
     
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/feed'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# ------------------------------    GALLERY/IMAGES    ------------------------------
def gallery(request):
    context = {
            'images': Image.objects.all()
    }
    return render(request, 'canvas/gallery.html', context)

class ImageListView(ListView):
    model = Image
    template_name = 'canvas/gallery.html'
    context_object_name = 'images'
    ordering = ['-date_posted']

class ImageDetailView(DetailView):
    model = Image

class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['title', 'image'] # IDK if i plan to add content to field. If i do, will need to update models and make migrations
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/gallery'
    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False
