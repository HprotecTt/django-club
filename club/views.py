from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.


def home(request):
    contex = {
        'posts': Post.objects.all()
    }
    return render(request, 'club/home.html', contex)


class PostListView(ListView):
    model = Post
    template_name = 'club/home.html'
    context_object_name = 'posts'
    # inverse order as date_posted
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    # default template_name =  <app>/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check if this post is wirten by this user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # default template_name =  <app>/<model>_<viewtype>.html
    # redirect to '/' after delete is success
    success_url = '/'

    # check if this post is wirten by this user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'club/about.html', {'title': 'About'})
