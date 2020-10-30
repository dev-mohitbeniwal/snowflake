from django.conf.urls import url, include
from rest_framework import routers
from liaise import views
from .api import *


router = routers.DefaultRouter()
router.register(r'tag', views.TagViewSet, basename='Tag')
router.register(r'vote', views.VoteViewSet, basename='Vote')
router.register(r'comment', views.CommentViewSet, basename='Comment')
router.register(r'answer', views.AnswerViewSet, basename='Answer')
router.register(r'question', views.QuestionViewSet, basename='Question')


urlpatterns = [
    url('', include(router.urls)),
    url(r'^index', views.index),
    url(r'tag/$', TagAPI.as_view()),
    url(r'tag/(?P<pk>[a-zA-Z0-9-]+)/$', TagAPI.as_view()),
    url(r'vote/$', VoteAPI.as_view()),
    url(r'vote/(?P<pk>[a-zA-Z0-9-]+)/$', VoteAPI.as_view()),
    url(r'comment/$', CommentAPI.as_view()),
    url(r'comment/(?P<pk>[a-zA-Z0-9-]+)/$', CommentAPI.as_view()),
    url(r'answer/$', AnswerAPI.as_view()),
    url(r'answer/(?P<pk>[a-zA-Z0-9-]+)/$', AnswerAPI.as_view()),
    url(r'question/$', QuestionAPI.as_view()),
    url(r'question/(?P<pk>[a-zA-Z0-9-]+)/$', QuestionAPI.as_view())
]