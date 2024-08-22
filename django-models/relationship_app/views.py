from django.shortcuts import render, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    
    # Render the list_books.html template with the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Define views for each user role and restrict access based on the user’s role.
def check_role(user, role):
    return user.is_authenticated and user.userprofile.role == role

@user_passes_test(lambda user: check_role (user, "Admin"))
def admin_view(request):
    return HttpResponse("Welcome Admin")

@user_passes_test(lambda user: check_role (user, "Librarian"))
def librarian_view(request):
    return HttpResponse("Welcome Librarian")

@user_passes_test(lambda user: check_role (user, "Librarian"))
def member_view(request):
    return HttpResponse("Welcome Member")