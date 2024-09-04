from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

        # A custom validation method to ensure the publication year is not in the future.
        def validate_publication_year(self, value):
            if value > datetime.datetime.now().year:
                raise serializers.ValidationError("Publication year cannot be in the future")
            return value

# Serializes the name field of the Author model
class AuthorSerializer(serializers.ModelSerializer):

    """ 
    A nested BookSerializer to serialize related Book instances dynamically.
    The books field is a read-only relationship that will show all books related to the author.
    The many=True parameter indicates that an author can have multiple books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']