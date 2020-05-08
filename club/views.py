from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Join
import logging

# Create your views here.

# Get an instance of a logger
logger = logging.getLogger('django')


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


class UserPostListView(ListView):
    model = Post
    template_name = 'club/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        # kwargs.get : get parameter from url
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # default template_name =  <app>/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'location', 'date_start', 'date_end']

    # set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check user permission
    def dispatch(self, request, *args, **kwargs):
        # check user role
        if not request.user.profile.role is 1:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'location', 'date_start', 'date_end']

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


@login_required
def joinCreate(request, pk):
    context = {}
    join = Join()
    post = get_object_or_404(Post, pk=pk)
    count = len(Join.objects.filter(user=request.user, post=post))
    logger.debug(f'count ======== {count}')
    if count is 0:
        is_joined = False
        join.user = request.user
        join.post = post
        join.save()
    else:
        is_joined = True

    context = {
        'post_title': post.title,
        'username': request.user.username,
        'is_joined': is_joined
    }

    return render(request, 'club/join_create.html', context)


# Join List filter by post
class JoinListView(LoginRequiredMixin, ListView):
    model = Join
    template_name = 'club/join_home.html'
    context_object_name = 'joins'
    paginate_by = 5

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return Join.objects.filter(post=post).order_by('-date_joined')


# Join List filter by user
class UserJoinListView(LoginRequiredMixin, ListView):
    model = Join
    template_name = 'club/join_by_user.html'
    context_object_name = 'joins'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return Join.objects.filter(user=user).order_by('-date_joined')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'club/users.html'
    context_object_name = 'users'
    paginate_by = 8
