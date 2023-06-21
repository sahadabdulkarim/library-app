from django.contrib import admin
from .models import Book, Category, Author, Genre


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "email")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "publication_date",
        "is_available",
        "price",
        "category",
        "rating",
    )
    list_filter = ("is_available", "category", "author")
    search_fields = ("title", "author__name", "category__name", "genre__name")
