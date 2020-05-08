from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, JoinListView, UserListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='club-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # pk means primary key
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('join/post=<int:pk>/', JoinListView.as_view(), name='join-by-post'),
    path('join/user=<str:username>/',
         JoinListView.as_view(), name='join-by-user'),
    path('users/', UserListView.as_view(), name='club-users'),
    path('about/', views.about, name='club-about'),
]
