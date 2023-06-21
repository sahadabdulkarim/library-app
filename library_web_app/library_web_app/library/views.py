from django.shortcuts import redirect, render, get_object_or_404
from django.views import View


from .models import Book, Author
from .form import AuthorForm, BookForm


# Create your views here.
def home(request):
    return render(request, "library/home.html")


def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "library/book_detail.html", {"book": book})


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, "library/author_list.html", {"authors": authors})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/create_book.html", {"form": form})


class CreateAuthorView(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, "library/create_author.html", {"form": form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("author_list")
        return render(request, "library/create_author.html", {"form": form})
