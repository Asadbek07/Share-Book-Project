from unicodedata import name
from django.urls import path

from library.views import UpdateShareableBookView, \
                          ShareableBooksView,\
                          UserBookDetailView,\
                          UserBookListView,\
                          CreateUserBookView,\
                          ShareBookView,\
                          DetailShareableBookView,\
                          UpdateUserBookView
                          


urlpatterns = [
    path("books/", UserBookListView.as_view(), name="book_list"),
    path("books/create", CreateUserBookView.as_view(), name="create_book"),
    path("books/<pk>/update", UpdateUserBookView.as_view(), name="update_book"),
    path("books/shareables/", ShareableBooksView.as_view(), name="shareable_books"),
    path("books/shareables/<pk>/", DetailShareableBookView.as_view(), name="detail_shareable_books"),
    path("books/shareables/<pk>/update", UpdateShareableBookView.as_view(), name="update_shareable_books"),
    path("books/<pk>/", UserBookDetailView.as_view(), name="book_detail"),
    path("books/share", ShareBookView.as_view(), name="share_book"),
]