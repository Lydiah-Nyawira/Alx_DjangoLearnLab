from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError

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
    
class LikeCreateAPIView(CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        
        # Check if the user has already liked the post
        if Like.objects.filter(user=self.request.user, post=post).exists():
            raise ValidationError("You already liked this post.")

        # Create the like
        like = serializer.save(user=self.request.user, post=post)

        # Create a notification
        Notification.objects.create(
            actor=self.request.user,
            recipient=post.author,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

        return like

class LikeDestroyAPIView(DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return get_object_or_404(Like, user=self.request.user, post=post)