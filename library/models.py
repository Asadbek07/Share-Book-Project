from django.conf import settings
from django.db import models

# Create your models here.

class StateOfUser:
    WANT_TO_READ = "O'qimoqchiman"
    READING = "O'qiyabman"
    HAVE_READ = "O'qib bo'ldim"
    ALL = [(state, state) for state in [WANT_TO_READ, READING, HAVE_READ]]

class Ratings:
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    ALL = [(rating, rating) for rating in range(ONE, FIVE + 1)]

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/%Y/%m/%d")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"
    

class UserBook(models.Model):
    book = models.ForeignKey(
      Book,
      on_delete=models.CASCADE,
      related_name="readers"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books"
    )
    state_of_user = models.CharField(max_length=255, default=StateOfUser.WANT_TO_READ, choices=StateOfUser.ALL)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=Ratings.ONE, choices=Ratings.ALL)


    def __str__(self):
        return f"{self.book.name} | {self.owner.username}"

    def get_absolute_url(self):
        return f"library/books/{self.id}"
    


class BookThatWillBeShared(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shareable_books"
    )

    book_id = models.ForeignKey(
        UserBook,
        on_delete=models.CASCADE,
        related_name="shareable_books"
    )
    shared = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created", )


    def __str__(self):
        return f"Owner : {self.user_id} | Book that will be shared : {self.book_id.name}"