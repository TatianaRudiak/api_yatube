from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)

comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', obtain_auth_token),
    path(
        'api/v1/posts/<int:post_id>/comments/',
        comments_list,
        name='comments-list'
    ),
    path(
        'api/v1/posts/<int:post_id>/comments/<int:comment_id>/',
        comment_detail,
        name='comment-detail'
    )
]
