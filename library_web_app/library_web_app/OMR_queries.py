from django.shortcuts import render
from library.models import Book, Genre, Author

# Find Books which are available:

Book.objects.filter(is_available=True).values("id", "title")

# Find books whose title has 'The Great':

Book.objects.filter(title__contains="The Great").values("id", "title")

# Find books with rating >= 4:

Book.objects.filter(rating__gte=4).values("id", "title")

# Find books published in the year 2002:

Book.objects.filter(publication_date__year=2002).values("id", "title")

# Query all Genres of a Book:
book_id = 1  # for book with id 1
book = Book.objects.get(id=book_id)
book.genre.all().values("id", "name")

# Query All books of a given Genre:

genre_id = 1  # for book with id 1
genre = Genre.objects.get(id=genre_id)
genre.book_set.all().values("id", "title")

# Query all books by a given Author:

author_id = 1  # for author with id 1
author = Author.objects.get(id=author_id)
author.book_set.all().values("id", "title")
