from django import forms
from .models import Book, Author, Category, Genre


class BookForm(forms.ModelForm):
    publication_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        to_field_name="name",
    )

    class Meta:
        model = Book
        fields = "__all__"


class AuthorForm(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Author
        fields = "__all__"
