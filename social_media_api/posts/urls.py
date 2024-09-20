from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

like_viewset = LikeViewSet.as_view({
    'post': 'create',   # Handle POST request to like a post
    'delete': 'destroy'  # Handle DELETE request to unlike a post
})


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedViewSet.as_view({'get': 'list'}), name='user-feed'),
    path('posts/<int:pk>/like/', like_viewset, name='post-like'),   # URL for liking a post
    path('posts/<int:pk>/unlike/', like_viewset, name='post-unlike'),  # URL for unliking a post
]