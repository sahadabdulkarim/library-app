import json
import requests

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound


# Create your views here.
def home(request):
    return render(request, "library/home.html")


def book_list(request):
    with open("booklist.json", encoding="UTF-8") as f:
        books = json.load(f)
    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, book_id):
    with open("booklist.json", encoding="UTF-8") as f:
        books = json.load(f)
        for book in books:
            if book["id"] == book_id:
                return render(request, "library/book_detail.html", {"book": book})

        return HttpResponseNotFound("Book not found")


class AuthorListView(View):
    def get(self, request):
        response = requests.get(
            "http://random-data-api.com/api/v2/users?size=10", timeout=5
        )
        authors = response.json()
        return render(request, "library/author_list.html", {"authors": authors})
