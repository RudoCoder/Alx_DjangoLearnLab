from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Book, Author

class BookAPITestCase(APITestCase):
    """
    Test case for the Book API endpoints.
    """

    def setUp(self):
        # Create a test author
        self.author = Author.objects.create(name="Chinua Achebe")
        # Create a test book
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease",
            publication_year=1960,
            author=self.author
        )
        # Create a user and token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)

        # URLs for the API endpoints
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # CRUD Tests
    def test_list_books(self):
        """Test retrieving list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    def test_create_book_authenticated(self):
        """Test creating a book with authentication."""
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "Arrow of God",
            "author": self.author.id,
            "publication_year": 1964
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication."""
        data = {
            "title": "Man of the People",
            "author": self.author.id,
            "publication_year": 1966
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test updating a book with authentication."""
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "Things Fall Apart - Updated",
            "author": self.author.id,
            "publication_year": 1958
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart - Updated")

    def test_delete_book_authenticated(self):
        """Test deleting a book with authentication."""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- Filtering, Searching, Ordering ---
    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(self.list_url, {"title": "Things Fall Apart"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author_name(self):
        """Test searching books by author's name."""
        response = self.client.get(self.list_url, {"search": "Achebe"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year_desc(self):
        """Test ordering books by publication year descending."""
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 1960)


    def authenticate(self):
        """
        Helper method to authenticate the user using the token.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
