from django.conf import settings
from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books"
    )
    def __str__(self):
        return f"Author: {self.author} | Name : {self.name}"
    