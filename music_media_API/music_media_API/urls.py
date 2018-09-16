"""music_media_API URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from api.resources import *
from tastypie.api import Api

from django.http import HttpResponse


def empty_view(request):
    return HttpResponse("Empty View")

v1_api = Api(api_name='v1')
note_resource = NoteResource()
user_resource = UserResource()
v1_api.register(note_resource)
v1_api.register(user_resource)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url('', empty_view, name='empty_view'),
]

