from django.db import models

# Create your models here.

# Model representing an author
class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        self.name
# Model representing a book
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    def __str__(self):
        self.title        