from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, UserLoginSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    
# Follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            request.user.following.add(user_to_follow)
            return Response({'message': 'Successfully followed.'}, status=200)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)

# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({'message': 'Successfully unfollowed.'}, status=200)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)