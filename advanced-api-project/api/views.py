from rest_framework import generics, permissions, filters, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

class BookviewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing book instances.
    Provides CRUD operations and supports filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

class BookListView(generics.ListAPIView):
    """
    List view retrieves all books in the system.
    Accessible to both authenticated and unauthenticated users.

    Filtering:
        - /api/books/?title=Things Fall Apart
        - /api/books/?author__name=Chinua Achebe
        - /api/books/?publication_year=1958

    Searching:
        - /api/books/?search=Fall
        - /api/books/?search=Chinua

    Ordering:
        - /api/books/?ordering=title
        - /api/books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally filter books by author name if provided in query parameters.
        """
        queryset = Book.objects.all()
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(publication_year=year)
        return queryset

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fileds allowed for searching
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering if none is specified
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView retrieves a single book by its ID (pk).
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    CreateView allows authenticated users to add a new book.
    includes validation from BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView allows authenticated users to update an existing book.
    Uses partial updates (PATCH) or full updates (PUT).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView allows authenticated users to delete a book by its ID (pk).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
