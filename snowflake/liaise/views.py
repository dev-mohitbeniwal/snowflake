from rest_framework_mongoengine import viewsets
from .serializer import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Success')


class TagViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()


class VoteViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = VoteSerializer

    def get_queryset(self):
        return Vote.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()