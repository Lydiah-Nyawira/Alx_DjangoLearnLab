# Command
book = Book.objects.get(title="Nineteen Eighty-four")
book.delete()
books = Book.objects.all()
print(books)

# Expected output
<QuerySet [<Book: 1984 by George Orwell>, <Book: 1984 by George Orwell>]>