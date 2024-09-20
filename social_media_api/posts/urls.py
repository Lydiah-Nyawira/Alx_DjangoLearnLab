from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedViewSet, LikeCreateAPIView, LikeDestroyAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedViewSet.as_view({'get': 'list'}), name='user-feed'),
    path('<int:pk>/like/', LikeCreateAPIView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', LikeDestroyAPIView.as_view(), name='unlike-post'),
    ]