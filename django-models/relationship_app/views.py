from django.shortcuts import render
from .models import Book

# Create your views here.
# function-based view
def list_books(request):
        return render(request, 'list_books.html')


# Class-based view
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'