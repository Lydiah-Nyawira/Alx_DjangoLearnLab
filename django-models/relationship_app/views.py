from django.http import HttpResponse
from .models import Book

# Create your views here.
# function-based view
def list_books(request):
    books = Book.objects.all()
    response_text = "List of Books:\n\n"
    for book in books:
        response_text += f"{book.title} by {book.author.name}\n"
    return HttpResponse(response_text, content_type='text/plain')


# Class-based view
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'