from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from api.managers import AlbumManager, SongManager

class CustomUser(AbstractUser):
    # followers, following, liked artists, genres
    artists = models.TextField()

    def __str__(self):
        return self.username

class Artist(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    release_date = models.DateField()
    objects = AlbumManager()

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    objects = SongManager()

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return '%s %s' % (self.title, self.body)
