from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


def home(request):
    contex = {
        'posts': Post.objects.all()
    }
    return render(request, 'club/home.html', contex)


class PostListView(ListView):
    model = Post
    template_name = 'club/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # inverse order as date_posted
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'club/about.html', {'title': 'About'})
