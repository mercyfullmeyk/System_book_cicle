from django.contrib import admin
from .models import Book, Litcoin


class BookAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'availability',
        'condition',
        'author',
    )
    search_fields = ('name', )
    empty_value_display = '-пусто-'


class LitcoinAdmin(admin.ModelAdmin):

    list_display = (
        'coins',
        'author',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Litcoin, LitcoinAdmin)
