from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from api.managers import AlbumManager, SongManager
from tastypie import fields

class Music(models.Model):
    title = models.CharField(max_length=80)
    genre = models.CharField(max_length=20)
    
class CustomUser(AbstractUser):
    # followers, following, liked artists, genres
    artists = models.ManyToManyField(Music)
    photo = models.ImageField()
    bio = models.TextField()
    userId = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

class Artist(Music):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Album(Music):
    aartist = models.ManyToManyField(Artist, blank=True)
    release_date = models.DateField()
    objects = AlbumManager()

    def __str__(self):
        return self.title

class Song(Music):
    sartist = models.ManyToManyField(Artist, blank=True)
    album = models.ManyToManyField(Album, blank=True)
    objects = SongManager()

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    userPosted = models.ForeignKey(CustomUser)
    sharedMusic = models.ForeignKey(Music)

    def __str__(self):
            return '%s %s %s' % (self.title, self.body, self.sharedMusic.title)
