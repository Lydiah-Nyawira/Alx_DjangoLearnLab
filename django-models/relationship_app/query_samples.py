from .models import Author, Book, Library, Librarian

# Query all books by specific author
def all_books_by_author(author_name):
    author = Author.objects.get(name='author_name')
    books_by_author = Book.objects.filter(author=author)

# List all books in a library
def list_all_books(library_name):
    library = Library.objects.get(name='library_name')
    books_in_library = library.books.all()
    return books_in_library

# Retrieve librarian for a library
def retrieve_librarian(library_name):
    library = library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian