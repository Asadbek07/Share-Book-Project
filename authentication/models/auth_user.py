from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class AuthUser(AbstractUser):
    phone_number = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/", blank=True)
    
    def get_absolute_url(self):
        return reverse("user_detail_update", args=[str(self.id)])
    
