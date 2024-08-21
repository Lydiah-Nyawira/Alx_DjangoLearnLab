from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    
    # Render the list_books.html template with the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'