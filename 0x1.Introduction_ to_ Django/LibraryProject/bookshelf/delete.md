# To delete a book import the 'Book model'
from bookshelf.models import Book

# Command
book = Book.objects.get(title="Nineteen Eighty-four")
book.delete()
books = Book.objects.all()
print(books)

# Expected output
<QuerySet [<Book: 1984 by George Orwell>, <Book: 1984 by George Orwell>]>