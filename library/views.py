from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from library.models import Book



class BookDetailView(DetailView):
    model = Book
    template_name = "library/books_detail.html"

class BookListView(ListView):
    model = Book
    template_name = "library/books_list.html"


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    fields = [
        'name',
        'isbn',
        'image',
        'rating',
        'author'
    ]
    template_name = "library/create_book.html"
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    success_url = "/"


class UpdateBookView(UpdateView):
    model = Book
    fields = [
        'name',
        'isbn',
        'image',
        'rating',
        'author'
    ]
    