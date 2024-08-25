# Command - retrieve all book instances
books = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Expected output
1984 George Orwell 1949