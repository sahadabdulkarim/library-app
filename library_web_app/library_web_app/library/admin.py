from django.contrib import admin
from .models import Book, Category, Author, Genre


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "birthdate", "email")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "publication_date",
        "is_available",
        "price",
        "category",
        "get_genres",
        "rating",
    )
    list_filter = ("is_available", "category", "author")
    search_fields = ("id", "title", "author__name", "category__name", "genre__name")

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])

    get_genres.short_description = "Genres"
