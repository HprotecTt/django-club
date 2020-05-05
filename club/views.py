from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    contex = {
        'posts': Post.objects.all()
    }
    return render(request, 'club/home.html', contex)


def about(request):
    return render(request, 'club/about.html', {'title': 'About'})
