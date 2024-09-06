from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model, including validation for publication_year.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
    
    def validate_publication_year(self, value):
        """
        Validate that the publication year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model, including a nested BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']