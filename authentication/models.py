from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class AuthUser(AbstractUser):
    pass




class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="following",
        on_delete=models.CASCADE
        )

    following_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="followers",
        on_delete=models.CASCADE
    )    

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user_id", "following_user_id"), )
        ordering = ("-created", )

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"    