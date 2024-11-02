from django.shortcuts import render
from .models import Book


def index(request):
    '''Функция отвечающая за главную страницу'''
    books_list = Book.objects.all()
    title = 'Каталог'
    context = {
        'title': title,
        'books': books_list
    }
    return render(request, 'books/test_index.html', context)


def book_detail(request, book_id):
    '''Функция отвечающая за страницу книги'''
    book = Book.objects.filter(id=book_id)
    book = book[0]
    context = {
        'book': book
    }
    return render(request, 'books/test_book.html', context)
