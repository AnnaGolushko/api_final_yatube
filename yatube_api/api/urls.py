from django.urls import include, path
from rest_framework import routers

from api.views import (CommentViewSet, GroupViewSet, PostViewSet,
                       UserViewSet, FollowViewSet)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet, basename='users')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet,
                basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
