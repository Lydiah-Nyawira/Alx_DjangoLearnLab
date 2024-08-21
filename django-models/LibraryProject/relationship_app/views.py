from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
# Function_based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class_based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'libary_detail.html'
    context_object_name = 'library'

# Implementing User Authentication
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
                  
# Custom registration view
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Custom logout view
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('login')  # Redirect to login page after logout