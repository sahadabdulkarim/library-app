from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from .models import Book, Author


# Create your views here.
def home(request):
    return render(request, "library/home.html")


def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return render(request, "library/book_detail.html", {"book": book})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Book not found")


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, "library/author_list.html", {"authors": authors})
