# Create.md

# Command
from bookshelf.models import Book

# Create a new book instance
book = Book(title="1984", author="George Orwell", publication_year="1949")
book.save()
print(book)
# Expected output
1984 by George Orwell


# retrieve.md

# Command - retrieve all book instances
books = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Expected output
1984 George Orwell 1949


# update.md

# Command
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Expected output
Nineteen Eighty-Four by George Orwell


# delete.md

# Command
book = Book.objects.get(title="Nineteen Eighty-four")
book.delete()
books = Book.objects.all()
print(books)
# Expected output
<QuerySet [<Book: 1984 by George Orwell>, <Book: 1984 by George Orwell>]>