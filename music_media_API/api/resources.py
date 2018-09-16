from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from api.models import Note, CustomUser
from django.contrib.auth.models import User
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = CustomUser.objects.all()
        object_class = CustomUser
        fields = ['username', 'musicLikes', 'photo', 'bio', 'userId']
        allowed_methods = ['get', 'post', 'put', 'patch']
        resource_name = 'user'
        excludes = ['email', 'password', 'is_superuser']
        filtering = {
            'username': ALL_WITH_RELATIONS,
            'userId': ALL_WITH_RELATIONS,
            'posts': ALL_WITH_RELATIONS,
        }
        authentication = Authentication()

    def obj_create(self, bundle, request=None, **kwargs):
        username, password = bundle.data['username'], bundle.data['password']
        try:
            bundle.obj = CustomUser.objects.create_user(username, '', password)
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        object_class = Note
        resource_name = 'note'
        fields = ['body', 'userIdPosted', 'musicShared']
        allowed_methods = ['get', 'post', 'put', 'patch']
        authentication = Authentication()
        filtering = {
            'userIdPosted': ALL_WITH_RELATIONS,
        }

    def obj_create(self, bundle, request=None, **kwargs):
        #body, userIdPosted, musicShared = bundle.data['body'], bundle.data['userIdPosted'], bundle.data['musicShared']
        super(ModelResource, self).obj_create(bundle, request=request, **kwargs)
        return bundle