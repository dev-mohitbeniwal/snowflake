from django.conf.urls import url, include
from rest_framework import routers
from cohort import views
from .api import *


router = routers.DefaultRouter()
router.register(r'badge', views.BadgeViewSet, basename='Badge')
router.register(r'post', views.PostViewSet, basename='Post')
router.register(r'developer', views.DeveloperViewSet, basename='Developer')


urlpatterns = [
    url('', include(router.urls)),
    url(r'^index', views.index),
    url(r'badge/$', BadgeAPI.as_view()),
    url(r'badge/(?P<pk>[a-zA-Z0-9-]+)/$', BadgeAPI.as_view()),
    url(r'post/$', PostAPI.as_view()),
    url(r'post/(?P<pk>[a-zA-Z0-9-]+)/$', PostAPI.as_view()),
    url(r'developer/$', DeveloperAPI.as_view()),
    url(r'developer/(?P<pk>[a-zA-Z0-9-]+)/$', DeveloperAPI.as_view())
]