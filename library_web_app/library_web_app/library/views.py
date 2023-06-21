from .models import Category, Genre
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
    book = get_object_or_404(Book, id=book_id)
    genres = book.genre.all()
    return render(request, "library/book_detail.html", {"book": book, "genres": genres})


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, "library/author_list.html", {"authors": authors})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            category_name = form.cleaned_data.get("category")
            category = Category.objects.get(name=category_name)
            book.category = category
            book.save()

            genre_names = form.cleaned_data.get("genre")
            genres = Genre.objects.filter(name__in=genre_names)
            book.genre.set(genres)

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


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, "library/update_book.html", {"form": form})
