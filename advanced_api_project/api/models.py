from django.db import models
from datetime import datetime

# Create your models here.
class Author(models.Model):
    """
    Author model to represent an author in the system or a writer of books.
    one author can have multiple books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model containing title, publication year and a link to its author Via ForeignKey.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.publication_year}"
