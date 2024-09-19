from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)  # Create a token for the user
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        
        # Generate or get the user's token
        token, created = Token.objects.get_or_create(user=user)
        
        return {
            'user': {
                'username': user.username,
                'bio': user.bio,
                'profile_picture': user.profile_picture.url if user.profile_picture else None,

                },
            'token': token.key  # Return the token as well
        }