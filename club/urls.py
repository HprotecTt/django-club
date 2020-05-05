from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='club-home'),
    path('about/', views.about, name='club-about'),
]
