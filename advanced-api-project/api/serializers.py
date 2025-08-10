from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation for publication year to ensure it is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

        def validate_publication_year(self, value):
            current_year = datetime.now().year
            if value > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Author model, including related books.
    Uses the nester BookSerializer to include books in the response.
    """
    books = BookSerializer(many=True, read_only=True) # Related name from author model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
