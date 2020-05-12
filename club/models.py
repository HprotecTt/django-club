from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


# Activity
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(
        default='ZUCC Univercity Library', max_length=100)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user is deleted, delete the post as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # use it as redirect
    # reverse will return the full path as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# Join an activity
class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} -> {self.post.title}'


# Club
class Club(models.Model):
    president = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(
        default='ZUCC Univercity Science Building No.4', max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Attend a club
class Attend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_attended = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} -> {self.club.title}'
