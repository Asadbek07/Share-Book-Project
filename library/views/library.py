from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from library.models import Book
from django.views.generic.edit import CreateView, UpdateView



class BookListView(ListView):
    model = Book
    template_name = "library/list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "library/detail.html"

class CreateBookView(CreateView):
    model = Book
    fields = [
        'name',
        'author',
        'image'
    ]
    template_name = "library/create.html"
    success_url = reverse_lazy("book_list")


class UpdateBookView(UpdateView):
    model = Book
    fields = [
        'name',
        'author',
        'image'
    ]
    template_name = "library/create.html"
    success_url = reverse_lazy("book_list")

