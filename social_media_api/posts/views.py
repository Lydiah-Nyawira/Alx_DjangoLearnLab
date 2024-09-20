from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to edit this post.")
        serializer.save()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to edit this comment.")
        serializer.save()

class UserFeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class LikeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, pk=None):
        # Use get_object_or_404 to fetch the post
        post = get_object_or_404(Post, pk=pk)
        
        # Use get_or_create to check for existing like
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new like
        like = Like.objects.create(user=request.user, post=post)

        # create_notification(request.user, post.author, 'liked your post', post)
        Notification.objects.create(
            actor=request.user,
            recipient=post.author,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        post = Post.objects.get(pk=pk)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)