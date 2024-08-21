from django.shortcuts import render
from .models import Book, Library
from django.http import HttpResponse
from django.views.generic import DetailView

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    
    # Create a plain text response with book titles and authors
    response_text = "List of Books:\n"
    for book in books:
        response_text += f"{book.title} by {book.author.name}\n"
    
    return HttpResponse(response_text, content_type='text/plain')

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'