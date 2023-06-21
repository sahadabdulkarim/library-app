from django.urls import path
from . import views
from .views import create_book, CreateAuthorView
from .views import (
    available_books,
    books_with_title,
    highly_rated_books,
    books_published_in_2002,
    book_genres,
    books_of_genre,
    books_by_author,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("booklist/", views.book_list, name="book_list"),
    path("book_detail/<int:book_id>/", views.book_detail, name="book_detail"),
    path("author_list/", views.AuthorListView.as_view(), name="author_list"),
    path("create-book/", create_book, name="create_book"),
    path("create-author/", CreateAuthorView.as_view(), name="create_author"),
    path("book/update/<int:book_id>/", views.update_book, name="update_book"),
    path("available-books/", available_books, name="available_books"),
    path("books-with-title/", books_with_title, name="books_with_title"),
    path("highly-rated-books/", highly_rated_books, name="highly_rated_books"),
    path(
        "books-published-in-2002/",
        books_published_in_2002,
        name="books_published_in_2002",
    ),
    path("book-genres/<int:book_id>/", book_genres, name="book_genres"),
    path("books-of-genre/<int:genre_id>/", books_of_genre, name="books_of_genre"),
    path("books-by-author/<int:author_id>/", books_by_author, name="books_by_author"),
]
