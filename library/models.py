from django.conf import settings
from django.db import models

# Create your models here.

class Ratings:
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    ALL = [(rating, rating) for rating in range(ONE, FIVE)]

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books"
    )
    image = models.ImageField(upload_to="books/%Y/%m/%d")
    rating = models.IntegerField(default=Ratings.ONE, choices=Ratings.ALL)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Author: {self.author} | Name : {self.name}"


class BookThatWillBeShared(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shareable_books"
    )

    book_id = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="shareable_books"
    )
    shared = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created", )


    def __str__(self):
        return f"Owner : {self.user_id} | Book that will be shared : {self.book_id.name}"