from unicodedata import name
from django.urls import path

from library.views import BookDetailView, BookListView, CreateBookView


urlpatterns = [
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/create", CreateBookView.as_view(), name="create_book"),
    path("books/<pk>/", BookDetailView.as_view(), name="book_detail"),
]