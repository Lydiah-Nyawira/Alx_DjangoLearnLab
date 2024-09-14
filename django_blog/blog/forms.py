from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Extend Django's user creation form for the registration form to include additional fields
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')