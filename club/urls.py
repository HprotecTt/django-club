from django.urls import path

from . import views
from .views import (AttendListView, ClubDetailView, ClubListView, JoinListView,
                    PostCreateView, PostDeleteView, PostDetailView,
                    PostListView, PostUpdateView, UserAttendListView,
                    UserJoinListView, UserListView, UserPostListView,
                    attendCreate, joinCreate)

urlpatterns = [
    path('', PostListView.as_view(), name='club-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # pk means primary key
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('join/new/?post_id=<int:pk>/', joinCreate, name='join-create'),
    path('join/?post_id=<int:pk>/', JoinListView.as_view(), name='join-by-post'),
    path('join/user/',
         UserJoinListView.as_view(), name='join-by-user'),
    path('attend/new/?club_id=<int:pk>/', attendCreate, name='attend-create'),
    path('attend/?club_id=<int:pk>/',
         AttendListView.as_view(), name='attend-by-club'),
    path('attend/user/',
         UserAttendListView.as_view(), name='attend-by-user'),
    path('clubs/', ClubListView.as_view(), name='club-list'),
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club-detail'),
    path('users/', UserListView.as_view(), name='club-users'),
    path('about/', views.about, name='club-about'),
]
