from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from api.managers import SongManager
from tastypie import fields

class Song(models.Model):
    title = models.CharField(max_length=80)
    spotifyId = models.PositiveIntegerField(default=0)
    appleMusicId = models.PositiveIntegerField(default=0)
    objects = SongManager()

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    userIdPosted = models.PositiveIntegerField(default=0)
    sharedMusic = models.ForeignKey(Song)
    
    def __str__(self):
            return '%s %s %s' % (self.title, self.body, self.sharedMusic.title)
    
class CustomUser(AbstractUser):
    # followers, following, liked artists, genres
    musicLikes = models.TextField(default='')
    photo = models.ImageField()
    bio = models.TextField()
    userId = models.PositiveIntegerField(default=0)
    posts = models.ManyToManyField(Note)

    def __str__(self):
        return self.username
