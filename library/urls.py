from unicodedata import name
from django.urls import path

from library.views import UpdateShareableBookView, \
                          ShareableBooksView,\
                          UserBookDetailView,\
                          UserBookListView,\
                          CreateUserBookView,\
                          ShareBookView,\
                          DetailShareableBookView,\
                          UpdateUserBookView,\
                          BookListView,\
                          BookDetailView,\
                          CreateBookView,\
                          UpdateBookView
                          


urlpatterns = [
    path("userbooks/", UserBookListView.as_view(), name="userbook_list"),
    path("userbooks/create", CreateUserBookView.as_view(), name="create_userbook"),
    path("userbooks/<int:pk>/update", UpdateUserBookView.as_view(), name="update_userbook"),
    path("userbooks/<int:pk>/", UserBookDetailView.as_view(), name="userbook_detail"),
    
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/create", CreateBookView.as_view(), name="book_create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/update", UpdateBookView.as_view(), name="book_update"),

    path("books/shareables/", ShareableBooksView.as_view(), name="shareable_books"),
    path("books/shareables/<int:pk>/", DetailShareableBookView.as_view(), name="detail_shareable_books"),
    path("books/shareables/<int:pk>/update", UpdateShareableBookView.as_view(), name="update_shareable_books"),
    path("books/share", ShareBookView.as_view(), name="share_book"),

]