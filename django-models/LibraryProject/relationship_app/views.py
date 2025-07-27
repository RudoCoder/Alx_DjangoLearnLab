from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # <- MUST match exactly
    return render(request, 'relationship_app/list_books.html', {'books': books})  # <- MUST match exactly

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
