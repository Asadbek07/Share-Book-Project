from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from library.models import UserBook, BookThatWillBeShared


class UserBookDetailView(DetailView):
    model = UserBook
    template_name = "user_books/books_detail.html"



class UserBookListView(LoginRequiredMixin, ListView):
    model = UserBook
    template_name = "user_books/books_list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class CreateUserBookView(LoginRequiredMixin, CreateView):
    model = UserBook
    fields = [
        'book',
        'state_of_user',
        'rating'
    ]
    template_name = "user_books/create_book.html"
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    success_url = "/"


class UpdateUserBookView(UpdateView):
    model = UserBook
    fields = [
        'state_of_user',
        'rating',
        'book'
    ]
    template_name = "user_books/update.html"
    