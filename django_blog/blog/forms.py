from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget

# Extend Django's user creation form for the registration form to include additional fields
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# Develop a form for the Post model using Django’s ModelForm to handle the creation and updating of blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
# CommentForm using Django’s ModelForm to facilitate comment creation and updating.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for tag input
        }
