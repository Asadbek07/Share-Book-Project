from django.contrib import admin
from django.utils.html import format_html
from library.models import Book, UserBook, BookThatWillBeShared

# Register your models here.

@admin.register(UserBook)
class BookAdmin(admin.ModelAdmin):

    def image_tag(self, queryset):
        return format_html(f'<img width="60" height="60" src="{queryset.book.image.url}"/>')

    image_tag.short_description = "Image"
    list_display = ["image_tag", "book", "owner", "rating", "state_of_user", "created"]
    list_editable = ("rating", "state_of_user")

    list_filter = ["rating", "created"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    def image_tag(self, queryset):
        return format_html(f'<img width="60" height="60" src="{queryset.image.url}"/>')

    image_tag.short_description = "Image"
    list_display = ["image_tag", "name", "author", "created"]

    list_filter = ["created"]



admin.site.register(BookThatWillBeShared)