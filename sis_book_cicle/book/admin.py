from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'availability'
    )
    search_fields = ('name', )
    empty_value_display = '-пусто-'


admin.site.register(Book, BookAdmin)
