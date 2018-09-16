from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from tastypie import fields

class Note(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    userIdPosted = models.CharField(max_length=80, default=0)
    musicShared = models.CharField(max_length=80, default=0)

    def __str__(self):
            return '%s %s' % (self.title, self.body)

class CustomUser(AbstractUser):
    # followers, following, liked artists, genres
    musicLikes = models.TextField(default='')
    photo = models.CharField(max_length=80, default=0)
    bio = models.TextField()
    userId = models.CharField(max_length=80, default=0)
    posts = models.ManyToManyField(Note)

    def __str__(self):
        return self.username