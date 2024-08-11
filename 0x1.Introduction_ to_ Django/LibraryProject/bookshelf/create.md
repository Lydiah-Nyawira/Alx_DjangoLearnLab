# Command
from bookshelf.models import Book

# Create a new book instance
book = Book(title="1984", author="George Orwell", publication_year="1949")
book.save()
print(book)
# Expected output
1984 by George Orwell