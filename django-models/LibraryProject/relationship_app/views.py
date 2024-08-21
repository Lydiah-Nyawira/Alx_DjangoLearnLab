from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

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
                  
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaded_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_books') # Redirect to a page after login
            else:
                # If authentication fails
                form.add_error(None, 'Invalid username or password')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'logout.html') 

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})          