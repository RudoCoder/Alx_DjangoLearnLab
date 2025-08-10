## Filtering, Searching & Ordering

### Filtering
- `/api/books/?title=Things Fall Apart`
- `/api/books/?author__name=Chinua Achebe`
- `/api/books/?publication_year=1958`

### Searching
- `/api/books/?search=Fall`
- `/api/books/?search=Chinua`

### Ordering
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year` (descending)

### Running Tests
To run the API tests:
```bash
python manage.py test api
