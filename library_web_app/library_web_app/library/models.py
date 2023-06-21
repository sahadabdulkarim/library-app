from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    book_code = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
