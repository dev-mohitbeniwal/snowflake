from rest_framework_mongoengine import viewsets
from .serializer import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Success')


class BadgeViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BadgeSerializer

    def get_queryset(self):
        return Badge.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class DeveloperViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = DeveloperSerializer

    def get_queryset(self):
        return Developer.objects.all()