 Introduction to Django
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

It follows the MVT architecture: Model–View–Template.

Django is batteries-included: it provides built-in tools for admin, authentication, sessions, ORM, etc.

🔁 Django Project Structure
When you create a Django project (django-admin startproject ProjectName), it creates:

markdown
Copy
Edit
ProjectName/
├── manage.py
├── ProjectName/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
Key Files:
manage.py – CLI tool to interact with the project.

settings.py – Project configurations (database, apps, middleware).

urls.py – Maps URLs to views.

wsgi.py/asgi.py – For deploying with WSGI/ASGI servers.

🧱 MVT Architecture
Component	Description
Model	Defines data structure and interacts with the database
View	Contains business logic and controls what the user sees
Template	HTML file that displays data dynamically

⚙️ Django Apps
Django projects are made of apps, which are modular components.

Create an app using:

bash
Copy
Edit
python manage.py startapp appname
Typical App Structure:
pgsql
Copy
Edit
appname/
├── models.py
├── views.py
├── urls.py
├── admin.py
├── apps.py
├── tests.py
└── migrations/
📦 Models
Models define the structure of database tables using Python classes.

Defined in models.py.

Example:
python
Copy
Edit
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
🛠️ Migrations
After changing models, you must run migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
💻 Django Admin
Admin panel is built-in and available at /admin.

Register models in admin.py:

python
Copy
Edit
from .models import Book
admin.site.register(Book)
You can customize list display, filters, and search in ModelAdmin.

🔗 URLs & Views
urls.py maps routes to views.

Views return responses (usually HTML or JSON).

URL Configuration:
python
Copy
Edit
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
View Function:
python
Copy
Edit
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")
🧩 Templates
Templates are HTML files with dynamic content using Django Template Language ({{ }} and {% %}).

Example:

html
Copy
Edit
<h1>Welcome, {{ user.username }}</h1>
🔐 Authentication
Django provides:

User model

Login/logout views

Decorators like @login_required

Admin user creation: python manage.py createsuperuser

🧪 Shell & ORM
Launch interactive shell:

bash
Copy
Edit
python manage.py shell
Use ORM for CRUD:

python
Copy
Edit
from app.models import Book
Book.objects.create(title="1984", author="Orwell", publication_year=1949)
books = Book.objects.all()
📤 Deployment Overview
Steps to deploy a Django app:

Set DEBUG = False in settings.py

Configure ALLOWED_HOSTS

Collect static files:

bash
Copy
Edit
python manage.py collectstatic
Use Gunicorn or uWSGI with NGINX

Deploy on platforms like Heroku, Render, DigitalOcean, etc.
