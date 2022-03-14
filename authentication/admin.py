from django.contrib import admin

from authentication.models import AuthUser, UserFollowing

# Register your models here.


admin.site.register(AuthUser)

admin.site.register(UserFollowing)
