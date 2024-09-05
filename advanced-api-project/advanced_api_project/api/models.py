from django.db import models

# Create your models here.
# Represents an author with a name field
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Represents a book with a title, publication year and associated author
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE) 
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title    