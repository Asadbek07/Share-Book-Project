from django.contrib import admin
from django.utils.html import format_html
from library.models import Book, BookThatWillBeShared

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    def image_tag(self, queryset):
        return format_html(f'<img width="60" height="60" src="{queryset.image.url}"/>')

    image_tag.short_description = "Image"
    list_display = ["image_tag", "name", "author", "rating", "created"]
    list_editable = ("rating", )
    search_fields = ["name"]

    list_filter = ["rating", "created"]


admin.site.register(BookThatWillBeShared)