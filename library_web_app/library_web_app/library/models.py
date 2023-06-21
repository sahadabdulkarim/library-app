from django.db import models

from django.db.models import (
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    TextField,
    DateTimeField,
    BooleanField,
    FloatField,
    DecimalField,
)


class Category(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = CharField(max_length=100)
    birthdate = DateField()
    email = EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = CharField(max_length=100, null=False)
    author = ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = DateField()
    created_date = DateTimeField(auto_now_add=True)
    is_available = BooleanField(default=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField()
    book_code = CharField(max_length=10)
    category = ForeignKey(Category, on_delete=models.CASCADE)
    genre = ManyToManyField(Genre)
    rating = FloatField()

    def __str__(self):
        return self.title
