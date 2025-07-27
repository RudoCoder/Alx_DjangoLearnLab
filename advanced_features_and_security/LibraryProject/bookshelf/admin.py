from django.contrib import admin
from .models import Book

# Custom admin display
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year', 'author')             # Sidebar filters
    search_fields = ('title', 'author')                      # Search bar for title or author

admin.site.register(Book, BookAdmin)  # Register with customization

# Register your models here.
