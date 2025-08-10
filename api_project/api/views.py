from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

# View for listing books only.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Require login

# View for retrieving, updating, and deleting a specific book.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]  # Only admin users can modify books
