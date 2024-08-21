from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Book, Library

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