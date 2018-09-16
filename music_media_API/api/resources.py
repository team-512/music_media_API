from tastypie.resources import ModelResource
from api.models import Note, CustomUser, Artist, Album, Song
from django.contrib.auth.models import User
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = CustomUser.objects.all()
        object_class = CustomUser
        fields = ['username', 'email']
        allowed_methods = ['get', 'post']
        resource_name = 'user'
        excludes = ['email', 'password', 'is_superuser']
        authentication = Authentication()

    def obj_create(self, bundle, request=None, **kwargs):
        username, password = bundle.data['username'], bundle.data['password']
        try:
            bundle.obj = CustomUser.objects.create_user(username, '', password)
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle

class ArtistResource(ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        resource_name = 'artist'

class AlbumResource(ModelResource):
    artist = fields.ForeignKey(ArtistResource, 'artist')

    class Meta:
        queryset = Album.objects.all()
        resource_name = 'album'

class SongResource(ModelResource):
    artist = fields.ForeignKey(ArtistResource, 'artist')
    album = fields.ForeignKey(AlbumResource, 'album')

    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization() # remove when deploying