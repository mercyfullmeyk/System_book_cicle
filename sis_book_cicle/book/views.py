from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


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


def book_create(request):
    '''Функция отвечающая за создание поста'''
    form = BookForm(request.POST or None,
                    files=request.FILES or None,)

    if form.is_valid():

        book = form.save(commit=None)
        book.availability = True
        book.save()

        return redirect('book:index')

    context = {'form': form}
    return render(request, 'books/create_book.html', context)
