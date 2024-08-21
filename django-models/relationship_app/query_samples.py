import django
import os

# Set up Django settings and environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_model.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    # Use filter to get all books written by the author
    books = Book.objects.filter(author=author)
    return books


def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

if __name__ == "__main__":
    # Example Queries
    print("Books by Author 'J.K. Rowling':", query_books_by_author('J.K. Rowling'))
    print("Books in Library 'Central Library':", list_books_in_library('Central Library'))
    print("Librarian for Library 'Central Library':", retrieve_librarian_for_library('Central Library'))