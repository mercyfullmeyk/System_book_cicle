from django.contrib import admin
from .models import Book, Litcoin, Rentsbook


class BookAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'availability',
        'condition',
        'author',
        'coins',
    )
    search_fields = ('name', )
    empty_value_display = '-пусто-'


class LitcoinAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'coins',
        'author',
    )


class RentsbookAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'arendator',
        'book',
        'agree_one',
        'agree_two',
        'in_rent',
        'start_rent',
        'end_rent',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Litcoin, LitcoinAdmin)
admin.site.register(Rentsbook, RentsbookAdmin)
